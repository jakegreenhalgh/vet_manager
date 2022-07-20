from db.run_sql import run_sql
from models.treatment import Treatment
from models.pet import Pet
import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository

def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        vet = vet_repository.select(row['vet_id'])
        owner = owner_repository.select(row['owner_id'])
        pet = Pet(row['name'], row['type'], row['dob'], owner, vet, row['id'])
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
        owner = owner_repository.select(result['owner_id'])
        result = Pet(result['name'], result['type'], result['dob'], owner, vet, result['id'])
    return result


def save(pet):
    sql = "INSERT INTO pets( name, type, dob, owner_id, vet_id ) VALUES ( %s, %s, %s, %s, %s) RETURNING id"
    values = [pet.name, pet.type, pet.dob, pet.owner.id, pet.vet.id]
    results = run_sql( sql, values )
    print(results)
    pet.id = results[0]['id']
    return pet

def update(pet):
    sql = "UPDATE pets SET (name, type, dob, owner_id, vet_id) = ( %s, %s, %s, %s, %s) WHERE id = %s"
    values = [pet.name, pet.type, pet.dob, pet.owner.id, pet.vet.id, pet.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)

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
        treatment = Treatment(row['check_in'], row['check_out'], vet, pet, row['notes'], row['id'])
        treatments.append(treatment)

    return treatments
