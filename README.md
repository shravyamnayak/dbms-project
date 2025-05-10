Doctor Appointment System

A full-stack Doctor Appointment System built using Flask (Python), MySQL, HTML, and CSS. The system allows patients to schedule, reschedule, and cancel doctor appointments, while providing admin and doctor roles with access to manage appointments, track their status, and handle user profiles. The system also sends email notifications using Flask-Mail.

Features

User Authentication:
Patients, doctors, and admins can register and log in with role-based access control.


Appointment Management:
Patients can book, reschedule, and cancel appointments.

Doctors can view, update, and manage appointments.

Admins have full control to view all appointments and users.


Appointment Status Tracking:
The system supports appointment statuses like Pending, Completed, Cancelled, and Missed.


Email Notifications:
Email alerts for appointment confirmation, rescheduling, and cancellation using Flask-Mail.


Responsive Frontend:
The frontend is built with HTML, CSS, and custom styles for responsive and user-friendly interfaces.



Technologies Used
Backend: Flask (Python)
Database: MySQL (PyMySQL connector)
Frontend: HTML, CSS (customized layout)
Email Service: Flask-Mail (Gmail SMTP server for email notifications)
Version Control: Git, GitHub


Installation
1. Clone the repository:

git clone https://github.com/YourUsername/your-repo-name.git
cd your-repo-name

2. Set up a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate


3. Install the required dependencies:
pip install -r requirements.txt


4. Configure the database:
Set up the MySQL database doctors_appointment (or any name of your choice).

Ensure the database is configured with the appropriate tables as defined in the project.

5. Set up environment variables for Flask-Mail:

For email notifications, make sure to configure Flask-Mail in config.py with your Gmail SMTP settings.


6. Run the application:

flask run

Visit http://127.0.0.1:5000 in your browser to start using the system.

Future Enhancements

Mobile App Integration: Build a mobile app for patients and doctors to manage appointments on the go.

Advanced Search and Filters: Allow users to search for appointments based on doctor specialization, date, etc.

Rating and Feedback System: Implement a feature where patients can rate doctors and provide feedback.

Payment Gateway Integration: Integrate payment systems for booking paid appointments or consultations.


License

This project is licensed under the MIT License - see the LICENSE.md file for details.

GitHub Repository: https://github.com/shravyamnayak/dbms-project
