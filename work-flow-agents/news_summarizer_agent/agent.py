from google.adk.agents import SequentialAgent
from .sub_agents.summarizer import summarizer_agent
from .sub_agents.web_searcher import news_reader_agent


# Define the root  agent
root_agent = SequentialAgent(
    name="news_summarizer_agent",
    #model="gemini-2.5-flash",
    description="An agent that searches for and summarizes news on a given topic.",
    sub_agents=[news_reader_agent,summarizer_agent],
)

