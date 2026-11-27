# import turtle
#
#
# def fizz_buzz(n):
#     for i in range(1, n + 1):
#         if i % 15 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
#
#
# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n //= 10
#     return total
#
#
# def alternate_case(s):
#     result = ""
#     for i, ch in enumerate(s):
#         if i % 2 == 0:
#             result += ch.upper()
#         else:
#             result += ch.lower()
#     return result
#
#
# def draw_polygon(t, sides, length):
#     for _ in range(sides):
#         t.forward(length)
#         t.left(360 / sides)
#
#
# fizz_buzz(16)
# print(digit_sum(1234))
# print(digit_sum(0))
# print(alternate_case("hello world"))
#
# screen = turtle.Screen()
# t = turtle.Turtle()
# t.pensize(3)
# t.penup()
# t.goto(0, 0)
# t.setheading(0)
#
# shapes = [
#     ("red", 3, -150, -30),
#     ("yellow", 4, -30, -30),
#     ("blue", 5, 90, -30),
# ]
#
# for color, sides, x, y in shapes:
#     t.penup()
#     t.goto(x, y)
#     t.setheading(0)
#     t.pencolor(color)
#     t.pendown()
#     draw_polygon(t, sides, 60)
#
# t.hideturtle()
# screen.mainloop()
# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
#
#
# def filled_square(t, size, color):
#     t.fillcolor(color)
#     t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     t.end_fill()
#
#
# colors = ["red", "blue", "red", "blue", "red"]
# x = -165
# y = -25
#
# for color in colors:
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     filled_square(t, 50, color)
#     x = x + 70
#
# wn.mainloop()
# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(2)
#
#
# def draw_square(t, size):
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#
#
# for i in range(12):
#     draw_square(t, 80)
#     t.left(30)
#
# wn.mainloop()
# import turtle
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
#
#
# def draw_square(t, size, is_filled):
#     if is_filled:
#         t.fillcolor("black")
#         t.begin_fill()
#     for i in range(4):
#         t.forward(size)
#         t.left(90)
#     if is_filled:
#         t.end_fill()
#
#
# for row in range(6):
#     for col in range(6):
#         t.penup()
#         t.goto(-120 + col * 40, -120 + row * 40)
#         t.pendown()
#         if (row + col) % 2 == 0:
#             draw_square(t, 40, True)
#         else:
#             draw_square(t, 40, False)
#
# wn.mainloop()