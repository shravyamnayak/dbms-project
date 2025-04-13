-- Use the database
USE doctors_appointment;

-- Insert dummy data into Patient table
INSERT INTO `Patient` (`patient_id`, `name`, `age`, `gender`, `blood_group`, `contact_no`, `email`, `previous_treatments`, `allergies`) VALUES
(1, 'John Smith', 35, 'Male', 'O+', '555-123-4567', 'john.smith@email.com', 'Appendectomy (2020)', 'Penicillin'),
(2, 'Emma Johnson', 28, 'Female', 'A-', '555-234-5678', 'emma.j@email.com', 'None', 'Latex'),
(3, 'Robert Williams', 45, 'Male', 'B+', '555-345-6789', 'robert.w@email.com', 'Knee surgery (2019), Hypertension treatment', 'Sulfa drugs'),
(4, 'Sarah Davis', 32, 'Female', 'AB+', '555-456-7890', 'sarah.d@email.com', 'None', 'None'),
(5, 'Michael Brown', 52, 'Male', 'O-', '555-567-8901', 'michael.b@email.com', 'Coronary bypass (2021)', 'Iodine'),
(6, 'Jennifer Wilson', 39, 'Female', 'A+', '555-678-9012', 'jennifer.w@email.com', 'Cesarean section (2018)', 'None'),
(7, 'David Miller', 47, 'Male', 'B-', '555-789-0123', 'david.m@email.com', 'Cholecystectomy (2017)', 'Aspirin'),
(8, 'Lisa Anderson', 29, 'Female', 'AB-', '555-890-1234', 'lisa.a@email.com', 'None', 'Shellfish'),
(9, 'James Taylor', 61, 'Male', 'O+', '555-901-2345', 'james.t@email.com', 'Cataract surgery (2022), Diabetes treatment', 'None'),
(10, 'Patricia Thomas', 41, 'Female', 'A+', '555-012-3456', 'patricia.t@email.com', 'Thyroidectomy (2020)', 'Codeine');

-- Insert dummy data into Doctor table
INSERT INTO `Doctor` (`doctor_id`, `name`, `specialization`, `experience`, `contact_no`, `email`) VALUES
(1, 'Dr. Amanda Rodriguez', 'Cardiology', 15, '555-111-2222', 'a.rodriguez@hospital.com'),
(2, 'Dr. Benjamin Lee', 'Orthopedics', 12, '555-222-3333', 'b.lee@hospital.com'),
(3, 'Dr. Catherine Chen', 'Pediatrics', 8, '555-333-4444', 'c.chen@hospital.com'),
(4, 'Dr. Daniel Wilson', 'Neurology', 20, '555-444-5555', 'd.wilson@hospital.com'),
(5, 'Dr. Elizabeth Stewart', 'Dermatology', 10, '555-555-6666', 'e.stewart@hospital.com'),
(6, 'Dr. Francis Murphy', 'General Surgery', 18, '555-666-7777', 'f.murphy@hospital.com'),
(7, 'Dr. Grace Kim', 'Gynecology', 14, '555-777-8888', 'g.kim@hospital.com'),
(8, 'Dr. Henry Patel', 'ENT', 9, '555-888-9999', 'h.patel@hospital.com');

-- Insert dummy data into Hospital table
INSERT INTO `Hospital` (`hospital_id`, `name`, `location`, `contact_no`) VALUES
(1, 'Central Medical Center', '123 Main Street, Downtown', '555-100-2000'),
(2, 'Westside Hospital', '456 Park Avenue, Westside', '555-200-3000'),
(3, 'Eastview Medical Complex', '789 Oak Boulevard, Eastside', '555-300-4000');

-- Insert dummy data into Medical table
INSERT INTO `Medical` (`medical_id`, `cost`, `location`) VALUES
(1, 1500.00, 'Central Pharmacy, 1st Floor'),
(2, 2000.00, 'Westside Medical Store, 2nd Floor'),
(3, 1800.00, 'Eastview Pharmacy, Ground Floor');

-- Insert dummy data into Receptionist table
INSERT INTO `Receptionist` (`receptionist_id`, `name`, `contact_no`) VALUES
(1, 'Nancy Clark', '555-321-9876'),
(2, 'Thomas Green', '555-432-8765'),
(3, 'Rebecca White', '555-543-7654');

