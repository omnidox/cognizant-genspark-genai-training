import turtle

def draw_fractal_branch(t, length, depth):
    """Recursively draws a fractal tree using the turtle module."""
    if depth == 0:
        return
    
    t.forward(length)
    t.left(30)
    draw_fractal_branch(t, length * 0.7, depth - 1)
    t.right(60)
    draw_fractal_branch(t, length * 0.7, depth - 1)
    t.left(30)
    t.backward(length)

def draw_fractal():
    """Sets up the turtle and draws a fractal tree."""
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    
    draw_fractal_branch(t, 100, 5)
    turtle.done()

if __name__ == "__main__":
    draw_fractal()
