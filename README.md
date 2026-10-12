# Simulated Device Monitoring and Alert System

# 1. Project Title

Laboratory Exercise 17 - Integrative Programming Project: Simulated Device Monitoring and Alert System

# 2. Project Description

This is a Python 3 program developed for CPP102. It monitors simulated temperature readings, classifies each reading, calculates a summary, and determines the overall device status.

The program uses lists, loops, conditions, and functions. No real devices or sensors are needed.

# 3. Project Objectives

- Use Python lists, loops, conditions, and functions.
- Accept and validate temperature readings.
- Classify readings as NORMAL, WARNING, or CRITICAL.
- Calculate the total, average, minimum, and maximum.
- Count each classification and calculate percentages.
- Determine the overall monitoring status.
- Practice testing, debugging, and GitHub version control.

# 4. Program Requirements

Initial readings:

readings = [28, 31, 35, 37, 29]

Temperature classifications:

| Temperature            |     Classification |
|     ---                |         ---        |
| Below 30 C             | NORMAL             |
| 30 C to 35 C inclusive | WARNING            |
| Above 35 C             | CRITICAL           |

Only whole numbers from 0 to 100 are accepted.

Overall status rules:

- ATTENTION REQUIRED - At least one CRITICAL reading exists.
- MONITOR - No CRITICAL readings exist, but at least one WARNING reading exists.
- NORMAL - All readings are NORMAL.

These rules are for classroom simulation only.

# 5. Program Features

The program has five menu options:

1. View Readings - Displays all readings.
2. Add Reading - Adds a valid temperature.
3. Classify Readings - Displays the classification of each reading.
4. Generate Summary - Displays the total, average, minimum, maximum, counts, percentages, and overall status.
5. Exit - Ends the program.

The menu repeats until the user chooses option 5. Invalid choices and readings display error messages.

# 6. Function Plan

|         Function Name          | Parameters  |        Returns        |               Purpose                |
|              ---               |     ---     |          ---          |                 ---                  |
| main()                         | None        | Nothing               | Runs the menu loop.                  |
| display\_menu()                | None        | Nothing               | Displays the menu.                   |
| classify\_reading(temperature) | temperature | Classification string | Classifies one reading.              |
| view\_readings(readings)       | readings    | Nothing               | Displays all readings.               |
| add\_reading(readings)         | readings    | Nothing               | Validates and adds a reading.        |
| classify\_readings(readings)   | readings    | Nothing               | Classifies all readings.             |
| generate\_summary(readings)    | readings    | Nothing               | Calculates and displays the summary. |

# 7. Tools and Concepts Used

Programming language: Python 3

Tools:

- Python IDLE or Visual Studio Code
- Git and GitHub
- Terminal or Python console

Python concepts:

- Lists and variables
- Input and output
- If, elif, and else
- While and for loops
- Functions and parameters
- Try and except
- Arithmetic operators
- Formatted strings

The program uses loops to calculate the total, minimum, maximum, and classification counts. It does not use sum(), min(), or max().

# 8. Sample Output

Expected output for the initial readings:

MONITORING SUMMARY
------------------
Number of readings  : 5
Total of readings   : 160
Average temperature : 32.00 C
Minimum temperature : 28 C
Maximum temperature : 37 C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED

Classification output:

READING CLASSIFICATION
----------------------
28 C -> NORMAL
31 C -> WARNING
35 C -> WARNING
37 C -> CRITICAL
29 C -> NORMAL

Replace or supplement this sample with actual output from your program.

# 9. Testing and Validation

The program must be tested using valid inputs, invalid inputs, boundary values, and menu choices.

Required tests include:

- View the initial readings.
- Add the reading 33.
- Reject abc.
- Reject -5.
- Reject 120.
- Confirm that 30 is WARNING.
- Confirm that 35 is WARNING.
- Check the initial summary.
- Enter an invalid menu choice.
- Exit the program.

Record the actual results and Pass or Fail ratings in test\_cases.md. Do not invent test results.

# 10. Project Folder Structure

Week17/
    device_monitor.py
    README.md
    test_cases.md

- device_monitor.py - Contains the Python program.
- README.md - Contains project documentation.
- test_cases.md - Contains the test results.

# 11. GitHub Version Control

Recommended commit messages:

1. Create Week17 project structure
2. Implement menu and reading management
3. Add classification and summary calculations
4. Implement input validation
5. Complete testing and documentation

Push the commits to GitHub and check that all three files are in the Week17 folder.

# 12. Conclusion and References

# Conclusion

This project uses Python lists, loops, conditions, functions, and input validation to create a simple monitoring system. It stores readings, classifies temperatures, calculates a summary, and determines the overall status.

Testing helps ensure that valid and invalid inputs are handled correctly. GitHub records the progress of the project.

# References

1. Python Software Foundation. The Python Tutorial. https://docs.python.org/3/tutorial/
2. Chacon, S., and Straub, B. Pro Git. https://git-scm.com/book/en/v2
3. GitHub Documentation. https://docs.github.com/en/get-started/writing-on-github
4. GitHub Documentation about READMEs. https://docs.github.com/en/repositories
5. CPP102 Weeks 13 to 16 Lecture and Laboratory Modules, Department of Computer Engineering, Pamantasan ng Cabuyao.
