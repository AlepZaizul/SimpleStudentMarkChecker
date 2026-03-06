user = ['student1', 'student2', 'student3']
spass = ['pass1','pass2','pass3']

attempt = 1
print ("============MARK CHECKER SYSTEM=============")
print ("===========ENTER YOUR CREDENTIAL============")

while attempt <=3:

    username = input("Enter Your Username :")
    password = input("Enter Your Password :")

    if username in user and password in spass:
        print("Login Success!")
        print("==================Check your Result=========================")
        name = str(input ("Enter Your Name: "))
        marks = int(input("Enter Your Marks: "))
        if (marks >=90 and marks <=100):
                grade= "A+"
                message = "Sangat Cemerlang! Tahniah"
        elif (marks >=80 and marks <=89):
                grade = "A"
                message = "Cemerlang1"
        elif (marks >=75 and marks <=79):
                grade = "A-"
                message = "Kepujian"
        elif (marks >=70 and marks <=74):
                grade = "B+"
                message = "Kepujian"
        elif (marks >=65 and marks <=69):
                grade = "B"
                messsage = "Kepujian"
        elif (marks >= 60 and marks <=64):
                grade = "B-"
                message = "Lulus"
        elif (marks >=55 and marks <=59):
                grade = "C+"
                message = "Lulus"
        elif (marks >= 50 and marks <=54):
                grade = "C"
                message = "Lulus"
        elif (marks >=47 and marks <=49):
                grade = "C-"
                message = "Lulus"
        elif (marks >=40 and marks <=46):
                grade = "C"
                message = "Lulus"

        else:
            grade ="F" 
            message = "GAGAL"
        print ("======================RESULT=====================================")
        print ("Hi! " +str(name)+ " This is Your Result: " +str(grade)+ " You are " +str(message))
        print ("=================================================================")
        break
    else: 
           print("Username or password does not contained in database")
           attempt +=1
else:
       print ("Your attempt exceed " +str(attempt - 1) + " times. Please contact Administrator for further information.")