from flask import Flask, render_template, request
import pickle

app = Flask(__name__) 
model = pickle.load(open('saved_model3.sav', 'rb'))

# Define a dictionary that maps flower classes to their respective image paths
flower_images = {
    "Iris-setosa": "/static/images/Irissetosa.png",
    "Iris-versicolor": "/static/images/Irisversicolor.png",
    "Iris-virginica": "/static/images/Irisvirginica.png"
}



@app.route('/')
def home():
    result = ''
    image_url = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    # Get input from form
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])
    
    # Make the prediction
    result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    
    # Get the image URL based on the prediction result
    image_url = flower_images.get(result, "static/images/default.jpg")  # Default image in case prediction fails
    
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
