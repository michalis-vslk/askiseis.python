def Luhn(card_number):
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1

    for i in range(0, num_digits):
        digit = int(card_number[i])

        if not (( i & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit
        
    if( (sum % 10) == 0 ):
        print ("Your Credit Card Number is Valid")
    else:
        print("Your Credit Card Number is Invalid")

def Entry(card_number):
    x=str(card_number)
    if (len(x)==16):
        try:
            Luhn(card_number)
        except:
            card_number=input("Your number does not contain 16-digits.Please try again by entering a new number: ")
            Entry(card_number)
    else:
        card_number=input("Your number does not contain 16-digits.Please try again by entering a new number: ")
        Entry(card_number)

card_number=input("Enter your 16-digit credit card number: ")
Entry(card_number)
