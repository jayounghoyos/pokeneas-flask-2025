from flask import Blueprint, jsonify, render_template
import random
import socket
from app.models import POKENEAS
from app.aws_utils import get_image_url

bp = Blueprint('main', __name__)

def get_container_id():
    """Obtiene el ID del contenedor Docker"""
    return socket.gethostname()

@bp.route('/')
def index():
    """Página de inicio"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pokeneas - Pokédex Paisa</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .container {
                background: white;
                border-radius: 20px;
                padding: 40px;
                box-shadow: 0 20px 60px rgba(0,0,0,0.3);
                text-align: center;
                max-width: 500px;
            }
            h1 { color: #333; }
            .links {
                margin-top: 30px;
            }
            .btn {
                display: block;
                margin: 15px 0;
                padding: 15px 30px;
                background: #667eea;
                color: white;
                text-decoration: none;
                border-radius: 10px;
                font-size: 18px;
                transition: all 0.3s;
            }
            .btn:hover {
                background: #5568d3;
                transform: translateY(-2px);
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1> Pokeneas </h1>
            <p>Pokédex de criaturas legendarias</p>
            <div class="links">
                <a href="/pokenea/json" class="btn"> Ver Pokenea (JSON)</a>
                <a href="/pokenea/image" class="btn"> Ver Pokenea (Imagen)</a>
            </div>
        </div>
    </body>
    </html>
    """

@bp.route('/pokenea/json')
def pokenea_json():
    """Ruta 1: Devuelve JSON con datos de un Pokenea aleatorio"""
    pokenea = random.choice(POKENEAS)
    
    return jsonify({
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "container_id": get_container_id()
    })

@bp.route('/pokenea/image')
def pokenea_image():
    """Ruta 2: Muestra imagen y frase de un Pokenea aleatorio"""
    pokenea = random.choice(POKENEAS)
    image_url = get_image_url(pokenea["imagen"])
    container_id = get_container_id()
    
    return render_template(
        'pokenea_image.html',
        pokenea=pokenea,
        image_url=image_url,
        container_id=container_id
    )