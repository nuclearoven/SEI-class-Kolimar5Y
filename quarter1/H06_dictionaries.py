#level1
def Student():
    """This function Creates a dictionary "student" with a student’s name, age and grade
    the function:
    -prints the name and grade of the student
    -adds a new parameter called school
    -changes the student’s grade
    -deletes the age parameter
    It returns the modified student dictionary"""
    # 1
    student = {"name": "Alice", "age": 16, "grade": "A"}
    # 2
    print(student["name"] + " "+ student["grade"])
    # 3
    student["school"] = "Greenwood High"
    # 4
    student["grade"] = "A+"
    # 5
    del student["age"]
    return student

def Capitals():
    """This function creates a dictionary "capitals" with countries and their capitals,
    -loops through the countries list
    -prints the name and capital city of each country, first separately then in a sentence.
    -finds if Germany is in the dictionary
    It returns the capitals dictionary"""
    # 1
    capitals = {
        "Germany": {"capitals": "Berlin"},
        "France": {"capitals": "Paris"},
        "USA": {"capitals": "Washington DC"}
    }
    for key in capitals:
        # 2
        print(key)
        # 3
        print(capitals[key]["capitals"])
        # 5
        print("the capital of " + key + " is " + capitals[key]["capitals"])
    # 4
    if "Germany" in capitals:
        print("Germany is in the dictionary")
    return capitals


#level 3
def Students():
    """This function creates a dictionary "students" with multiple students and their name, age and grade,
    - prints Bob’s grade
    -adds a third student named Charlie and assigns them the age of 15 and the A grade
    -changes Alice’s grade to A+.
    -loops through the students and prints their name and grade
    returns the modified students dictionary"""
    #1
    students = {
        "Alice": {"age": 16, "grade": "A"},
        "Bob": {"age": 17, "grade": "B"},
    }
    #2
    print(students["Bob"]["grade"])
    #3
    students["Charlie"] = {"age": 15, "grade": "A"}
    #4
    students["Alice"]["grade"] = "A+"
    #5
    for key in students:
        print(key + students[key]["grade"])
    return students

Student()
Capitals()
Students()