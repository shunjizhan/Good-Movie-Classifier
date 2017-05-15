import sys
from sklearn.tree import DecisionTreeClassifier

def readFile(filename):
  lines = [line.rstrip('\n').rstrip('\r').split(' ')[1:] for line in open(filename)]
  return lines

def decision_tree_predict(features):
  budget = features[0]
  genre = features[1]
  actor = features[2]
  director = features[3]
  if (genre == "0"):    # documentary
    if (budget == "0"):
      return "0"
    else:
      return "1"
  elif (genre == "1"):  # Drama
    if (budget == "0"):
      if (actor == "1"):
        return "0"
      else:
        return "1"
    else:
      return "1"
  else:                 # comedy
    if(director == "0"):
      return "0"
    else:
      if (budget == "0"):
        return "1"
      if (budget == "1"):
        return "0"
      else:
        return "1"

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

clf = DecisionTreeClassifier(random_state=0)
clf.fit(features, values)

# prediction = clf.predict(features_test)
prediction = []
for i in range (0, len(features_test)):
  prediction.append(decision_tree_predict(features_test[i]))

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

# print "True positives = {}".format(TP)
# print "True negatives = {}".format(TN)
# print "False positives = {}".format(FP)
# print "False negatives = {}".format(FN)
# print "Error rate = {}".format(err)

same = []
correct = 0
for i in range(0, len(values_test)):
  if (values_test[i] == prediction[i]):
    same.append('1')
    correct += 1
  else:
    same.append('0')

print values_test
print prediction
print same
print correct * 1.0 / len(values_test)







