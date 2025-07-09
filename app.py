# Import required libraries from FastAPI and Pydantic
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

# Import the GraphBuilder class from the agentic workflow module
from agent.agentic_workflow import GraphBuilder

# Initialize FastAPI app
app = FastAPI()

# Define request body structure using Pydantic
class QueryRequest(BaseModel):
    query: str  # Input query from user

# Define POST endpoint to handle travel agent queries
@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        # Print incoming query object (for debugging/logging)
        print(query)

        # Initialize graph using a specific LLM model provider
        graph = GraphBuilder(model_provider="groq")

        # Build or get the reactive app graph (pipeline/workflow)
        react_app = graph()

        # Generate a visualization of the graph and save it as a PNG image
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        # Log where the graph image is saved
        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        # Prepare the input messages for the LLM agent
        # Assuming input query format: {"question": "your text"}
        messages = {"messages": [query.query]}

        # Invoke the graph with the user's message
        output = react_app.invoke(messages)

        # Parse the response: check if it's a dict with messages
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Take the last AI-generated response
        else:
            final_output = str(output)  # Fallback: convert output to string

        # Return the final response in a JSON object
        return {"answer": final_output}

    # Handle unexpected errors and return them in the response
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
