   def print(n):
    var1 = 1
    var2 = 1
    for i in range(n):
        for j in range(n - 1,i,-1):
            print(" ", end = "")
         for k in range(1, var1 + 1):
            print(abs(k - var2), end="") 
        var1 += 2
        var2 += 1
        print()
n = 5
printt(n)
