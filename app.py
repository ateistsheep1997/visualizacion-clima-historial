from flask import Flask, render_template
import pandas as pd

# Initialize the Flask application
app = Flask(__name__)

# Define the home route that renders the index.html template
@app.route('/')
def home():
    return render_template('index.html')

# Run the application in debug mode if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)