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
    check_in = request.form['check_in']
    check_out = request.form['check_out']
    vet_id = request.form['vet_id']
    pet_id = request.form['pet_id']
    notes = request.form['notes']
    vet = vet_repository.select(vet_id)
    pet = pet_repository.select(pet_id)
    treatment = Treatment(check_in, check_out, vet, pet, notes)
    treatment_repository.save(treatment)
    return redirect('/treatments')


@treatments_blueprint.route("/treatments/<id>/delete", methods=['POST'])
def delete_treatment(id):
    treatment_repository.delete(id)
    return redirect('/treatments')

@treatments_blueprint.route("/treatments/<id>/edit", methods = ["GET"])
def edit(id):
    treatment = treatment_repository.select(id)
    vets = vet_repository.select_all()
    pets = pet_repository.select_all()
    return render_template("/treatments/edit.html", treatment = treatment, pets=pets, vets=vets)

@treatments_blueprint.route("/treatments/<id>", methods = ["POST"])
def update(id):
    check_in = request.form['check_in']
    check_out = request.form['check_out']
    vet_id = request.form['vet_id']
    pet_id = request.form['pet_id']
    notes = request.form['notes']
    vet = vet_repository.select(vet_id)
    pet = pet_repository.select(pet_id)
    treatment = Treatment(check_in, check_out, vet, pet, notes, id)
    treatment_repository.update(treatment)
    return redirect(f"/treatments/{treatment.id}")