from turtle import *
import colorsys

speed(2000)
bgcolor("black")
h = 0

penup()
goto(-15, -80)
pendown()
color("green")

begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

penup()
goto(0, 0)
pendown()
for i in range(16):
    for j in range(18):
        color("yellow")  
        h += 0.005
        rt(90)  
        circle(150 - j * 6, 90)
        lt(90)
        circle(150 - j * 6, 90)
        rt(180)
    circle(40, 24)

penup()
goto(-15, -5)
pendown()
color("grey")
begin_fill()
circle(40)  
end_fill()

header_text = "ELLA SABÍA QUE ALGÚN DÍA PASARÍA 🌻"
color("white")  
penup()
goto(-180, 250)  
pendown()
write(header_text, align="left", font=("Arial", 15, "normal"))

done()
