from db.run_sql import run_sql
from models.treatment import Treatment
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

def select_all():
    treatments = []

    sql = "SELECT * FROM treatments"
    results = run_sql(sql)

    for row in results:
        pet = pet_repository.select(row['pet_id'])
        vet = vet_repository.select(row['vet_id'])
        treatment = Treatment(row['check_in'], row['check_out'], vet, pet, row['notes'], row['id'])
        treatments.append(treatment)
    return treatments

def select(id):
    result = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        pet = pet_repository.select(result['pet_id'])
        vet = vet_repository.select(result['vet_id'])
        result = Treatment(result['check_in'], result['check_out'], vet, pet, result['notes'], result['id'])
    return result

def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(treatment):
    sql = "INSERT INTO treatments ( check_in, check_out, pet_id, vet_id, notes ) VALUES ( %s, %s, %s, %s, %s ) RETURNING id"
    values = [treatment.check_in, treatment.check_out, treatment.pet.id, treatment.vet.id, treatment.notes]
    results = run_sql( sql, values )
    treatment.id = results[0]['id']
    return treatment

def update(treatment):
    sql = "UPDATE treatments SET (check_in, check_out, pet_id, vet_id, notes) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [treatment.check_in, treatment.check_out, treatment.pet.id, treatment.vet.id, treatment.notes, treatment.id]
    run_sql(sql, values)