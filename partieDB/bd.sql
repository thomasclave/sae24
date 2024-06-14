-- Création de la base de données
CREATE DATABASE IF NOT EXISTS sae24;
USE sae24;

-- Création de la table Salle
CREATE TABLE Salle (
    Nom VARCHAR(30) PRIMARY KEY,
    Bat VARCHAR(5),
    Longueur INT, 
    Largeur INT 
);

-- Création de la table Capteur
CREATE TABLE Capteur (
    IDcapteur INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(10),
    NomSalle VARCHAR(30),
    Pos_X INT,
    Pos_Y INT,
    FOREIGN KEY (NomSalle) REFERENCES Salle(Nom)
);

-- Création de la table Data
CREATE TABLE Data (
    IDdata INT AUTO_INCREMENT PRIMARY KEY,
    X INT,
    Y INT,
    Date DATE,
    Time TIME,
    Type VARCHAR(10),
    NomSalle VARCHAR(30),
    FOREIGN KEY (NomSalle) REFERENCES Salle(Nom)
);
