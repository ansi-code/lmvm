import re
import subprocess

import openai


class LmAgent:
    def __init__(self, openai_api_key):
        openai.api_key = openai_api_key

    def run(self, goal):
        state = ""
        action = ""
        result = ""
        while True:
            print(f"{HEADER}\nGOAL \"{goal}\"\nSTATE \"{state}\"\nACTION \"{action}\"\nRESULT \"{result}\"\n")

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"{HEADER}\nGOAL \"{goal}\"\nSTATE \"{state}\"\nACTION \"{action}\"\nRESULT \"{result}\"\n",
                temperature=1,
                max_tokens=256,
                top_p=1,
                best_of=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            print(response)

            message = response.choices[0].text.strip()

            match = re.search(r"NEXT_ACTION \"(.*)\"", message)
            if match is None:
                break
            next_action = match.group(1)
            if next_action is "":
                break

            match = re.search(r"NEXT_STATE \"(.*)\"", message)
            if match is None:
                break
            next_state = match.group(1)
            if next_state is "":
                break

            state = next_state
            action = next_action

            print(f"Executing: {action}")
            result = subprocess.getoutput(action)

        return result


HEADER = """
[LMVM]
The Language Modeling Virtual Machine (LMVM) is a tool for interacting with a computer operating system using natural language commands. LMVM uses OpenAI's GPT language model to interpret and execute commands.

[GOAL]
The user provides a natural language description of a task they wish to accomplish. LMVM will attempt to translate this description into a sequence of executable commands that achieve the desired outcome.

[STATE]
LMVM maintains a string representing the current state of the system, which is updated after each command is executed. This state may be used by LMVM to generate subsequent commands.

[ACTION]
LMVM generates a string containing a command to be executed based on the current state and the desired outcome. This command may involve calling one or more system utilities or executing a script.

[RESULT]
After each command is executed, LMVM captures the output produced by the command as a string and stores it in the RESULT field. The output format should be a single line containing the relevant information, such as the path to a file or directory or the result of a computation. If the command produces no output, the RESULT field should be left blank.

[FORMAT]
The output format for commands executed by LMVM should be consistent across all actions. The output should be a string containing two lines of text, formatted as follows:

NEXT_STATE "state"
NEXT_ACTION "action"

Here, "state" should be the name of the next state of the system, and "action" should be the command to be executed to transition to that state. If there is no next state or action to be executed, the corresponding field should be left blank.
"""
