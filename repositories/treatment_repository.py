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
        treatment = Treatment(row['date'], pet, vet, row['notes'], row['id'])
        treatments.append(treatment)
    return treatments


def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(treatment):
    sql = "INSERT INTO treatments ( date, pet_id, vet_id, notes ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [treatment.date, treatment.pet.id, treatment.vet.id, treatment.notes]
    results = run_sql( sql, values )
    treatment.id = results[0]['id']
    return treatment
