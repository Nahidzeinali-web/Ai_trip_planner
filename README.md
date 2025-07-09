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


uvicorn main:app --host 0.0.0.0 --port 8000 --reload

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

This guide explains how to run your full-stack AI Trip Planner application, which includes a FastAPI backend and a Streamlit frontend.

---

## ✅ Step 1: Open Terminal and Activate the Environment

First, navigate to your project directory:

```bash
cd C:\Users\Nahid\OneDrive - Calmi2\Desktop\Ai_trip_planner
```

Then activate your virtual environment:

```bash
env\Scripts\activate
```

> Make sure you see `(env)` before the command prompt, indicating the environment is activated.

---

## ✅ Step 2: Run the FastAPI Backend

In the same terminal, start the FastAPI server:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

- ✅ Use `127.0.0.1` (not `0.0.0.0`) for better local access.
- ✅ Keep this terminal open while using the app.
- ✅ Visit [http://localhost:8000/docs](http://localhost:8000/docs) to verify the FastAPI server is running.

---

## ✅ Step 3: Run the Streamlit Frontend

Open a **second terminal window**, navigate to the same folder:

```bash
cd C:\Users\Nahid\OneDrive - Calmi2\Desktop\Ai_trip_planner
```

Then run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Streamlit will launch in your browser at:

```
http://localhost:8501
```

---

## ✅ Test the Full Stack Connection

1. Type a prompt in the Streamlit UI (e.g., `Plan a trip to Tokyo for 3 days`).
2. It will send a POST request to:

```
http://localhost:8000/query
```

3. The FastAPI backend will return the response using your AI pipeline.

---

## ✅ That's it!

Now you're running a full-stack AI-powered travel planner on your machine 🎉
