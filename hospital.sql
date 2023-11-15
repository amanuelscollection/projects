/*
This code was written to create a database for a hospital with several different tables to represent the different moving parts in one.
*/

DROP DATABASE IF EXISTS hospital;
CREATE DATABASE hospital;
USE hospital;

CREATE TABLE Patient
(PatientID INT PRIMARY KEY,
Name VARCHAR(255),
Address VARCHAR(255),
PhoneNumber VARCHAR(15));

CREATE TABLE HealthRecord
(RecordID INT PRIMARY KEY,
PatientID INT,
Disease VARCHAR(255),
Date DATE,
Status VARCHAR(255),
Description TEXT,
FOREIGN KEY (PatientID) REFERENCES Patient(PatientID));

CREATE TABLE Room
(RoomNumber INT PRIMARY KEY,
Capacity INT,
FeePerNight DECIMAL(10,2));

CREATE TABLE Physician 
(PhysicianID INT PRIMARY KEY,
Name VARCHAR(255),
CertificationNumber VARCHAR(255),
FieldOfExpertise VARCHAR(255),
Address VARCHAR(255),
PhoneNumber VARCHAR(15));

CREATE TABLE Nurse 
(NurseID INT PRIMARY KEY,
Name VARCHAR(255),
CertificationNumber VARCHAR(255),
Address VARCHAR(255),
PhoneNumber VARCHAR(15));

CREATE TABLE Instruction 
(InstructionCode INT PRIMARY KEY,
Fee DECIMAL(10,2),
Description TEXT);

CREATE TABLE Medication 
(MedicationID INT PRIMARY KEY,
Name VARCHAR(255),
AmountPerDay INT);

CREATE TABLE Care 
(CareID INT PRIMARY KEY,
PatientID INT,
NurseID INT,
InstructionCode INT,
Date DATE,
Status VARCHAR(255),
FOREIGN KEY (PatientID) REFERENCES Patient(PatientID),
FOREIGN KEY (NurseID) REFERENCES Nurse(NurseID),
FOREIGN KEY (InstructionCode) REFERENCES Instruction(InstructionCode));

CREATE TABLE Invoice 
(InvoiceID INT PRIMARY KEY,
PatientID INT,
Date DATE,
Amount DECIMAL(10,2),
FOREIGN KEY (PatientID) REFERENCES Patient(PatientID));

CREATE TABLE Payment 
(PaymentID INT PRIMARY KEY,
PatientID INT,
Date DATE,
Amount DECIMAL(10,2),
FOREIGN KEY (PatientID) REFERENCES Patient(PatientID));
