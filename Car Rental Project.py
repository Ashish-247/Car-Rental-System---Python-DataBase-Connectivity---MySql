#Car Rental Project

import mysql.connector as sql

mydb = sql.connect(
    host = "localhost",
    username = "root",
    password = "root"
)

cur = mydb.cursor()
cur.execute("Create Database if not exists Carrentalsystem")
cur.execute("USE Carrentalsystem")

table = "Create Table if not exists rentCar(Customer_Name varchar(50),id INT primary key, phone_Number INT, " \
        "Cars_Rented INT, Days INT, Bill_Amount INT)"

cur.execute(table)
carSumQuerry = "select SUM(Cars_Rented) from rentCar"
carSum = cur.execute(carSumQuerry)
carSum = cur.fetchall()
#print("carSum",carSum, type(carSum))
totalNoOfCars = 20 - carSum[0][0]
while(True):
    print()
    print("Welocme To Travel Guide")
    print("Total Number Of Cars Available = ", totalNoOfCars)

    print("""Press
        1 To Rent Cars
        2 To Deposit Cars
        3 To View Data
        4 To Exit
        """)
    print()
    option = int(input())

    if option == 1:
        print("""Condition:
            1. One Car for One Day : 500/-
            2. Adhaar Card and Driving Licence is Mandatory
            """)
        agree = (input("Press Y if agreed OR N is not Agreed : "))
        while(True):
            if agree == "Y" or agree == "y":
                carsRented = int(input("Enter number of cars to be rented : "))
                if carsRented > totalNoOfCars:
                    print("Sorry !! Only", totalNoOfCars, " are Cars remaining !!")
                else:
                    days = int(input("For how many days cars are required : "))
                    name = (input("Enter your name : "))
                    phoneNo = int(input("Enter your Phone Number : "))
                    id = int(input("Enter your Id Number : "))
                    print("Your Total Bill Amount is ", carsRented*days*500)
                    accept = input("Enter Y to Accept Deal OR N to Reject : ")
                    if accept == "Y" or accept == "y":
                        print("Congratulations !! Your Booking is Confirmed.")
                        totalNoOfCars =  totalNoOfCars - carsRented
                        print("Total Number Of Cars Available = ", totalNoOfCars)

                        insert = "INSERT INTO rentCar VALUES (%s, %s, %s, %s, %s, %s)"
                        cur.execute(insert,(name,id,phoneNo,carsRented,days,carsRented*days*500))
                        mydb.commit()
                    else:
                        print("OK Thanks !! No Booking is Done.")
                        print("Total Number Of Cars Available = ", totalNoOfCars)
                    break
            else:
                print("OK Thanks !! No Booking is Done.")
                break


    elif option == 2:
        enterYourId = int(input("Enter your ID No. : "))
        enterYourIdList = [None]
        enterYourIdList[0] = enterYourId
        #print(enterYourIdList)
        compareIdQuerry = "select id from rentCar where id = (%s)"
        CompareId = cur.execute(compareIdQuerry,enterYourIdList)
        CompareId = cur.fetchone()
        #print("compareID",CompareId, type(CompareId))

        if CompareId == None:
            print("Id Not Found")
        else:
            #print("Your Value is ",CompareId[0])
            carToDeposit = int(input("Enter No. of Cars to be deposited : "))
            carsHiredQuerry = "select Cars_Rented from rentCar where id = (%s)"
            carsHired = cur.execute(carsHiredQuerry, enterYourIdList)
            carsHired = cur.fetchone()
            #print("carsHired : ",carsHired)
            if carToDeposit > carsHired[0]:
                print("Sorry !! Input is Wrong")
            else:
                if carToDeposit == carsHired[0]:
                    deleteRecord = "Delete from rentCar where id = (%s)"
                    cur.execute(deleteRecord,enterYourIdList)
                    mydb.commit()
                    print("All Cars Deposited. Customer Record Deleted.")
                else:
                    carsRemaining = carsHired[0] - carToDeposit
                    #print("carsRemaining : ",carsRemaining, type(carsRemaining))
                    updateRecord = "UPDATE rentCar SET Cars_Rented = {} WHERE id = %s".format(carsRemaining)
                    cur.execute(updateRecord, enterYourIdList)
                    mydb.commit()
                    print("Customer Record Updated. {} Cars still remaining to be deposited.".format(carsRemaining))
                totalNoOfCars = totalNoOfCars + carToDeposit
                print("Total Number Of Cars = ", totalNoOfCars)


    elif option == 3:
        enterYourId = int(input("Enter your ID No. : "))
        enterYourIdList = [None]
        enterYourIdList[0] = enterYourId
        # print(enterYourIdList)
        viewQuerry = "select * from rentCar where id = (%s)"
        view = cur.execute(viewQuerry, enterYourIdList)
        view = cur.fetchone()

        if view == None:
            print("Id Not Found")
        else:
            print("Customer Name = ", view[0])
            print("ID = ", view[1])
            print("Phone Number = ", view[2])
            print("Cars Rented = ", view[3])
            print("Days = ", view[4])
            print("Bill Amount = ", view[5])


    elif option == 4:
        print("Thankyou for visiing us !!")
        break


    else:
        print("Wrong Input")
        print("Plase give correct input")





