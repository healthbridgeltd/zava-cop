CREATE DATABASE movies;
USE movies;

CREATE TABLE director (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255)
);

CREATE TABLE film (
    id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    release_year YEAR NOT NULL,
    description TEXT,
    director_id INT UNSIGNED,
    rating INT UNSIGNED,
    FOREIGN KEY (director_id) REFERENCES director (id)
);

INSERT INTO director (name) VALUES ('Steven Spielberg'), ('Stanley Kubrick'), ('Martin Scorsese');
INSERT INTO film (title, release_year, description, director_id, rating)
VALUES
    ('Duel', 1971, 'Big truck chases man in red car.', 1, 88),
    ('The Shining', 1980, 'Man goes mad looking after haunted hotel.', 2, 84),
    ('Goodfellas', 1990, 'Gangsters steal money and kill people.', 3, 96);
