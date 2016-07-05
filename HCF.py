def hcf():
    a=int(raw_input("Enter the number: "))
    b=int(raw_input("Enter the number: "))
    if a<b:
        smaller=a
    else:
        smaller=b

    for i in range(1,smaller+1):
        if a%i==0 and b%i==0:
            HCF=i
            
    print HCF

hcf()
