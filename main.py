import os
import json
import requests

import discord

from dotenv import load_dotenv

print(f"""
  _____           _          _____                          
 |  __ \\         | |        / ____|                         
 | |__) __ _ _ __| |_ _   _| |  __  __ _ _ __ ___   ___ ___ 
 |  ___/ _` | '__| __| | | | | |_ |/ _` | '_ ` _ \\ / _ / __|
 | |  | (_| | |  | |_| |_| | |__| | (_| | | | | | |  __\\__ \\
 |_|   \\__,_|_|   \\__|\\__, |\\_____|\\__,_|_| |_| |_|\\___|___/
                       __/ |                                
                      |___/                                 
""")

req = requests.get('https://api.github.com/repos/pjsph/PartyGames/tags')
response = json.loads(req.text)
if req.status_code == 200:
    print(response)
