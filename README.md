# AI-Based Trip Planner with Agentic AI and LLMOps

An advanced AI-powered trip planning system designed to streamline travel planning by leveraging real-time data and large language models (LLMs). Plan comprehensive and personalized trips worldwide with accurate and up-to-date information.

## Key Features

* **Real-Time Weather Information:** Access current weather data to plan activities accordingly.
* **Attractions and Activities:** Discover top attractions and curated activities based on your destination.
* **Hotel Cost Estimation:** Obtain accurate hotel pricing and availability.
* **Currency Conversion:** Real-time currency exchange rates for budgeting and financial planning.
* **Itinerary Planner:** Generate detailed and optimized daily itineraries.
* **Total Expense Estimation:** Summarize all travel expenses for informed budgeting.
* **Generated Trip Summary:** Automatically create an insightful summary of your planned trip.

## Technology Stack

* **Agentic AI:** Enables autonomous planning and decision-making capabilities.
* **LLMOps:** Ensures efficient deployment, management, and scalability of large language models.

## Getting Started with commend

print(shutil.which("uv"))```

```pip install uv```

```uv init AI_Travel_Planner``` 

Follow these steps to set up the project environment:

```bash
# Deactivate any existing Conda environment-#if you have conda then first deactivate that
conda deactivate

# List available Python versions managed by uv
uv python list

# Install a specific Python version
uv python install cpython-3.11.13-windows-x86_64-none

# Confirm installation by listing Python versions again
uv python list

# Create a virtual environment named 'env' with a specific Python version
uv venv env cpython-3.13.0-windows-x86_64-none

# Alternative explicit method to create a virtual environment with specified Python version
uv venv env --python cpython-3.13.0-windows-x86_64-none

# Activate the virtual environment (Windows)
C:\Users\Nahid\OneDrive - Calmi2\Desktop\Ai_trip_planner\env\Scripts\activate.bat

# Alternative way to activate the virtual environment
env\Scripts\activate.bat

# List installed packages in the current uv-managed virtual environment
uv pip list

# Install the LangChain package using uv
uv pip install langchain

# Verify that LangChain has been successfully installed
uv pip list

# install requirements
uv pip install -r requirements.txt

# Display the command history in the terminal
DOSKEY /history

```

Your environment is now ready for development.


# AI Trip Planner Repository Structure

```
.
├── agent/
├── config/
├── exception/
├── logger/
├── notebook/
├── prompt_library/
├── tools/
├── utils/
├── .env.name
├── .gitignore
├── .python-version
├── README.md
├── main.py
├── my_graph.png
├── pyproject.toml
├── requirements.txt
├── setup.py
├── streamlit_app.py
└── uv.lock
```
