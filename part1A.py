import math
from collections import Counter

def readFile(filePath):
    with open(filePath, 'r') as file:
        return file.read()
    
def preProcessing(text):
    # Keep only alphabetic characters, convert to lowercase and remove the spaces and special characters...
    return ''.join(char.lower() for char in text if char.isalpha())

def calculateProb(events):
    total_events = len(events)
    frequency = Counter(events)
    # print(f"Frequencies of all the alphabets {frequency}")
    probabilities = {event: round(count / total_events , 10) for event, count in frequency.items()}
    return sorted(probabilities.items(),key =lambda x: x[1],reverse=True)

def top10Events(probabilities,n=10):
    return probabilities[:n]

def analysisFileA(filePath):
    print("\nPART (a): Analyze Letters for fileA")
    text = readFile(filePath)
    letters = preProcessing(text)
    # print(letters)
    probabilities = calculateProb(letters)
    print(f"Probabilities of all the alphabets: {probabilities}")
    topLetters = top10Events(probabilities, 10)
    print(f"Top 10 Letters in fileA: {topLetters}")
    return probabilities



filePathA='./fileA.txt'
# filePathB='./fileB.txt'
# filePathC='./fileC.txt'
# filePathD='./fileD.txt'

# (a) Determine the probability of each alphabet in the English language. Upper-case
# and lower-case alphabets are considered the same. List the top ten alphabets that
# occur in fileA.
if __name__ == "__main__":
    probA = analysisFileA(filePathA)







