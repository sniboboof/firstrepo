def fizzbuzz(n):
    if n % (3*5) == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)

def fizzbuzzetc(n, sounds=[(3, "fizz"), (5, "buzz")]):
    foundasound = False
    noise = ""
    for asound in sounds:
        if n%asound[0]==0:
            noise = noise+asound[1]
            foundasound=True
    
    if foundasound:
        return noise
    else:
        return str(n)


if __name__=="__main__":
    print "1:"+fizzbuzz(1)
    print "3:"+fizzbuzz(3)
    print "5:"+fizzbuzz(5)
    print "15:"+fizzbuzz(15)
    print "42:"+fizzbuzz(42)
    print "45:"+fizzbuzz(45)
    print "1600:"+fizzbuzzetc(1600, [(3, "fizz"), (5, "buzz"), (10, "dec"), (100, "cent"), (400, "quad")])
