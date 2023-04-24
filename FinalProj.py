

class Class:

    def __init__(self):
        self.students = [] 

    def add_student(self, name):
        self.students.append([name+''])
                
    def add_assignment(self, assignment_type, assignment_name, max_points):
        count = 0
        for x in self.students:
            self.students[count].append(assignment_type)
            self.students[count].append(assignment_name)
            while (True):
                grade = input("Please enter the grade for: {} ".format(self.students[count][0]))
                if (grade.isdigit() == False or int(grade) < 0):
                    print("Error: grade must be a number greater than or equal to zero")
                    
                else:
                    break
            self.students[count].append(int(grade))
            self.students[count].append(max_points)
            count += 1
        

    def delete_assignment(self, delete):
        for x in self.students:
            for y in range(len(x)):
                if (delete == x[y] and (x[y-1] == "Test" or x[y-1] == "Homework")):
                    del x[y-1]
                    del x[y-1]
                    del x[y-1]
                    del x[y-1]
                    break

    def edit_assignment(self, student, edit, change):    
        for x in self.students:
            if (student == x[0]):
                for y in range(len(x)-1):
                    if (edit == x[y]): 
                        x[y+1] = change  
    
    def get_assignment_grade(self): 
        count = 0
        for x in self.students:
            y_count = 0
            for y in range(3, len(x), 5):
                self.students[count].insert(y+2, x[y]/x[y+1])
                y_count += 1
                if (y_count == (len(x)-1)/5): 
                    count += 1
                    

    def total_grade(self):
        count = 0
        for x in self.students:
            score_total = 0
            max_total = 0
            if (x[2] == "A" or x[2] == "B" or x[2] == "C" or x[2] == "D" or x[2] == "F"):
                for y in range(5, len(x)-1, 4):
                    score_total += int(x[y])
                    max_total += int(x[y+1])
                    if (y == len(x)-2):
                        self.students[count].pop(1)
                        self.students[count].pop(1)
                        self.students[count].insert(1, score_total/max_total)
                        if (float(x[1]) >= .9):
                            self.students[count].insert(2, "A")
                        elif (float(x[1]) >= .8):
                            self.students[count].insert(2, "B")
                        elif (float(x[1]) >= .7):
                            self.students[count].insert(2, "C")
                        elif (float(x[1]) >= .6):
                            self.students[count].insert(2, "D")
                        else:
                            self.students[count].insert(2, "F")
                        count += 1
            else:
                for y in range(3, len(x)-1, 4):
                    score_total += int(x[y])
                    max_total += int(x[y+1])
                    if (y == len(x)-2):
                        self.students[count].insert(1, score_total/max_total)
                        if (float(x[1]) >= .9):
                            self.students[count].insert(2, "A")
                        elif (float(x[1]) >= .8):
                            self.students[count].insert(2, "B")
                        elif (float(x[1]) >= .7):
                            self.students[count].insert(2, "C")
                        elif (float(x[1]) >= .6):
                            self.students[count].insert(2, "D")
                        else:
                            self.students[count].insert(2, "F")
                        count += 1

    def show_grades(self):
        for x in self.students: 
            print('\n')
            print(x[0], "Total Grade: ", "{:.2%}".format(x[1]), x[2], '\n')

            for y in range(3, len(x)-2, 4):
                print(*x[y:y+4])



 

def main():

    while (True):
        new_class = input("\nPlease enter the name of your existing class, otherwise enter 1 for a new class: ")
        class_name = new_class + ".txt"
        if (new_class == "1"):
            new_class = input("\nPlease enter the name of the new class: ")
            class_name = new_class + ".txt"
            new_class = Class()

            while (True): 
                new_student = input("\nPlease enter the name of a student, if all students are entered, enter 1: ")
                if (new_student == "1"):
                    break
                else: 
                    new_class.add_student(new_student)
        else:
            new_class = Class()

            try: 
                with open(class_name, 'r') as f:
                
                    for x in f:
                        number = x.split()
                        new_class.students.append(number)
            except FileNotFoundError:
                print("Error: file not found.")
                break

        while(True):
            cont = input("\nPlease enter\n1 to see all grades \n2 to create/edit/delete assignments \n3 to exit the program: ")

            if (cont == "1"):
                try:
                    new_class.total_grade()
                except AttributeError:
                    Print("\nError: no assignments were found.")
                try: 
                    new_class.show_grades()
                except IndexError:
                    print("\nError: no assignments were found.")


            elif (cont == "2"):
                while (True):                   
                    new_assignment = input("\nPlease enter \n1 to add an assignment \n2 to delete an assignment \n3 to edit an assignment\n4 if all assignments are entered: ")
                    
                    while (True):
                        if (new_assignment == "1"):
                            assignment_type = input("\nPlease enter the type of assignment: Homework or Test: ")
                            if (assignment_type != "Homework"):
                                if (assignment_type != "Test"):
                                    print("\nError: Assignment type has to be Test or Homework.")
                                    break

                            assignment_name = input("\nPlease enter the name of the assignment: ")
                            if (assignment_name == "Homework" or assignment_name == "Test"):
                                print("\nError: Assignment Name cannot be Test or Homework.")
                                break

                            max_points = (input("\nPlease enter the max points of the assignment: "))
                            if (max_points.isdigit() == False):
                                print("\nError: max points must be a positive number.")
                                break

                            elif (int(max_points) <= 0):
                                print("\nError: max points cannot be less than or equal to 0")
                                break

                            else:
                                new_class.add_assignment(assignment_type, assignment_name, int(max_points))
                                break

                        elif (new_assignment == "2"):
                            delete = input("\nPlease spell out which assignment needs to be deleted: ")
                            new_class.delete_assignment(delete)
                            break

                        elif (new_assignment == "3"):
                            student = input("\nPlease spell out which student needs to be edited: ")
                            edit = input("\nPlease spell out which assignment needs to be edited: ")
                            change = input("\nPlease enter the grade it will be changed to: ")
                            if (change.isdigit() == False or int(change) <= 0 ):
                                print("Error: change in grade must be a positive number.")
                            else:
                                new_class.edit_assignment(student, edit, int(change))
                                break

                        else:
                             break

                    break

                else:
                    break
            else:
                with open(class_name, 'w') as f:
                    for x in new_class.students:
                        for y in range(len(x)):
                            f.write(str(x[y]) + " ")
                            if (y == len(x)-1):
                                f.write("\n")
                    break 
        break

            

main()