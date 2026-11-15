# 🏥 Hospital Management System (PS No. 47)

A menu-driven console application built in **Python 3** to manage hospital patient records in memory. Developed as a First Semester project for **Bachelor of Technology in Computer Science and Engineering** at **Rungta International Skills University**.

---

## 📋 Problem Statement

Develop a menu-driven console application to manage hospital patient records without using external files. Users can add new patients, view all records, search by Patient ID, update existing details, and delete patient records.

### Key Specifications
* **Language:** Python 3
* **Concepts Used:** Nested Dictionaries, Modular Functions, CRUD Operations, Input Validation
* **Patient ID Format:** Auto-generated starting from `P101` (increments by 1)
* **Record Fields:** `Name`, `Age` (`0` to `120`), `Disease`, `Doctor`
* **Storage:** Kept in memory during runtime

---

## ✨ Features

* **Add Patient (`1`):** Validates non-empty text fields and ensures age is between `0` and `120` before generating a unique ID.
* **View All Patients (`2`):** Displays all active patient records in a clean, readable format.
* **Search Patient by ID (`3`):** Quickly fetches details for a specific Patient ID.
* **Update Patient Details (`4`):** Allows selective updates to a patient's name, age, disease, or assigned doctor.
* **Delete Patient Record (`5`):** Removes a record by ID and displays the remaining patient count.
* **Error Handling:** Displays clear feedback when an ID does not exist, inputs are invalid, or no records are stored.

---

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Run the Python script:**
   ```bash
   python hospital_management.py
   ```
   *(Note: Replace `hospital_management.py` with your actual `.py` filename if different.)*

---

## 🧪 Test Cases Verified

| Test Case | Scenario | Sample Input | Expected & Actual Output |
| :--- | :--- | :--- | :--- |
| **Test Case 1** | Normal Input | Option `1`, Name: `Ravi Kumar`, Age: `35`, Disease: `Fever`, Doctor: `Dr. Mehta` | `Patient added. ID: P101 \| Ravi Kumar \| 35 \| Fever \| Dr. Mehta` |
| **Test Case 2** | Boundary Input | Option `1`, Name: `Baby Sen`, Age: `0`, Disease: `Jaundice`, Doctor: `Dr. Rao` | `Patient added. ID: P101 \| Baby Sen \| 0 \| Jaundice \| Dr. Rao` |
| **Test Case 3** | Invalid Age | Option `1`, Name: `Amit Das`, Age: `abc` | `Invalid age. Enter a number between 0 and 120. Patient not added.` |
| **Test Case 4a** | Update Record | Option `4`, ID: `P101`, New Disease: `Typhoid` | `Patient P101 updated. Disease: Typhoid` |
| **Test Case 4b** | Delete Record | Option `5`, ID: `P101` | `Patient P101 deleted. Total patients: 0` |
| **Test Case 4c** | Empty Records | Option `2` (after deletion) | `No patient records found.` |

---

## 📁 Project Structure

```text
├── hospital_management.py   # Main Python source code
└── README.md                # Project documentation
```

---

## 🎓 Academic Details

* **University:** Rungta International Skills University
* **School:** School of Computer Science and Engineering
* **Program:** B.Tech Computer Science and Engineering (1st Semester)
* **Problem Statement No.:** 47
