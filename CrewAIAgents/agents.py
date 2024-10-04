from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()
import os

os.environ['OPENAI_API_KEY']= os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME'] = 'gpt-4-0125-preview'

# create a Research Agent with YT videos

blog_researcher= Agent(
    role= 'Blog researcher from Youtube videos',
    goal= 'Get the relevant video content for the topic {topic} from YT channel',
    verbose= True,
    memory= True,
    backstory= (
        "Expert in understanding videos in AI data science, machine learning and Gen AI and providing suggetions."
    ),
    tools=[yt_tool],
    llm='gpt-4-0125-preview',
    allow_delegation=True
)


# creating a senior blog writer agent with YT tools

blog_writer= Agent(
    role= 'Blog writer',
    goal= 'Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory= True,
    backstory=(
    """
    with a flair for simplifying complex topics, you craft
    engaging narratives that captivate and educate, brining new
    discoveries to light in an accessible manner
    """
    ),
    tools=[yt_tool],
    llm='gpt-4-0125-preview',
    allow_delegation=False
)