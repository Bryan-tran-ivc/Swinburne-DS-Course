USE project2_db;
CREATE TABLE IF NOT EXISTS eoi (
    EOInumber INT AUTO_INCREMENT PRIMARY KEY,
    JobReferenceNumber VARCHAR(100) NOT NULL,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATETIME,
    Gender VARCHAR(10) NOT NULL,
    StreetAddress VARCHAR(100) NOT NULL,
    SuburbTown VARCHAR(50) NOT NULL,
    State VARCHAR(20) NOT NULL,
    Postcode VARCHAR(10) NOT NULL,
    EmailAddress VARCHAR(100) NOT NULL,
    PhoneNumber VARCHAR(15) NOT NULL,
    Skills TEXT,
    OtherSkills TEXT,
    Terms BOOLEAN NOT NULL,
    Status ENUM('New', 'Current', 'Final') DEFAULT 'New'
);
