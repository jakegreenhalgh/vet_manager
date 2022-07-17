DROP TABLE vets;
DROP TABLE pets
DROP TABLE treatments;

CREATE TABLE vets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  type VARCHAR(255),
  dob VARCHAR(255),
  contact_number INT,
  vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE treatments (
  id SERIAL PRIMARY KEY,
  date_performed VARCHAR,
  pet_id INT NOT NULL REFERENCES pets(id) ON DELETE CASCADE,
  vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE,
  notes TEXT
);