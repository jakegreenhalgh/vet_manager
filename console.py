from models.pet import Pet
from models.treatment import Treatment
from models.vet import Vet
from models.owner import Owner

import repositories.vet_repository as vet_repository
import repositories.owner_repository as owner_repository
import repositories.pet_repository as pet_repository
import repositories.treatment_repository as treatment_repository

treatment_repository.delete_all()
pet_repository.delete_all()
owner_repository.delete_all()
vet_repository.delete_all()

vet1 = Vet("Kay Neine")
vet_repository.save(vet1)

vet2 = Vet("Jim McFursson")
vet_repository.save(vet2)

owner1 = Owner("Sue", "55548523", True)
owner_repository.save(owner1)

owner2 = Owner("Bob", "5559314", True)
owner_repository.save(owner2)

owner3 = Owner("John", "5559314", True)
owner_repository.save(owner3)

owner4 = Owner("Skrek", "5559345", True)
owner_repository.save(owner4)

pet1 = Pet("Hooty Owlson", "Owl", "07/05/2008", owner1, vet1)
pet_repository.save(pet1)

pet2 = Pet("Hamela Anderson", "Pig", "12/02/2010", owner2, vet2)
pet_repository.save(pet2)

pet3 = Pet("Llama Del Rey", "Llama", "19/10/2015", owner2, vet2)
pet_repository.save(pet3)

pet4 = Pet("Chewbarkka", "Dog", "27/04/2010", owner3, vet1)
pet_repository.save(pet4)

pet5 = Pet("Donkey", "Donkey", "22/04/2001", owner4, vet1)
pet_repository.save(pet5)

treatment1 = Treatment("15/07/2022", vet1, pet1, "Patient had a broken wing")
treatment_repository.save(treatment1)