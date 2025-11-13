#level1
def Student():
    """This function Creates a dictionary with a student’s name, age and grade,prints the name and grade of the student,
    adds a new parameter called school, changes the student’s grade and finally deletes the age parameter"""
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
Student()

#level 2

def Capitals():
    """This function creates a dictionary with countries and their capitals, It then loops through the countries list
    and prints their name and capital city, first separately then in a sentence.
    Then it finds if Germany is in the dictionary"""
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
Capitals()

#level 3
def Students():
    """This function creates a dictionary with multiple students and their name, age and grade, it prints Bob’s grade,
    It adds a third student named Charlie and assigns them the age of 15 and the A grade, it also changes Alice’s grade to A+.
    It then loops through the students and prints their name and grade"""
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
Students()