-- Insert dummy data into Appointment table
INSERT INTO `Appointment` (`appointment_id`, `patient_id`, `doctor_id`, `date`, `time`, `status`) VALUES
(1, 1, 1, '2025-04-15', '09:00:00', 'Scheduled'),
(2, 2, 3, '2025-04-15', '10:30:00', 'Scheduled'),
(3, 3, 2, '2025-04-16', '11:00:00', 'Scheduled'),
(4, 4, 5, '2025-04-16', '14:00:00', 'Scheduled'),
(5, 5, 1, '2025-04-17', '15:30:00', 'Scheduled'),
(6, 6, 7, '2025-04-17', '16:45:00', 'Scheduled'),
(7, 7, 6, '2025-04-18', '09:30:00', 'Scheduled'),
(8, 8, 8, '2025-04-18', '11:15:00', 'Scheduled'),
(9, 9, 4, '2025-04-19', '10:00:00', 'Scheduled'),
(10, 10, 5, '2025-04-19', '13:00:00', 'Scheduled'),
(11, 1, 1, '2025-04-05', '09:30:00', 'Completed'),
(12, 3, 2, '2025-04-06', '14:15:00', 'Completed'),
(13, 5, 1, '2025-04-07', '11:00:00', 'Completed'),
(14, 7, 6, '2025-04-08', '16:30:00', 'Completed'),
(15, 9, 4, '2025-04-09', '10:45:00', 'Completed');

-- Insert dummy data into Prescription table
INSERT INTO `Prescription` (`prescription_id`, `appointment_id`, `medicine_name`, `dosage`, `instructions`) VALUES
(1, 11, 'Atenolol', '50mg', 'Take one tablet daily in the morning with food.'),
(2, 11, 'Aspirin', '81mg', 'Take one tablet daily after dinner.'),
(3, 12, 'Ibuprofen', '400mg', 'Take one tablet every 6 hours as needed for pain.'),
(4, 12, 'Calcium supplement', '500mg', 'Take once daily with food.'),
(5, 13, 'Lisinopril', '10mg', 'Take one tablet daily in the morning.'),
(6, 13, 'Atorvastatin', '20mg', 'Take one tablet at bedtime.'),
(7, 14, 'Antibiotic ointment', '', 'Apply to incision area twice daily.'),
(8, 14, 'Acetaminophen', '500mg', 'Take two tablets every 6 hours as needed for pain.'),
(9, 15, 'Gabapentin', '300mg', 'Take one capsule three times daily.'),
(10, 15, 'Vitamin D3', '2000 IU', 'Take one tablet daily with meal.');

-- Insert dummy data into Treatment table
INSERT INTO `Treatment` (`treatment_id`, `appointment_id`, `treatment_name`, `cost`, `duration`) VALUES
(1, 11, 'ECG', 250.00, '30 minutes'),
(2, 11, 'Blood pressure monitoring', 50.00, '15 minutes'),
(3, 12, 'X-ray', 300.00, '20 minutes'),
(4, 12, 'Physical therapy consultation', 150.00, '45 minutes'),
(5, 13, 'Cardiac stress test', 500.00, '60 minutes'),
(6, 14, 'Post-operative wound check', 100.00, '30 minutes'),
(7, 15, 'Neurological assessment', 350.00, '45 minutes'),
(8, 15, 'EEG', 450.00, '60 minutes');

-- Insert dummy data into Medical_Report table
INSERT INTO `Medical_Report` (`record_id`, `patient_id`, `diagnosis`, `previous_treatments`, `allergies`) VALUES
(1, 1, 'Hypertension, Grade 1', 'Appendectomy (2020)', 'Penicillin'),
(2, 3, 'Osteoarthritis of right knee', 'Knee surgery (2019), Hypertension treatment', 'Sulfa drugs'),
(3, 5, 'Coronary artery disease, stable', 'Coronary bypass (2021)', 'Iodine'),
(4, 7, 'Post-cholecystectomy syndrome', 'Cholecystectomy (2017)', 'Aspirin'),
(5, 9, 'Diabetic neuropathy, Progressive glaucoma', 'Cataract surgery (2022), Diabetes treatment', 'None');

-- Insert dummy data into Payment table
INSERT INTO `Payment` (`payment_id`, `appointment_id`, `amount`, `payment_method`, `status`, `date`) VALUES
(1, 11, 350.00, 'Credit Card', 'Completed', '2025-04-05'),
(2, 12, 500.00, 'Health Insurance', 'Completed', '2025-04-06'),
(3, 13, 550.00, 'Credit Card', 'Completed', '2025-04-07'),
(4, 14, 450.00, 'Health Insurance', 'Completed', '2025-04-08'),
(5, 15, 850.00, 'Debit Card', 'Completed', '2025-04-09'),
(6, 1, 300.00, 'Health Insurance', 'Pending', '2025-04-15'),
(7, 2, 250.00, 'Cash', 'Pending', '2025-04-15'),
(8, 3, 450.00, 'Health Insurance', 'Pending', '2025-04-16'),
(9, 4, 200.00, 'Credit Card', 'Pending', '2025-04-16'),
(10, 5, 350.00, 'Health Insurance', 'Pending', '2025-04-17');