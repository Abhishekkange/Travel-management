import mysql.connector as co
def Transportation_Data():
    print("-----------------------WELCOME TO TRANSPORTATION INFO. BL0CK------------------------")
    print("1.Transport_details")
    print("2.Delete_Transport_details")
    print("3.Input_Transportation_details")
    print("4.Return to Main Menu")
    y=int(input("enter your choice"))
    if y==1:
        Transportation_details()
    elif y==2:
        Delete_Transportation_details()
    elif y==3:
        Input_Transportation_details()
    elif y==4:
        return
    else:
        print("OOPS !! SOMETHING WENT WRONG")
        print("PRESS ANY KEY TO RETURN TO MAIN MENU")


def Transportation_details():
    try:
        mycon=co.connect(host='localhost',user='abhishek',passwd='abhishek',database='Tourism')
        cursor=mycon.cursor()
        cursor.execute("select * from transport")
        data=cursor.fetchall()
        print(data)
        print("----------------------------------------------------------------------------------------------------------------------------------------------------")
        Transportation_Data()
        
    except:
        print("OOPS !! SOMETHING WENT WRONG")
        print("PRESS ANY KEY TO RETURN TO MAIN MENU")

def Delete_Transportation_details():
    try:
        pass       #code remaining




    except:
        print("OOPS !! SOMETHING WENT WRONG")
        print("PRESS ANY KEY TO RETURN TO MAIN MENU")




def Input_Transportation_details():
    try:
         mycon=co.connect(host="localhost",user="abhishek",passwd="abhishek",database="Tourism")
         cursor=mycon.cursor()
         Destination=input("enter the destination")
         Flight_details=input("enter flight details")
         Railway_details=input("enter rail details")
         Bus_details=input("enter bus details")
         query=("insert into transport(Destination,Flight_details,Railway_details,Bus_details) VALUES(%s,%s,%s,%s)")
         val=(Destination,Flight_details,Railway_details,Bus_details)
         cursor.execute(query,val)
         mycon.commit()
         print("record is been saved in record")
         print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
         Transportation_Data()
    except:
        print("Something went wrong Data not entered")
    


        





        
        
