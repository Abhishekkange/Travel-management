import mysql.connector as co
def Tourist_Data():
    print("---------------TOURIST DATA BLOCK--------")
    print("|1.Tourist details")
    print("|2.Delete tourist details")
    print("|3.Insert tourist details")
    print("|4.return to Main Menu")
    print("- - - - -- - - - - - - - - - - - - - - ")
    x=int(input("choose one of above functions"))
    if x==1:
      Tourist_details()
    elif x==2:
        Delete_Tourist_details()
    elif x==3:
        Insert_Tourist_details()
    elif x==4:
        return
    else:
        print("invalid input")
        print("press any key to return to main menu")

def Tourist_details():
    try:
        mycon=co.connect(host="localhost",user="abhishek",passwd="abhishek",database="Tourism")
        cursor=mycon.cursor()
        cursor.execute("select * from tourist_data")
        data=cursor.fetchall()
        print(data)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        Tourist_Data()
    except:
        print("error")

def Delete_Tourist_details():
    try:
        pass     #code to be written here


    except:
        print("error")

def Insert_Tourist_details():
    try:
        mycon=co.connect(host="localhost",user="abhishek",passwd="abhishek",database="tourism")
        cursor=mycon.cursor()
        sr_no=int(input("enter sr_no"))
        First_Name=input("enter first Name")
        Last_Name=input("enter last name")
        Phone_No=input("enter phone no")
        query="INSERT INTO tourist_data(sr_no,First_Name,Last_Name,Phone_No) VALUES(%s,%s,%s,%s)"
        val=(sr_no,First_Name,Last_Name,Phone_No)
        cursor.execute(query,val)
        mycon.commit()
        print("record is been saved in record")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                       
              
    except:
        print("Something Went wrong Data not entered")
    

    

   






        



        
