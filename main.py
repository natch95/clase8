#Dependencias
import os
import sqlite3
from flask import Flask, render_template, request, session, escape
from flask import redirect, url_for, g
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mail import Mail, Message

#Configuracion general del software
app = Flask(__name__)
app.config['DEBUG'] = True

#Configuracion del email
app.config.update(
    DEBUG=True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT= 465,
    MAIL_USE_TLS= False,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'masterlist.suppliers@gmail.com',
    MAIL_PASSWORD= 'Celeste:801020363'
)
mail = Mail(app)

@app.route('/crearempresa', methods=['GET', 'POST'])
def crearempresa():
    if request.method == "GET":
        return render_template("crearempresa.html", contact=None)

    if request.method == "POST":
        contact=request.form.to_dict()
        values=[contact['entidad'],contact['tel'],contact['email'],contact['representante'],contact['usuario'],contact['emailusuario']]
            change_db("INSERT INTO contact(entidad,tel,email,representante,usuario,emailusuario) VALUES(?,?,?,?,?,?,?,?,?,?,?)")
        return redirect(url_for("empresa"))

if __name__ == "__main__"
    db.create_all()
    app.run(debug=True)
