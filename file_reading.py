#Create a variable
vocab = {}

# Read document, "r" stands for read and encoding="utf-8" is so we can use ä, ö, ü
with open("Vocab.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split("\t")
        # the “\t” splits the line into two parts using the tab
        if len(parts) == 2:
            english, german = parts
            vocab[english.strip()] = german.strip()
