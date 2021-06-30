def SUM(num): #함수 정의
    hap=0 #변수 선언
    for i in range(1,num+1): #1부터 num까지 for문
        if num%i==0: #i로 나누었을 때 나누어떨어지는 경우
            hap+=i #i를 hap에 더해라
    return hap #hap을 반환

a=int(input("양의 정수를 입력하세요: ")) #양의 정수 입력받기
for x in range(2,a+1):
    for y in range(2,x):
        if x%y==0:
            print(x,SUM(x))
