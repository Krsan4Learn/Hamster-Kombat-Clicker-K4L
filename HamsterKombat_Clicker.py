import importlib.util
import sys
import subprocess
import base64

# List of required packages
required_packages = ['pyautogui', 'keyboard', 'pyfiglet', 'rich' ]

# Function to check and install packages
def check_and_install_packages(packages):
    for package in packages:
        spec = importlib.util.find_spec(package)
        if spec is None:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        else:
            print(f"{package} is already installed.")

# Check and install required packages
check_and_install_packages(required_packages)

# Now import the libraries
import pyautogui
import time
import keyboard
import pyfiglet
from rich.console import Console
from rich.panel import Panel
from time import sleep


# Encoded information (base64 encoded)
encoded_info = """
QnkgLS0+OiB3d3cua3JzYW40bGVhcm4uY29tCllvdXRib29rIC0+OiB3d3cueW91dHViZS5jb20vQGtyc2FuNGxlYXJuCnRlbGVncmFtZSAtLT46ICBAIG9tYXJtb2htYWQ=
"""

def decode_info(encoded_info):
    decoded_info = base64.b64decode(encoded_info).decode('utf-8')
    return decoded_info

# Function to generate ASCII art image
def generate_ascii_image(text):
    ascii_banner = pyfiglet.figlet_format(text)
    return ascii_banner

# Function to show intro
def show_intro():
    console = Console()

    # Convert text to a Rich Text object for progressive display
    ascii_banner = generate_ascii_image("krsan4learn.com")
    console.print(ascii_banner)

    sleep(1)

    # Display rights information inside the box
    decoded_info = decode_info(encoded_info)
    console.print(Panel(decoded_info, expand=False, border_style="bold magenta"))

    sleep(2)
    console.clear()

# Function to handle main logic
def main():
    # Number of clicks per second
    clicks_per_second = 1000

    # Calculate the time between clicks
    interval = 1 / clicks_per_second

    # Display the intro screen
    show_intro()

    # Message to the user to confirm that the script has started (to avoid accidental clicks)
    input("Press 'Enter' to start clicking : ")

    # Get the current location of the mouse
    x, y = pyautogui.position()

    # A message is displayed to the user informing him to click on (s) if he wants to stop the program
    print("The script is working now ، Press the letter 's' to stop the script.")

    try:
        # Clicking started
        while not keyboard.is_pressed('s'):
            pyautogui.click(x, y)
            time.sleep(interval)
    except KeyboardInterrupt:
        print("The script has been stopped by the user!.")
    finally:
        print("The script has been stopped!.")

# Run as the main program
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
