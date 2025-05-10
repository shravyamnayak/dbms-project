# 🩺 Doctor Appointment System

![Doctor Appointment System Banner](https://github.com/shravyamnayak/dbms-project/blob/main/banner.png)

A full-stack web application built using **Flask (Python)**, **MySQL**, **HTML**, and **CSS**, designed to streamline the process of booking and managing doctor appointments. This role-based system supports **Patients**, **Doctors**, and **Admins**, offering features like appointment scheduling, status tracking, profile management, and email notifications.

---

## 🚀 Features

### 🔐 Role-Based Authentication
- Patients, Doctors, and Admins can register and securely log in.
- Each user has access only to role-appropriate features.

### 📅 Appointment Management
- **Patients**: Book, reschedule, and cancel appointments.
- **Doctors**: View and update appointments.
- **Admins**: Full access to all appointments and user data.

### 🔄 Appointment Status Tracking
- Statuses include: `Pending`, `Completed`, `Cancelled`, and `Missed`.

### 📧 Email Notifications
- Real-time email alerts for:
  - Appointment confirmation  
  - Rescheduling updates  
  - Cancellations  
- Powered by **Flask-Mail** with Gmail SMTP.

### 🌐 Responsive Frontend
- Clean and user-friendly interface using custom **HTML & CSS**.
- Fully responsive across devices.

---

## 🛠️ Tech Stack

| Layer             | Technology               |
|------------------|--------------------------|
| **Backend**       | Flask (Python)           |
| **Frontend**      | HTML, CSS (Custom)       |
| **Database**      | MySQL with PyMySQL       |
| **Email Service** | Flask-Mail (Gmail SMTP)  |
| **Version Control** | Git & GitHub           |

---

## ⚙️ Installation Guide

### 📋 Prerequisites
- Python 3.8+
- MySQL Server
- Git

### 1. 📥 Clone the Repository
```bash
git clone https://github.com/shravyamnayak/dbms-project.git
cd dbms-project
```

### 2. 🧪 Set Up a Virtual Environment (Optional)
```bash
python -m venv venv
# On Linux/macOS
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. 📦 Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. 🗃️ Configure the MySQL Database
- Create a MySQL database named `doctors_appointment`.
- Ensure all required tables are created based on the schema.

### 5. ✉️ Configure Flask-Mail
Edit `config.py`:
```python
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = 'your-email@gmail.com'
MAIL_PASSWORD = 'your-app-password'
```

### 6. ▶️ Run the App
```bash
flask run
```

Access the app at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖼️ Screenshots 
<!-- Uncomment and update the image paths -->
<!--
### 📋 Login Page
![Login Page](screenshots/login.png)

### 🗓️ Appointment Dashboard
![Dashboard](screenshots/dashboard.png)
-->

---

## 🌟 Future Enhancements

- 📱 **Mobile App Integration**: Cross-platform mobile apps for patients and doctors.
- 🔍 **Advanced Search & Filters**: Filter by specialization, date, and availability.
- ⭐ **Ratings & Feedback**: Let patients rate and review doctors.
- 💳 **Payment Integration**: Secure online payments for consultations.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE.md](LICENSE.md) file for details.

---

## 🔗 GitHub Repository

🔗 [GitHub – shravyamnayak/dbms-project](https://github.com/shravyamnayak/dbms-project)
