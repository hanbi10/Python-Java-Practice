while True:
    n = int(input())
    
    if n==0: 
        break
    arr = []
    
    for _ in range(n):
        
        ss = input()
        arr.append([ss.upper(),ss])
        
<<<<<<< HEAD
    print(sorted(arr,key = lambda x : (x[0]))[0][1])
    
=======
    print(sorted(arr,key = lambda x : (x[0]))[0][1])
>>>>>>> 3f613666d291a69a8c4b094a45bf01a6e91cab37
