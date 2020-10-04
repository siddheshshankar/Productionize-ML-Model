# Importing the necessary Libraries
import pickle
from flask_cors import cross_origin
from flask import Flask, render_template, request

app = Flask(__name__)

filename = 'survival_prediction.pickle'
model = pickle.load(open(filename, 'rb'))


@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def homepage():
    if request.method == 'POST':
        pclass = request.form['pclass']
        sex = request.form['sex']
        age = request.form['age']
        sibsp = request.form['sibsp']
        parch = request.form['parch']
        fare = request.form['fare']

        conditions = {
            'Pclass': pclass,
            'Sex': sex,
            'Age': age,
            'SibSp': sibsp,
            'Parch': parch,
            'Fare': fare
        }

        try:
            survival_prediction = model.predict([list(conditions.values())])
        except ValueError:
            return_str = 'Please fill all the fields.'
            return render_template('main.html', return_str=return_str)

        if survival_prediction[0] == 0.0:
            return_str = 'With the given conditions model predicts that person may not survive.'
            return render_template('main.html', return_str=return_str)
        else:
            return_str = 'With the given conditions model predicts that person may survive.'
            return render_template('main.html', return_str=return_str)

    else:
        return render_template('main.html')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
