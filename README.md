# 📚 Library Management System

*A comprehensive Library Management System with Python CLI interface and MySQL database backend.*

---

## 📖 Project Overview

This is a full-featured Library Management System that combines database design with a Python command-line interface. The system provides role-based access control for Customers, Employees, and Administrators, enabling complete library operations from book management to borrowing workflows.

The project demonstrates proficiency in **database design, Python programming, object-oriented programming, and system architecture**.

---

## ✨ Features

### 🔐 Authentication System
- User registration and login
- Role-based access control (Customer, Employee, Admin)
- Input validation for emails, phone numbers, and passwords

### 👥 User Roles & Capabilities

#### **Customers**
- Browse and search available books
- Borrow books with automatic availability checking
- Return books with late fee calculations
- View personal borrowing history

#### **Employees**
- Add, edit, and remove books from inventory
- Manage book details (title, ISBN, copies, language, pages, etc.)
- Handle authors, publishers, and categories
- Complete book catalog management

#### **Administrators**
- Full employee management (add, edit, remove)
- Customer account management
- System-wide user administration
- Access to all system features

### 📚 Core Functionality
- **Book Management**: Complete CRUD operations for books, authors, publishers, categories
- **Borrowing System**: Issue tracking, due dates, return processing
- **Fee Calculation**: Automatic late fee computation (5 EGP per day)
- **Inventory Tracking**: Real-time book availability updates
- **Policy Management**: System policies and rules display

---

## 🏗️ Database Schema

The system includes the following main entities:

- **User** → Base user information with role differentiation
- **Admin** → Responsible for managing employees and customers accounts, overseeing library operations, and maintaining system integrity.
- **Customer** → Library members who borrow books
- **Employee** → Staff members who manage books
- **Book** → Book catalog with availability tracking
- **Author** → Book authors information
- **Publisher** → Publishing company details
- **Category** → Book categorization system
- **Branch** → Library branch locations
- **Borrow** → Borrowing transaction records with status tracking

---

## ⚙️ Technologies Used

- **Backend**: Python 3.x
- **Database**: MySQL 8.0+
- **Database Connector**: mysql-connector-python
- **Architecture**: Object-Oriented Programming (OOP)
- **Design Pattern**: MVC-inspired structure

---

## 📂 Project Structure

```bash
LibraryManagementSystem/
├── Main.py                 # Application entry point
├── services/
│   └── Authentication.py   # User authentication logic
├── core/                   # Core business logic
│   ├── Admin.py           # Admin functionality
│   ├── Employee.py        # Employee operations
│   ├── Customer.py        # Customer operations
│   ├── Book.py            # Book management
│   ├── Author.py          # Author operations
│   ├── Publisher.py       # Publisher management
│   ├── Category.py        # Category handling
│   ├── Borrow.py          # Borrowing system
│   ├── Policies.py        # System policies
│   └── User.py            # User operations
├── database/
│   ├── DBConnection.py    # Database connection handler
│   └── Models.py          # Data models and entities
├── Library Management System.sql  # Database schema
└── README.md
```

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- MySQL Server 8.0 or higher
- pip (Python package manager)

### Step 1: Clone the Repository
```bash
git clone <your-repository-url>
cd LibraryManagementSystem
```

### Step 2: Install Dependencies
```bash
pip install mysql-connector-python
```

### Step 3: Database Setup
1. Open MySQL and create the database:
```sql
source "Library Management System.sql"
```

2. Update database credentials in `database/DBConnection.py`:
```python
self.conn = mysql.connector.connect(
    host="127.0.0.1",
    user="your_username",        # Update this
    password="your_password",    # Update this
    database="LibrarySystem"
)
```

### Step 4: Run the Application
```bash
python Main.py
```

---

## 🎮 Usage

### Getting Started
1. Run the application with `python Main.py`
2. Choose from the main menu:
   - **Sign Up**: Register as a new customer
   - **Log in**: Access your account
   - **Policies**: View library policies
   - **Exit**: Close the application

### Sample User Workflow

#### For Customers:
1. Sign up with valid email and phone number
2. Log in with your credentials
3. Browse available books
4. Search for specific titles
5. Borrow books (automatically updates inventory)
6. Return books (calculates late fees if applicable)

#### For Employees:
1. Log in with employee credentials
2. Add new books to the system
3. Edit existing book information
4. Remove books from inventory
5. Manage authors, publishers, and categories

#### For Administrators:
1. Log in with admin credentials
2. Add or remove employee accounts
3. Manage customer accounts
4. Edit user information across the system

---

## 💡 Key Features in Detail

### Smart Inventory Management
- Automatic stock updates when books are borrowed/returned
- Real-time availability checking
- Prevents over-borrowing of limited copies

### Late Fee System
- Automatic calculation based on return date vs due date
- Configurable fee structure (currently 5 EGP per day)
- Integrated with return processing

### Data Validation
- Email format validation (@gmail.com requirement)
- Egyptian phone number format validation (+201xxxxxxxxx)
- Password strength requirements
- Duplicate email prevention

### Dynamic Data Management
- Automatic creation of new authors, publishers, and categories
- Referential integrity maintenance
- Cascading updates across related tables

---

## 🔧 Configuration

### Database Configuration
Update connection settings in `database/DBConnection.py`:
- Host address
- Username and password
- Database name
- Port (if different from default)

### Business Rules
Modify fee calculations in `core/Borrow.py`:
```python
fees = delay_days * 5  # Change fee amount per day
```

### Validation Rules
Adjust validation patterns in authentication and user management modules:
- Email format requirements
- Phone number patterns
- Password complexity rules

---

## 📊 Database Queries & Operations

The system supports various complex operations:
- Multi-table joins for book details with authors and publishers
- Borrowing status tracking with date calculations
- User role-based data filtering
- Inventory management with real-time updates
- Transaction history with fee calculations

---

## 🛡️ Security Features

- Role-based access control
- Input validation and sanitization
- SQL injection prevention through parameterized queries
- Password-based authentication
- Data integrity constraints

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

---

## 📝 License

This project is created for educational purposes and portfolio demonstration.

---

## 📧 Contact

For questions or suggestions regarding this Library Management System, please feel free to reach out.

---

**Note**: This system is designed for educational purposes and demonstrates database design, Python programming, and system architecture concepts. For production use, additional security measures and error handling should be implemented.
