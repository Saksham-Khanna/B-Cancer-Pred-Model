from flask import Flask, request, render_template
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = request.form['feature']
        features_list = features.split(',')
        features_array = np.array(features_list, dtype=np.float32)

        pred = model.predict(features_array.reshape(1, -1))
        result = 'Cancerous' if pred[0] == 1 else 'Not Cancerous'

        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction="Invalid")

if __name__ == "__main__":
    app.run(debug=True)
