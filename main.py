import subprocess

def get_wifi_password(profile_name):
    try:
        # Run netsh command to show Wi-Fi profile details
        command = ["netsh", "wlan", "show", "profile", profile_name, "key=clear"]
        output = subprocess.check_output(command, shell=True, text=True)

        # Parse output for "Key Content"
        for line in output.splitlines():
            if "Key Content" in line:
                return line.split(":")[1].strip()
        return "Password not found."
    except Exception as e:
        return f"Error: {e}"

# Example usage
wifi_name = "Your_WiFi_Name"  # Replace with your Wi-Fi name
print(get_wifi_password(wifi_name))