from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load saved model
model = joblib.load("model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        hours = float(request.form['hours'])
        sleep = float(request.form['sleep'])
        previous = float(request.form['previous'])

        prediction = model.predict([[hours, sleep, previous]])

        return render_template('index.html', result=round(prediction[0], 2))

    return render_template('index.html')  # 👈 this line is key

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)