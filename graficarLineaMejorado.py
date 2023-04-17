from tkinter import *
from tkinter import messagebox
app = Tk()
app.geometry("800x700")

def cuadricula():
    lienzo.create_rectangle(1,1, 700,500, outline="black", width=3, fill="white")
    for i in range(50, 651, 10):
        lienzo.create_line(i, 50, i, 450, fill="gray")#lineas y
    for i in range(50, 451, 10):
        lienzo.create_line(50, i, 650, i, fill="gray", width=0.2)#lineas x
    for i in range(50, 451, 50): # numeros de "y"
        a = 250 - i
        if a != 0:
            lienzo.create_line(346, i, 354, i, width=2, fill="red")
            lienzo.create_text(330, i, text=a, fill="red")                    
    for i in range(50, 651, 50): # numeros de "x"
        a = -350 + i
        if a != 0:
            lienzo.create_line(i, 246, i, 254, width=2, fill="red")
            lienzo.create_text(i, 270, text=a, fill="red")
    lienzo.create_line(350, 50, 350, 450, width=2, fill="red")
    lienzo.create_line(50, 250, 650, 250, width=2, fill="red")
    
def graficarLinea():
    X1, Y1, X2, Y2= x1.get(), y1.get(), x2.get(), y2.get()
    if X1 and Y1 and X2 and Y2:
        if ( X1.isnumeric() or (X1[0] == "-" and X1[1:].isnumeric()) ) and ( Y1.isnumeric() or (Y1[0] == "-" and Y1[1:].isnumeric()) ) and ( X2.isnumeric() or (X2[0] == "-" and X2[1:].isnumeric()) ) and ( Y2.isnumeric() or (Y2[0] == "-" and Y2[1:].isnumeric()) ):
            X1 = int(X1) + 350
            X2 = int(X2) + 350
            Y1 = 250 - int(Y1)
            Y2 = 250 - int(Y2)
            rangoX = [i for i in range(50,651)]
            rangoY = [i for i in range(50,451)]
            if X1 in rangoX and X2 in rangoX and Y1 in rangoY and Y2 in rangoY:
                Y = Y1-Y2
                X = X2-X1
                if X <= 0 >= Y:
                    X *= -1
                    Y *= -1
                for i in range(1,24,1):
                    if Y % i == 0 == X % i:
                        Y /= i
                        X /= i
                        i -= 1
                if X == 0:
                    m = "Pendiente indefinida"
                elif Y == 0:
                    m = "Pendiente nula"
                else:
                    m = '{:.2f}/{:.2f} = {:.2f}/{:.2f} = {:.2f}'.format(Y1-Y2, X2-X1, Y, X, Y/X)
                cuadricula()
                lienzo.create_line(X1, Y1, X2, Y2, fill="blue", width=2.5)
                lienzo.create_oval(((X1 + X2)/2)-5, ((Y1 + Y2)/2)-5, ((X1 + X2)/2)+5, ((Y1 + Y2)/2)+5, fill="skyblue")
                longitud.set( "%.2f"%(((X2-X1)**2)+((Y2-Y1)**2))**0.5)
                pendiente.set(m)
                puntoMedio.set(f'({((X1+X2)/2)-350} , {((Y2+Y1)/-2)+250})')
            else:
                messagebox.showinfo("Error", "Uno o mas datos ingresados rebasan el rango permitido")
        else: 
            messagebox.showinfo("Error", "Los datos deben ser numeros enteros")
    else:
        messagebox.showinfo("Error", "asegurese que todos los campos esten llenos")

def reset():
    cuadricula()
    x1.set("")    
    y1.set("")    
    x2.set("")    
    y2.set("")    
    longitud.set("")    
    pendiente.set("")    
    puntoMedio.set("")    

lienzo = Canvas(app, width=700, height=500, bg="white")
lienzo.place(x=50,y=100)
cuadricula()

x1, x2, y1, y2, longitud, pendiente, puntoMedio = StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()

Label(app, text="x1").place(x=20,y=20)
Label(app, text="y1").place(x=190,y=20)
Label(app, text="x2").place(x=20,y=70)
Label(app, text="y2").place(x=190,y=70)

Entry(app, textvariable=x1).place(x=50,y=20)
Entry(app, textvariable=y1).place(x=220,y=20)
Entry(app, textvariable=x2).place(x=50,y=70)
Entry(app, textvariable=y2).place(x=220,y=70)

#Resultados
Label(app, text="Longitud").place(x=360,y=20)
Label(app, text="Pendiente").place(x=360,y=70)
Label(app, text="Punto medio").place(x=570,y=20)

Entry(app, textvariable=longitud).place(x=430,y=20)
Entry(app, textvariable=pendiente, width=50).place(x=430,y=70)
Entry(app, textvariable=puntoMedio).place(x=660,y=20)

Button(app, text="Graficar", command=graficarLinea).place(x=300,y=620)
Button(app, text="Reset", command=reset).place(x=360,y=620)

app.mainloop()