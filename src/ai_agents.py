from dotenv import load_dotenv
from agents import Agent
from tools import execute_sql

load_dotenv()

converter_agent = Agent(
    name="Text to SQL converter",
    instructions="""
        You are a database assistant for SQLite.

        Convert the user's request into a safe SELECT query, call the execute_sql tool, and return the result clearly.

        Rules:
        - Only use SELECT queries.
        - Never use DROP, DELETE, UPDATE, INSERT, ALTER, CREATE, or PRAGMA.
        - If the request is unsafe, return UNSAFE_QUERY.
        - Use only existing tables and columns.
        """,
    model="gpt-4o-mini",
    tools=[execute_sql]

)