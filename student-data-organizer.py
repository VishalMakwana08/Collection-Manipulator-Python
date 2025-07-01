#This Is Python Project For Student Data Organize By Using Collection Manipulator -
#like list , tupel , set , dict
#this program allowed to add student data , update , delete and display 
#Created By 'Vishal Makwana'

print("Welcome To The Student Data Organizer!\n")
student_data=dict()
all_student_data=dict()
#program start
while(True):
    #choices
    print("Select An Option:")
    print("1.Add New Student")
    print("2.Display All Student")
    print("3.Update Student Information")
    print("4.Delete Student Information")
    print("5.Display Subject Offered")
    print("6.Exit")
    choice=int(input("Enter Your Choice:"))
    #match case
    match(choice):
        case 1:
              #add new student
              print("\nEnter Student Detail:\n")
              studentId=int(input("Student Id:"))
              name=input("Name:")
              age=int(input("Age:"))
              grade=input("Grade:")
              dob=input("Date Of Birth (YYYY-MM-DD):")
              subjects=input("Subjects (comma-separeted):")
              print("\nStudent  Added Successfully\n")
              std_subjects=set(subjects.split(','))
             
              student_data={"Id":studentId,"Name":name,"Age":age,"Grade":grade,"DOB":dob,"Subjects":std_subjects}
              all_student_data[studentId]=student_data
            
        case 2:
             #display students records
             print("----Display All Student Detils----")
             for i in all_student_data.keys():
                  for j in all_student_data[i].keys():
                       print(f"{j} : {all_student_data[i][j]}",end="|")
                  print("")
             print("")

            
        case 3:
            #update student records
            upadte_id=int(input("Enter Student Id You Want To Update:")) 
           
            count=int(0)
                   
            for i in all_student_data.keys():
                if i == upadte_id:
                    count+=int(1)
                    break
            if count==1:
                    print("select option:\n")
                    print("1.update name")
                    print("2.update age")
                    print("3.update grade")
                    print("4.update dob")
                    print("5.update subjects")
                    print("6.No Need To Update")
                    option=int(input("Enter Any Option:"))

                    match(option):
                            case 1:
                              new_name=input("Enter New Name:")
                              all_student_data[upadte_id]["Name"]=new_name
                              print("\nName Updated")
                            case 2:
                              new_age=int(input("Enter New Age:"))
                              all_student_data[upadte_id]["Age"]=new_age
                              print("\nAge Updated")
                            case 3:
                              new_grade=(input("Enter New Grade:"))
                              all_student_data[upadte_id]["Grade"]=new_grade
                              print("\nGrade Updated")
                            case 4:
                              new_dob=(input("Enter New DOB (YYYY-MM-DD):"))
                              all_student_data[upadte_id]["DOB"]=new_dob
                              print("\nDOB Updated")
                            case 5:
                              new_subjects=input("Enter New Subjects (comma-separeted):")
                              new_sub=set(new_subjects.split(','))
                              all_student_data[upadte_id]["Subjects"]=new_sub
                            case 6:
                                pass
            else:
                 print("\nThis Id Is Not Available\n")
        case 4:
            #delete student records
            delete_id=int(input("Enter Student Id You Want To Delete:")) 
           
            count=int(0)
                   
            for i in all_student_data.keys():
                if i == delete_id:
                    count+=int(1)
                    break
            if count==1:
                deleted_rec=all_student_data.pop(delete_id)
                print(f"Deleted Record Is:{deleted_rec}")
            else:
                print("\nId Not Found")
        case 5:
            #available subjects
            print("--Offered Subjects Is 'maths,physics,chemistry'---")
        case 6:
          #exit
          print("\nEnd Of Program")
          print("\nThank You GoodBye!")
          break
        case _:
            print("Invalid Choice")
