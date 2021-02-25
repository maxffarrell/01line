from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    xmin=min(x0,x1)
    xmax=max(x0,x1)
    if(x0==xmax):#swap pts
        x0=xmin
        x1=xmax
        ytemp=y0
        y0=y1
        y1=ytemp

    x0=int(x0)
    y0=int(y0)
    x1=int(x1)
    y1=int(y1)
    
    dy=int(y1-y0)
    dx=int(x1-x0)
    
    if (dx==0):#vertical
        #print("vert")
        for y in range(y0, y1+1):
            plot(screen, color, x0, y)
        for y in range(y1+1, y0):
            plot(screen, color, x0, y)
    elif (dy/dx>0 and dy/dx<=1):#O1&O5, credit to Abhishek Sharma on YouTube
        #print("O1&O5")
        p=2*dy-dx
        y=y0
        for x in range(x0,x1+1):
            plot(screen,color,x,y)
            if(p>0):
                y+=1
                p-=2*dx
            x+=1
            p+=2*dy
    elif (dy/dx>1):#O2&O6
        #print("O2&O6")
        p=-dy+2*dx
        x=x0
        for y in range(y0,y1+1):
            plot(screen,color,x,y)
            if(p>0):
                x+=1
                p-=2*dy
            y+=1
            p+=2*dx
    elif((dy/dx)<-1):#O3&O7
        #print("O3&O7")
        #print(dy/dx)
        p=dy+2*dx
        x=x1
        for y in range(y1,y0+1):
            plot(screen,color,x,y)
            if(p>0):
                x+=1
                p+=2*dy
            x-=1
            p+=2*dx
    elif((dy/dx)>=-1 and (dy/dx)<0):#O4&O8
        #print("O4&O8")
        #print(dy/dx)
        p=2*dy+dx
        y=y0
        for x in range(x0,x1+1):
            plot(screen,color,x,y)
            if(p<0):
                y-=1
                p+=2*dx
            x+=1
            p+=2*dy
    else:#horizontal
        #print("h")
        for x in range(x0, x1+1):
            plot(screen, color, x, y0)
