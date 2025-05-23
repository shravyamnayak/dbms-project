# 🩺 Doctor Appointment System

> A role-based web app to simplify booking, managing, and tracking doctor appointments with real-time email notifications.

![Doctor Appointment System Banner](https://github.com/shravyamnayak/dbms-project/blob/main/static/banner.png)

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

| Layer             | Technology                                                                                      |
|-------------------|------------------------------------------------------------------------------------------------|
| **Backend**       | ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)  |
| **Frontend**      | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)     |
| **Database**      | ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![PyMySQL](https://img.shields.io/badge/PyMySQL-3776AB?style=for-the-badge&logo=python&logoColor=white)     |
| **Email Service** | ![Flask-Mail](https://img.shields.io/badge/Flask--Mail-333333?style=for-the-badge&logo=mailchimp&logoColor=white) 
| **Version Control** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)         |

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

## 🖼️ Project Screenshots

Here are some key screens from the **Doctor Appointment System** showcasing the main features and UI:

<table>
  <tr>
    <td align="center" style="padding: 15px;">
      <img src="screenshots/home.png" alt="Home Page" width="280" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
      <br/>
      <strong>🏠 Home Page</strong>
      <p style="max-width: 280px; color: #555; font-style: italic; font-size: 0.9em;">
        Welcome screen with navigation to key features and quick info.
      </p>
    </td>
    <td align="center" style="padding: 15px;">
      <img src="screenshots/login.png" alt="Login Page" width="280" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
      <br/>
      <strong>🔐 Login Page</strong>
      <p style="max-width: 280px; color: #555; font-style: italic; font-size: 0.9em;">
        Secure login with email and password authentication.
      </p>
    </td>
  </tr>
  <tr>
    <td align="center" style="padding: 15px;">
      <img src="screenshots/appointment.png" alt="Appointment Page" width="280" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
      <br/>
      <strong>📅 Appointment Dashboard</strong>
      <p style="max-width: 280px; color: #555; font-style: italic; font-size: 0.9em;">
        View and manage your scheduled appointments easily.
      </p>
    </td>
    <td align="center" style="padding: 15px;">
      <img src="screenshots/reschedule.png" alt="Reschedule Page" width="280" style="border-radius: 10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);"/>
      <br/>
      <strong>🔄 Reschedule Page</strong>
      <p style="max-width: 280px; color: #555; font-style: italic; font-size: 0.9em;">
        Easily reschedule appointments with just a few clicks.
      </p>
    </td>
  </tr>
</table>

---

## 🤝 Contributing
Contributions are welcome!
Feel free to open issues for bugs or feature requests, or submit pull requests.

Please adhere to the existing code style and add tests when applicable.

 ---
 
## 🌟 Future Enhancements

- 📱 **Mobile App Integration**: Cross-platform mobile apps for patients and doctors.
- 🔍 **Advanced Search & Filters**: Filter by specialization, date, and availability.
- ⭐ **Ratings & Feedback**: Let patients rate and review doctors.
- 💳 **Payment Integration**: Secure online payments for consultations.

---

## 📫 Contact
GitHub: shravyamnayak

Email: shravyamnayak@gmail.com

---
## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE.md](LICENSE.md) file for details.

---

## 🔗 GitHub Repository

🔗 [GitHub – shravyamnayak/dbms-project](https://github.com/shravyamnayak/dbms-project)

---
If you want it in any other format (like pure text, no markdown, or HTML), just let me know!
