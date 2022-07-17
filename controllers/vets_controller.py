from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.vet import Vet
import repositories.vet_repository as vet_repository

vets_blueprint = Blueprint("vets", __name__)

@vets_blueprint.route("/vets")
def vets():
    vets = vet_repository.select_all() # NEW
    return render_template("vets/index.html", vets = vets)

@vets_blueprint.route("/vets/<id>")
def show(id):
    vet = vet_repository.select(id)
    return render_template("vets/show.html", vet=vet)
