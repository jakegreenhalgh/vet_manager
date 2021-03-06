DROP TABLE vets;
DROP TABLE owners;
DROP TABLE pets;
DROP TABLE treatments;

CREATE TABLE vets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE owners (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  contact_number VARCHAR(255),
  registered BOOLEAN
);

CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  type VARCHAR(255),
  dob DATE,
  owner_id INT NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
  vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE
);

CREATE TABLE treatments (
  id SERIAL PRIMARY KEY,
  check_in DATE,
  check_out DATE,
  pet_id INT NOT NULL REFERENCES pets(id) ON DELETE CASCADE,
  vet_id INT NOT NULL REFERENCES vets(id) ON DELETE CASCADE,
  notes TEXT
);