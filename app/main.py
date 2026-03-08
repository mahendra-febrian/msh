import sys
import os
import subprocess

def find_in_PATH(command):
    for path in os.environ.get("PATH", "").split(os.pathsep):
        full_path = os.path.join(directory, command)
                
        if os.path.exists(path) and os.access(path, os.X_OK):
            return full_path

    # If the command_name is not found
    return None

def main():
    while True:
        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        # Parse single quotes
        tokens = []
        current = ""
        is_in_single_quotes = False

        for character in command:
            if character == "'":
                is_in_single_quotes = not is_in_single_quotes
            elif character == " " and not is_in_single_quotes:
                if current:
                    tokens.append(current)
                    current = ""
            else:
                current += character

        if current:
            tokens.append(current)

        # Check if the user input refers to the "exit" command
        if command == "exit":
            break

        # Check if the user input refers to the "echo" command
        elif command.startswith("echo"):
            print(command[5:])

        # Check if the user input refers to the "pwd" command
        elif command == "pwd":
            print(os.getcwd())

        # Check if the user input refers to the "cd" command
        elif command.startswith("cd"):
            arguments = command[3:]

            if os.path.exists(arguments):
                os.chdir(arguments)
            elif arguments == "~":
                home = os.getenv('HOME')
                os.chdir(home)
            else:
                print(f"cd: {arguments}: No such file or directory")

        # Check if the user input refers to the "type" command
        elif command.startswith("type"):
            arguments = command[5:]

            # Check if the argument refers to a shell builtin
            if arguments in ["exit", "echo", "type", "pwd", "cd"]:
                print(f"{arguments} is a shell builtin")

            # Check if the argument refers to an existing executable in the PATH
            else:
                full_path = find_in_PATH(arguments)

                if full_path:
                    print(f"{arguments} is {result}")
                else:
                    print(f"{arguments}: not found")

        # Check if the argument refers to an existing executable in the PATH
        else:
            command = command.split(" ")
            args = command[1:]
            command = command[0]

            full_path = find_in_PATH(command)

            if full_path:
                subprocess.call([command] + args)
            else:
                print(f"{command}: command not found")

if __name__ == "__main__":
    main()