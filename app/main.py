import sys
import os


def main():
    while True:
        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        # Check if the user input is the "exit" command
        if command == "exit":
            break

        # Check if the user input is the "echo" command
        elif command.startswith("echo"):
            print(command[5:])

        # Check if the user input is the "type" command
        elif command.startswith("type"):
            command = command[5:]

            # Check if the argument is a shell builtin
            if command in ["exit", "echo", "type"]:
                print(f"{command} is a shell builtin")

            # Check if the argument exists in the PATH
            else:
                path = os.environ.get("PATH", "")
                path_dirs = path.split(os.pathsep)
                found = False

                for directory in path_dirs:
                    path = os.path.join(directory, command)
                
                    if os.path.exists(path) and os.access(path, os.X_OK):
                        full_path = path
                        print(f"{command} is {full_path}")
                        found = True
                        break

                # If the command_name is not found
                if not found:
                    print(f"{command}: not found")

        # If the user_input is not found
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()