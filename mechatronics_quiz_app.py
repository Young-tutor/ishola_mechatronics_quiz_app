# ==========================================
# MECHATRONICS QUIZ APP
# ==========================================

# DISPLAY WELCOME MESSAGE

print("================================")
print("     MECHATRONICS QUIZ APP")
print("================================")

# COLLECT USER'S NAME

name = input("Enter your name: ")

print(f"\nWelcome {name}!")
print("Test your knowledge of Mechatronics!")


# ==========================================
# DIFFICULTY SELECTION
# ==========================================

print("\nSELECT DIFFICULTY LEVEL")
print("1. Easy")
print("2. Medium")
print("3. Hard")

# Convert user's choice to an integer

try:
    choice = int(input("Choose a level (1-3): "))

except ValueError:
    choice = 1
    print("Invalid input! Defaulting to Easy.")


# Determine the selected difficulty

if choice == 1:
    level = "Easy"

elif choice == 2:
    level = "Medium"

elif choice == 3:
    level = "Hard"

else:
    print("Invalid choice! Defaulting to Easy.")
    level = "Easy"

print("\nYou selected:", level)


# ==========================================
# FUNCTION TO CHECK ANSWERS
# ==========================================

def check_answer(user_answer, correct_answer):

    if user_answer == correct_answer:
        return True

    else:
        return False


# ==========================================
# FUNCTION TO CALCULATE PERCENTAGE
# ==========================================

def calculate_percentage(score, total):

    return (score / total) * 100


# ==========================================
# FUNCTION TO ASSIGN GRADE
# ==========================================

def get_grade(percentage):

    if percentage >= 80:
        return "Excellent"

    elif percentage >= 60:
        return "Very Good"

    elif percentage >= 40:
        return "Good"

    else:
        return "Keep Practising"


# ==========================================
# FUNCTION TO VALIDATE USER ANSWERS
# ==========================================

def get_valid_answer():

    while True:

        answer = input("Your answer (A/B/C/D): ").upper()

        if answer in ["A", "B", "C", "D"]:
            return answer

        else:
            print("Invalid input! Please enter A, B, C or D.")


# ==========================================
# EASY QUESTIONS
# ==========================================

easy_questions = [

    {
        "question": "What does PLC stand for?",
        "options": [
            "A. Power Logic Circuit",
            "B. Programmable Logic Controller",
            "C. Program Line Control",
            "D. Power Load Controller"
        ],
        "answer": "B"
    },

    {
        "question": "Which device measures temperature?",
        "options": [
            "A. Thermistor",
            "B. Capacitor",
            "C. Transistor",
            "D. Diode"
        ],
        "answer": "A"
    },

    {
        "question": "What is the unit of electrical resistance?",
        "options": [
            "A. Volt",
            "B. Ampere",
            "C. Ohm",
            "D. Watt"
        ],
        "answer": "C"
    },

    {
        "question": "Which component stores electrical charge?",
        "options": [
            "A. Capacitor",
            "B. Resistor",
            "C. Switch",
            "D. Fuse"
        ],
        "answer": "A"
    },

    {
        "question": "What does a sensor do?",
        "options": [
            "A. Produces electricity",
            "B. Detects physical changes",
            "C. Stores data",
            "D. Controls speed"
        ],
        "answer": "B"
    }

]


# ==========================================
# MEDIUM QUESTIONS
# ==========================================

medium_questions = [

    {
        "question": "What is the SI unit of power?",
        "options": [
            "A. Joule",
            "B. Watt",
            "C. Volt",
            "D. Ohm"
        ],
        "answer": "B"
    },

    {
        "question": "Which component allows current to flow in one direction?",
        "options": [
            "A. Resistor",
            "B. Capacitor",
            "C. Diode",
            "D. Inductor"
        ],
        "answer": "C"
    },

    {
        "question": "What is the main function of an actuator?",
        "options": [
            "A. Produce movement",
            "B. Measure temperature",
            "C. Store charge",
            "D. Measure resistance"
        ],
        "answer": "A"
    },

    {
        "question": "Which motor operates using DC supply?",
        "options": [
            "A. DC motor",
            "B. Transformer",
            "C. Alternator",
            "D. Induction generator"
        ],
        "answer": "A"
    },

    {
        "question": "What does PWM stand for?",
        "options": [
            "A. Power Wire Method",
            "B. Pulse Width Modulation",
            "C. Power Wave Measurement",
            "D. Pulse Watt Meter"
        ],
        "answer": "B"
    }

]


# ==========================================
# HARD QUESTIONS
# ==========================================

hard_questions = [

    {
        "question": "Which controller uses proportional, integral and derivative actions?",
        "options": [
            "A. PLC",
            "B. PID controller",
            "C. Relay",
            "D. Rectifier"
        ],
        "answer": "B"
    },

    {
        "question": "What is the purpose of feedback in a control system?",
        "options": [
            "A. Increase noise",
            "B. Compare output with reference input",
            "C. Stop all operations",
            "D. Reduce input voltage"
        ],
        "answer": "B"
    },

    {
        "question": "Which sensor is commonly used to measure angular position?",
        "options": [
            "A. Potentiometer",
            "B. Thermistor",
            "C. Fuse",
            "D. Capacitor"
        ],
        "answer": "A"
    },

    {
        "question": "What does ADC stand for?",
        "options": [
            "A. Automatic Digital Control",
            "B. Analog to Digital Converter",
            "C. Active Data Circuit",
            "D. Advanced Digital Counter"
        ],
        "answer": "B"
    },

    {
        "question": "Which device converts electrical energy into mechanical energy?",
        "options": [
            "A. Generator",
            "B. Transformer",
            "C. Electric motor",
            "D. Rectifier"
        ],
        "answer": "C"
    }

]


# ==========================================
# SELECT QUESTIONS BASED ON DIFFICULTY
# ==========================================

if level == "Easy":

    questions = easy_questions

elif level == "Medium":

    questions = medium_questions

else:

    questions = hard_questions


# ==========================================
# DISPLAY QUESTIONS AND RETAKE FEATURE
# ==========================================

while True:

    # Reset score for every attempt

    score = 0

    # Display each question

    for question in questions:

        print("\n" + question["question"])

        # Display answer options

        for option in question["options"]:

            print(option)

        # Collect and validate user's answer

        user_answer = get_valid_answer()

        # Check whether the answer is correct

        if check_answer(user_answer, question["answer"]):

            print("Correct!")
            score += 1

        else:

            print("Incorrect!")
            print("Correct answer:", question["answer"])


    # ======================================
    # CALCULATE FINAL RESULT
    # ======================================

    total = len(questions)

    percentage = calculate_percentage(score, total)

    grade = get_grade(percentage)


    # DISPLAY QUIZ RESULTS

    print("\n========== QUIZ RESULT ==========")

    print("Name:", name)

    print("Difficulty:", level)

    print("Score:", score, "/", total)

    print("Percentage:", round(percentage, 2), "%")

    print("Performance:", grade)

    print("================================")


    # ======================================
    # RETAKE OPTION
    # ======================================

    again = input(
        "\nWould you like to retake the quiz? (yes/no): "
    ).lower()

    if again != "yes":

        print("\nThank you for using Mechatronics Quiz App!")

        break