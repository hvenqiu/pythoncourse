xmin = -10
xmax = 10

ymin = -10
ymax = 10

rangx = xmax - xmin
rangy = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600)
    xscl = width/rangx
    yscl = -height/rangy    

def grid(xscl, yscl):
    strokeWeight(1)
    stroke(0, 255,255)
    for i in range(xmin, xmax+1):
        line(int(i*xscl), int(ymin*yscl), int(i*xscl), int(ymax*yscl))
    for i in range(ymin, ymax+1):
        line(xmin*xscl, i*yscl, xmax*xscl, i*yscl)
    stroke(0)
    line(0, ymin*yscl, 0, ymax*yscl)
    line(xmin*xscl, 0, xmax*xscl, 0)

def f(x):
    #return x**2
    return 6*x**3 + 31*x**2 + 3*x -10

def graphfunction():
    x = xmin
    while x < max:
        # fill(0)
        stroke(255,0,0)
        line(x*xscl, f(x)*yscl, (x+0.1)*xscl, f(x+0.1)*yscl)
        x = x + 0.1


def draw():
    global xscl, yscl  
    background(255)
    translate(width/2, height/2)
    griddrawed = False
    if griddrawed == False:
        grid(xscl, yscl)
        griddrawed = True
    fill(0)
    #   ellipse(3*xscl, 6*yscl, 5, 5)
    graphfunction()
    