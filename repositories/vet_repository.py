from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets( name ) VALUES ( %s ) RETURNING id"
    values = [vet.name]
    results = run_sql( sql, values )
    vet.id = results[0]['id']
    return vet


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)
    for row in results:
        user = Vet(row['name'], row['id'])
        vets.append(user)
    return vets


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        vet = Vet(result['name'], result['id'] )
    return vet


def delete_all():
    sql = "DELETE FROM vets"
    run_sql(sql)
