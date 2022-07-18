from db.run_sql import run_sql
from models.vet import Vet

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
    vet.id = results[0][0]
    return vet
