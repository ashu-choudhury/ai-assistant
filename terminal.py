# Copyright 2025 Ashu Choudhury
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import subprocess


def shel(command: str):

    """
    Execute a Windows shell command and return its output, error, and return code.

    **Important Notes**:
    - This function is designed for Windows machines.
    - It allows you to run single commands one by one.
    - If a command asks for user input (like yes/no), it cannot answer interactively.
    - You can run commands that automatically handle prompts by appending the necessary flags (e.g., `-y` with `npm init`).

    **Editing or Modifying Commands**:
    - If you'd like to modify or specify a specific file path for a command, please provide the **full path** to the executable or the script. For example:
        - `"C:\\Program Files\\NodeJS\\npm.exe init -y"`
        - `"C:\\path\\to\\your\\script.bat"`

    Parameters:
        command (str): 
            The Windows shell command to execute. This can be any valid command 
            that runs in the Windows Command Prompt. Commands that require automatic 
            confirmation, like `npm init -y`, are ideal for this use case.

    Returns:
        dict: 
            A dictionary containing the following fields:
            - "returncode" (int): The exit code of the command. `0` indicates success.
            - "stdout" (str): The standard output of the command, stripped of trailing whitespace.
            - "stderr" (str): The standard error of the command, stripped of trailing whitespace.
            - "success" (bool): A convenience field that is `True` if the return code is `0`, and `False` otherwise.

        If an exception occurs, the dictionary will contain:
            - "error" (str): A description of the exception that occurred.
    """
    try:
        # Start the process with Popen
        cmd = subprocess.Popen(
            command, 
            shell=True,          # Enable shell execution
            text=True,           # Use strings instead of bytes
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE   # Capture standard error
        )
        
        # Wait for the process to complete and capture output
        stdout, stderr = cmd.communicate()
        
        # Return the result in a structured dictionary
        return {
            "returncode": cmd.returncode,
            "stdout": stdout.strip(),
            "stderr": stderr.strip(),
            "success": cmd.returncode == 0  # Determine success based on return code
        }
    except Exception as e:
        # Handle and return any exception that occurs
        return {
            "error": str(e),
        }
