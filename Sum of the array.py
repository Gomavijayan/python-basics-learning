def calSumUtil( a , b , n , m ):
    sum = [0] * n
    i = n - 1
    j = m - 1
    k = n - 1
    carry = 0
    s = 0
    while j >= 0:
        s = a[i] + b[j] + carry
        sum[k] = (s % 10)
        carry = s // 10
         
        k-=1
        i-=1
        j-=1
    while i >= 0:
        s = a[i] + carry
        sum[k] = (s % 10)
        carry = s // 10
         
        i-=1
        k-=1
     
    ans = 0
    if carry:
        ans = 10
    for i in range(n):
        ans += sum[i]
        ans *= 10
     
    return ans 
def calSum(a, b, n, m ):
     if n >= m:
        return calSumUtil(a, b, n, m)
    else:
        return calSumUtil(b, a, m, n)
a = [ 9, 3, 9 ]
b = [ 6, 1 ]
n = len(a)
m = len(b)
print(calSum(a, b, n, m))
