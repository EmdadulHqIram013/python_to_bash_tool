import argparse
import os
from python_to_bash.converter import python_to_bash, validate_python_code, cleanup_temp_file

def main():
    parser = argparse.ArgumentParser(description="Convert Python script to a Bash script.")
    parser.add_argument('save_directory', nargs='?', default=os.path.join(os.path.expanduser('~'), 'Downloads'),
                        help="Directory to save the Bash script.")
    args = parser.parse_args()
    
    save_directory = args.save_directory

    print("Please enter your Python code (end with Ctrl-D):")
    python_code = sys.stdin.read()

    is_valid, error_msg = validate_python_code(python_code)
    if not is_valid:
        print(f"Invalid Python code: {error_msg}")
        return

    temp_file, bash_script = python_to_bash(python_code, save_directory)
    
    cleanup_choice = input("Do you want to delete the temporary Python file? (yes/no): ").strip().lower()
    if cleanup_choice == 'yes':
        cleanup_temp_file(temp_file)
    else:
        print(f"Temporary file kept at: {temp_file}")

if __name__ == "__main__":
    main()
