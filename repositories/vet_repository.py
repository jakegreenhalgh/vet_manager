from db.run_sql import run_sql
from models.vet import Vet
from models.pet import Pet

def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        vet = Vet(row['name'], row['id'])
        vets.append(vet)
    return vets


def select(id):
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        vet = Vet(result['name'], result['id'] )
    return vet

def delete(id):
    sql = "DELETE FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)

def save(vet):
    sql = "INSERT INTO vets( name ) VALUES ( %s ) RETURNING id"
    values = [vet.name]
    results = run_sql( sql, values )
    vet.id = results[0]['id']
    return vet

def pets(vet):
    pets = []

    sql = '''
    SELECT pets.* FROM pets
    INNER JOIN vets
    ON pets.vet_id = vets.id
    WHERE vets.id = %s
    '''
    values = [vet.id]
    results = run_sql(sql, values)

    for row in results:
        pet = Pet(row['name'], row['type'], row['dob'], row['contact_number'], vet, row['id'])
        pets.append(pet)

    return pets