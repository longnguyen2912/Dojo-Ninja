from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')


@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template('dojos.html', dojos=dojos)

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    print(request.form)
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def get_dojos(id):
    data = {
        "id":id
    }
    dojo = Dojo.get_ninja(data)
    return render_template('dojoShow.html', dojo = dojo)