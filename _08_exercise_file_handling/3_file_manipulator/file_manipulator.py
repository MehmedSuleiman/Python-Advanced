import os

while True :
    line = input()
    if line == 'End':
        break

    command, file_name, *args = line.split("-")
    if command == 'Create':
        with open(file_name, 'w') as f:
            pass

    if command == 'Add':
        file = open(file_name, 'a')
        file.write(args[0]+"\n")
        file.close()

    if command == 'Replace':
        try:
            content = None
            with open(file_name, 'r') as file:
                content = file.read().replace(args[0], args[1])
            with open(file_name, 'w') as file:
                file.write(content)

        except FileNotFoundError:
            print("An error occurred")
    if command == 'Delete':
        try:
            os.remove(file_name)
        except FileNotFoundError:
            print("An error occurred")