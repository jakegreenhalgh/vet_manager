import pdb
from controllers.user_controller import users
from models.owner import Owner
from models.treatment import Treatment
from models.vet import Vet

import repositories.owner_repository as owner_repository
import repositories.treatment_repository as treatment_repository
import repositories.vet_repository as vet_repository

visit_repository.delete_all()
location_repository.delete_all()
user_repository.delete_all()

user1 = User('Samwise Gamgee')
user_repository.save(user1)

user2 = User('Frodo Baggins')
user_repository.save(user2)

user3 = User('Gollum')
user_repository.save(user3)

location1 = Location('Mordor', 'Attractions')
location_repository.save(location1)

location2 = Location('The Prancing Pony', 'Tavern')
location_repository.save(location2)

visit1 = Visit(user1, location1, '0 stars, far too hot')
visit_repository.save(visit1)

visit2 = Visit(user3, location1, '5 stars, would visit again if I could')
visit_repository.save(visit2)

visit3 = Visit(user1, location2, '4 stars, plenty of beer available')
visit_repository.save(visit3)

visit4 = Visit(user2, location2, '3 stars, too crowded, could not find my wizard friend')
visit_repository.save(visit4)

# user1_locations = user_repository.locations(user1)

# for location in user1_locations:
#     print(location.__dict__)

location1_users = location_repository.users(location1)

for location in location1_users:
    print(location.__dict__)

pdb.set_trace()
