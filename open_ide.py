import subprocess
from find_tool_executable import find_tool_executable
from tool_details import TOOL_DETAILS

def open_ide(tool_name):
    tool_keyword, executable_name = TOOL_DETAILS[tool_name]
    tool_executable = find_tool_executable(tool_keyword, executable_name)

    if tool_executable:
        try:
            subprocess.Popen([tool_executable])
            return True, f"{tool_name} opened successfully."
        except Exception as e:
            return False, f"Failed to open {tool_name}. Error: {e}"
    else:
        return False, f"Executable for {tool_name} not found. Make sure it is installed."