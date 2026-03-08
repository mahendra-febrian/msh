import sys
import os
import subprocess

def search_in_PATH(command, path_dirs):
    found = False

    for directory in path_dirs:
        path = os.path.join(directory, command)
                
        if os.path.exists(path) and os.access(path, os.X_OK):
            full_path = path
            found = True
            return full_path
            break

    # If the command_name is not found
    if not found:
        return False

def main():
    while True:
        #Initialize path
        path = os.environ.get("PATH", "")
        path_dirs = path.split(os.pathsep)

        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        # Check if the user input refers to the "exit" command
        if command == "exit":
            break

        # Check if the user input refers to the "echo" command
        elif command.startswith("echo"):
            print(command[5:])

        # Check if the user input refers to the "type" command
        elif command.startswith("type"):
            arguments = command[5:]

            # Check if the argument refers to a shell builtin
            if arguments in ["exit", "echo", "type"]:
                print(f"{arguments} is a shell builtin")

            # Check if the argument refers to an existing executable in the PATH
            else:
                result = search_in_PATH(arguments, path_dirs)

                if not result:
                    print(f"{arguments}: not found")
                else:
                    print(f"{arguments} is {result}")

        # Check if the argument refers to an existing executable in the PATH
        else:
            result = search_in_PATH(command, path_dirs)

            if not result:
                print(f"{command}: command not found")
            else:
                command = command.split(" ")
                args = command[1:]
                command = command[0]
                
                subprocess.call([command] + args)

if __name__ == "__main__":
    main()