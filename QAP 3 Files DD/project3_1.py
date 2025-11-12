# Honest Harry owns a used car lot and would like a program to keep track of his sales. Follow good programming practise using Comments, Constants, and Spacing. Add at least 3 functions to the program. I will accept the FormatValues.py library as a function option – but you need to add a new function(s) to the library – make it relevant.
# The program will repeat until the user enters the word “END” for the Customer First Name. Input for the program will be the customer first name (must be entered – adjust to title case), the customer last name (must be entered – adjust to title case), the phone number (must be entered - must be 10 digits), the plate number (must be entered – must be 6 characters - convert to all caps – BONUS: entered in the format XXX999), the car make (ie: Toyota), the car model (ie: Corolla), the year (ie: 2018), the selling price (does not exceed $50,000.00), the amount of the trade in (does not exceed the selling price), and the salespersons name (must be entered). NOTE: Validation is only required as specified.
# The invoice date is the current system date. The customer’s name is the first initial and the last name, the phone number should be formatted as shown, the Car Details are the Year, Make and Model – ie: 2014 Toyota Corolla. The program should create a Receipt ID for the sale in the form XX-XXX-XXXX where the first two characters are the customer initials, the middle 3 characters are the last 3 digits in the license plate number, and the final 4 characters are the last 4 digits of the phone number.
# The program should calculate the price after trade, the licence fee, the transfer fee, the HST, Subtotal, and the total sales price. The price after trade is the selling price less the trade in amount. The licence fee is standard rate in NL of $75.00 on cars with a selling price up to and including $15,000.00 and $165.00 on cars with a selling price over $15,000.00. The transfer fee 1% of the selling price - if the selling price is more than $20,000.00, an additional 1.6% luxury tax is calculated on the selling price and added to the transfer fee. The Subtotal is the Price after trade plus the License Fee plus the Transfer Fee. Taxes (HST) are calculated at 15% on the Subtotal. The total sales price is the subtotal plus the HST.
# Prepare the loop at the end for the payment schedule. It is based on the Total Sales Price. The payment schedule uses a loop based on the number of years the customer will use to pay off the car. For each of 4 years, calculate the number of monthly payments (Years * 12), the financing fee at 39.99 per year, the total price as the total sales price plus the financing fee, and the monthly payment (The Total Price divided by the number of months). The first payment date is the 1st day of the next month – if the day is the 25th or later, add an extra month to the payment date.

# Description: A program that prints sales receipt for Honest Harry used car lot sales.
# Author: Darrell Declaro
# Date: 11/11/2025


# Define required libraries.
import os
import functionLibrary as funclib
os.system("cls") 


# Define program constants.
clientName = "Ricky Bowen"                      
clientAddrss = "1078 Bauline Line Extension"    
clientCity = "Bauline"                          
clientProv = "nl"                               
clientPostal = "a1k 0k7"                       
clientHomePhone = "(709) 784-4866"
car_yr = "XXXX"
car_brand = "XXXXXXXXXXXXX"
car_model = "XXXXXXXXXX"
car_details = car_yr + " " + car_brand + " " + car_model
sold_to = clientName[0].upper() + " " + clientAddrss
yr = 4
date = 'MON dd, yyyy'
receipt_no = 'XX-XX-XXXX'
ten_thou = '$99,999.99'
one_thou = '$9,999.99'
hundrs = '$999.99'


# Define program functions.



# Main program starts here.
    

    
# Gather user inputs.



# Perform required calculations.



# Display results
print()
print(f"Honest Harry Car Sales {'Invoice Date: ':>39s}{date:>17}")
print(f"Used Car Sales and Receipt {'Receipt No: ':>33s}{receipt_no:>19}")
print()
print(f"{'':42s}{'Sales price:':<18}{ten_thou:>19}")
print(f"Sold to:{'':34s}{'Trade Allowance:':<18}{ten_thou:>19}")
print(f"{'_'*37:>79}")
print(f"{'':5s}{sold_to:<37}{'Price after Trade:':<18}{ten_thou:>19}")
print(f"{'':5s}{clientHomePhone:<37}{'License Fee:':<18}{ten_thou:>19}")
print(f"{'':42s}{'Transfer Fee:':<18}{ten_thou:>19}")
print(f"{'_'*37:>79}")
print(f"Car Details:{'':30s}{'Subtotal:':<18}{ten_thou:>19}")
print(f"{'':42s}{'HST: ':<18}{ten_thou:>19}")
print(f"{'':<5s}{car_details:<30}{'_'*37:>44}\n")
print(f"{'':42s}{'Total sales price:':<18}{ten_thou:>19}")
print(f"{'_'*79}")
print()
print(f"{'':32s}{'Financing':<9}{'':8s}{'Total'}{'':13s}{'Monthly'}")
print(f"{'':5s}{'# Years'}{'':5s}{'# Payments'}{'':8s}{'Fee'}{'':11s}{'Price'}{'':13s}{'Payment'}")
print(f"{'_'*69:^80}")

for i in range(1,yr+1):
    print(f"{'':8s}{i}{'':12s}{i*12}{'':10s}{hundrs:<8}{'':6s}{ten_thou:<11}{'':6s}{one_thou:>10}")

print(f"{'_'*69:^80}")
print(f"{'':5s}First payment date: dd-MON-yyyy")
print(f"{'_'*79:^80}")
print(f"{'Best used cars at the best prices!':^80}\n")

# RULER REFERENCE ONLY (to be disregarded)
print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
print("         1         2         3         4         5         6         7         8")



# Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.