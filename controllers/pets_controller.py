from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    treatments = pet_repository.treatments(pet)
    return render_template("pets/show.html", pet=pet, treatments=treatments)


@pets_blueprint.route("/pets/new", methods=['GET'])
def new_pet():
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    return render_template("pets/new.html", vets = vets, owners=owners)

@pets_blueprint.route("/pets",  methods=['POST'])
def create_pet():
    pet_name = request.form['name']
    pet_type = request.form['type']
    pet_dob = request.form['dob']
    owner = owner_repository.select(request.form['pet_owner'])
    vet = vet_repository.select(request.form['pet_vet'])
    pet = Pet(pet_name, pet_type, pet_dob, owner, vet, id)
    pet_repository.save(pet)
    return redirect('/pets')


@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')
