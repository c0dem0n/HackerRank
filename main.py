def fibonacci():
    nterms = int(input("Enter input : "))
    n1 = 0 
    n2 = 1 
    count = 1 
    if nterms == 0:
        print("Please enter number above 0")
    elif nterms == 1:
        print("Fibonacchi sequesnce is %d", nterms)
    else:
        while count < nterms :
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth 
            count += 1
        
        
        
fibonacci()
            
            
    
    