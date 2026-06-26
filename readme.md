<div align="center">

# -- ! Student Data Organizer ! --
### *Interactive Console-Based Student Record Management System*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Collections](https://img.shields.io/badge/Collections-List%2FDict%2FSet%2FTuple-FF6F00?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Console](https://img.shields.io/badge/Console-Interactive%20CLI-4CAF50?style=for-the-badge&logo=windowsterminal&logoColor=white)](https://www.python.org/)
[![Data](https://img.shields.io/badge/Data-CRUD%20Operations-9C27B0?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)

<br/>

> *"Data is only as powerful as the structure that holds it — master collections, and you master Python."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [📦 Data Structures Used](#-data-structures-used)
- [🧩 Core Operations](#-core-operations)
- [🛠️ Tech Stack](#️-tech-stack)
- [📈 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [📄 License](#-license)
- [👤 Author](#-author)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Student Data Organizer** is a beginner-friendly, interactive Python console application that demonstrates core programming concepts such as **Python collections (List, Dictionary, Set, Tuple)**, **type casting**, **input validation**, and **CRUD operations**. The program presents a menu-driven interface that runs continuously until the user chooses to exit.

This project is designed to:
- Strengthen understanding of Python's four core collection types and their properties
- Practice user input validation, type casting, and menu-driven program design
- Apply CRUD (Create, Read, Update, Delete) logic on structured data
- Demonstrate mutability vs immutability using real-world student records

---

## 🎯 Problem Statement

> **Objective:** Build a console-based interactive tool to manage student records using Python collections.

You are building a student management utility for academic use. The program must accept user choices from a menu and execute the corresponding task — adding, displaying, updating, or deleting student records — while tracking unique subjects using a Set.

| 📂 Feature | 📄 Type | 🔍 Description |
|------------|---------|----------------|
| Add Student | CRUD — Create | Collects and stores student info into a dictionary |
| Display All Students | CRUD — Read | Prints formatted records for all students |
| Update Student | CRUD — Update | Modifies mutable fields of a student record |
| Delete Student | CRUD — Delete | Removes a student record by ID |
| View Subjects | Set Operations | Displays all unique subjects across all students |

The goal is to demonstrate **Python collection concepts and CRUD operations** through a clean, menu-driven interactive program.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔁 **Infinite Menu Loop** | Program runs continuously until user selects Exit |
| 📋 **4 Collection Types** | List, Dictionary, Set, and Tuple all used meaningfully |
| 🎓 **Student CRUD** | Full Create, Read, Update, and Delete operations |
| 🔒 **Immutable ID Storage** | Student ID and DOB stored in a Tuple to prevent changes |
| 🔡 **Type Casting** | Input strings cast to `int` (age) and `float` (GPA) with error handling |
| 🏷️ **Unique Subject Tracking** | Global Set ensures no duplicate subjects are stored |
| 🖥️ **CLI Interface** | Simple, clean text-based menu for user interaction |
| ✅ **Input Validation** | Duplicate IDs, invalid types, and empty fields are caught and reported |
| 📐 **Formatted Table Output** | Student records displayed using f-strings and `.format()` for alignment |

---

## 🏗️ Project Structure

```
📦 student-data-organizer/
│
├── 📄 student_organizer.py   ← Main Python script (entry point)
│
└── 📄 README.md              ← Project documentation
```

---

## 🔄 Project Workflow

```
Program Start
      │
      ▼
┌─────────────────────────────┐
│   Display Main Menu         │  ← Options 1–6
└────────────┬────────────────┘
             │
   ┌─────────┼──────────┬────────────┬───────────┐
   ▼         ▼          ▼            ▼           ▼
┌──────┐ ┌──────┐  ┌────────┐  ┌────────┐  ┌──────────┐
│Add   │ │View  │  │Update  │  │Delete  │  │View      │
│Student│ │All   │  │Student │  │Student │  │Subjects  │
└──┬───┘ └──┬───┘  └───┬────┘  └───┬────┘  └────┬─────┘
   │        │           │           │             │
   ▼        ▼           ▼           ▼             ▼
┌─────────────────────────────────────────────────────┐
│             Update Data Structures                  │
│     student_records_list  |  unique_subjects_set    │
└───────────────────────┬─────────────────────────────┘
                        │
                        ▼
              Loop Back to Menu
                        │
               (Choice: 6) Exit ✅
```

---

## 📦 Data Structures Used

### 🗂️ 1. List — Master Student Records

> Stores all student dictionaries. Demonstrates **mutability** — records can be added or deleted.

```python
student_records_list = []
student_records_list.append(student_dict)   # Add student
del student_records_list[index]             # Delete student
```

---

### 📖 2. Dictionary — Individual Student Details

> Organizes each student's data as key-value pairs for easy access and updates.

```python
student_dict = {
    "id_tuple": (student_id, dob),   # Immutable tuple reference
    "name": name,
    "age": age,                       # int (type cast from input)
    "grade": grade,                   # float (type cast from input)
    "subjects": subjects_list         # Mutable list of subjects
}
```

---

### 🔒 3. Tuple — Immutable Student Identity

> Stores Student ID and Date of Birth together. Demonstrates **immutability** — cannot be changed after creation.

```python
id_tuple = (student_id, dob)
s_id, s_dob = student["id_tuple"]   # Tuple unpacking
```

---

### 🏷️ 4. Set — Unique Subjects Tracker

> Automatically eliminates duplicate subjects across all students. Demonstrates **set uniqueness**.

```python
unique_subjects_set = set()
unique_subjects_set.add(subject)     # Duplicates ignored automatically
```

---

## 🧩 Core Operations

### ➕ Add Student (Create)

> Collects student details with input validation, type casting, and duplicate ID checking.

**Key Logic:**
```python
try:
    age = int(input("Enter Age: ").strip())
    grade = float(input("Enter Grade/GPA: ").strip())
except ValueError:
    print("Invalid input! Registration canceled.")
    continue
```

**Sample Output:**
```
--- Add New Student ---
Enter Student ID: S001
Enter Name: Ayush
Enter Age: 20
Enter Grade/GPA: 8.5
Enter Date of Birth (YYYY-MM-DD): 2004-05-10
Enter subjects (comma-separated): Math, Physics, CS
Success: Student Ayush added successfully!
```

---

### 📋 Display All Students (Read)

> Prints all student records in a formatted table using mixed string formatting methods.

**Key Logic:**
```python
base_info = f"{s_id:<10} | {student['name']:<15} | {student['age']:<5} | {student['grade']:<6.2f} | {s_dob:<12} | "
final_row = "{}{}".format(base_info, subjects_str)
print(final_row)
```

**Sample Output:**
```
ID         | Name            | Age   | Grade  | DOB          | Subjects
---------------------------------------------------------------------------
S001       | Ayush           | 20    | 8.50   | 2004-05-10   | Math, Physics, CS
S002       | Priya           | 21    | 9.10   | 2003-08-22   | Biology, Chemistry
```

---

### ✏️ Update Student (Update)

> Finds student by ID and allows selective update of mutable fields.

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔍 Linear Search | Iterates list to find matching ID |
| 🔒 Immutable Skip | `id_tuple` (ID + DOB) cannot be changed |
| ✅ Blank-to-Skip | Press Enter without input to keep existing value |
| 🏷️ Set Update | New subjects added to `unique_subjects_set` |

---

### 🗑️ Delete Student (Delete)

> Removes a student record from the list using the `del` keyword by index.

**Key Logic:**
```python
del student_records_list[index_to_delete]
print(f"Success: Removed student record for {deleted_student}.")
```

---

### 🏷️ View Unique Subjects (Set Display)

> Displays all unique subjects sorted alphabetically from the global Set.

**Sample Output (range of enrolled subjects):**
```
--- Unique Subjects Offered ---
1. Biology
2. Chemistry
3. CS
4. Math
5. Physics
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| 🐍 **Python** | 3.8+ | Core programming language |
| 📋 **List** | Built-in | Mutable master record storage |
| 📖 **Dictionary** | Built-in | Per-student key-value data organization |
| 🔒 **Tuple** | Built-in | Immutable ID and DOB storage |
| 🏷️ **Set** | Built-in | Unique subject tracking without duplicates |
| 🔁 **While Loop** | Built-in | Infinite menu loop control |
| 🔂 **For Loop** | Built-in | Record iteration and subject collection |
| 🖨️ **print() / input()** | Built-in | Console I/O and user interaction |
| 📐 **f-strings / .format()** | Python 3.6+ | Mixed formatted string output |

---

## 📈 Results & Insights

After running the program, the following outputs are produced:

- ✅ **Full CRUD System** — Add, view, update, and delete student records seamlessly
- 🔒 **Immutability Demonstrated** — Student ID and DOB locked in Tuples post-creation
- 🔄 **Mutability Demonstrated** — List and Dictionary fields updated dynamically
- 🏷️ **Unique Subject Set** — Global subject pool auto-deduplicates on every addition
- 🔢 **Type Safety** — Age and GPA inputs validated and cast with proper error handling
- 🔁 **Persistent Menu** — Program loops back after every task until manually exited
- ⚠️ **Error Feedback** — Duplicate IDs, invalid types, and missing records are all handled

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Beginner Friendly** | Covers all four Python collection types in one project |
| 🔄 **CRUD Coverage** | Full Create, Read, Update, Delete logic in a single script |
| 📚 **Educational** | Practically demonstrates mutability vs immutability |
| 🖥️ **No Dependencies** | Runs with pure Python — no external libraries needed |
| ⚡ **Lightweight** | Single-file script, instantly runnable from any terminal |
| 🧪 **Extensible** | Easy to add GPA filtering, export to CSV, or sort records |
| 📖 **Readable Code** | Clear `if-elif-else` menu structure makes logic easy to follow |
| 🛡️ **Input Safety** | Type casting errors and duplicate IDs are caught and reported |

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full details.

```
MIT License — Free to use, modify, and distribute with attribution.
```

---

## 👤 Author

<div align="center">

### Vaidehi Vyas

[![GitHub](https://img.shields.io/badge/GitHub-yourhandle-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/isamaliya16)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ayush-isamaliya-686533312/)

> *"Every record stored is a step closer to mastering the art of organized data."*

**🎓 Role:** Junior Python Developer | Programming Enthusiast \
**📍 Location:** India\
**🛠️ Skills:** Python · Collections · CLI Applications · CRUD Operations · Data Structures

</div>

---

## 🙏 Acknowledgements

Special thanks to the following resources and communities that made this project possible:

- 📚 [Python Official Docs](https://docs.python.org/3/) — Official Python language reference
- 📋 [Real Python — Dictionaries](https://realpython.com/python-dicts/) — In-depth dictionary tutorials
- 🏷️ [GeeksForGeeks — Sets](https://www.geeksforgeeks.org/sets-in-python/) — Set operations and examples
- 🔒 [Python Docs — Tuples](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) — Immutable sequences
- 🖥️ [W3Schools Python](https://www.w3schools.com/python/) — Beginner Python reference
- 📐 [Python f-strings Guide](https://realpython.com/python-f-strings/) — Formatted string literals
- 💬 [Stack Overflow Community](https://stackoverflow.com/) — Problem-solving support
- 📖 [Kaggle Learn](https://www.kaggle.com/learn) — Python and programming courses

---

<div align="center">

---


</div>
