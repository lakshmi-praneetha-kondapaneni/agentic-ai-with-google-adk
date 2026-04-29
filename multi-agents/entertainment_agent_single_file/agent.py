from google.adk.agents import LlmAgent
MODEL_NAME="gemini-2.5-flash"

joke_agent = LlmAgent(
    name="joke_agent",
    model=MODEL_NAME,        
    instruction="""Tell a joke when asked.""",
    description="An agent which create jokes",
    )

story_agent = LlmAgent(
    name="story_agent",
    model=MODEL_NAME,    
    instruction="""Choose a random topic and write a 10 lines story.""",
    description="An agent which is good at writing small stories",
    )


song_agent = LlmAgent(
    name="song_agent",
    model=MODEL_NAME,
    instruction="""Choose a random topic and write a 4 lines song.""",
    description="An agent which is good at writing small songs",
)

# Define the root  agent
root_agent = LlmAgent(
    name="entertainment_agent",
    model=MODEL_NAME,
    instruction="""You are a entertainer which uses other available agents to write stories, songs or jokes 
         Instructions:
         - Please greet the user and offer the services you provide and ask for thier choice
         - Based on user preference use of the sub agents to get the output and present to the user""",
    description="An agent which entertains people with songs, stories or jokes",
    sub_agents=[song_agent, story_agent, joke_agent],
)