from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet

def save(pet):
    sql = "INSERT INTO pets( name ) VALUES ( %s ) RETURNING id"
    values = [pet.name]
    results = run_sql( sql, values )
    pet.id = results[0]['id']
    return pet


def select_all():
    pets = []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)
    for row in results:
        pet = pet(row['name'], row['id'])
        pets.append(pet)
    return pets


def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        pet = pet(result['name'], result['id'] )
    return pet


def delete_all():
    sql = "DELETE FROM pets"
    run_sql(sql)

def locations(pet):
    locations = []

    sql = '''
    SELECT locations.* FROM locations
    INNER JOIN visits
    ON visits.location_id = locations.id
    WHERE visits.pet_id = %s
    '''
    values = [pet.id]
    results = run_sql(sql, values)

    for row in results:
        location = Location(row['name'], row['category'], row['id'])
        locations.append(location)

    return locations
