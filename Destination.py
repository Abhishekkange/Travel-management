import mysql.connector as co
def Destination_Data():
    print("----------------------WELCOME TO DESTINATION INFO BAR-----------------")
    print("|1.destination details")
    print("|2.Delete destination details")
    print("|3.Update destination details")
    print("|4.return to Main Menu")
    x=int(input("enter your choice"))
    if x==1:
      Destination_details()
    elif x==2:
      Delete_Destination_details()
    elif x==3:
      Insert_Destination_details()
    elif x==4:
      return
    else:
        print("OOPS !! SOMETHING WENT WRONG")
        print("PRESS ANY KEY TO RETURN TO MAIN MENU")


def Destination_details():
    try:
        mycon=co.connect(host="localhost",user="abhishek",passwd="abhishek",database="Tourism")
        cursor=mycon.cursor()
        cursor.execute("select * from destination")
        data=cursor.fetchall()
        print(data)
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        Destination_Data()

    except:
        print("OOPS !! SOMETHING WENT WRONG")

def Delete_Destination_details():
    try:
        pass
                     #code remaing


    except:
        print("OOPS !! SOMETHING WENT WRONG")  

def Insert_Destination_details():
    try:
         mycon=co.connect(host="localhost",user="abhishek",passwd="abhishek",database="Tourism")
         cursor=mycon.cursor()
         Destination=input("enter destination")
         Place=input("enter place")
         Hotel=input("enter hotel")
         Guide=input("guide required or not{yes/no")
         query="INSERT INTO destination(Destination,Place,Hotel,Guide) VALUES(%s,%s,%s,%s)"
         val=(Destination,Place,Hotel,Guide)
         cursor.execute(query,val)
         mycon.commit()
         print("Data Entered Succesfully")
         print("----------------------------------------------------------------------------------------------------------------------------------------------------") 
    except:
        print("Something went wrong Data not entered")
        
     




        


        
        
