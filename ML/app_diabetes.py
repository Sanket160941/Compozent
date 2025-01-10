from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the diabetes prediction model
with open(r'C:\Users\Sanket M\OneDrive\Documents\Task List\ML\Diabetes_Prediction\Diabetes_Prediction.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home_page():
    # Renders the home page where the user can input data for prediction
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == "POST":
        data = request.form

        # Collect input features from the form and convert them to the required data types
        pregnancies = int(data.get("pregnancies"))
        glucose = float(data.get("glucose"))
        bloodpressure = float(data.get("bloodpressure"))
        skinthickness = float(data.get("skinthickness"))
        insulin = float(data.get("insulin"))
        bmi = float(data.get("bmi"))
        diabetespedigreefunction = float(data.get("diabetespedigreefunction"))
        age = float(data.get("age"))

        # Prepare the input array
        user_input = np.array([[pregnancies, glucose, bloodpressure, skinthickness, insulin, 
                                bmi, diabetespedigreefunction, age]])
        
        # Use the trained model to predict the diagnosis
        model_output = model.predict(user_input)
        prediction = "Diabetic" if model_output[0] == 1 else "Non-Diabetic"

        return render_template('index.html', prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=8000)
