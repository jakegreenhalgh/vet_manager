from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", pets = pets)

@pets_blueprint.route("/pets/<id>")
def show(id):
    pet = pet_repository.select(id)
    return render_template("pets/show.html", pet=pet)


@pets_blueprint.route("/pets/new", methods=['GET'])
def new_pet():
    vets = vet_repository.select_all()
    return render_template("pets/new.html", vets = vets)

@pets_blueprint.route("/pets",  methods=['POST'])
def create_pet():
    pet_name = request.form['name']
    pet_type = request.form['type']
    pet_dob = request.form['dob']
    contact_number = request.form['contact_number']
    vet = vet_repository.select(pet_vet)
    pet = Pet(pet_name, pet_type, pet_dob, contact_number, vet, id)
    pet_repository.save(pet)
    return redirect('/pets')


@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_task(id):
    pet_repository.delete(id)
    return redirect('/pets')
