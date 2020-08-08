from turtle import *
speed(10)
hideturtle()
color('purple', 'green')
begin_fill()
while True:
    forward(400)
    left(155)
    if abs(pos()) < 1:
        break
end_fill()
done()