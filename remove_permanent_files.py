import os
import shutil

def remove_permanent_files():
    appdata_path = os.getenv("APPDATA")
    jetbrains_path = os.path.join(appdata_path, "JetBrains")
    messages = []
    try:
        os.remove(os.path.join(jetbrains_path, "PermanentUserId"))
        messages.append("PermanentUserId removed successfully.")
    except FileNotFoundError:
        messages.append("PermanentUserId file not found.")
    except Exception as e:
        messages.append(f"Failed to remove PermanentUserId. Error: {e}")

    try:
        os.remove(os.path.join(jetbrains_path, "PermanentDeviceId"))
        messages.append("PermanentDeviceId removed successfully.")
    except FileNotFoundError:
        messages.append("PermanentDeviceId file not found.")
    except Exception as e:
        messages.append(f"Failed to remove PermanentDeviceId. Error: {e}")

    return messages