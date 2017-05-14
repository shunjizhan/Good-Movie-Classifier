import sys
from sklearn.tree import DecisionTreeClassifier

def readFile(filename):
  lines = [line.rstrip('\n').rstrip('\r').split(' ')[1:] for line in open(filename)]
  return lines

#~~ main ~~#
trainingData = readFile(sys.argv[1])[1:]
testingData = readFile(sys.argv[2])[1:]
features = []
features_test = []
values = []
values_test = []

for one in trainingData:
  features.append(one[:-1])
  values.append(one[-1])

for one in testingData:
  features_test.append(one[:-1])
  values_test.append(one[-1])

clf = DecisionTreeClassifier(random_state = 0, criterion='entropy')
clf.fit(features, values)

prediction = clf.predict(features_test)

N = len(prediction)
TP = 0
FN = 0
TN = 0
FP = 0
for i in range (0, N):
  if (prediction[i] == values_test[i]):
    if (prediction[i] == "1"):
      TP += 1
    else:
      TN += 1
  else:
    if (prediction[i] == "1"):
      FP += 1
    else:
      FN += 1
err = (FN + FP) * 1.0 / N

print "True positives = {}".format(TP)
print "True negatives = {}".format(TN)
print "False positives = {}".format(FP)
print "False negatives = {}".format(FN)
print "Error rate = {}".format(err)