# adk_orchestrator/tools/xface_tools.py
from adk.tools import FunctionTool
import time

def execute_shell_command_mock(command: str, exec_dir: str = "/app") -> dict:
    """
    (MOCK) Executes a shell command. This function simulates calling the
    xface Sandbox API by printing the command and returning a success message.
    """
    print(f"--- MOCK TOOL CALLED ---")
    print(f"Executing command: '{command}' in directory: '{exec_dir}'")
    print(f"------------------------")

    # Simulate a network delay
    time.sleep(1)

    return {
        "success": True,
        "message": f"Command '{command}' executed successfully in mock environment.",
        "data": {
            "session_id": "mock_session_123",
            "status": "completed",
            "returncode": 0
        }
    }

# Instantiate the tool for the ADK using the mock function
shell_tool = FunctionTool(
    fn=execute_shell_command_mock,
    description="A tool to execute shell commands in a secure, isolated environment."
)
