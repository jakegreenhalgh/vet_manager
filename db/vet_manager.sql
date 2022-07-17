DROP TABLE pets
DROP TABLE vets;
DROP TABLE treatments;

CREATE TABLE vets (
  id SERIAL PRIMARY KEY,
  vet_name VARCHAR(255)
);

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  pet_name VARCHAR(255),
  animal_type VARCHAR(255),
  date_of_birth VARCHAR(255)
  owner_contact_number INT(255)
  vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE treatments (
  id SERIAL PRIMARY KEY,
  pet_id INT NOT NULL REFERENCES petss(id) ON DELETE CASCADE,
  vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE,
  treatment_notes TEXT
);