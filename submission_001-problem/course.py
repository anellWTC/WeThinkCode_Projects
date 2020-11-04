# Step 1
def create_outline(): # default function
    course_topics = set(["Introduction to Python",
                    "Tools of the Trade",
                    "How to make decisions",
                    "How to repeat code",
                    "How to structure data",
                    "Functions",
                    "Modules"]) # creating a set
    
    sorted_list = list(course_topics) #convert set to list
    sorted_list.sort()  # sorting the list in alphabetical order
    print("Course Topics:")
    for topic in sorted_list: # for loop
        print(f"* {topic}") # display contents in set
        
    pass

# Step 2
    print("Problems:") # printing problems
    problems = ["Problem 1","Problem 2","Problem 3"] # storing info to be displayed after each heading
    custom_dict = dict() # create a dictionary
    for topic in sorted_list: # for loop
        custom_dict.update({topic:problems}) # update course_topics with subheadings
        print(f"* {topic} : ", end = "") # end keeps it all inline , otherwise problems 1 to 3 moves in a new line
        print(*custom_dict[topic],sep=", ")
# Step 3
    print("Student Progress:") # printing Student Progress
    #creating a tuple to display student information
    student1 = ("Nyari","Introduction to Python","Problem 2","[COMPLETED]")
    student2 = ("Adam","How to make decisions","Problem 1","[GRADED]")
    student3 = ("Daniel","Functions","Problems 3","[COMPLETED]")
    student4 = ("Gareth","How to structure data","Problems 1","[STARTED]")
# Step 4
    students = [student1,student2,student3,student4]
    new_list = []
    for status in students: # for loop, sorting status only 3 status available   
            if status[3] == "[STARTED]":
                new_list.append(status)
    for status in students:
        if status[3] == "[GRADED]":
            new_list.append(status)
    for status in students:
        if status[3] == "[COMPLETED]":
            new_list.append(status)
    nr = 1
    for student, module, problem, status in new_list: # refer to tuples from line 23 to 28
        print(f"{str(nr)}. ", end = '')
        print(f"{student} - {module} - {problem} {status}")
        nr += 1
if __name__ == "__main__":
    create_outline()