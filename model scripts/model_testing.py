import pickle
filename = 'survival_prediction.pickle'
model = pickle.load(open(filename, 'rb'))
conditions = {
                'Pclass': 1,
                'Sex': 1,
                'Age': 0,
                'SibSp': 3,
                'Parch': 4,
                'Fare': 28.80
             }
survival_prediction = model.predict([list(conditions.values())])

if survival_prediction[0] == 0.0:
    print('With the given conditions model predicts that person may not survive.')
else:
    print('With the given conditions model predicts that person may survive.')
