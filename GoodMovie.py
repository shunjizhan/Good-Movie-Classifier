import sys
import math

def readFile(filename):
  lines = [line.rstrip('\n').rstrip('\r') for line in open(filename)]
  return lines

trainingData = readFile(sys.argv[1])[1:]
testingData = readFile(sys.argv[2])

print trainingData
