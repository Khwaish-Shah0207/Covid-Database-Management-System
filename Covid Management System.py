#SOURCE CODE FOR Covid Management

print("****************************************************************************")
print("*                                                                          *")
print("*             Welcome to Covid Management System             *")
print("*                                                                          *")
print("****************************************************************************")
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",passwd='1234')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists covid_management")
mycursor.execute("use covid_management")
mycursor.execute("create table if not exists staff(sno varchar(25) not null,name varchar(25) not null, age varchar(25) not null, gender char(1) not null,post varchar(25) not null,salary varchar(25) not null)")
mycursor.execute("create table if not exists patients(sno varchar(25) not null,name varchar(25) not null,age varchar(25) not null, gender varchar(25) not null, date date not null)")
mycursor.execute("create table if not exists login(admin varchar(25) not null,password varchar(25) not null)")
mycursor.execute("create table if not exists sno(patient varchar(25) not null,staff varchar(25) not null)")
mycursor.execute("select * from sno")
z=0
for i in mycursor:
    z=1
if z==0:
    mycursor.execute("insert into sno values('0','0')")
mydb.commit()
j=0
mycursor.execute("select * from login")

for i in mycursor:
    j=1
if(j==0):
    mycursor.execute("insert into login values('Admin','ng')")
    mydb.commit()
