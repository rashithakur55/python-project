# PS 19 - Student Grade Calculator

## Student Details
- **Student Name:** Rashi Thakur
- **University:** Rungta International Skills University, School of Information Technology
- **Course:** Bachelor of Computer Application (BCA)
- **PS No:** 19
- **GitHub:** [rashithakur55](https://github.com/rashithakur55)

## 1. Project Overview
This project is developed as part of the college curriculum. It takes a student's marks in five subjects, calculates the total, percentage, grade and pass/fail result, and allows more students to be entered through a loop.

## 2. Objectives
- To solve the project problem efficiently using Python 3 (variables, conditions, functions).
- To demonstrate working code execution and test case validations.

## 3. Features
- Single-file execution (`one.py`).
- Clear input and output display.
- Marks validation (only numbers from 0 to 100 are accepted).
- Grade: >=85 A, >=70 B, >=55 C, >=40 D, below 40 F.
- Pass with 40% or more, otherwise Fail.
- Tested against all required test cases.

## 4. Requirements
- Python 3.x installed on your system.

## 5. How to Run
```
python one.py
```

## 6. Files in this Repository
| File | Description |
|---|---|
| `one.py` | Main Python program |
| `README.md` | Project details and test cases |
| `test_cases.txt` | Input values for the 4 test cases |
| `Test_cases_passed.pdf` | Screenshots of test cases passed |
| `PS19_Student_Grade_Calculator.pdf` | Project details from the project allocation PDF |

## 7. Test Cases

### Test Case 1: Normal Input
- **Input:** Name: Aman, Marks: 80, 70, 90, 60, 50
- **Output:**
```
Aman | Total: 350 | Percentage: 70.00% | Grade: B |
Result: Pass
```

### Test Case 2: Boundary / Minimum Input
- **Input:** Name: Neha, Marks: 40, 40, 40, 40, 40
- **Output:**
```
Neha | Total: 200 | Percentage: 40.00% | Grade: D |
Result: Pass
```

### Test Case 3: Invalid Input
- **Input:** Name: Ravi, Marks for subject 2: 105, then abc, then 75
- **Output:**
```
Invalid marks. Enter a number between 0 and 100.
Invalid marks. Enter a number between 0 and 100.
(Second subject is accepted as 75)
```

### Test Case 4: Different Valid Scenario
- **(a) Input:** Name: Riya, Marks: 95, 88, 92, 90, 85, Another student? y
- **Output:**
```
Riya | Total: 450 | Percentage: 90.00% | Grade: A |
Result: Pass
```
- **(b) Input:** Name: Karan, Marks: 30, 35, 40, 25, 20
- **Output:**
```
Karan | Total: 150 | Percentage: 30.00% | Grade: F |
Result: Fail
```
