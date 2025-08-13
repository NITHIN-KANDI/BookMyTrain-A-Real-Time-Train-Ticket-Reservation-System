 🚆 BookMyTrain – Real-Time Train Ticket Reservation System

 📌 Overview
BookMyTrain is an easy-to-use, web-based train ticket reservation system built with the Flask framework. It integrates AJAX for real-time updates, Bootstrap for responsive design, and MySQL for secure and efficient database management.  
The platform allows users to:
- Search trains by station, date, and time.
- Check real-time seat availability.
- Book tickets with dynamic seat layouts.
- Manage user profiles and booking history.
- Ensure secure logins with authentication.

---

 🛠 Features
- Train Search – Find trains by departure/arrival stations, travel dates, and times.
- Dynamic Seat Selection – Interactive seat layouts with real-time updates.
- User Authentication – Secure registration and login system.
- CRUD Operations – Manage bookings, train schedules, and user data.
- Responsive UI – Mobile-friendly design using Bootstrap.
- Real-Time Updates – AJAX integration for smooth, page-refresh-free interactions.

---

 📂 Tech Stack
 Frontend
- HTML, CSS, Bootstrap
- JavaScript, jQuery, AJAX

 Backend
- Python (Flask Framework)
- MySQL Database

 Architecture
- MVC (Model-View-Controller) pattern for scalability and maintainability.

---

 🚀 Installation & Setup

 Prerequisites
- Python 3.x
- MySQL Server
- pip (Python package manager)

 Steps
1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/BookMyTrain.git
   cd BookMyTrain
   ```

2. Create and activate virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate    On Mac/Linux
   venv\Scripts\activate       On Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Setup Database
   - Create a MySQL database:
     ```sql
     CREATE DATABASE bookmytrain;
     ```
   - Import the schema (provided in `database.sql`).

5. Configure Database Connection
   - Update config.py with your MySQL username, password, and DB name.

6. Run the Application
   ```bash
   flask run
   ```
   - The app will be available at: `http://127.0.0.1:5000`

---

 📊 Performance Highlights
- Desktop Performance:  
  - Perfect 100% GTmetrix performance score for optimized speed.  
  - LCP: 685ms, CLS: 0.02, TBT: 54ms.  

- Mobile Performance:  
  - Optimized load times for real-world mobile conditions.  

---

 📸 Screenshots
1. Homepage – Train booking and PNR status check.  
2. Search Results – List of available trains with booking options.  
3. Seat Selection – Interactive seat layout (available/selected/booked).  
4. Booking Confirmation – Ticket details with booking ID and journey info.  

---

 👥 Authors

K Nithin

---

 📜 License
This project is licensed under the MIT License – feel free to use and modify.

---

 📚 References
See the [Project Report](BookMyTrain_Team_05.pdf) for detailed methodology, related work, and performance analysis.
