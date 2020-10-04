# Required Libraries
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

# Reading Dataset
data = pd.read_csv("https://raw.githubusercontent.com/BigDataGal/Python-for-Data-Science/master/titanic-train.csv")
data.columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age',
                'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']

# Dealing with outliers/anomalies/missing data
data['Age'] = data['Age'].fillna(round(data['Age'].mean()))
gender_dict = {'male': 1, 'female': 0}
data.replace(gender_dict, inplace=True)

predictors_vars = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
response_var = ['Survived']

X = data[predictors_vars]
y = data[response_var]

# Data Scaling
scalar = StandardScaler()
X_transform = scalar.fit_transform(X)

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=100)

# Setting up grid parameters and running grid search cross validation for Decision tree classification.
grid_param = {
    'criterion': ['gini', 'entropy'],
    'max_depth': range(2, 20, 1),
    'min_samples_leaf': range(2, 10, 1),
    'min_samples_split': range(2, 10, 1),
    'splitter': ['best', 'random']
}

classifier = DecisionTreeClassifier()

grid_search = GridSearchCV(estimator=classifier,
                           param_grid=grid_param,
                           cv=5,
                           n_jobs=-1)
grid_search.fit(X_train, y_train)
best_parameters = grid_search.best_params_
print(f'Best Parameters are: {best_parameters}')

# Fitting on the basis of best parameters
DTclassifier = DecisionTreeClassifier(criterion='gini',
                                      max_depth=7,
                                      min_samples_leaf=2,
                                      min_samples_split=6,
                                      splitter='random')
DTclassifier.fit(X_train, y_train)

# Model Prediction
y_pred = DTclassifier.predict(X_test)

# Score
print(classification_report(y_test, y_pred))

# Create pickle file
filename = 'survival_prediction.pickle'
pickle.dump(DTclassifier, open(filename, 'wb'))
