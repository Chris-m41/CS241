"""
This file contains the following classes:
    CreditCard
    Address

and then it contains a main function.

Your task it to break it into three files, then tar them up, and submit.
"""

from creditCard import CreditCard

def main():
    cc = CreditCard()

    cc.name = input("Name: ")
    cc.number = input("Number: ")
    
    print("Mailing Address:")
    cc.mailing_address.street = input("Street: ")
    cc.mailing_address.city = input("City: ")
    cc.mailing_address.state = input("State: ")
    cc.mailing_address.zip = input("Zip: ")
    
    print("Billing Address:")
    cc.billing_address.street = input("Street: ")
    cc.billing_address.city = input("City: ")
    cc.billing_address.state = input("State: ")
    cc.billing_address.zip = input("Zip: ")
    print("\n")

    cc.display()

if __name__ == "__main__":
    main()
