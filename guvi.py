num = open('sample.txt').read()
number = int(num)

def integer_to_english(number):
    if number>=1 and number<=1000:
        a = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen','twenty ','thirty ','fourty ','fifty ','sixty ','seventy ','eighty ','ninty ']
        if number<=20:
            if number%10==0: return a[number]
            else: return a[number]
        elif number<100:
            b=number-20
            r=b%10
            b//=10
            return a[20+b]+a[r]
        elif number<1000:
            if number%100==0:
                b=number//100
                return a[b]+' hundred'
            else:
                r=number%100
                b=number//100
                if r<=20:
                    return a[b]+' hundred'+' and '+a[r]
                else:
                    r=r-20
                    d=r//10
                    r%=10
                    return a[b]+' hundred'+' and '+a[20+d]+a[r]
        elif number==1000:
            return 'one thousand'
        else:
            return -1
my_list = str(integer_to_english(number))

f = open("sample.txt", "a")
i = 1
while i < 2:
    f.write(str(my_list))
    i = i + 1
f.close()

#open and read the file after the appending:
f = open("sample.txt", "r")
print(f.read())