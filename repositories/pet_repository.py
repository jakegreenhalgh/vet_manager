from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet
import repositories.vet_repository as vet_repository

def save(pet):
    sql = "INSERT INTO pets( name, type, dob, contact_number, vet_id ) VALUES ( %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.type, pet.dob, pet.contact_number, pet.vet.id]
    results = run_sql( sql, values )
    pet.id = results[0]['id']
    return pet


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
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        pet = Pet(result['name'], result['type'], result['dob'], result['contact_number'], result['vet'], result['id'])
    return pet


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

