import sys
import os
import subprocess
import shlex

def find_in_PATH(command):
    for path in os.environ.get("PATH", "").split(os.pathsep):
        full_path = os.path.join(path, command)

        if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
            return full_path

    return None

def main():
    while True:
        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        tokens = shlex.split(command);
        command = tokens[0]
        arguments = tokens[1:]

        if ">" in arguments or "1>" in arguments:
            os.system(command)

        # Check if the user input refers to the "exit" command
        if command == "exit":
            break

        # Check if the user input refers to the "echo" command
        elif command.startswith("echo"):
            print(" ".join(arguments))

        # Check if the user input refers to the "pwd" command
        elif command == "pwd":
            print(os.getcwd())

        # Check if the user input refers to the "cd" command
        elif command.startswith("cd"):
            directory = arguments[0]

            if os.path.exists(directory):
                os.chdir(directory)
            elif directory == "~":
                os.chdir(os.getenv('HOME'))
            else:
                print(f"cd: {directory}: No such file or directory")

        # Check if the user input refers to the "type" command
        elif command.startswith("type"):
            arguments = arguments[0]

            # Check if the argument refers to a shell builtin
            if arguments in ["exit", "echo", "type", "pwd", "cd"]:
                print(f"{arguments} is a shell builtin")

            # Check if the argument refers to an existing executable in the PATH
            else:
                full_path = find_in_PATH(arguments)

                if full_path:
                    print(f"{arguments} is {full_path}")
                else:
                    print(f"{arguments}: not found")

        # Check if the argument refers to an existing executable in the PATH
        else:
            full_path = find_in_PATH(command)

            if full_path:
                subprocess.call([command] + arguments)
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()