loop1='y'
while(loop1=='y' or loop1=='Y'):
    print("_______________________")
    print("1.Admin")
    print("2.Patient")
    print("3.Exit")
    print("_______________________")
    ch1=int(input("Enter your choice: "))
    if(ch1==1):
        pas=input("Enter your Password: ")
        mycursor.execute("select * from login")
        for i in mycursor:
            username,password=i
        if(pas==password):
            loop2='n'
            while(loop2=='n' or loop2=='N'):
                print("________________________")
                print("1.Add patients")
                print("2.Add Staff")
                print("3.Display Patients Record")
                print("4.Display Staff Record")
                print("5.change password")
                print("6.Remove Patients")
                print("7.Remove Staff")
                print("8.Logout")
                print("________________________")
                ch2=int(input("Enter your choice: "))
                if(ch2==1):
                    loop3='y'
                    while(loop3=='y' or loop3=='Y'):
                        name=input("Enter patients name: ")
                        age=input("Enter patients age: ")
                        gender=input("Enter patients gender: ")
                        date=input("Enter date of conformation of covid: ")
                        mycursor.execute("select * from sno")
                        for i in mycursor:
                            patient,staff=i
                            patient=int(patient)+1
                        
                        mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"','"+date+"')")
                        
                        mycursor.execute("update sno set patient='"+str(patient)+"'")
                        mydb.commit()
                        print("data of Patient has been saved successfully...")
                        mycursor.execute("select * from patients")
                        t=0
                        for i in mycursor:
                            t+=1
                            t_id1,name1,age1,gender1,date1=i
                        print(f"Total number of Corona Infected patients--> {patient}")
                                                    
                        print(f"Active Corona Cases--> {t}")

                        print(f"This patient with id {t_id1} will be in quarantine upto 14 days from {date1}")
                        
                        loop3=input("Do You Want To Enter More Data Of More Patients(y/n): ")
                    loop2=input("Do You Want To Logout(y/n): ")
                elif(ch2==2):
                    loop3='y'
                    while(loop3=='y' or loop3=='Y'):
                        name=input("Enter New Staff Name: ")
                        age=input("Enter Age: ")
                        gender=input("Enter gender(m/f): ")
                        post=input("Enter His/Her post: ")
                        salary=input("Enter His/Her Salary: ")
                        
                        mycursor.execute("select * from sno")
                        for i in mycursor:
                            patient,staff=i
                            staff=int(staff)+1
                            
                        mycursor.execute("insert into staff values('"+str(staff)+"','"+name+"','"+age+"','"+gender+"','"+post+"','"+salary+"')")
                        mycursor.execute("update sno set staff='"+str(staff)+"'")
                        mydb.commit()
                        print(f"staff with id {staff} has been saved successfully...")
                        
                        mycursor.execute("select * from staff")
                        t=0
                        for i in mycursor:
                            t+=1
                            
                        print(f"Active Staff Members--> {t}")

                        loop3=input("Do You Want To Enter More Staff Data(y/n) :")
                    loop2=input("Do You Want To LogOut(y/n): ")
                elif(ch2==3):
                    idd=input("Enter patient's ID: ")
                    t_id2,name2,age2,gender2,date2=["","","","",""]
                    mycursor.execute("select * from patients where sno='"+idd+"'")
                    for i in mycursor:
                        t_id2,name2,age2,gender2,date2=i
                    print("| ID | NAME | AGE | GENDER | CORONA POSITIVE DATE |")
                    print(f"| {t_id2} | {name2} | {age2} | {gender2} | {date2} |")
                elif(ch2==4):
                    idd=input("Enter Staff ID: ")
                    t_id3,name3,age3,gender3,past3,salary3=["","","","","",""]
                    mydb.commit()
                    mycursor.execute("select * from staff where sno='"+idd+"'")
                    for i in mycursor:
                        t_id3,name3,age3,gender3,past3,salary3=i
                    print("| ID | NAME | AGE | GENDER | POST | SALARY |")
                    print(f"| {t_id3} | {name3} | {age3} | {gender3} | {past3} | {salary3} |")
                elif(ch2==5):
                    pas=input("Enter Old Password: ")
                    mycursor.execute("select * from login")
                    for i in mycursor:
                        username,password=i
                    if(pas==password):
                        npas=input("Enter New Password: ")
                        mycursor.execute("update login set password='"+npas+"'")
                        mydb.commit()
                    else:
                        print("Wrong Password...")
                elif(ch2==6):
                    loop3='y'
                    while(loop3=='y' or loop3=='Y'):
                        idd=input("Enter Patient ID")
                        mycursor.execute("delete from patients where sno='"+idd+"'")
                        mydb.commit()
                        print("Patient has been removed successfully")
                        loop3=input("Do You Want To Remove More Patients(y/n): ")
                    
                elif(ch2==7):
                    loop3='y'
                    while(loop3=='y' or loop3=='Y'):
                        idd=input("Enter Staff ID")
                        mycursor.execute("delete from Staff where sno='"+idd+"'")
                        mydb.commit()
                        print("Staff has been removed successfully")
                        loop3=input("Do You Want To Remove More Staff(y/n): ")
                elif(ch2==8):
                    break
    elif(ch1==2):
        print("Thank You for coming forward for your test...")
        icough=input("Are you feeling cough?(y/n): ").lower()
        dry_cough='n'
        cough='n'
        if(icough=='y' or icough=='Y'):
            dry_cough=input("Are you feeling dry cough(y/n): ").lower()
            cough=input("Are you feeling normal cough(y/n):").lower()
            
        sneeze=input("Are You feeling Sneeze?(y/n): ").lower()
        pain=input("Are You feeling pain in your body?(y/n): ").lower()
        weakness=input("Are You feeling weakness?(y/n): ").lower()
        mucus=input("Are You feeling any mucus(y/n)").lower()
        itemp=int(input("please Enter your temprature: "))
        if(itemp<=100):
            temp='low'
        else:
            temp='high'
        breath=input("Are you having difficulty in breathing: ").lower()
        if(dry_cough=='y' and sneeze=='y' and pain=='y' and weakness=='y' and temp=='high' and breath=='y'):
            print("Sorry To Say But According to us u are suffering from Corona.......")
            name=input("Enter your name: ")
            age=input("Enter your age: ")
            gender=input("Enter your gender(m/f): ")
            
            mycursor.execute("select * from sno")
            for i in mycursor:
                patient,staff=i
                patient=int(patient)+1
            mycursor.execute("insert into patients values('"+str(patient)+"','"+name+"','"+age+"','"+gender+"',now())")
            mycursor.execute("update sno set patient='"+str(patient)+"'")
            mydb.commit()
            print("data of Patient has been saved successfully...")
            print(f"Total number of Corona Infected patients--> {patient}")
            mycursor.execute("select * from patients")
            t=0
            for i in mycursor:
                t+=1
                
            print(f"Active Corona Cases--> {t}")
            mycursor.execute("select * from patients")
            for i in mycursor:
                t_id5,name5,age5,gender5,date5=i
            print(f"This patient with id {t_id5} will be in quarantine upto 14 days from {date5}")
        elif(dry_cough=='y' and sneeze=='y' and pain=='n' and weakness=='n' and temp=='low' and breath=='n'):
            print("Nothing To worry, its just due to Air Pollution...")
            
        elif(cough=='y' and mucus=='y' and sneeze=='y' and pain=='n' and weakness=='n' and temp=='low' and breath=='n'):
            print("nothing to worry, its just Common Cold...")
        else:
            print("You are not corona infected, if u are feeling somwething wrong, you just need to rest... ")
            print("If then also you can't feel better,please consult to your doctor.")
    elif(ch1==3):
        break
