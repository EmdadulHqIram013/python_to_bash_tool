import os
import tempfile
import subprocess

def validate_python_code(code):
    try:
        compile(code, '<string>', 'exec')
        return True, ""
    except SyntaxError as e:
import os
import tempfile
import subprocess

def validate_python_code(code):
    try:
        compile(code, '<string>', 'exec')
        return True, ""
    except SyntaxError as e:
        return False, str(e)

def python_to_bash(python_code, save_directory):
    temp_file = tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False)
    temp_file.write(python_code)
    temp_file.close()
   
    os.makedirs(save_directory, exist_ok=True)

    bash_script_file = os.path.join(save_directory, "converted_script.sh")

    bash_script = f"""#!/bin/bash
python3 {temp_file.name}
"""

    with open(bash_script_file, "w") as f:
        f.write(bash_script)
    subprocess.run(["chmod", "+x", bash_script_file])
   
    print(f"Successfully converted Python code to Bash script: {bash_script_file}")
    return temp_file.name, bash_script_file

def cleanup_temp_file(temp_file):
    try:
        os.remove(temp_file)
        print(f"Temporary file {temp_file} deleted.")
    except Exception as e:
        print(f"Error deleting temporary file: {e}")
