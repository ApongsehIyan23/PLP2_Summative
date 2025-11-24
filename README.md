# 🚀 Startup Connect

**A Professional Networking Platform for the Rwandan Startup Ecosystem**

Startup Connect is a command-line application that bridges the gap between startup founders, experienced mentors, and potential investors in Rwanda. Built as a LinkedIn-inspired platform specifically tailored for the East African entrepreneurial landscape.
---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Database Setup](#-database-setup)
- [Configuration](#-configuration)
- [Running the Application](#-running-the-application)
- [Project Structure](#-project-structure)
- [Usage Guide](#-usage-guide)
- [Sample Test Data](#-sample-test-data)
- [Team Members](#-team-members)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### Core Functionality
- ✅ **Secure Authentication**: SHA-256 password hashing with `getpass` for hidden input
- ✅ **Role-Based Profiles**: Distinct profiles for Founders, Mentors, and Investors
- ✅ **Industry Matching**: Smart matching algorithm based on industry categories
- ✅ **Profile Display**: Tabular format using `tabulate` library for clean data presentation
- ✅ **Dashboard Analytics**: View connection statistics and pending requests
- ✅ **Multi-Industry Support**: FinTech, HealthTech, AgriTech, EdTech, Logistics, GreenTech

### Technical Features
- 🔐 **Environment-Based Security**: Credentials stored in `.env` files
- 🗄️ **Normalized MySQL Database**: Proper foreign keys, constraints, and ENUM types
- 🎨 **Professional CLI**: Clean menu system with screen clearing and formatting
- 📊 **Real-Time Statistics**: Live tracking of connections and requests
- 🔄 **Connection Management**: Send, accept, and decline connection requests

---

## 🛠 Tech Stack

- **Language**: Python 3.8+
- **Database**: MySQL 8.0+
- **Key Libraries**:
  - `mysql-connector-python` - Database connectivity
  - `python-dotenv` - Environment variable management
  - `tabulate` - Table formatting for data display
  - `hashlib` - Password hashing (built-in)
  - `getpass` - Secure password input (built-in)

---

## 📦 Prerequisites

Before you begin, ensure you have:

1. **Python 3.8 or higher**
   ```bash
   python --version
   ```

2. **MySQL 8.0 or higher**
   ```bash
   mysql --version
   ```

3. **pip** (Python package manager)
   ```bash
   pip --version
   ```

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/ApongsehIyan23/PLP2_Summative.git
cd PLP2_Summative
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install mysql-connector-python python-dotenv tabulate
```

---

## 🗄️ Database Setup

### Step 1: Create MySQL Database

```bash
# Login to MySQL
mysql -u root -p

# In MySQL prompt:
CREATE DATABASE startup_connect;
EXIT;
```

### Step 2: Database Schema Creation

The application automatically creates all required tables on first run. The schema includes:
- `users` - Core user information
- `founders` - Startup founder details
- `mentors` - Mentor-specific information
- `investors` - Investor-specific information
- `connections` - Connection requests and relationships

Tables are created automatically by the `create_all_tables()` function in `db_connection/init_db.py`.

---

## ⚙️ Configuration

### Create Environment File

Create a file named `credentials.env` in the `db_connection` folder:

```bash
# db_connection/credentials.env

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=startup_connect
DB_PORT=3306
```

**⚠️ IMPORTANT**: 
- Replace `your_mysql_password` with your actual MySQL password
- The `.gitignore` already includes `*.env` to prevent credential exposure

---

## ▶️ Running the Application

### Start the Application

```bash
python main.py
```

### First Run Experience

1. **Welcome Screen**: Press Enter to continue
2. **Welcome Menu**: 
   - Option 1: Register (Create new account)
   - Option 2: Login (Existing users)
   - Option 3: Exit
3. **Registration Process**:
   - Choose role (1=Founder, 2=Mentor, 3=Investor)
   - Fill in common details (username, name, industry, bio)
   - Enter role-specific information
   - Confirm details and create account
4. **Login**: Use your username and password to access the platform

---

## 📁 Project Structure

```
PLP2_Summative/
│
├── main.py                          # Application entry point
│
├── db_connection/
│   ├── __init__.py
│   ├── init_db.py                   # Database connection & table creation
│   └── credentials.env              # Database credentials (gitignored)
│
├── models/
│   ├── __init__.py
│   ├── user.py                      # Base User class with common methods
│   ├── founder.py                   # Founder class (inherits from User)
│   ├── mentor.py                    # Mentor class (inherits from User)
│   └── investor.py                  # Investor class (inherits from User)
│
├── registration/
│   ├── __init__.py
│   └── register.py                  # User registration logic
│
├── login/
│   ├── __init__.py
│   └── loginuser.py                 # User authentication logic
│
├── welcome/
│   ├── __init__.py
│   └── begin.py                     # Welcome screens and menu
│
├── menu/
│   ├── __init__.py
│   └── main_menu.py                 # Main menu after login
│
├── .gitignore                       # Git ignore rules
└── README.md                        # This file
```

---

## 📖 Usage Guide

### Registration Process

**Common Fields (All Users):**
- Username (unique identifier)
- Full Name
- Industry (FinTech, HealthTech, AgriTech, etc.)
- Bio (short description)
- Password (minimum 8 characters)

**Founder-Specific Fields:**
- Startup Name
- Startup Description
- Years of Operation (Less than 1 year, 1-2 years, 3-5 years, 5+ years)
- Stage (Idea, Early, Growth, Established)

**Mentor-Specific Fields:**
- Expertise (area of specialization)
- Years of Experience (0-5, 5-10, 10-20, 20+ years)
- Availability (5-10, 10-20, 20+ hours/week)
- Previous Mentorships (0-5, 5-10, 10-20, 20+)

**Investor-Specific Fields:**
- Investment Stage (Idea, Early, Growth, Established)
- Investment Range (1k-5k, 5k-10k, 10k+)
- Previous Investments (0-5, 5-10, 10-20, 20+)

---

### Main Menu Options

After logging in, users can access:

```
1. View Dashboard          → Profile info and connection statistics
2. Find & Connect         → Browse or search for users
   - Browse all users in your industry
   - Search by name
3. Manage Connections     → Handle connection requests
4. View Connections       → See accepted connections
5. Logout                 → Return to welcome menu
```

---

### Finding Matches

**Browse All Users:**
- Displays all users in the same industry
- Shows Name, Role, and Bio in a formatted table
- Uses `tabulate` library for clean presentation
- Sorted alphabetically by name

**Search by Name:**
- Enter any part of a user's name
- Case-insensitive substring matching
- Results filtered by your industry
- Returns matching profiles in table format

---

### Dashboard Statistics

The dashboard displays:
- User profile information
- Role-specific details
- **Statistics:**
  - Total Connections (accepted)
  - Pending Requests Received
  - Pending Requests Sent

---

## 🧪 Sample Test Data

### Sample Industries in Dataset:
- **FinTech** (Financial Technology)
- **HealthTech** (Healthcare Technology)
- **AgriTech** (Agricultural Technology)
- **EdTech** (Educational Technology)
- **Logistics**
- **GreenTech** (Clean Energy/Sustainability)

### Example Profiles:

**Founders:**
- Jean Claude Mugisha (FinTech) - AgroPay Rwanda
- Ange Keza (HealthTech) - Sano Health
- Claudine Uwase (AgriTech) - SmartFarm RW

**Mentors:**
- Marie Uwera (FinTech) - Financial Inclusion Expert
- Dr. Emmanuel Ngoga (HealthTech) - Healthcare Operations
- Joseph Gasana (AgriTech) - Agricultural Value Chain

**Investors:**
- Olivier Kayitare (FinTech) - Kigali Ventures
- Solange Mukamazimpaka (HealthTech) - Angel Investor
- Bernard Gashumba (AgriTech) - AgriTech Fund Manager

---

## 🔐 Security Features

1. **Password Hashing**: All passwords are hashed using SHA-256 before storage
2. **Hidden Input**: Uses `getpass` module to hide password input
3. **Environment Variables**: Sensitive credentials stored in `.env` files
4. **SQL Injection Protection**: Uses parameterized queries with `%s` placeholders
5. **Input Validation**: Comprehensive validation for all user inputs

---

## 🎯 Key Implementation Details

### OOP Architecture
- **Base Class**: `User` contains common methods (get_stats, find_matching_profiles)
- **Inheritance**: Founder, Mentor, Investor classes inherit from User
- **Polymorphism**: Each class has specific display and database methods

### Database Design
- **Normalized Structure**: Separate tables for users and role-specific data
- **ENUM Types**: Used for predefined options (stage, investment_range, etc.)
- **Foreign Keys**: Proper relationships with ON DELETE CASCADE
- **Constraints**: UNIQUE and CHECK constraints for data integrity

### Connection Logic
- Prevents duplicate connections
- Tracks connection status (Pending, Accepted, Declined)
- Bidirectional relationship handling
- Real-time statistics calculation

---

## 👥 Team Members

This project was collaboratively developed by a team of 6 students:
1. Apongseh Iyan
2. Davine Uwase
3. Yves N
4. David N
5. Imena Kizito
6. Faustine N
**Course**: PLP Python Programming  
**Project**: Summative Assessment

---

## 🐛 Known Issues & Future Enhancements

### Current Limitations:
- Connection request actions not yet implemented in UI
- Search by name feature needs integration
- No password recovery mechanism
- Limited to one industry per user

### Planned Features:
- [ ] Complete connection request workflow (accept/decline)
- [ ] Advanced search with filters
- [ ] Direct messaging between connected users
- [ ] Export connections to CSV
- [ ] Email notifications
- [ ] Admin dashboard
- [ ] Profile editing capabilities

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add NewFeature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

### Development Guidelines:
- Follow PEP 8 style guide
- Add docstrings to all functions
- Test thoroughly before submitting
- Update documentation for new features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


## 📞 Contact & Support

**Project Repository**: [https://github.com/ApongsehIyan23/PLP2_Summative](https://github.com/ApongsehIyan23/PLP2_Summative)

For issues or questions:
- Open an issue on GitHub
- Contact the development team

---

## 🌟 Show Your Support

If you find this project useful, please give it a ⭐ on GitHub!

---

**Built with ❤️ for the Rwandan Startup Ecosystem 🇷🇼**