from xml.dom.domreg import registered
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
from models.owner import Owner
import repositories.owner_repository as owner_repository

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    return render_template("owners/index.html", owners = owners)

@owners_blueprint.route("/owners/<id>")
def show(id):
    owner = owner_repository.select(id)
    pets= owner_repository.pets(owner)
    return render_template("owners/show.html", owner=owner, pets=pets)


@owners_blueprint.route("/owners/new", methods=['GET'])
def new_owner():
    owners = owner_repository.select_all()
    return render_template("owners/new.html", owners = owners)

@owners_blueprint.route("/owners",  methods=['POST'])
def create_owner():
    owner_name = request.form['owner_name']
    contact_number = request.form['contact_number']
    registered = True
    owner = Owner(owner_name, contact_number, registered, id)
    owner_repository.save(owner)
    return redirect('/owners')

@owners_blueprint.route("/owners/<id>/edit", methods = ["GET"])
def edit(id):
    owner = owner_repository.select(id)
    return render_template("/owners/edit.html", owner = owner)

@owners_blueprint.route("/owners/<id>", methods = ["POST"])
def update(id):
    owner_name = request.form['owner_name']
    contact_number = request.form['contact_number']
    registered = True
    owner = Owner(owner_name, contact_number, registered, id)
    owner_repository.update(owner)
    return redirect(f"/owners/{owner.id}")

@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_owner(id):
    owner_repository.delete(id)
    return redirect('/owners')
