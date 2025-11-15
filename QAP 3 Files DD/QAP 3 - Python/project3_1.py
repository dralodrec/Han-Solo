# Description: A program that prints sales receipt for Honest Harry used car lot sales.
# Author: Darrell Declaro
# Date: 11/11/2025


# Define required libraries.
import os
import datetime
import functionLibrary as funclib
os.system("cls") 


# Define program constants.
LICENCCE_FEE_STD_RATE = 75
LICENCCE_FEE_LUX_RATE = 165
TRANSFER_FEE_STD_RATE = .01
TRANSFER_FEE_LUX_RATE = .016
HST_RATE = 0.15
FINANCE_FEE_RATE = 39.99


# Main program starts here.
    
# Gather user inputs.
choice = "y"
while choice.lower() == "y":

    clientFirstName = "john"
    clientLastName  = "smith"                                        
    clientHomePhone = "7097844866"
    car_lic_plate = "jmh372"
    car_yr = "2022"
    car_brand = "toyota"
    car_model = "tundra"
    inputClsalesPrice = 50000
    inputCltradeAllw = 4500

   
    # clientFirstName =  funclib.F_exit("Enter Customer First Name (END to quit): ")
    # clientLastName =  funclib.F_exit("Enter Customer Last Name (END to quit): ")
    # clientHomePhone = funclib.F_phone_val("Enter Phone Number (9999999999): ", 10)
    # car_lic_plate = funclib.F_licPlate("Enter Vehicle Licence Plate (XXX999): ", 6)
    # car_brand = input("Enter Vehicle Brand (ie: Toyota): ")
    # car_model = input("Enter Vehicle Model (ie: Corolla): ")
    # car_yr = input("Enter Vehicle Year (ie: 2018): ")
    # inputClsalesPrice = funclib.F_exitCondi_2("Enter Vehicle Selling Price: ", 0, 50000)
    # inputCltradeAllw = funclib.F_exitCondi_2("Enter Vehicle Trade Allowance: ", 0, inputClsalesPrice)
    # salesPerName =  funclib.F_validate("Enter Salespersons Name: ")
    

    salesPrice = funclib.FDollar2(inputClsalesPrice)
    tradeAllowance = funclib.FDollar2(inputCltradeAllw)
    inputDate = datetime.datetime.now()
    inputDate2 = funclib.modDate(inputDate)
    fpaymentDate = funclib.FDate_ddMonyy(inputDate2)
    invoiceDate = funclib.FDate_Monddyyyy(inputDate)
    receipt_no = funclib.Freceipt(clientFirstName,clientLastName,car_lic_plate,clientHomePhone)
    sold_to = funclib.Fname(clientFirstName,clientLastName)
    clientHomePhone = funclib.Fphone(clientHomePhone)

    car_details = car_yr + " " + car_brand + " " + car_model
    car_details = car_details.title()

    
    # Perform required calculations.
    priceAfterTrade = inputClsalesPrice - inputCltradeAllw

    if (inputClsalesPrice <= 15000):
        licenseFee = LICENCCE_FEE_STD_RATE
    else: 
        licenseFee = LICENCCE_FEE_LUX_RATE

    if (inputClsalesPrice > 20000):
        transferFee = (TRANSFER_FEE_LUX_RATE * inputClsalesPrice) + (TRANSFER_FEE_STD_RATE * inputClsalesPrice)
    else:
        transferFee = TRANSFER_FEE_STD_RATE * inputClsalesPrice

    subtotal = priceAfterTrade + licenseFee + transferFee
    hst = subtotal * HST_RATE
    totalSalesPrice = subtotal + hst


    # Display results
    os.system('cls')
    print()
    print(f"Honest Harry Car Sales {'Invoice Date: ':>39s}{invoiceDate:>17}")
    print(f"Used Car Sales and Receipt {'Receipt No: ':>33s}{receipt_no:>19}")
    print()
    print(f"{'':42s}{'Sales price:':<18}{salesPrice:>19}")
    print(f"Sold to:{'':34s}{'Trade Allowance:':<18}{tradeAllowance:>19}")
    print(f"{'_'*37:>79}")
    print(f"{'':5s}{sold_to:<37}{'Price after Trade:':<18}{funclib.FDollar2(priceAfterTrade):>19}")
    print(f"{'':5s}{clientHomePhone:<37}{'License Fee:':<18}{funclib.FDollar2(licenseFee):>19}")
    print(f"{'':42s}{'Transfer Fee:':<18}{funclib.FDollar2(transferFee):>19}")
    print(f"{'_'*37:>79}")
    print(f"Car Details:{'':30s}{'Subtotal:':<18}{funclib.FDollar2(subtotal):>19}")
    print(f"{'':42s}{'HST: ':<18}{funclib.FDollar2(hst):>19}")
    print(f"{'':<5s}{car_details:<30}{'_'*37:>44}\n")
    print(f"{'':42s}{'Total sales price:':<18}{funclib.FDollar2(totalSalesPrice):>19}")
    print(f"{'_'*79}")
    print()
    print(f"{'':32s}{'Financing':<9}{'':8s}{'Total'}{'':13s}{'Monthly'}")
    print(f"{'':5s}{'# Years'}{'':5s}{'# Payments'}{'':8s}{'Fee'}{'':11s}{'Price'}{'':13s}{'Payment'}")
    print(f"{'_'*69:^80}")

    funclib.Fcalcu(4,FINANCE_FEE_RATE,totalSalesPrice)

    print(f"{'_'*69:^80}")
    print(f"{'':5s}First payment date: {fpaymentDate}")
    print(f"{'_'*79:^80}")
    print(f"{'Best used cars at the best prices!':^80}\n")
    print("\n\n")
    # see if the user wants to continue
    choice = input("Would you like to try again (y/n): ")
    os.system('cls')
    print()

print("bye!")
# RULER REFERENCE ONLY 
# print("12345678901234567890123456789012345678901234567890123456789012345678901234567890")
# print("         1         2         3         4         5         6         7         8")



# Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.