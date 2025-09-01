drop database if exists LibrarySystem;
create database if not exists LibrarySystem;
use LibrarySystem;

create table Branch (
	branch_id int auto_increment primary key,
    branch_name varchar(100) not null,
    location varchar(100)
);

create table Category (
	category_id int auto_increment primary key,
    category varchar(50) not null
);

create table Publisher (
	publisher_id int auto_increment primary key,
	publisher_name varchar(50)
);

create table Book (
	book_id int auto_increment primary key,
    title varchar(100) not null,
    isbn varchar(20) unique,
    language varchar(50),
    no_copies int,
    no_pages int,
    released_year int,
    category_id int,
    branch_id int,
    publisher_id int,
    foreign key (category_id) references Category(category_id),
	foreign key (publisher_id) references Publisher(publisher_id),
    foreign key (branch_id) references Branch(branch_id)
);

create table User (
	user_id int auto_increment primary key,
	first_name varchar(50),
    last_name varchar(50),
    email varchar(100) unique,
    phone_no varchar(15),
    username varchar(50) unique,
    password varchar(100),
	role enum('Employee', 'Customer'),
	branch_id int,
	foreign key (branch_id) references Branch(branch_id)
);

create table Employee (
    employee_id int,
    primary key(employee_id),
    foreign key (employee_id) references User(user_id)
);

create table Customer (
    customer_id int,
    address varchar(100),
    primary key(customer_id),
    foreign key (customer_id) references User(user_id)
);

create table Borrow (
	issued_id int auto_increment primary key,
    book_id int,
    customer_id int,
    issue_date date,
    due_date date,
    return_date date,
    status ENUM('borrowed', 'returned', 'late') DEFAULT 'borrowed',
    foreign key (book_id) references Book(book_id),
	foreign key (customer_id) references Customer(customer_id)
);