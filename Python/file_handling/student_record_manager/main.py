print("Welcome to student record manager !!!")
while True:

    print("What Do you want to do? ")
    print("1 for Add new student")
    print("2 for display student record")
   
    user_request=int(input("Enter Your Choice: "))
    if (user_request==1):
        f=open("student.txt","a")
        name=input("Enter Student Name: ")
        roll_no=input("Enter Your Roll.No: ")
        mark=input("Enter Your Mark: ")
        f.write(name+" ")
        f.write(roll_no+" ")
        f.write(mark+" \n")
        f.close()

    elif(user_request==2):
        with open("student.txt","r") as f:
            data=f.read()
            print(data)


    

        
        

    choice=input("Do You want to continue(Y/N)").upper()
    if (choice=="N" or choice=="NO"):
        break;









