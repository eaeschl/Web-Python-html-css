# print("Hello world!")
a = "Edsel"
# print("Hola "+a+", como estás?...")
from flask import Flask

app = Flask(__name__)
@app.route('/hello')
def pagina_inicial():
    return "Hola "+a+", como estás?..."

@app.route('/test')
def pagina_inicial():
    return "Esta es una prueba... "