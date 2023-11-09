from app import app
from flask import redirect

@app.route('/')
def index():
    return redirect("home")

@app.route('/home')
def home():
    """
    Definindo pagina home
    """
    return '<h1>Administracao de Barbearia</h1>'