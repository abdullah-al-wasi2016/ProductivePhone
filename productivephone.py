"""This is the ProductivePhone, the large project which started at August 2025.
This has more improved code, as this is using Python 3.
"""

print("/" * 10 + " Starting " + "/" * 10)

# Step 1: Import libraries
import pyaudio
import wave
import subprocess
import random
import pyttsx3
import webbrowser
import openai
from dotenv import load_dotenv

# Step 2: Define functions
def CallApp(name, number):
    _my_list = []
    _my_list.append(name)
    _my_list.append(number)
    print(_my_list)
    