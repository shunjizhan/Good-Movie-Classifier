import sys
from sklearn.tree import DecisionTreeClassifier

def readFile(filename):
  lines = [line.rstrip('\n').rstrip('\r').split(' ')[1:] for line in open(filename)]
  return lines



trainingData = readFile(sys.argv[1])[1:]
testingData = readFile(sys.argv[2])[1:]
features = []
features_test = []
values = []
values_test = []

for one in trainingData:
  # print one
  features.append(one[:-1])
  values.append(one[-1])

for one in testingData:
  # print one
  features_test.append(one[:-1])
  values_test.append(one[-1])




clf = DecisionTreeClassifier(random_state=0)
clf.fit(features, values)

prediction = clf.predict(features_test)
print list(map(int, prediction))
print list(map(int, values_test))
# print features_test
# print " "
# print values_test
