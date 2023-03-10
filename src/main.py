"""
    Language Modeling Virtual Machine (LMVM) is a Python-based virtual machine that utilizes language modeling
    techniques to interact with a Docker Alpine Linux container.
"""
import os
from dotenv import load_dotenv
load_dotenv()

from core.lmagent import LmAgent

if __name__ == '__main__':
    print("Language Modeling Virtual Machine (LMVM)")
    print("""
  _      __  ____      ____  __ 
 | |    |  \/  \ \    / /  \/  |
 | |    | \  / |\ \  / /| \  / |
 | |    | |\/| | \ \/ / | |\/| |
 | |____| |  | |  \  /  | |  | |
 |______|_|  |_|   \/   |_|  |_|

 OPEN-SOURCE PROJECT | https://github.com/ansi-code/lmvm
 by Andrea Silvi (ansi-code)

 Language Modeling Virtual Machine (LMVM) is a Python-based virtual machine that utilizes language modeling 
 techniques to interact with a Docker Alpine Linux container.
    """)
    print('\n')

    agent = LmAgent(openai_api_key=os.getenv('OPENAI_API_KEY'))
    agent.run(goal="Create a test folder, go into it, and show the final path")
    # agent.run(goal="Write an Hello World Python program and run it")
