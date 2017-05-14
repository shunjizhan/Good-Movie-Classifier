import sys
from sklearn.tree import DecisionTreeClassifier

def readFile(filename):
  lines = [line.rstrip('\n').rstrip('\r').split(' ')[1:] for line in open(filename)]
  return lines



trainingData = readFile(sys.argv[1])[1:]
features = []
values = []

for one in trainingData:
  print one
  # features.append(one[:-1])
  # values.append[one[-1:]]

testingData = readFile(sys.argv[2])

clf = DecisionTreeClassifier(random_state=0)
# clf.fit(features, values)

# print features
# print values
