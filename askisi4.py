def ASCIICode(word):
    listbinary = [bin(ord(x))[2:].zfill(8) for x in word]
    binarynum=''.join(listbinary)
    num=int(binarynum,2)
    typenum=str(num)
    print("The ASCII value of " + word + " is: " + typenum)
    if num > 1:   
        for i in range(2, num//2):  
            if (num % i) == 0:
               print(num, "is not a prime number")
               break
            else: 
                print(num, "is a prime number")
                break
    else: 
        print(num, "is not a prime number")

ASCIICode("python")
