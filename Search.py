import requests
import random
import string
import re
from sys import exit
from colorama import Fore, Style

import signal

def signal_handler(sig, frame):
    print(f"\n{Fore.RED}Process interrupted by user. Exiting...{Style.RESET_ALL}")
    exit(0)

signal.signal(signal.SIGINT, signal_handler)

print(rf"""
{Fore.YELLOW}
    Coded By GhosT LulzSec
    Telegram : @WW6WW6WW6
    GitHub: https://github.com/69d9
    All rights reserved.

            o  o   o  o
         |\/ \^/ \/|  
         |,-------.|  
       ,-.(|)   (|),-. 
       \_*._ ' '_.* _/  
        /-.--' .-`\  
   ,--./    `---'    \,--. 
   \   |(  )     (  )|   /  
hjw \  |         |  /  
`97  \ | /|\     /|\ | /  
     /  \-._     _,-/  \  
    //| \  `---'  // |\\  
   /,-.,-.\       /,-.,-.\  
  o   o   o      o   o    o  
""")

try:
    search = input(f"{Fore.CYAN}Please enter a keyword to search for onion links: {Style.RESET_ALL}")
    number = int(input(f"{Fore.CYAN}How many onion links would you like to retrieve? {Style.RESET_ALL}"))

    if " " in search:
        search = search.replace(" ", "+")

    url = f"https://ahmia.fi/search/?q={search}"

    with open("user-agents.txt", "r+") as a:
        users = random.choice(a.readlines()).strip()

    header = {
        "User-Agent": users
    }

    results_limt = number
    result_collected = 0

    webs = requests.get(url, headers=header).text
    reg = r"\w+\.onion"
    data = re.findall(reg, webs)
    filename = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(5))
    data = list(dict.fromkeys(data))

    with open(f"{filename}.txt", "a+") as f:
        for i in data:
            if result_collected >= results_limt:
                break
            i = i + "\n"
            f.write(i)
            result_collected += 1

    print(f"{Fore.BLUE}\nProcess completed successfully! All results have been saved in: {filename}.txt{Style.RESET_ALL}")

except KeyboardInterrupt:
    print(f"\n{Fore.RED}Process interrupted by user. Exiting...{Style.RESET_ALL}")
    exit(0)
except Exception as e:
    print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
    exit(1)
