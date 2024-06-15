-- Create database
CREATE DATABASE IF NOT EXISTS sae24;
USE sae24;

-- Create table Salle
CREATE TABLE Salle (
    NomSalle VARCHAR(30) PRIMARY KEY,
    Bat VARCHAR(5),
    Longueur INT NOT NULL,
    Largeur INT NOT NULL
);

-- Create table Capteur
CREATE TABLE Capteur (
    IDcapteur INT AUTO_INCREMENT PRIMARY KEY,
    TypeCapt VARCHAR(10) NOT NULL,
    NomSalle VARCHAR(30) NOT NULL,
    Pos_X INT NOT NULL,
    Pos_Y INT NOT NULL,
    FOREIGN KEY (NomSalle) REFERENCES Salle(NomSalle)
);

-- Create table Data
CREATE TABLE Data (
    IDdata INT AUTO_INCREMENT PRIMARY KEY,
    X INT NOT NULL,
    Y INT NOT NULL,
    Date DATE NOT NULL,
    Time TIME NOT NULL,
    TypeCapt VARCHAR(10) NOT NULL,
    NomSalle VARCHAR(30) NOT NULL,
    FOREIGN KEY (NomSalle) REFERENCES Salle(NomSalle)
);
