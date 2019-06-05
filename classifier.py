import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model, metrics
from sklearn.naive_bayes import MultinomialNB
from get_features import train_set
from get_features import test_set
def pad_to_square(M):
    maxlen = 2579#max(len(row) for row in M)
    zeros = np.zeros((len(M),maxlen))
    for enu, row in enumerate(M):
        zeros[enu, :len(row)] += row
    return zeros
vtrain_data = []
for feature, gender in train_set:
    row = []
    for key, value in feature[0].items():
        row.append(value)
    for value in feature[1]:
        row.append(float(value))
    for key, value in feature[2].items():
        row.append(value)
    vtrain_data.append(row)

vtrain_data = np.array(vtrain_data)

vtrain_data = pad_to_square(vtrain_data)

vtest_data = []
for feature, gender in test_set:
    row = []
    for key, value in feature[0].items():
        row.append(value)
    for value in feature[1]:
        row.append(float(value))
    for key, value in feature[2].items():
        row.append(value)
    vtest_data.append(row)

vtest_data = np.array(vtest_data)

vtest_data = pad_to_square(vtest_data)


train_target = [int(gender=='M') for t, gender in train_set]
eval_target = [int(gender=='M') for t, gender in test_set]

print("Multinomial Naive Bayes:")
# create multinomial NM object
clf = MultinomialNB()

# train the model using the training sets
clf.fit(vtrain_data, train_target)

# then scoring
x = clf.score(vtrain_data, train_target)

y = clf.score(vtest_data,eval_target)
# predict the gender for the testing data
nb_pred = clf.predict(vtest_data)

print("training fit score:",x)
print("testing fit score:",y)
print("Naive Bayes prediction for testing set:",nb_pred)
print("Evaluation target", eval_target)
match = [i for i, j in zip(nb_pred, eval_target) if i == j]
print(match)
print("number classified correctly:",len(match))
print("Linear regression:")

#linear regression model
# create linear regression object
reg = linear_model.LinearRegression()

# train the model using the training sets
reg.fit(vtrain_data, train_target)
z = reg.score(vtrain_data,train_target)

print("training fit score:",z)

# regression coefficients
print('Coefficients: \n', reg.coef_)

# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(vtest_data, eval_target)))
# predict gender for testing
lin_pred = reg.predict(vtest_data)

# plotting linear regression results
fig, ax = plt.subplots()
plt.title("Linear Regression Results")
plt.ylim(-5,5) # cutting out the outliers
ax.scatter(eval_target, lin_pred, edgecolors=(0, 0, 0))
ax.plot([0,1], [0,1], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
