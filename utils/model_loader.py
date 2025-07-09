import os
from dotenv import load_dotenv  # For loading environment variables from .env file
from typing import Literal, Optional, Any
from pydantic import BaseModel, Field
from utils.config_loader import load_config  # Custom config loader
from langchain_groq import ChatGroq  # Groq LLM wrapper from LangChain
from langchain_openai import ChatOpenAI  # OpenAI LLM wrapper from LangChain

# Optional: Load environment variables (uncomment if needed)
load_dotenv()

class ConfigLoader:
    """
    Loads configuration using a custom config loader.
    """
    def __init__(self):
        print(f"Loaded config.....")
        self.config = load_config()  # Load configuration dictionary
    
    def __getitem__(self, key):
        # Allow access to config items via dictionary-style indexing
        return self.config[key]


class ModelLoader(BaseModel):
    """
    Loads and returns a language model (LLM) based on provider (Groq or OpenAI).
    Uses pydantic BaseModel for validation and structure.
    """
    model_provider: Literal["groq", "openai"] = "groq"  # Only allow "groq" or "openai"
    config: Optional[ConfigLoader] = Field(default=None, exclude=True)  # Config is excluded from serialization

    def model_post_init(self, __context: Any) -> None:
        # Called automatically after the pydantic model is initialized
        self.config = ConfigLoader()

    class Config:
        # Allows custom Python objects like ConfigLoader to be used in fields
        arbitrary_types_allowed = True

    def load_llm(self):
        """
        Load and return the LLM model depending on the provider.
        Supports: Groq and OpenAI.
        """
        print("LLM loading...")
        print(f"Loading model from provider: {self.model_provider}")

        if self.model_provider == "groq":
            # Load Groq-based LLM
            print("Loading LLM from Groq..............")
            groq_api_key = os.getenv("GROQ_API_KEY")  # Read Groq API key from env
            model_name = self.config["llm"]["groq"]["model_name"]  # Get model name from config
            llm = ChatGroq(model=model_name, api_key=groq_api_key)

        elif self.model_provider == "openai":
            # Load OpenAI-based LLM
            print("Loading LLM from OpenAI..............")
            openai_api_key = os.getenv("OPENAI_API_KEY")  # Read OpenAI API key from env
            model_name = self.config["llm"]["openai"]["model_name"]
            # NOTE: This hardcodes the model_name to "o4-mini", override if needed
            llm = ChatOpenAI(model_name="o4-mini", api_key=openai_api_key)

        return llm