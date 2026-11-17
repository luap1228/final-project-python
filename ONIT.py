while True:

    print("o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o")
    print("|                           - WELCOME TO PYTHON -                                 |")
    print("o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o")
    print("|   [1] INTRODUCTION TO PROGRAMMING                                               |")
    print("|   [2] PYTHON BASIC SYNTAX                                                       |")
    print("|   [3] ARITHMETIC OPERATORS AND EXPRESSION                                       |")
    print("|   [4] BASIC INPUT AND OUTPUT IN PYTHON                                          |")
    print("|   [5] CONDITIONAL STATEMENTS IN PYTHON                                          |")
    print("|   [6] LOGICAL OPERATOR                                                          |")
    print("|   [7] INTRODUCTION TO ITERATION AND LOOP                                        |")
    print("|   [0] EXIT                                                                      |")
    print("o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o=o")
    choi = int(input("       ENTER YOUR CHOICE: "))


    if choi == 1:
        print("\n  =============== MODULE 1 ===============")
        print("        INTRODUCTION TO PROGRAMMING")
        print("  =========================================")
        print("\n   -LESSON 1: WHAT IS PROGRAMMING?-")
        print("Programming is the process of creating")
        print("instructions that tell a computer what to do.")
        print("\n   -LESSON 2: WHAT IS PYTHON?-")
        print("Python is high level programming language.")
        print("It is used for websites, application, games, and other computer programs.")
        print("\n   -LESSON 3: WHY LEARN PYTHON?-")
        print("1. Easy to understand")
        print("2. Readable syntax")
        print("3. Versatile programming language")
        print("4. Useful in many fields")
        print("\n               EXAMPLE:")
        print("print(\"Hello, World!\")")
        print("\n               OUTPUT:")
        print("Hello, World!\n")

        back = input("\nDO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break



    elif choi == 2:
        print("\n  =============== MODULE 2 ===============")
        print("            PYTHON BASIC SYNTAX")
        print("  =========================================")
        print("\n   -LESSON 1: WHAT IS PYTHON SYNTAX?-")
        print("Syntax refers to the set of rules that tells")
        print("us how to correctly write a program in Python")
        print("\n   -LESSON 2: PYTHON IS CASE SENSITIVE")
        print("Python treats  uppercase and lowercase letters  differently.")
        print("Example: age and AGE are different variables.")
        print("\n   -LESSON 3: INDENTATION-")
        print("Indentation means adding spaces at the")
        print("beginning of a line to organize code blocks.")
        print("\n               EXAMPLE:")
        print("if 10 > 5:")
        print("     print(\"Ten is greater than five\")")
        print("\n   -LESSON 4: PRINT STATEMENT")
        print("The print() function displays information on the screen.")
        print("\n               EXAMPLE:")
        print("print(\"Hello, Python!\")")
        print("\n   -LESSON 5: PRINTING TEST")
        print("Text or strings must be enclosed in")
        print("quotation marks.")
        print("\n               EXAMPLES:")
        print("print(\"Hello\")")
        print("print(\"Welcome to Python\")")
        print("\n   -LESSON 6: PRINTING NUMBERS")
        print("Numbers can be printed without quotation marks")
        print("\n               EXAMPLES:")
        print("print(100)")
        print("print(25.5)")
        print("\n   -LESSON 7: PYTHON COMMENTS")
        print("Comments are ignored by Python.")
        print("They are used to explain the code.")

        print("\n               EXAMPLE:")
        print("# This is a single-line comment")

        print("\n   -LESSON 8: VARIABLES-")
        print("A variable is a named storage location")
        print("used to keep data in a program.")

        print("\n               EXAMPLE:")
        print('name = "John"')
        print("age = 20")

        print("\n   -LESSON 9: VARIABLE NAMING RULES-")
        print("1. A variable must start with a letter or underscore.")
        print("2. A variable cannot start with a number.")
        print("3. Variable names are case-sensitive.")
        print("4. Do not use spaces in variable names.")
        print("5. Use descriptive names when possible.")

        print("\nVALID VARIABLE NAMES:")
        print("name, age, first_name, totalAmount")

        print("\nINVALID VARIABLE NAMES:")
        print("2name, first name, total-amount")

        print("\n   -LESSON 10: CONSTANTS-")
        print("A constant is a value that should not change.")
        print("Python commonly uses uppercase names for constants.")

        print("\n               EXAMPLE:")
        print("PI = 3.14159")

        print("\n   -LESSON 11: BASIC DATA TYPES-")
        print("int   - Whole numbers")
        print("float - Decimal numbers")
        print("str   - Text or strings")
        print("bool  - True or False")

        print("\n   -LESSON 12: DECLARATION OF VARIABLES-")
        print('name = "Maria"')
        print("age = 20")
        print("grade = 89.5")
        print("is_enrolled = True")

        print("\n   -LESSON 13: OUTPUT VARIABLES-")
        name = "Clark College"
        print("school = 'Clark College'")
        print("print(school)")
        print("\nOUTPUT:")
        print(name)

        print("\nPRINTING MULTIPLE VARIABLES:")
        a = "I"
        b = "LOVE"
        c = "PYTHON"
        print(a, b, c)

        back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        back = input("\nDO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break



    elif choi == 3:
        print("\n  =============== MODULE 3 ===============")
        print("      ARITHMETIC OPERATORS AND EXPRESSION")
        print("  =========================================")

        print("\n   -LESSON 1: ARITHMETIC OPERATORS-")
        print("Arithmetic operators are symbols used")
        print("to perform mathematical calculations.")

        print("\n PYTHON ARITHMETIC OPERATORS:")
        print("+   Addition")
        print("-   Subtraction")
        print("*   Multiplication")
        print("/   Division")
        print("//  Floor Division")
        print("%   Modulus")
        print("**  Exponentiation")

        print("\n               EXAMPLE PROGRAM:")
        a = 10
        b = 5

        print("A =", a)
        print("B =", b)
        print("Addition:", a + b)
        print("Subtraction:", a - b)
        print("Multiplication:", a * b)
        print("Division:", a / b)
        print("Floor Division:", a // b)
        print("Modulus:", a % b)
        print("Exponentiation:", a ** b)

        print("\n   -LESSON 2: EXPRESSIONS IN PYTHON-")
        print("An expression is a combination of values,")
        print("variables, and operators that produces a result.")

        print("\n               EXAMPLE:")
        a = 2
        b = 3
        c = 4
        print("a = 2, b = 3, c = 4")
        print("a + b * c =", a + b * c)

        print("\n   -LESSON 3: ORDER OF OPERATIONS-")
        print("Python follows PEMDAS:")
        print("P - Parentheses")
        print("E - Exponents")
        print("M - Multiplication")
        print("D - Division")
        print("A - Addition")
        print("S - Subtraction")

        print("\n EXERCISE 1: STUDENT GRADES")
        math = 85
        science = 88
        english = 90
        average = (math + science + english) / 3

        print("Math:", math)
        print("Science:", science)
        print("English:", english)
        print("Average Grade:", round(average, 2))

        print("\n EXERCISE 2: RECTANGLE AREA AND PERIMETER")
        length = 12
        width = 8

        area = length * width
        perimeter = 2 * (length + width)

        print("Length:", length)
        print("Width:", width)
        print("Area:", area)
        print("Perimeter:", perimeter)

        back = input("\nDO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break



    elif choi == 4:
        print("\n  =============== MODULE 4 ===============")
        print("       BASIC INPUT AND OUTPUT IN PYTHON")
        print("  =========================================")

        print("\n   -LESSON 1: ACCEPTING USER INPUT-")
        print("The input() function allows users to enter")
        print("information into a Python program.")

        print("\n SYNTAX:")
        print('name = input("Enter your name: ")')

        print("\n               EXAMPLE:")
        name = input("Enter your name: ")
        age = input("Enter your age: ")

        print("\n   -LESSON 2: FORMATTING OUTPUT-")
        print("The print() function displays information.")
        print("You can use commas to separate variables.")

        print("\n OUTPUT:")
        print("Name:", name)
        print("Age:", age)

        print("\n   -LESSON 3: CONVERTING INPUT TO OTHER DATA TYPES-")
        print("int()   - Converts a value into an integer.")
        print("float() - Converts a value into a decimal number.")
        print("str()   - Converts a value into a string.")

        print("\n               EXAMPLE: FLOAT INPUT")
        try:
            grade = float(input("Enter your grade: "))
            print("Your grade is:", grade)
        except ValueError:
            print("Invalid decimal number!")

        print("\n   -LESSON 4: BOOLEAN INPUT-")
        print("Boolean values are True or False.")

        answer = input("Are you a student? (yes/no): ")
        is_student = answer.lower() == "yes"
        print("Student status:", is_student)

        print("\n   -LESSON 5: GROCERY RECEIPT-")

        customer = input("Customer Name: ")
        item = input("Item Name: ")

        try:
            price = float(input("Price per Item: "))
            quantity = int(input("Quantity Purchased: "))

            total = price * quantity
            vat = total * 0.12
            final_total = total + vat

            print("\n========== GROCERY RECEIPT ==========")
            print("Customer:", customer)
            print("Item:", item)
            print("Price:", price)
            print("Quantity:", quantity)
            print("Total Cost:", total)
            print("VAT (12%):", vat)
            print("Amount to Pay:", final_total)
            print("=====================================")

        except ValueError:
            print("INVALID INPUT! Please enter numbers.")

        back = input("\nDO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break





    elif choi == 5:
        print("\n  =============== MODULE 5 ===============")
        print("        CONDITIONAL STATEMENTS")
        print("  =========================================")

        print("\n   -LESSON 1: CONDITIONAL STATEMENTS-")
        print("Conditional statements allow a program to")
        print("make decisions based on certain conditions.")

        print("\n   -LESSON 2: RELATIONAL OPERATORS-")
        print("==  Equal to")
        print("!=  Not equal to")
        print(">   Greater than")
        print("<   Less than")
        print(">=  Greater than or equal to")
        print("<=  Less than or equal to")

        print("\n               EXAMPLE:")
        score = 85
        print("Score:", score)
        print("Is score greater than 75?", score > 75)

        print("\n   -LESSON 3: THE IF STATEMENT-")
        age = 20

        if age >= 18:
            print("You are an adult.")

        print("\n   -LESSON 4: THE IF-ELSE STATEMENT-")
        score = 65

        if score >= 75:
            print("Passed")
        else:
            print("Failed")

        print("\n   -LESSON 5: THE IF-ELIF-ELSE STATEMENT-")
        grade = int(input("Enter your grade: "))

        if grade >= 90 and grade <= 100:
            print("Excellent")
        elif grade >= 85:
            print("Very Good")
        elif grade >= 75:
            print("Passed")
        elif grade >= 0:
            print("Failed")
        else:
            print("Invalid Grade")

        print("\n   -LESSON 6: NESTED CONDITIONS-")
        number = int(input("Enter a number: "))

        if number >= 0:
            if number == 0:
                print("The number is zero.")
            else:
                print("The number is positive.")
        else:
            print("The number is negative.")

        back = input("\nDO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break



    elif choi == 6:
        print("\n  =============== MODULE 6 ===============")
        print("        LOGICAL OPERATORS")
        print("  =========================================")

        print("\n   -LESSON 1: WHAT ARE LOGICAL OPERATORS?-")
        print("Logical operators combine or reverse")
        print("conditions in a Python program.")

        print("\n THREE LOGICAL OPERATORS:")
        print("AND - True if all conditions are True.")
        print("OR  - True if at least one condition is True.")
        print("NOT - Reverses the result of a condition.")

        print("\n   -LESSON 2: AND OPERATOR-")
        print("The AND operator returns True only when")
        print("both conditions are True.")

        age = 20
        has_id = True

        print("\n               EXAMPLE:")
        print("Age:", age)
        print("Has ID:", has_id)
        print("Can enter:", age >= 18 and has_id)

        print("\n AND TRUTH TABLE:")
        print("TRUE  AND TRUE  =", True and True)
        print("TRUE  AND FALSE =", True and False)
        print("FALSE AND TRUE  =", False and True)
        print("FALSE AND FALSE =", False and False)

        print("\n   -LESSON 3: OR OPERATOR-")
        print("The OR operator returns True when at least")
        print("one condition is True.")

        print("\n OR TRUTH TABLE:")
        print("TRUE  OR TRUE  =", True or True)
        print("TRUE  OR FALSE =", True or False)
        print("FALSE OR TRUE  =", False or True)
        print("FALSE OR FALSE =", False or False)

        print("\n               EXAMPLE:")
        day = "Saturday"

        if day == "Saturday" or day == "Sunday":
            print("It's the weekend!")
        else:
            print("It's a regular school day.")

        print("\n   -LESSON 4: NOT OPERATOR-")
        print("The NOT operator reverses the result")
        print("of a condition.")

        print("\n NOT TRUTH TABLE:")
        print("NOT TRUE  =", not True)
        print("NOT FALSE =", not False)

        print("\n               EXAMPLE:")
        is_raining = False

        if not is_raining:
            print("You can go outside.")
        else:
            print("Bring an umbrella.")

        print("\n   -LESSON 5: COMBINING LOGICAL OPERATORS-")
        age = 20
        score = 90

        if age >= 18 and score >= 75:
            print("Requirements completed!")
        else:
            print("Requirements not completed.")

        back = input("\nDO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break



    elif choi == 7:
        print("\n  =============== MODULE 7 ===============")
        print("        ITERATION AND LOOPS")
        print("  =========================================")

        print("\n   -LESSON 1: INTRODUCTION TO ITERATION-")
        print("Iteration means repeating a process.")
        print("Each repetition is called an iteration.")

        print("\n   -LESSON 2: WHY USE LOOPS?-")
        print("Loops allow a program to perform the same")
        print("task multiple times without repeating code.")

        print("\n WITHOUT A LOOP:")
        print('print("Study Python")')
        print('print("Study Python")')
        print('print("Study Python")')

        print("\n USING A LOOP:")
        print("for number in range(3):")
        print('    print("Study Python")')

        print("\n   -LESSON 3: TYPES OF LOOPS-")
        print("1. FOR LOOP")
        print("2. WHILE LOOP")

        print("\n   -LESSON 4: PYTHON FOR LOOP-")
        print("A for loop repeats instructions for each")
        print("item in a sequence.")

        print("\n SYNTAX:")
        print("for variable in sequence:")
        print("    statement")

        print("\n               EXAMPLE: PRINT NUMBERS 1 TO 5")

        for number in range(1, 6):
            print(number)

        print("\n   -LESSON 5: COUNTING DOWN WITH RANGE()-")

        for number in range(5, 0, -1):
            print(number)

        print("\n   -LESSON 6: OUTPUT ODD NUMBERS-")
        for number in range(1, 10, 2):
            print(number)

        print("\n   -LESSON 7: OUTPUT EVEN NUMBERS-")
        for number in range(2, 11, 2):
            print(number)

        print("\n   -LESSON 8: PYTHON WHILE LOOP-")
        print("A while loop repeats a block of code")
        print("as long as its condition is True.")

        count = 1

        while count <= 5:
            print("Count:", count)
            count += 1

        back = input("\nDO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break


    elif choi == 0:
        print("\n==========================================")
        print("THANK YOU FOR USING PYTHON TUTORIAL!")
        print("          END OF THE PROGRAM")
        print("==========================================")
        break

    else:
        print("\nINVALID CHOICE! PLEASE SELECT 0 TO 7.")

        back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        while back != "Y" and back != "N":
            print("INVALID CHOICE!")
            print("PLS CHOICE A Y AND N!")
            back = input("DO YOU WANT TO GO IN MAIN MENU?  YES FOR Y AND NO FOR N (Y/N): ").upper()

        if back == "Y":
            print("\n     GOING TO MAIN MENU!\n")

        elif back == "N":
            print("\n     BYE SEE YOU NEXT TIME!")
            break




