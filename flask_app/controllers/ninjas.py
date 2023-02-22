from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/ninjas')
def ninjas():
    return render_template('newNinja.html', dojos= Dojo.get_all())

@app.route('/create/ninja', methods=["POST"])
def newNinja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')
