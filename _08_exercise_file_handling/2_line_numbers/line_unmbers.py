from string import punctuation

with open("text.txt") as read_file, open("output.txt", "w") as write_file:
    for idx, line in enumerate(read_file):
        letters = 0
        punctuations_count = 0

        for char in line:
            if char.isalpha():
                letters += 1
            elif char in punctuation:
                letters += 1

        write_file.write(f'Line {idx +1}: {line.rstrip()} ({letters})({punctuations_count})\n')