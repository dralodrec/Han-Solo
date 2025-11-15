from datetime import date
import os

# Function will accept a value and format it to dd-Mon-yy.
def FDate_ddMonyy(DateValue):
    DateValueStr = DateValue.strftime("%d-%b-%y")
    return DateValueStr

# Function will accept a value and format it to Mon dd,yyyy.
def FDate_Monddyyyy(DateValue):
    DateValueStr = DateValue.strftime("%b %d,%Y")
    return DateValueStr

# Function will add/less a value to Mon dd yyyy.
def modDate(currDate):
    currDate = date.today()
    currYear = currDate.year
    currMonth = currDate.month

    if (currDate.day >= 25):
        currMonth += 2
    else:
        currMonth += 1
    
    if (currMonth > 12):
        currMonth -= 12
        currYear += 1

    newDate = date(currYear, currMonth, 1)
    return newDate

# Function will accept a value and format it to $#,###.##.
def FDollar2(DollarValue):
    DollarValueStr = "${:,.2f}".format(DollarValue)
    return DollarValueStr

# Function will accept a value and format it to #,###.##.
def FComma2(Value):
    ValueStr = "{:,.2f}".format(Value)
    return ValueStr

# Function will format receipt to uniqueID.
def Freceipt(value1, value2, value3, value4):
    # get the initials from value1
    value1 = value1[0].upper()
    
    # get the initials from value2
    value2 = value2[0].upper()

    # get the 3 middle characters of value3
    value3 = value3[2:5].upper()

    # get the last 4 characters of value4 
    value4 = value4[-4:]

    newValue = value1 + value2 + "-" + value3 + "-" + value4
    return newValue

# Function will format client name first initial and last names will all be capitalized.
def Fname(value1, value2):
    value1 = value1[0].upper()
    newValue = value1 + ". " + value2.title()
    return newValue

# Function will format phone number display (XXX) XXX-XXXX
def Fphone(value):
    countryCode = value[0:3]
    areaCode = value[3:6]
    localNum = value[-4:]
    value = "(" + countryCode  + ") " + areaCode + "-" + localNum
    return value

# Function will validate licence plate entry
def F_licPlate(prompt):
    while True:
        user_input = input(prompt)
        charac_3_alpha = user_input[0:3]
        charac_3_digit = user_input[3:6]
        if user_input == 0 or user_input == "":
            print("Incorrect Entry")
        elif len(str(user_input)) < 6 or len(str(user_input)) > 6:
            print("Please enter correct format")
        elif  charac_3_alpha.isalpha() == False or charac_3_digit.isdigit() == False:
            print("Please enter correct format")
        else:
            return user_input

# Function will validate entry to exit
def F_exit(prompt):
    while True:
        user_input = input(prompt)
        if user_input == "END" :
            print("\nGood Bye!\n\n")
            os._exit(0)
        elif user_input == 0 or user_input == " " or user_input == "":
            print("Incorrect Entry")
        elif user_input.isdigit() == True:
            print("Entry cannot be a number")
        else:
            return user_input

# Function will validate entry 
def F_validate(prompt):
    while True:
        user_input = input(prompt)
        if user_input == 0 or user_input == " " or user_input == "":
            print("Incorrect Entry")
        elif user_input.isdigit() == True:
            print("Entry cannot be a number")
        else:
            return user_input

# Function will validate conditional entry with exit 
def F_phone_val(prompt, characterLenght):
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
        except:
            print(f"Entry must be greater than zero or an integer")
        else:
            if (user_input == 0 or user_input == ""):
                print(f"Incorrect Entry")
            elif (len(str(user_input)) <= characterLenght or len(str(user_input)) > characterLenght ):
                print(f"Please enter correct format")
            else:
                return user_input

# Function will validate conditional entry with exit 
def F_exitCondi_2(prompt, lowValue, highValue):
    while True:
        user_input = input(prompt)
        try:
            user_input = int(user_input)
        except:
            print(f"Entry must be greater than {lowValue} or an integer")
        else:
            if (user_input <= lowValue or user_input > highValue):
                print(f"Entry must be greater than {lowValue} or less than {highValue}")
            else:
                return user_input


# Function will calculate the payment schedule
def Fcalcu(Years, Finance_Fee_Rate, totalSalesPrice):
    for i in range(1, Years + 1):
        finance_fee = i * Finance_Fee_Rate
        totalPrice = finance_fee + totalSalesPrice
        months = i * 12
        monthlyPayments = totalPrice / months
        print(f"{'':8s}{i}{'':11s}{months}{'':11s}{FDollar2(finance_fee):<8}{'':6s}{FDollar2(totalPrice):<11}{'':6s}{FDollar2(monthlyPayments):>10}")