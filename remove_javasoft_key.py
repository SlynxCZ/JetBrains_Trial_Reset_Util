import subprocess

def remove_javasoft_key():
    result = subprocess.run(["reg", "delete", "HKEY_CURRENT_USER\\Software\\JavaSoft", "/f"], capture_output=True, text=True)
    if result.returncode == 0:
        return True, "JavaSoft key removed successfully."
    else:
        return False, f"Failed to remove the JavaSoft key:\n{result.stderr}"