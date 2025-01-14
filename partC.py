from partA import readFile,calculateProb,top10Events
from partB import entropyCalculation
def preprocess_text_for_words(text):
    # Remove punctuation, convert to lowercase, and split into words
    return ''.join(char.lower() if char.isalnum() or char.isspace() else ' ' for char in text).split()

def analyze_words(file_path, file_label):
    print(f"\nPART (c): Analyze Words for {file_label}")
    text = readFile(file_path)
    words = preprocess_text_for_words(text)
    probabilities = calculateProb(words)
    entropy = entropyCalculation(probabilities)
    top_words = top10Events(probabilities, n=10)
    print(f"Entropy of Words in {file_label}: {entropy}")
    print(f"Top 10 Words in {file_label}: {top_words}")
    return probabilities, entropy

filePathC='./fileC.txt'
filePathD='./fileD.txt'
if __name__ == "__main__":
    probC, entropyC = analyze_words(filePathC, "fileC")
    # probD, entropyD = analyze_words(filePathD, "fileD")