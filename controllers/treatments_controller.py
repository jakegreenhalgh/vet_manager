from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.treatment import Treatment
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

treatments_blueprint = Blueprint("treatments", __name__)

@treatments_blueprint.route("/treatments")
def treatments():
    treatments = treatment_repository.select_all()
    return render_template("treatments/index.html", treatments = treatments)

@treatments_blueprint.route("/treatments/<id>")
def show(id):
    treatment = treatment_repository.select(id)
    return render_template("treatments/show.html", treatment=treatment)

@treatments_blueprint.route("/treatments/new", methods=['GET'])
def new_treatment():
    vets = vet_repository.select_all()
    pets = pet_repository.select_all()
    return render_template("treatments/new.html", vets = vets, pets=pets)

@treatments_blueprint.route("/treatments",  methods=['POST'])
def create_treatment():
    date_performed = request.form['date_performed']
    vet_id = request.form['vet_id']
    pet_id = request.form['pet_id']
    notes = request.form['notes']
    vet = vet_repository.select(vet_id)
    pet = pet_repository.select(pet_id)
    treatment = Treatment(date_performed, vet, pet, notes)
    treatment_repository.save(treatment)
    return redirect('/treatments')


@treatments_blueprint.route("/treatments/<id>/delete", methods=['POST'])
def delete_treatment(id):
    treatment_repository.delete(id)
    return redirect('/treatments')
