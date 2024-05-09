# Python to Bash Tool

A simple command-line tool to convert Python scripts to Bash scripts.

## Features

- Convert Python code to a Bash script
- Validates Python code syntax before conversion
- Option to delete temporary Python file after conversion

## Installation and Execution Instructions:

1. Clone the repository:

   ```bash
   git clone https://github.com/EmdadulHqIram013/python_to_bash_tool.git
   cd python_to_bash_tool

2. Install the Tool with --user Flag::
   ```bash
   pip install --user .
3. Update path
   ```bash
   export PATH=$PATH:~/.local/bin
   echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
   source ~/.bashrc
5. Run the Tool:
   ```bash
   pytobash
