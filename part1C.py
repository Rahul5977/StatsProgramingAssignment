from part1A import readFile,calculateProb,top10Events
from part1B import entropyCalculation

def preProssesWord(text):
    # Remove punctuation, convert to lowercase, and split into words
    return ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text).split()

def analyzeWords(file_path, file_label):
    print(f"\nPART (c): Analyze Words for {file_label}")
    text = readFile(file_path)
    words = preProssesWord(text)
    probabilities = calculateProb(words)
    # print(f"Probabilities :{probabilities}")
    # entropy = entropyCalculation(probabilities)
    top_words = top10Events(probabilities, n=10)
    # print(f"Entropy of Words in {file_label}: {entropy}")
    print(f"Top 10 Words in {file_label}: {top_words}")
    return probabilities

def analyzeWordsD(file_path, file_label):
    print(f"\nPART (c): Analyze Words for {file_label}")
    text = readFile(file_path)
    words = preProssesWord(text)
    probabilities = calculateProb(words)
    entropy = entropyCalculation(probabilities)
    # top_words = top10Events(probabilities, n=10)
    print(f"Entropy of Words in {file_label}: {entropy}")
    # print(f"Top 10 Words in {file_label}: {top_words}")
    # return probabilities, entropy

filePathC='./fileC.txt'
filePathD='./fileD.txt'
if __name__ == "__main__":
    probC = analyzeWords(filePathC, "fileC")
    entropyD = analyzeWordsD(filePathD, "fileD")