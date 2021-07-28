from turtle import *
shape("turtle")
pencolor("red")
begin_fill()
fillcolor("YELLOW")
for i in range (3):
    forward(100)
    lt(360/3)
end_fill()
begin_fill()
fillcolor("GREEN")
for j in range(4):
    forward(100)
    rt(90)
end_fill()
done()
