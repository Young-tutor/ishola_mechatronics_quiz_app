Mechatronics Quiz App
=====================

A simple multiple-choice quiz program written in Python. It asks questions about basic Mechatronics topics like sensors, motors, actuators and control systems.


Project Description
-------------------

This is my Python mini project. The program asks for your name, lets you pick a difficulty level (Easy, Medium or Hard), and then asks you five questions. At the end it shows your score, your percentage and a performance grade. You can also retake the quiz if you want to.

I made it to practise lists, functions, loops and if/elif/else decisions.


Features
--------

- Asks for the user's name and welcomes them
- Three difficulty levels: Easy, Medium and Hard
- Five questions in each level, 15 questions in total
- Multiple-choice answers (A, B, C and D)
- Checks each answer automatically
- Shows the correct answer when you get a question wrong
- Calculates the score and the percentage
- Gives a performance grade at the end
- Lets you retake the quiz


Requirements
------------

- Python 3
- No extra libraries are needed


How to Run the Program
----------------------

1. Install Python 3 if you do not have it.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Type this and press Enter:

```
python mechatronics_quiz_app.py
```

If that does not work, try `python3` instead of `python`. You can also run the file on your phone with Pydroid 3.

Sample output:

```
================================
     MECHATRONICS QUIZ APP
================================
Enter your name: Samson

Welcome Samson!
Test your knowledge of Mechatronics!

SELECT DIFFICULTY LEVEL
1. Easy
2. Medium
3. Hard
Choose a level (1-3): 1

You selected: Easy

What does PLC stand for?
A. Power Logic Circuit
B. Programmable Logic Controller
C. Program Line Control
D. Power Load Controller
Your answer (A/B/C/D): B
Correct!

...

Which component stores electrical charge?
A. Capacitor
B. Resistor
C. Switch
D. Fuse
Your answer (A/B/C/D): B
Incorrect!
Correct answer: A

...

========== QUIZ RESULT ==========
Name: Samson
Difficulty: Easy
Score: 4 / 5
Percentage: 80.0 %
Performance: Excellent
================================

Would you like to retake the quiz? (yes/no): no

Thank you for using Mechatronics Quiz App!
```


How the Program Works
---------------------

First, the program prints a welcome message and asks for your name.

Then it asks you to choose a difficulty level by typing 1, 2 or 3. The input is changed to a number with int(). If you type a letter or something else that is not a number, the program does not crash. It uses try and except and goes to Easy by default. If you type a number that is not 1, 2 or 3, it also goes to Easy.

The questions are stored in three lists, one for each level (easy_questions, medium_questions and hard_questions). Each question is a dictionary that has the question, a list of four options and the correct answer. The program picks the list that matches the level you chose.

A for loop then goes through the questions one by one and prints the question with its options. The function get_valid_answer() uses a while loop to keep asking until you type A, B, C or D. It also changes your answer to capital letters, so typing "b" works the same as "B".

The function check_answer() compares your answer with the correct one. If it is right, the score goes up by 1. If it is wrong, the program shows the correct answer.

After the last question, calculate_percentage() works out the percentage and get_grade() gives the performance grade:

- 80% and above: Excellent
- 60% to 79%: Very Good
- 40% to 59%: Good
- Below 40%: Keep Practising

Then the program prints the name, difficulty, score, percentage and grade. Finally it asks if you want to retake the quiz. If you type "yes", the score goes back to zero and the quiz starts again at the same level. If you type anything else, the program ends.


Original Features
-----------------

These are the extra things I added myself:

- Three difficulty levels, each with its own questions
- A performance grade (like Excellent or Keep Practising) in addition to the score and percentage
- Answer checking, so the program only accepts A, B, C or D and also accepts small letters
- A retake option so you can try again without restarting the program
- The program shows the correct answer when you get a question wrong


Project Folder Structure
------------------------

```
ishola_mechatronics_quiz_app/
    mechatronics_quiz_app.py
    README.md
```


Author Information
------------------

Name: Ishola Samson

Course: ND2 Mechatronics Engineering

School: Yaba College of Technology (YabaTech)
