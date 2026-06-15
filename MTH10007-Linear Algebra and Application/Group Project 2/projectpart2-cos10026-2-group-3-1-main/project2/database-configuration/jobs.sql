USE project2_db;

CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    banner TEXT,
    aside TEXT,
    first_section TEXT,
    second_section TEXT,
    title VARCHAR(200),
    reference VARCHAR(20),
    salary VARCHAR(100),
    description TEXT,
    responsibilities TEXT,
    skills TEXT,
    apply TEXT
);