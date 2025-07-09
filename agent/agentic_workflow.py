# Import necessary modules and classes for model loading, prompt templates, graph management, and tool definitions
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool

class GraphBuilder():
    def __init__(self, model_provider: str = "groq"):
        # Initialize the language model with a specified provider
        self.model_loader = ModelLoader(model_provider=model_provider)
        self.llm = self.model_loader.load_llm()
        
        # Initialize an empty tool list
        self.tools = []
        
        # Instantiate each tool category
        self.weather_tools = WeatherInfoTool()
        self.place_search_tools = PlaceSearchTool()
        self.calculator_tools = CalculatorTool()
        self.currency_converter_tools = CurrencyConverterTool()
        
        # Extend the tools list with individual tools from each tool category
        self.tools.extend([
            *self.weather_tools.weather_tool_list, 
            *self.place_search_tools.place_search_tool_list,
            *self.calculator_tools.calculator_tool_list,
            *self.currency_converter_tools.currency_converter_tool_list
        ])
        
        # Bind the tools to the LLM for tool-augmented reasoning
        self.llm_with_tools = self.llm.bind_tools(tools=self.tools)
        
        # Placeholder for the final graph object
        self.graph = None
        
        # Define the system prompt to guide the agent's behavior
        self.system_prompt = SYSTEM_PROMPT
    
    def agent_function(self, state: MessagesState):
        """The main agent function that invokes the LLM with tools"""
        user_question = state["messages"]
        
        # Combine the system prompt with user messages
        input_question = [self.system_prompt] + user_question
        
        # Generate the model's response with potential tool use
        response = self.llm_with_tools.invoke(input_question)
        
        # Return updated message state
        return {"messages": [response]}
    
    def build_graph(self):
        """Constructs the LangGraph with agent and tools"""
        graph_builder = StateGraph(MessagesState)
        
        # Add nodes to the graph: the agent and the tools
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        
        # Define edges: start → agent → (conditionally) tools → agent → end
        graph_builder.add_edge(START, "agent")
        graph_builder.add_conditional_edges("agent", tools_condition)
        graph_builder.add_edge("tools", "agent")
        graph_builder.add_edge("agent", END)
        
        # Compile the graph for execution
        self.graph = graph_builder.compile()
        return self.graph
    
    def __call__(self):
        # Enables instance to be called as a function to build the graph
        return self.build_graph()
