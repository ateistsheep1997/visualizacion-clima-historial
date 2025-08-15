from flask import Flask, render_template
import pandas as pd

# Inicializa la aplicación Flask
app = Flask(__name__)

# Define la ruta principal que renderiza la plantilla index.html
@app.route('/')