import os
import subprocess
import glob

def find_tool_executable(tool_keyword, executable_name):
    program_files = os.environ.get("PROGRAMFILES", r"C:\Program Files")
    user_profile = os.environ.get("USERPROFILE")
    local_programs = os.path.join(user_profile, "AppData", "Local", "Programs")

    potential_paths = [
        os.path.join(program_files, "JetBrains"),
        os.path.join(local_programs)
    ]

    for jetbrains_path in potential_paths:
        # Debug: print the paths being searched
        print(f"Searching in: {jetbrains_path}")

        search_pattern = os.path.join(jetbrains_path, f"*{tool_keyword}*\\bin\\{executable_name}")
        matching_executables = glob.glob(search_pattern, recursive=True)

        # Debug: print the matching executables found
        print(f"Matching executables: {matching_executables}")

        if matching_executables:
            return matching_executables[0]  # Return the first matching executable

    return None