# building a simple calculator
# copyright of this code has Abdirizak abdullahi hussein 
print ('KADOORO XISAABTA AAD RABTO:')
print ("1.KUDAR")
print ("2.KA JAR ")
print ("3.ku dhufasho")
print ("4.QEYB ")
print ("5. KM TO M")
print("6. M TO KM")
#options and then backend 
operation = input ()
if operation == "1":
   num1 = input ("soo gali numberka koowaad:")
   num2 = input("soo gali numberka labaad:")
   print ("jawaabtu waa: " + str (int(num1)+ int(num2)))

elif operation == "2":
    num1 = input("soo gali numberka koowaad:")
    num2 = input("soo gali numberka labaad: ")
    print("jawaabtu waa: " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("soo gali numberka koowaad:")
    num2 = input("soo gali numberka labaad: ")
    print ("jawaabtu waa: " + str (int(num1) * int(num2)))
elif operation == "4":
    num1 = input("soo gali numberka koowaad:")
    num2 = input("soo gali numberka labaad:")
    print ("jawaabtu waa: " + str (int(num1)/ int(num2)))
elif operation == "5":
    num1 = int(input("SOO GALI TIRADA LAGUU BADALAYO:"))
    print ("jawaabtu waa:" , int(num1) * 1000 , "M")
elif operation == "6":
    num1 = int(input("SOO GALI TIRADA LAGUU BADALAYO:"))
    print ("jawaabtu waa:" , int(num1) / 1000 , "KM")
if operation == "0":
    print("CREATED ME: Eng.ABDIRIZAK ABDULLAHI HUSSEIN")
else:
    print ("waxaad galisay waa qalad ")

