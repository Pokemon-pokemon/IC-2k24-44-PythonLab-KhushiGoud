# Python Dictionary — Part A: Programs

## 📌 Overview

This project contains five Python programs demonstrating the practical use of dictionaries, nested dictionaries, comprehensions, aggregation, searching, sorting, and data validation.

Each program solves a real-world problem using Python dictionary operations and follows the requirements provided in the assignment.

## 🎯 Objectives

- Understand dictionaries and nested dictionaries.
- Perform CRUD operations: Create, Read, Update, and Delete.
- Use dictionary methods such as `.get()`, `.setdefault()`, and `.update()`.
- Apply dictionary and list comprehensions.
- Perform grouping, filtering, sorting, and aggregation.
- Validate user input and handle invalid operations safely.
- Generate reports from stored data.

## 📂 Programs Included

### Q1. Student Database

**Concepts:** Nested dictionaries, validation, comprehensions, and reports.

**Features:**
- Add, update, delete, and display student records.
- Store student names and subject-wise marks.
- Reject duplicate roll numbers.
- Validate marks within the range of 0–100.
- Calculate each student's average marks.
- Identify the topper and highest scorer in each subject.
- Find students scoring below 40 in any subject.
- Group students according to grades A, B, C, D, and F.

### Q2. Employee Database

**Concepts:** Dictionary operations, grouping, aggregation, sorting, and comprehensions.

**Features:**
- Add, update salary, delete, and search employees.
- Calculate department-wise payroll and headcount.
- Identify the highest-paid employee in each department.
- Sort employees by salary in descending order.
- Create a new dictionary applying a 10% raise to employees earning below ₹50,000.
- Identify the department with the highest average salary.
- Display an appropriate message when an employee does not exist.

### Q3. Library Record System

**Concepts:** Nested dictionaries, lists, state management, and validation.

**Features:**
- Add books and increase copies for existing ISBNs.
- Issue and return books.
- Track members holding each book.
- Enforce book availability and a maximum limit of two books per member.
- Prevent duplicate issues and invalid returns.
- Search for books and generate library reports.
- Find books by author, unavailable books, never-issued books, and members holding multiple books.

### Q4. Word Frequency Counter

**Concepts:** String processing, dictionaries as counters, sorting, and comprehensions.

**Features:**
- Accept a paragraph from the user.
- Convert text to lowercase and remove punctuation.
- Count word frequencies using `.get()`.
- Display the top N words, breaking ties alphabetically.
- Find words appearing exactly once.
- Invert the frequency dictionary.
- Group unique words by their length.
- Search for a word without crashing when it is absent.
- Handle empty input gracefully.

### Q5. Phone Directory

**Concepts:** Dictionaries with list values, reverse lookup, validation, and grouping.

**Features:**
- Add and delete contacts.
- Add multiple phone numbers to an existing contact.
- Update email addresses and cities.
- Validate phone numbers as exactly 10 digits.
- Prevent duplicate phone numbers across contacts.
- Perform case-insensitive partial-name searches.
- Build a reverse phone lookup dictionary.
- Group contacts by city.
- Find contacts with multiple phone numbers.
- Display the directory alphabetically.

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Data Structures:** Dictionaries, nested dictionaries, and lists
- **Concepts:** Dictionary methods, comprehensions, loops, conditions, functions, sorting, and input validation



## 🧪 Testing and Validation

The programs should be tested with:

- Valid and invalid user inputs.
- Duplicate student IDs, employee IDs, ISBNs, and phone numbers where applicable.
- Missing records during search, update, or deletion.
- Boundary values such as marks of 0 and 100.
- Library issue and return restrictions.
- Empty paragraphs and words that are not found.
- Reports using the supplied sample data.

## 📚 Learning Outcomes

After completing these programs, students will be able to:

1. Design and manipulate nested dictionary structures.
2. Implement menu-driven applications.
3. Apply comprehensions to transform and filter data.
4. Perform searches and generate reports.
5. Enforce business rules through input validation.
6. Handle common edge cases without unexpected program termination.



