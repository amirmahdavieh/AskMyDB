from dotenv import load_dotenv
from agents import Agent, set_default_openai_client, set_tracing_disabled, set_default_openai_api
from tools import execute_sql
from openai import OpenAI, AsyncOpenAI
import os

load_dotenv()

instructions = """
    You are a database assistant for SQLite.

        Convert the user's request into a safe SELECT query, call the execute_sql tool, and return the result clearly.

        Rules:
        - Only use SELECT queries.
        - Never use DROP, DELETE, UPDATE, INSERT, ALTER, CREATE, or PRAGMA.
        - If the request is unsafe, return UNSAFE_QUERY.
        - Use only existing tables and columns.
"""

'''converter_agent = Agent(
    name="Text to SQL converter",
    instructions=instructions,
    model="gpt-4o-mini",
    tools=[execute_sql]
)'''

set_tracing_disabled(True)
groq = AsyncOpenAI(api_key=os.getenv("GROQ_API_KEY"), base_url="https://api.groq.com/openai/v1")
model_name = "llama-3.3-70b-versatile"

set_default_openai_client(groq)
set_default_openai_api("chat_completions")

converter_agent = Agent(
    name="Text to SQL converter",
    instructions=instructions,
    model=model_name,
    tools=[execute_sql] 
)
