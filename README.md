# SQLLLM

SQLLLM is a Streamlit application that turns natural-language questions into MySQL queries, runs them against your database, and visualizes the result with Plotly.

## Features

- Ask database questions in plain English.
- Generate MySQL 8 compatible SQL with an LLM.
- Execute generated SQL through SQLAlchemy.
- Display query results as a Pandas DataFrame.
- Render charts automatically as bar, line, pie, scatter, or table views.
- Inspect database schema automatically from the connected database.

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq chat model via `langchain_groq`
- MySQL
- SQLAlchemy
- Pandas
- Plotly

## Project Structure

```text
.
├── app.py                  # Streamlit app entry point
├── database/
│   ├── connector.py        # Database connection setup
│   ├── executor.py         # SQL execution helper
│   └── schema.py           # Database schema inspector
├── llm/
│   ├── config.py           # Environment variable loading
│   ├── llm.py              # Groq LLM client
│   └── sql_generator.py    # Prompt and SQL/chart JSON generation
├── plots/
│   └── charts.py           # Plotly chart rendering
├── requirements.txt
└── SQLLLMS.ipynb
```

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd SQLLLM
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
pip install streamlit plotly sqlalchemy
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
API_KEY=your_groq_api_key
DATABASE_URL=mysql+pymysql://username:password@host:3306/database_name
```

Example for a local MySQL database:

```env
API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/sakila
```

## Run the App

```bash
streamlit run app.py
```

Then open the local Streamlit URL shown in your terminal.

## Usage

1. Start the Streamlit app.
2. Enter a question such as:

```text
Show revenue by movie categories
```

3. Click **Generate**.
4. Review the generated SQL, result table, and chart.

## How It Works

1. `database/schema.py` reads table names, columns, and relationships from MySQL.
2. `llm/sql_generator.py` sends the schema and user question to the LLM.
3. The LLM returns JSON containing SQL, chart type, axes, and title.
4. `database/executor.py` executes the SQL and returns a Pandas DataFrame.
5. `plots/charts.py` renders the selected Plotly visualization.

## Environment Variables

| Variable | Description |
| --- | --- |
| `API_KEY` | Groq API key used by `langchain_groq.ChatGroq` |
| `DATABASE_URL` | SQLAlchemy database URL for your MySQL database |

## Notes

- The app currently targets MySQL 8.
- Generated SQL is executed directly against the configured database, so use a safe development database while testing.
- The model is configured in `llm/llm.py`.
- The current app expects the LLM response to be valid JSON.

