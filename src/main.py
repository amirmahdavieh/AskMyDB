import asyncio
from agents import Runner
from ai_agents import converter_agent

async def main():
    result = await Runner.run(
        converter_agent,
        "Retrieve the names of the employees with more than 90000 salary."
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())