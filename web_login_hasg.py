# web_login_hash.py

import sqlite3
from flask import Flask, request, render_template_string
import bcrypt

# Usuarios válidos del grupo
usuarios_validos = ["lucas gonzalez", "benjamin chavez"]

# Inicializa la base de datos SQLite
def init_db():
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            usuario TEXT,
            hash_pass TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Agrega usuarios con contraseñas hasheadas
def agregar_usuario(usuario, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    hash_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    c.execute("INSERT INTO usuarios (usuario, hash_pass) VALUES (?, ?)", (usuario.lower(), hash_pass))
    conn.commit()
    conn.close()

# Valida login
def validar_usuario(usuario, password):
    conn = sqlite3.connect('usuarios.db')
    c = conn.cursor()
    c.execute("SELECT hash_pass FROM usuarios WHERE usuario=?", (usuario.lower(),))
    resultado = c.fetchone()
    conn.close()
    if resultado:
        return bcrypt.checkpw(password.encode(), resultado[0])
    return False

# App web Flask
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    mensaje = ""
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]
        if usuario.lower() in usuarios_validos and validar_usuario(usuario, password):
            mensaje = f"✅ Bienvenido, {usuario}."
        else:
            mensaje = "❌ Usuario o contraseña incorrecta."
    return render_template_string('''
        <h2>Login DRY7122</h2>
        <form method="post">
            Usuario: <input type="text" name="usuario"><br>
            Contraseña: <input type="password" name="password"><br>
            <input type="submit" value="Ingresar">
        </form>
        <p>{{mensaje}}</p>
    ''', mensaje=mensaje)

if __name__ == "__main__":
    init_db()

    # ⚠️ Solo descomentar esto una vez para registrar los usuarios
    agregar_usuario("lucas gonzalez", "clave123")
    agregar_usuario("benjamin chavez", "clave456")

    # Ejecutar en puerto 5800 accesible en DEVASC
    app.run(host="0.0.0.0", port=5800)

