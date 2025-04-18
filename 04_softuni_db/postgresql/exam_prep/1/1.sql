CREATE TABLE owners
(
    id           SERIAL PRIMARY KEY,
    name         VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    address      VARCHAR(50)
);

CREATE TABLE animal_types
(
    id          SERIAL PRIMARY KEY,
    animal_type VARCHAR(30) NOT NULL
);

CREATE TABLE cages
(
    id             SERIAL PRIMARY KEY,
    animal_type_id INTEGER NOT NULL,
    FOREIGN KEY (animal_type_id) REFERENCES animal_types (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE animals
(
    id             SERIAL PRIMARY KEY,
    name           VARCHAR(30) NOT NULL,
    birthdate      DATE        NOT NULL,
    owner_id       INTEGER,
    animal_type_id INTEGER     NOT NULL,
    FOREIGN KEY (owner_id) REFERENCES owners (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (animal_type_id) REFERENCES animal_types (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

CREATE TABLE volunteers_departments
(
    id              SERIAL PRIMARY KEY,
    department_name VARCHAR(30) NOT NULL
);

CREATE TABLE volunteers
(
    id            SERIAL PRIMARY KEY,
    name          VARCHAR(50) NOT NULL,
    phone_number  VARCHAR(15) NOT NULL,
    address       VARCHAR(50),
    animal_id     INTEGER,
    department_id INTEGER     NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES animals (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (department_id) REFERENCES volunteers_departments (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

create TABLE animals_cages
(
    cage_id   INTEGER NOT NULL,
    animal_id INTEGER NOT NULL,
    FOREIGN KEY (cage_id) REFERENCES cages (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (animal_id) REFERENCES animals (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);