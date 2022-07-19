from db.run_sql import run_sql
from models.treatment import Treatment
from models.pet import Pet
import repositories.vet_repository as vet_repository

def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['type'], row['dob'], row['contact_number'], vet, row['id'])
        pets.append(pet)
    return pets


def select(id):
    result = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        vet = vet_repository.select(result['vet_id'])
        result = Pet(result['name'], result['type'], result['dob'], result['contact_number'], vet, result['id'])
    return result


def save(pet):
    sql = "INSERT INTO pets( name, type, dob, contact_number, vet_id ) VALUES ( %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.type, pet.dob, pet.contact_number, pet.vet.id]
    results = run_sql( sql, values )
    pet.id = results[0]['id']
    return pet


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def treatments(pet):
    treatments = []
    vet = None

    sql = '''
    SELECT treatments.* FROM treatments
    INNER JOIN pets
    ON treatments.pet_id = pets.id
    WHERE pets.id = %s
    '''
    values = [pet.id]
    results = run_sql(sql, values)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        treatment = Treatment(row['date_performed'], vet, pet, row['notes'], row['id'])
        treatments.append(treatment)

    return treatments
