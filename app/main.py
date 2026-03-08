import sys
import os


def main():
    while True:
        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        # "exit" command
        if command == "exit":
            break

        # "echo" command
        if command.startswith("echo"):
            print(command[5:])

        # "type" command
        elif command.startswith("type"):
            if command[5:] in ["exit", "echo", "type"]:
                print(f"{command[5:]} is a shell builtin")
            elif :
                for
                if os.path.exists(os.path.split(path, os.pathsep)[i]) and os.access(PATH, os.X_OK):
                    print(f"{command[5:]} is {PATH}")
            else:
                print(f"{command[5:]}: not found")

        # Command not found
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
