from db.run_sql import run_sql
from models.owner import Owner
from models.vet import Vet
from models.pet import Pet
import repositories.vet_repository as vet_repository

def select_all():
    owners = []

    sql = "SELECT * FROM owners"
    results = run_sql(sql)
    for row in results:
        owner = Owner(row['name'], row['contact_number'], row['registered'], row['id'] )
        owners.append(owner)
    return owners


def select(id):
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        owner = Owner(result['name'], result['contact_number'], result['registered'], result['id'] )
    return owner

def delete(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def save(owner):
    sql = "INSERT INTO owners( name, contact_number, registered ) VALUES ( %s, %s, %s ) RETURNING id"
    values = [owner.name, owner.contact_number, owner.registered]
    results = run_sql( sql, values )
    owner.id = results[0]['id']
    return owner

def pets(owner):
    pets = []

    sql = '''
    SELECT pets.* FROM pets
    INNER JOIN owners
    ON pets.owner_id = owners.id
    WHERE owners.id = %s
    '''
    values = [owner.id]
    results = run_sql(sql, values)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['name'], row['type'], row['dob'], owner, vet, row['id'])
        pets.append(pet)

    return pets