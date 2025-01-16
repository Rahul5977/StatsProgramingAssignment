# (b) The measure of uncertainty is determined by its entropy. Entropy should be com-
# puted as
# X
# H= (−pi log pi )
# where pi is the probability of event i. If we consider the occurrence of alphabets in
# English as events of interest, determine the entropy. In other words, determine the
# uncertainty of alphabets in the English language using fileB.

from part1A import readFile,preProcessing,calculateProb,math
# import math

def entropyCalculation(probabilities):
    return -sum(p * math.log2(p) for _, p in probabilities if p>0)

def analyseFileB(filePath):
    print("\nPART (b): Analyze Letters for fileB")
    text = readFile(filePath)
    letters = preProcessing(text)
    probabilities = calculateProb(letters)
    # print(f"Probabilities :{probabilities}")
    entropy = entropyCalculation(probabilities)
    print(f"Entropy of Letters in fileB: {entropy}")
    return entropy
if __name__ == "__main__":

    filePathB='./fileB.txt'
    entropy=analyseFileB(filePathB)