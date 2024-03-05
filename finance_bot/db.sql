CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(20) UNIQUE
);

CREATE TABLE item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT(200) NOT NULL,
    cost INTEGER NOT NULL,
    date TEXT NOT NULL,  
    category INTEGER,
    FOREIGN KEY(category) REFERENCES category(id)
);

INSERT into category(name) VALUES
('food'),
('entertainment'),
('house'),
('comunication'),
('transport'),
('toiletry'),
('other');
