import turtle
import random
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing ball - Maulana ID")
wn.tracer(0)


def font():
    turtle.color("white")
    turtle.speed(0)
    turtle.penup()
    turtle.setpos(-120, 0)
    turtle.write("      Maulana ID\nGithub : Maulana-Coder", font=("Consolas", 15, "bold",))
    turtle.penup()
    turtle.hideturtle()
font()

balls = []

# jika ingin menambah jumlah atau mengurangi bentuknya ganti angka 20 sesuai yang kalian mau
for _ in range(20):
    balls.append(turtle.Turtle())

colors = ["red", "orange", "yellow", "lime", "blue", "purple", "white"]
shapes = ["circle", "triangle", "square"]

for ball in balls:    
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-240, 240)
    y = random.randint(200, 300)
    ball.goto(x, y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.dz = random.randint(-5, 5)

gravity = 0.1

while True:
    time.sleep(0.005)
    wn.update()

    for ball in balls:
        
        ball.rt(ball.dz)
        ball.dy -= gravity
        ball.sety(ball.ycor() + ball.dy)
        ball.setx(ball.xcor() + ball.dx)

        # Collision
        if ball.xcor() >= 250:
            ball.dx *= -1
            ball.dz *= -1

        if ball.xcor() <= -250:
            ball.dx *= -1
            ball.dz *= -1
            
        # Bounce
        if ball.ycor() <= -250:
            ball.sety(-250)
            ball.dy *= -1
            ball.dz *= -1
