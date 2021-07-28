def checkOddEven(n):
    if n%2==0:
        a="짝수"
        return a
    else:
        a="홀수"
        return a

n=int(input("숫자 n 입력 : "))
print(checkOddEven(n))
