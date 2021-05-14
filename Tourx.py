from Support_files import Tourist
from Support_files import Destination
from Support_files import Transportation

print("------------TOURX---------------")
print("\t\t..............................")
print("........Ultimate solution for travel managment......")
while True:
     print("1.Tourist_Data")
     print("2.Destination_Data")
     print("3.Transportation_Data")
     print("4.About Tourx")
     print("5.Exit")

     w=int(input("enter your choice"))
     if w==1:
          Tourist.Tourist_Data()
     elif(w==2):
         Destination.Destination_Data()
     elif(w==3):
         Transportation.Transportation_Data()

     elif(w==4):
         file1=open('About Tourex.txt','r')
         row=file1.readlines()
         for i in row:
             print(i)
     elif(w==5):
          print("Exiting Tourex.......Have a Good Day")
          x=int(input("Press Enter Key"))
          if(x==0):
               break
          else:
               break
    
     else:
         print("Invalid input")
         print("press any key to continue")
