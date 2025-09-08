# adk_orchestrator/agents/sheikh_agent.py
import os
from adk.agents import LlmAgent
from adk.models.llms import Gemini
from dotenv import load_dotenv
from tools.xface_tools import shell_tool

load_dotenv()

# Configure the agent to use the Gemini model
gemini_model = Gemini(api_key=os.getenv("GEMINI_API_KEY"))

# Define the main Sheikh agent
SheikhAgent = LlmAgent(
    name="Sheikh",
    model=gemini_model,
    instruction=(
        "You are Sheikh, a general-purpose AI software engineering agent. "
        "Your goal is to complete user requests by executing commands in a secure shell. "
        "Analyze the user's request, plan the necessary shell commands, and use your tool to execute them one by one."
    ),
    tools=[
        shell_tool,
        # We can add more tools here (e.g., file_tool, browser_tool)
    ],
)
