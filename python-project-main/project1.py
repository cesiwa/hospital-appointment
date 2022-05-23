from audioop import add
from ssl import create_default_context

import dict
import sqlite3
import dataBase



keydental= list(dict.dentalHealthDoctors.keys())
daydental= list(dict.dentalHealthDoctors.values())

keyPsychology = list(dict.psychology.keys())
dayPsychology = list(dict.psychology.values())

keySkin= list(dict.skin.keys())
daySkin = list(dict.skin.values())

while(1):

    def DentalHealth():

        def DentalHealthAppointmentCreated():
            print("""
            Your appointment has been created.
            **********************************
            *****Appointment Information******
            ***Doctor: {}***
            ***Appointment Date:{}***
            """.format(keydental[chooseDentalDoctor-1],daydental[chooseDentalDoctor-1]["day"][chooseDay-1]))
    
        

        try:
            chooseDentalDoctor=int(input("""
            **WELCOME TO THE DENTAL HEALTH DEPARTMENT**

            Dental Health department has {} doctors.
            These doctors:
            1-Prof. Dr. {}
            2-Asst. Prof.{}
            3-Prof. Dr. {}
            """.format(len(dict.dentalHealthDoctors.keys()),*keydental)))
        except:
            print("Not a Number")
        
        if chooseDentalDoctor==1:
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keydental[chooseDentalDoctor-1],*daydental[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keydental[chooseDentalDoctor-1],*daydental[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    DentalHealthAppointmentCreated()
             
        if chooseDentalDoctor==2:
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keydental[chooseDentalDoctor-1],*daydental[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keydental[chooseDentalDoctor-1],*daydental[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    DentalHealthAppointmentCreated()
        
        try:
            if chooseDentalDoctor==3:
                chooseDay=int(input("""
                {}'s available days:
                1-){}
                2-){}
                3-){}
            
                """.format(keydental[chooseDentalDoctor-1],*daydental[0]["day"])))
        except:
            print("wrong number")

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                    
                """.format(keydental[chooseDentalDoctor-1],*daydental[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    DentalHealthAppointmentCreated()
                
            
        
        


    def Psychology():
        def PsychologyAppointmentCreated():
             print("""
            Your appointment has been created.
            **********************************
            *****Appointment Information******
            ***Doctor: {}***
            ***Appointment Date:{}***
            """.format(keydental[choosePsychologyDoctor-1],dayPsychology[choosePsychologyDoctor-1]["day"][chooseDay-1]))

        try:
            choosePsychologyDoctor=int(input("""
            **WELCOME TO THE PSYCHOLOGY DEPARTMENT**

            Psychology department has {} doctors.

            The available doctors:
                1-Asst. Prof. {}
                2-Prof. Dr. {}
                3-Asst. Prof. Will WALSH {}

            """.format(len(keyPsychology),*keyPsychology)))
        except:
            print("WRONG NUMBER")   

        if choosePsychologyDoctor == 1:
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keyPsychology[choosePsychologyDoctor-1],*dayPsychology[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keyPsychology[choosePsychologyDoctor-1],*dayPsychology[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    PsychologyAppointmentCreated()

        if choosePsychologyDoctor ==2:
            
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keyPsychology[choosePsychologyDoctor-1],*dayPsychology[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keyPsychology[choosePsychologyDoctor-1],*dayPsychology[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    PsychologyAppointmentCreated()

        if choosePsychologyDoctor ==3:
            
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keyPsychology[choosePsychologyDoctor-1],*dayPsychology[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keyPsychology[choosePsychologyDoctor-1],*dayPsychology[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    PsychologyAppointmentCreated()



      
        
        print("a")


    def Skin():
        
        def SkinAppointmentCreated():
             print("""
            Your appointment has been created.
            **********************************
            *****Appointment Information******
            ***Doctor: {}***
            ***Appointment Date:{}***
            """.format(keySkin[chooseSkinDoctor-1],daySkin[chooseSkinDoctor-1]["day"][chooseDay-1]))

        try:
            chooseSkinDoctor=int(input("""
            **WELCOME TO THE PSYCHOLOGY DEPARTMENT**

            Psychology department has {} doctors.

            The available doctors:
                1-Asst. Prof. {}
                2-Prof. Dr. {}
                3-Asst. Prof. Will WALSH {}

            """.format(len(keySkin),*keySkin)))
        except:
            print("WRONG NUMBER")   

        if chooseSkinDoctor == 1:
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keyPsychology[chooseSkinDoctor-1],*daySkin[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keyPsychology[chooseSkinDoctor-1],*daySkin[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    SkinAppointmentCreated()

        if chooseSkinDoctor ==2:
            
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keySkin[chooseSkinDoctor-1],*daySkin[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keySkin[chooseSkinDoctor-1],*daySkin[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    SkinAppointmentCreated()

        if chooseSkinDoctor ==3:
            
            chooseDay=int(input("""
            {}'s available days:
            1-){}
            2-){}
            3-){}
        
            """.format(keyPsychology[chooseSkinDoctor-1],*daySkin[0]["day"])))

            if chooseDay==1 or chooseDay==2 or chooseDay==3:
                chooseDate=int(input("""
                {}'s available dates:
                1-){}
                2-){}
                3-){}
                
                """.format(keySkin[chooseSkinDoctor-1],*daySkin[0]["date"])))

                if chooseDate==1 or chooseDate==2 or chooseDate == 3:
                    SkinAppointmentCreated()


        
        
        print("a")

    def Welcome():
        while(1):
            departmentChoose=int(input(""""
            Please select the department you want to make an appointment with.
                    1-Mouth, jaw and Dental Health Department
                    2-Psychology Department
                    3-Skin Department
            """))
            if departmentChoose==1:
                DentalHealth()
                break

            elif departmentChoose==2:
                Psychology()
                break

            elif departmentChoose==3:
                Skin()
                break
            else:
                print("WRONG CHOOSE. TRY AGAİN")
                continue


    choose=int(input("""
    Welcome. What do you want to do?
    1-) User Login
    2-) User Register
    3-) Doctor Login
    4-) EXIT
    """))
    if choose==1:
        username=input("Please enter your username\n")
        for i in dict.users.items():
            if username==i[0]:
                password=int(input("Please enter your password.\n"))
                if password==i[1]:
                    print("giriş başarılı")
                    Welcome()

    elif choose==2:
        try:
            newUser=input("Enter new username\n")
            newpassword = int(input("Enter new password. But just number :))\n"))
        except:
            print("Not A Number")

        dict.users.setdefault(newUser,newpassword)
        print(dict.users)

        Welcome()

    elif choose==3:
        dr_Log_Reg = int(input("1-) Login \n or \n 2-)Register ? "))
        if dr_Log_Reg ==1:
            dr_log_username = print("Please enter your username")
            

        elif dr_Log_Reg == 2:
            doctor_username = input("Enter your username")
            doctor_password = int(input("Enter your password"))

            def insert(username,password):

                add_command = """INSERT INTO doctors VALUES("{} " , {})"""
               
                dataBase.query.execute(add_command.format(username,password))
                

            insert(doctor_username,doctor_password)

    else:
        print("WRONG NUMBER CHOOSE PLEASE AGAİN")

