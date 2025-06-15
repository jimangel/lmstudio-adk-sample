import os
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm  # For multi-model support
from .sub_agents.google_search_agent import google_search_agent
from google.adk.tools.agent_tool import AgentTool

# enable "server" in developer mode and load a model (might not be needed)
os.environ['LM_STUDIO_API_BASE'] = "http://127.0.0.1:1234/v1/"

root_agent = Agent(
    name="weather_agent_gpt",
    model=LiteLlm(model="lm_studio/qwen3-1.7b"), # gemma-3-1b
    description="Provides information.",
    instruction="You are a helpful assistant."
                "Use the 'google_search' tool for real-time requests or data."
                "Present information clearly.",
    #tools=[get_weather, get_current_time],
    tools=[
        AgentTool(agent=google_search_agent),
    ],
)
