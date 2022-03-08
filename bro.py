"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html

This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""
import sys 
import math
from tkinter import font
from tkinter.font import ITALIC
from tkinter.ttk import Style
import turtle 
import colorama
t = turtle.Turtle()
t.speed(1000)
t.getscreen().bgcolor('#C1FDD1')
want = input("What geometric shape do you want:")

if want == "square" or want == "s" :
 a = float(input("How long is the rib?:"))
 for n in range(1):
   t.color('black','#a0c8f0')
   t.begin_fill()
 for n in [1, 2, 3, 4]:
   t.forward(a*10)
   t.left(90)
   t.speed('fastest')
 for n in range(1):
   t.end_fill()
 print("Shape related data are:")
 sum1 = float(a*4) 
 sum2 = float(a**2)
 sum3 = float(a *math.sqrt(2))
 for n in range(1):
   t.left(45)
   t.color('red')
   t.forward(sum3*10)
   #print("circumference : {0} | square area : {1} |diagonal d = {2}".format(sum1,sum2,sum3))
 from tabulate import tabulate
 #create data
 #create data
 data = [["circumference", sum1], 
        ["square area", sum2], 
        ["diagonal d", sum3]]
  
  #define header names
 col_names = ["Team", "Points"]
  
  #display table
 print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
else:
 if want == "rectangle" or want == "r" :
   a = float(input("the length of the rectangle:"))
   b = float(input("the width of the rectangle:"))
   for n in [1,2]:
     t.forward(a*10)
     t.left(90)
     t.forward(b*10)
     t.left(90)
     t.speed('fastest')
   print("Shape related data are:")
   sum1 = float(a + b) * (2) 
   sum2 = float(a*b)
   sum3 = float(math.sqrt(a**2+b**2))
   for n in ['red']:
    t.left(45)
    t.color(n)
    t.forward(sum3*10)
   #for n in ['red']:
    #t.left(float(0.5(a/sum3)))
    #t.color(n)
    #t.forward(sum3*10)
   print("circumference : {0} | rectangle area : {1} |diagonal d = {2}".format(sum1,sum2,sum3))
 else:
  if  want == "triangle" or want == "t" :
     #def main():
     # pp = ["yes","yeah","yup"]
   a = float(input("the length of the base of the triangle:"))
   for n in [1]:
    t.color('black','#a0c8f0')
    t.begin_fill()  
    t.forward(a*10)
   c = float(input("first degree angle:"))
   for n in [1]:
    t.left(180 - c)
   b = float(input("The length of the side is adjacent to the base:")) 
   for n in [1]:
     t.forward(b*10)
   d = float(input("second degree angle:"))
   if d + c >= 180 :
     print(" \nenter some valid shit _bitch")
     raise SystemExit
   else:
     for n in [1]:
      t.left(180-d)  
   print("_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
     #again = str(input("Do you want to try it again: ")).lower()
     #if again in pp :
     #  main()    
     #main()
   ab = float((a**2)+(b**2))
   cc = float(math.sqrt(ab))
   aa = float((b**2)-(a/2)**2)
   ac = float(math.sqrt(aa))
   bb = float((ac**2)+((a/2)**2))
   ccc = float(math.sqrt(bb))
   #C = float(180 - (c + d))
   gg = (180-(c+d))
   R = (d * math.pi) / 180
   h = (math.sin(R))*(b) 
   q = math.sqrt((b**2) - (h**2))
   p = (cc - q)
   r =  (a + b  - cc) / 2
   r2 = (a) /2
   r3 = (math.sqrt(3)/6) *a
   r4 = math.tan(c/2 * math.pi / 180) * (a/2)
   cicr = 2 * math.pi * r
   arci = math.pi * (r**2)
   sum3 = float(a + b) * (2) 
   sum4 = float(a*b)
   ca = 180 - c
   rr = math.cos(ca*math.pi/180) * b
   h2 = math.sqrt(b**2 - rr**2)
   c4 = math.sqrt((a+rr)**2 + (h2**2))
   sat = float((rr*h2)/2)
   bat = float(((a+rr)*h2)/2)
   sum33 = float((a+rr) + h2) * 2
   sum44 = float((a+rr) + h2) 
   if c == 90 or d == 90 or c + d == 90 and a != cc:
     for n in [1]:
       t.forward(cc*10)
       t.end_fill()
       t.color('green')
       print("\nShape related data are:")
       style = ('Courier',10,'italic')
       t.write(""" ------right triangle-------   """,font=style,align='right' )
     print("""                                                          
                                                                    . *| 
                                                            c   . *    |                                                              
                                                            . *        | b
                                                          *____________|
                                                                a
     
     """)
     sum1 = float(a + b + cc)
     sum2 = float((a*b)/2)
     ##print("             ------right triangle-------\n| circumference : {0} | | triangle area : {1} | | The hypotenuse 'c' : {2}   ".format(sum1,sum2,cc))
     for n in ['red']:
      t.left(((c+d) - 180)-180)
      t.penup()
      t.forward(a*9)
      t.pendown()
      t.color(n)
      t.left(90) 
      t.forward(10) 
      t.right(90)
      t.forward((a*10)-(a*9))
      t.right(90)
      t.forward(10) 
      t.penup()
      t.left(180)
      t.fd(b*10)
      t.left(90)
      t.pendown()
     ##print("| third degree angle: {0} | ".format(gg))
     for n in range(5):
      t.color("blue")
      t.fd(a)
      t.penup()
      t.fd(a)
      t.pendown()
     for n in [1]:
      t.left(90)
     for n in range(5):
      t.color('blue')
      t.fd(b)
      t.penup()
      t.fd(b)
      t.pendown()
     ##print("| rectangle or square circumference : {0} | rectangle or square area : {1} | |diagonal d = {2} |".format(sum3,sum4,cc))
     for n in range (1):
      t.left(90+gg)
      t.fd(p*10)
      t.color('green')
      t.right(90)
     for n in range(5):
      t.fd(h)
      t.penup()
      t.fd(h)
      t.pendown()
     for n in range(1):     
      t.right(180)
     for n in range(1):
       t.penup()
       t.fd((h/1.2)*10)#/2
       t.right(90)
       t.penup()
       t.fd(5)
       t.pendown()
       t.left(90)
       t.fd(9)
       t.left(180)
       t.fd(14)
       t.penup()
       t.left(90)
       t.fd(5)
       t.pendown()
       t.left(90)
       t.fd(5)
       t.left(90)
       t.fd(5)
       t.penup()
       t.fd(5)
       t.right(90)
       t.fd((h-h/1.2)*10)
       t.pendown()
     ##print("| length height 'h': {0} |".format(h))
     for n in range(1):
        t.penup()
        t.left(90)
        t.fd((p/2)*10)
        t.right(90)
        t.fd(5)
        t.pendown()
        t.fd(10)
        t.right(90)
        t.circle(-2.5,180)
        t.left(90)
        t.penup()
        t.fd(10)
        t.left(90)
        t.fd(((p/2)*10)+(q/2)*10)
        t.left(90)
        t.fd(5)
        t.pendown()
        t.fd(5)
        t.left(90)
        t.circle(-2.5,180)
        t.right(90)
        t.fd(5)
        t.penup()
        t.fd(10)
        t.left(90)
        t.fd((q/2)*10)
        t.pendown()
     ##print("| p : {0} | q : {1} | ".format(p,q))
     for n in range(1):
       t.color('orange')
       t.right(180 - d)
       t.right(d/2)
     for n in range(15):
       t.fd(cc/3)
       t.penup()
       t.fd(cc/3)
       t.pendown()
     for n in range(1):
       t.penup()
       t.fd(-cc*10)
       t.right(d/2)
       t.fd(cc*10)
       t.left(180)
       t.left(-gg/2)
       t.pendown()
     for n in range(15): 
       t.fd(cc/3) 
       t.penup()
       t.fd(cc/3)
       t.pendown()
     for n in range(1):
      t.penup()
      t.fd(-cc*10)
      t.right(gg/2)
      t.fd((a-r)*10)
      t.pendown()
      t.color('#430606')
      t.circle(r*10)
      t.left(90)
      t.fd(r*10)
      t.right(90)
      t.fd(r*10)
     ##print("""| circumference of a circle : {0} |
     ##| area of a circle : {1} | | r : {2} |""".format(cicr,arci,r))
       #t.fd(b*10)
       #t.right(180-(180-(gg+90)))
       #t.fd(h*10)
     for n in range(1):
        t.left(90)
     
     
     from tabulate import tabulate
     data = [[ "circumference", sum1], 
            ["triangle area", sum2],
            ["The hypotenuse 'c'",cc],
            ["third degree angle", gg],
            ["rectangle or square circumference", sum3],
            ["rectangle or square area ", sum4],
            ["diagonal d", cc],
            ["length height 'h'", h], 
            ["length q", q], 
            ["length p", p],
            ["circumference of a circle", cicr], 
            ["area of a circle", arci], 
            ["r", r], 
            ["third degree angle", ac]]
  
       #define header names
     #col_names = ["Shape related data are:"]
     #col_names = ["right triangle"]
     col_names = ["data", "xx"]
  
     #display table
     print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   else:
    if b == ccc and d != c and c < 90  :
     for n in [1] :
      t.forward(b*10)
      t.end_fill()
     print("Shape related data are:")
     print("""                                                          
                                                                    . *| 
                                                           (c)  . *    |                                                              
                                                            . *        | (b) = a
                                                          *____________|
                                                                (a) = b
     
     """)
     sum1 = float(a + b + b) 
     sum2 = float((a/2)*b)
     for n in range(1):
      t.penup()
      t.left(180)
      t.fd((b/2)*10)
      t.left(180-30)
      t.pendown()
      t.color("red")
      t.fd(3)
      t.left(180)
      t.fd(6)
      t.left(180)
      t.fd(3)
      t.right(180-30)
     for n in range(1):
      t.penup()
      t.fd((b/2)*10)
      t.right(180-d)
      t.fd((b/2)*10)
      t.right(180-30)
      t.pendown()
      t.color("red")
      t.fd(3)
      t.left(180)
      t.fd(6)
      t.left(180)
      t.fd(3)
      t.left(180-30)
     #print("          ------isosceles triangle-------\n|circumference : {0} |  triangle area : {1} |".format(sum1,sum2))
     for n in ['green']:
      t.penup()
      t.left(180)
      t.fd((b/2)*10)
      t.left(180-d)
      t.left(d/2)
      #t.left(((c +d)-180)-180)
      t.forward((ac)*10)
      t.color(n)
      t.pendown()
      #t.right(90)
      #t.forward(ac*10)
     for n in range(1):
       t.left(180)
       #t.fd(ac*10)
       #t.left(180)
       t.color("green")
     for n in range(5):
      t.fd(ac/1.3)
      t.penup()
      t.fd(ac/1.3)
      t.pendown()
       #t.fd((ac/1.3)*10)#/2
     for n in range (1):
       t.right(90)
       t.penup()
       t.fd(5)
       t.pendown()
       t.left(90)
       t.fd(9)
       t.left(180)
       t.fd(14)
       t.penup()
       t.left(90)
       t.fd(5)
       t.pendown()
       t.left(90)
       t.fd(5)
       t.left(90)
       t.fd(5)
       t.penup()
       t.fd(5)        
       t.pendown()
       t.right(90)
       t.fd((ac-ac/1.3)*10)
     for n in range(1):
         t.penup()
         t.color("#430606")
         t.left(180-d/2) 
         t.fd((b)*10)
         t.left(180-gg)
         t.fd(((a/2)/2)*10)#t.fd((a/2)*10) nononoo
         t.pendown()
         t.left(30)
         t.fd(4.5)
         t.left(180)
         t.fd(9)
         t.left(180)
         t.fd(4.5)
         t.right(30)
         t.penup()
         t.fd((a/2)*10)#nonoononononoonnon
         t.pendown()
         t.left(30)
         t.fd(4.5)
         t.left(180)
         t.fd(9)
         t.left(180)
         t.fd(4.5)
         t.right(30)
         t.right(180)
         t.penup()
         t.fd(((a/2)/2)*10)#nononononoonononnononononononoonnno
         t.pendown()
         t.left(180)
         t.circle(r4*10)
         t.left(90)
     for n in range(5):
         t.penup()
         t.fd(r4/1.3)
         t.pendown()
         t.fd(r4/1.3)
     for n in range(1):
         t.penup()
         t.left(90)
         t.fd(5)
         t.pendown()
         t.fd(5)
         t.left(90)
         t.fd(5)
         t.penup()
         t.left(180)
         t.fd(5)
         t.right(90)
         t.fd(10)
         t.left(90)
         t.pendown()
     for n in range(5):
         t.penup()
         t.fd(r4-(r4/1.3))
         t.pendown()
         t.fd(r4-(r4/1.3))
     for n in range(1):
         t.left(180-120)
     for n in range(5):
         t.penup()
         t.fd(r4)
         t.pendown()
         t.fd(r4)
     from tabulate import tabulate
     data = [[ "circumference", sum1], 
            ["triangle area", sum2]]
     col_names = ["data", "xx"]
  
     #display table
     print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
#wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
    else:
     if b == ccc and b == a :
       for n in [1] :
        t.forward(b*10)
        t.end_fill()
        t.color('green')
       style = ('Courier',10,'italic')
       t.write(""" equilateral triangle""",font=style,align='right' )
       print("Shape related data are:")
       print("""                                                          
                                                                    . *| 
                                                    b=a = (c)   . *    |                                                              
                                                            . *        | (b) = a=c
                                                          *____________|
                                                                (a) = b=c
     
       """)
       sum1 = float(a + a + a ) 
       sum2 = float(math.sqrt(3)/4) * (a**2)
       for n in range(1):
         t.penup()
         t.left(180-60)
         t.fd((a/2)*10)
         t.pendown()
         t.color("red")
         t.left(30)
         t.fd(4.5)
         t.left(180)
         t.fd(9)
         t.left(180)
         t.penup()
         t.fd(4.5)
         t.right(30)
         t.fd((a/2)*10)
         t.left(180-60)
         t.pendown()
       for n in range(1):
         t.penup()
         t.fd((b/2)*10)
         t.pendown()
         t.left(180-80)
         t.fd(4.5)
         t.left(180)
         t.fd(9)
         t.left(180)
         t.fd(4.5)
         t.right(180-80)
         t.penup()                  
         t.fd((b/2)*10)
         t.left(180-60)
         t.pendown()
       for n in range(1):
        t.penup()
        t.fd((b/2)*10)
        t.pendown()
        t.right(180-80)
        t.fd(4.5)
        t.left(180)
        t.fd(9)
        t.right(180)
        t.fd(4.5)        
        t.left(180-80)
        t.penup()
        t.fd((b/2)*10)
        t.pendown()
       print("          ------equilateral triangle-------\ncircumference : {0} |  triangle area : {1} | | degree angles: {2}°".format(sum1,sum2,gg))
       for n in range(1):
        t.penup()
        t.left(180-60)
        t.forward((a/2)*10)
        t.left(90)
        t.pendown()
        t.color("green")
       for n in range(5):
         t.fd(ac/2)
         t.penup()
         t.fd(ac/2)
         t.pendown()
       for n in range(1):
        t.penup()
        t.right(90)
        t.penup()
        t.fd(5)
        t.pendown()
        t.left(90)
        t.fd(9)
        t.left(180)
        t.fd(14)
        t.penup()
        t.left(90)
        t.fd(5)
        t.pendown()
        t.left(90)
        t.fd(5)
        t.left(90)
        t.fd(5)
        t.penup()
        t.fd(5)
        t.right(90)
        #t.fd((ac-ac/2)*10)
        t.pendown()
       for n in range(5):
         t.fd(ac/2)
         t.penup()
         t.fd(ac/2)
         t.pendown() 
       print("| triangle height: {0} |".format(ac)) 
       for n in range(1):
         t.penup()
         t.color("#430606")
         t.left(180-30) 
         t.fd((a)*10)
         t.left(180-60)
         t.fd(((a/2)/2)*10)#t.fd((a/2)*10) nononoo
         t.pendown()
         t.left(30)
         t.fd(4.5)
         t.left(180)
         t.fd(9)
         t.left(180)
         t.fd(4.5)
         t.right(30)
         t.penup()
         t.fd((a/2)*10)#nonoononononoonnon
         t.pendown()
         t.left(30)
         t.fd(4.5)
         t.left(180)
         t.fd(9)
         t.left(180)
         t.fd(4.5)
         t.right(30)
         t.right(180)
         t.penup()
         t.fd(((a/2)/2)*10)#nononononoonononnononononononoonnno
         t.pendown()
         t.left(180)
         t.circle(r3*10)
         t.left(90)
       for n in range(5):
         t.penup()
         t.fd(r3/1.3)
         t.pendown()
         t.fd(r3/1.3)
       for n in range(1):
         t.penup()
         t.left(90)
         t.fd(5)
         t.pendown()
         t.fd(5)
         t.left(90)
         t.fd(5)
         t.penup()
         t.left(180)
         t.fd(5)
         t.right(90)
         t.fd(10)
         t.left(90)
         t.pendown()
       for n in range(5):
         t.penup()
         t.fd(r3-(r3/1.3))
         t.pendown()
         t.fd(r3-(r3/1.3))
       for n in range(1):
         t.left(180-120)
       for n in range(5):
         t.penup()
         t.fd(r3)
         t.pendown()
         t.fd(r3)
       for n in range(1):
         t.left(90)

       print("""| circumference of a circle : {0} || area of a circle :{1} | | r : {2} |""".format(cicr,arci,r3))
       from tabulate import tabulate
       data = [["circumference", sum1], 
            ["triangle area", sum2],
            ["degree angle", gg],
            ["Height", ac],
            ["circumference of a circle", cicr], 
            ["area of a circle", arci], 
            ["r", r3]]
  
            #define header names
           #col_names = ["Shape related data are:"]
           #col_names = ["right triangle"]
       col_names = ["data", "xx"]
  
            #display table 
       print(tabulate(data, headers=col_names, tablefmt="fancy_grid"))
         
          #c degree angles:{3}°".format(sum1,sum2,ac,gg))
     else:  
       if c >90 and d != gg :
         for n in range(1):
            t.fd(c4*10)
            t.end_fill()
         print("Shape related data are :")
         print("""                                                      . */ 
                                                               (c)  . *   /
                                                                . *      /                                                            
                                                            . *         /(b) 
                                                          *____________/
                                                                (a) 
     
         """)
         sum1 = a + b + c4
         sum2 = bat - sat 
         r5 = (sum2) / (sum1/2)
         banga = math.tan((180-(gg/2+90))*math.pi/180) * r5
         banga1 = math.tan((120/2)*math.pi/180) * r5
         arci5 = math.pi * (r5**2)
         cicr5 = 2 * math.pi * r5
          #banga2 = -1*math.tan((d/2)*math.pi/180) * r5 + b
          #n = math.sin((180-((gg/2)+90))*math.pi/180) * r5
          #x = math.sqrt((n**2)-(r5**2))
         print("""| circumference : {0} || area :{1} | """.format(sum1,sum2))
         for n in range(1):
            t.penup()
            t.left(180 -gg)
            t.fd(a*10)
            t.pendown()
            t.color('red')
          #for n in range(5):
           # t.fd(rr) 
           # t.penup()
           # t.fd(rr)
           # t.pendown()
         for n in range(1):
           t.fd((rr/2)*10)
           t.left(90)
           t.penup()
           t.fd(5)
           t.pendown()
           t.fd(10)
           t.penup()
           t.left(180)
           t.fd(15)
           t.pendown()
           t.left(90)
           t.fd((rr/2)*10)
         print("""|  : {0} |""".format(rr))
         for n in range(1):
            t.left(90)
            t.color('green')
          #for n in range(5):
           # t.fd(h2)
            #t.penup()
            #t.fd(h2)
            #t.pendown()
         for n in range(1):
            t.fd((h2/1.2)*10)#/2
            t.right(90)
            t.penup()
            t.fd(5)
            t.pendown()
            t.left(90)
            t.fd(9)
            t.left(180)
            t.fd(14)
            t.penup()
            t.left(90)
            t.fd(5)
            t.pendown()
            t.left(90)
            t.fd(5)
            t.left(90)
            t.fd(5)
            t.penup()
            t.fd(5)
            t.pendown()
            t.right(90)
            t.fd((h2-h2/1.2)*10)
         print("""| h : {0} |""".format(h2))
         for n in range(1):
            t.left(90)
            t.color("blue")
         for n in range(5):
           t.fd(a+rr)
           t.penup()
           t.fd(a+rr)
           t.pendown()
         for n in [1]:
           t.left(90)
         for n in range(5):
            t.fd(h2)
            t.penup()
            t.fd(h2)
            t.pendown()
         print("| rectangle circumference : {0} | rectangle area : {1} | | diagonal d = {2} |".format(sum33,sum44,c4))
         for n in range(1):
            t.left(90)
            t.penup()
            t.fd((banga)*10)
            t.pendown()
            t.color('#430606')
            t.circle(r5*10)
            t.left(90)
            t.fd(r5/2*10)
            t.penup()
            t.left(90)
            t.fd(5)
            t.pendown()
            t.fd(5)
            t.left(90)
            t.fd(6)
            t.penup()
            t.left(180)
            t.fd(6)
            t.right(90)
            t.fd(10)
            t.left(90)
            t.pendown()
            t.fd(r5/2*10)
            t.penup()
            t.left(180)
            t.fd(r5*10)
            t.speed(1000990)
            t.left(90)
            t.fd((a-banga)*10)
            t.left(180-c)
            #t.fd((b-banga1)*10)
            #t.left(180)
            t.fd((b-banga1-r5)*10)
            t.left(90)
            t.pendown()
            t.fd(r5*10)
            #t.pendown()
            #t.fd(r5*10)
            t.left(90)
         print("""| circumference of a circle : {0} || area of a circle : {1} | | r : {2} |""".format(cicr5,arci5,r5))
          #print("""| circumference : {0} || area :{1} | | r : {2} | h : {3} | c: {4}""".format(sum1,sum2,rr,h2,c4))



turtle.done()
#print("             ------right triangle-------\n| circumference : {0} |\n| triangle area : {1} |\n| The hypotenuse : {2} |\n| third degree angle: {3} |\n| length height 'h': {4} |\n| p : {5} | q : {6}  ".format(sum1,sum2,cc,gg,h,p,q))
