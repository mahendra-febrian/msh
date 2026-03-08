import sys


def main():
    while True:
        # TODO: Uncomment the code below to pass the first stage
        sys.stdout.write("$ ")

        # Wait for user input
        command = input()

        if command == "exit":
            break

        if command.startswith("echo"):
            print(command[5:])
        elif command.startswith("type"):
            if command[5:] in ["exit", "echo", "type"]:
                print(f"{command[5:]} is a shell builtin")
            else:
                print(f"{command[5:]}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
