# LMVM (Language Modeling Virtual Machine)

LMVM is a Python-based virtual machine that utilizes language modeling techniques to interact with a Docker Alpine Linux container. 
The VM includes a GPT-based policy agent that can execute command line actions and respond with the output. 
The state space is infinite and the agent has a memory, which is included in every request and response. 
The memory is a compressed JSON structure with a maximum size of 128 tokens.

## Getting Started

To use LMVM, you will need to have Docker and Python installed on your system. 
You will also need an OpenAI API key to use the GPT-based policy agent.

Clone the repository:
```bash
$ git clone https://github.com/ansi-code/lmvm.git
```

Install the required Python packages.
```bash
$ pip install -r requirements.txt
```

Set up your OpenAI API key by setting the OPENAI_API_KEY environment variable.

```bash
$ export OPENAI_API_KEY=YOUR_API_KEY
```

Run the main.py script to start the VM.

```bash
$ python src/main.py
```

## Usage
Once the VM is running, you can interact with it by entering commands at the prompt. 
The commands should be framed as actions that the policy agent can execute on the Docker container.
For example, you can enter RUN pwd to execute the pwd command on the container.

The policy agent will generate a response to every command, which will be displayed on the output. 
The response may include information from the memory, which is updated with every command.

You can set a goal for the policy agent to achieve by entering it at the prompt. 
The policy agent will continue to execute commands and generate responses until it achieves the specified goal.

## Contributing

Contributions to LMVM are welcome! 
If you have an idea for a new feature or would like to report a bug, please open an issue or submit a pull request.

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](./LICENSE) file for details.
