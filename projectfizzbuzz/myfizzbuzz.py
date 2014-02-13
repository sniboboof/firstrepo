def fizzbuzz(n):
    if n % (3*5) == 0:
        return "fizzbuzz"
    elif n % 3 == 0:
        return "fizz"
    elif n % 5 == 0:
        return "buzz"
    else:
        return str(n)

#def fizzbuzzetc(n, ):


if __name__=="__main__":
    print "1:"+fizzbuzz(1)
    print "3:"+fizzbuzz(3)
    print "5:"+fizzbuzz(5)
    print "15:"+fizzbuzz(15)
    print "42:"+fizzbuzz(42)
    print "45:"+fizzbuzz(45)
