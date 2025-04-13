-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS doctors_appointment;

-- Use the database
USE doctors_appointment;

-- Set SQL mode
SET SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO';

-- Enable foreign key checks
SET FOREIGN_KEY_CHECKS = 1;

-- Table structure for table `Patient`
DROP TABLE IF EXISTS `Patient`;
CREATE TABLE `Patient` (
  `patient_id` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `blood_group` varchar(5) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `previous_treatments` text,
  `allergies` text,
  PRIMARY KEY (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Doctor`
DROP TABLE IF EXISTS `Doctor`;
CREATE TABLE `Doctor` (
  `doctor_id` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `experience` int DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`doctor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Appointment`
DROP TABLE IF EXISTS `Appointment`;
CREATE TABLE `Appointment` (
  `appointment_id` int NOT NULL,
  `patient_id` int DEFAULT NULL,
  `doctor_id` int DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` time DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`appointment_id`),
  KEY `patient_id` (`patient_id`),
  KEY `doctor_id` (`doctor_id`),
  CONSTRAINT `Appointment_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `Patient` (`patient_id`),
  CONSTRAINT `Appointment_ibfk_2` FOREIGN KEY (`doctor_id`) REFERENCES `Doctor` (`doctor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Prescription`
DROP TABLE IF EXISTS `Prescription`;
CREATE TABLE `Prescription` (
  `prescription_id` int NOT NULL,
  `appointment_id` int DEFAULT NULL,
  `medicine_name` varchar(255) DEFAULT NULL,
  `dosage` varchar(100) DEFAULT NULL,
  `instructions` text,
  PRIMARY KEY (`prescription_id`),
  KEY `appointment_id` (`appointment_id`),
  CONSTRAINT `Prescription_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `Appointment` (`appointment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Treatment`
DROP TABLE IF EXISTS `Treatment`;
CREATE TABLE `Treatment` (
  `treatment_id` int NOT NULL,
  `appointment_id` int DEFAULT NULL,
  `treatment_name` varchar(100) DEFAULT NULL,
  `cost` decimal(10,2) DEFAULT NULL,
  `duration` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`treatment_id`),
  KEY `appointment_id` (`appointment_id`),
  CONSTRAINT `Treatment_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `Appointment` (`appointment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Medical_Report`
DROP TABLE IF EXISTS `Medical_Report`;
CREATE TABLE `Medical_Report` (
  `record_id` int NOT NULL,
  `patient_id` int DEFAULT NULL,
  `diagnosis` text,
  `previous_treatments` text,
  `allergies` text,
  PRIMARY KEY (`record_id`),
  KEY `patient_id` (`patient_id`),
  CONSTRAINT `Medical_Report_ibfk_1` FOREIGN KEY (`patient_id`) REFERENCES `Patient` (`patient_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Payment`
DROP TABLE IF EXISTS `Payment`;
CREATE TABLE `Payment` (
  `payment_id` int NOT NULL,
  `appointment_id` int DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `payment_method` varchar(50) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `appointment_id` (`appointment_id`),
  CONSTRAINT `Payment_ibfk_1` FOREIGN KEY (`appointment_id`) REFERENCES `Appointment` (`appointment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Receptionist`
DROP TABLE IF EXISTS `Receptionist`;
CREATE TABLE `Receptionist` (
  `receptionist_id` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`receptionist_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Hospital`
DROP TABLE IF EXISTS `Hospital`;
CREATE TABLE `Hospital` (
  `hospital_id` int NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`hospital_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- Table structure for table `Medical`
DROP TABLE IF EXISTS `Medical`;
CREATE TABLE `Medical` (
  `medical_id` int NOT NULL,
  `cost` decimal(10,2) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`medical_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;