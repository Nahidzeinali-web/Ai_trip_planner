# FastAPI core import
from fastapi import FastAPI

# Enable CORS (Cross-Origin Resource Sharing)
from fastapi.middleware.cors import CORSMiddleware

# Import custom agentic workflow class to build the AI graph
from agent.agentic_workflow import GraphBuilder

# Utility function to save output to a document (optional)
from utils.save_to_document import save_document

# Standard response class from Starlette for handling errors
from starlette.responses import JSONResponse

# Built-in modules
import os
import datetime

# Load environment variables from a .env file
from dotenv import load_dotenv
load_dotenv()

# Define request schema using Pydantic
from pydantic import BaseModel

# Initialize FastAPI app instance
app = FastAPI()

# Add CORS middleware (necessary if the frontend runs on a different domain or port)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ In production, replace '*' with a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the structure of incoming POST requests
class QueryRequest(BaseModel):
    question: str  # The input question or prompt from the user

# POST endpoint to handle AI query requests
@app.post("/query")
async def query_travel_agent(query: QueryRequest):
    try:
        print(query)  # Log the input request

        # Initialize the AI workflow graph with a selected model provider (e.g., Groq)
        graph = GraphBuilder(model_provider="groq")
        react_app = graph()  # Instantiate the graph pipeline

        # Draw and save the visual representation of the graph as a Mermaid PNG
        png_graph = react_app.get_graph().draw_mermaid_png()
        with open("my_graph.png", "wb") as f:
            f.write(png_graph)

        print(f"Graph saved as 'my_graph.png' in {os.getcwd()}")

        # Prepare the input message for the agent
        messages = {"messages": [query.question]}

        # Invoke the AI agent with the user message
        output = react_app.invoke(messages)

        # If output is a dictionary with "messages", extract the latest content
        if isinstance(output, dict) and "messages" in output:
            final_output = output["messages"][-1].content  # Get the last AI response
        else:
            final_output = str(output)  # Fallback to raw string conversion

        # Return the final answer in a JSON response
        return {"answer": final_output}

    # Catch and return any errors during processing
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
