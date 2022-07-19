from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
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
    owner = owner(owner_name, id)
    owner_repository.save(owner)
    return redirect('/owners')


@owners_blueprint.route("/owners/<id>/delete", methods=['POST'])
def delete_task(id):
    owner_repository.delete(id)
    return redirect('/owners')
