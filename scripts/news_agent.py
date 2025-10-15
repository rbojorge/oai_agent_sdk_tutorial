import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in the enviroment variables")

# import Agent, Runner and **function_tool**, then we define a llm model
from agents import Agent, Runner, function_tool, WebSearchTool

from pydantic import BaseModel

llm_model = "gpt-4o-mini"

# create the agent
web_search_agent = Agent(
    name="News Agent",
    instructions="""
        You are a news agent that can search the web for the latest news on a given topic.
        Compile the information you find into a concise 1 paragraph summary. No markdown, just plain text.
    """,
    model=llm_model,
    tools=[
        WebSearchTool(),
    ],
)

while True:
    query = input("Enter your news query (or 'quit' to exit): ")
    if query.lower() == "quit":
        break

    result = Runner.run_sync(web_search_agent, input=query)
    print("\nResult:")
    print(result.final_output)
    print("\n" + "-" * 50 + "\n")
