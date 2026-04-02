from tkinter import *
from tkinter import ttk
from painter import draw_graphic

def finish():
    root.destroy()

def getData():
    global dydx, solution, x0, xn, y0, step, epsilon
    dydx, solution, x0, xn, y0, step, epsilon = \
        dydx_entry.get(), solution_entry.get(), x0_entry.get(), xn_entry.get(), \
        y0_entry.get(), step_entry.get(), epsilon_entry.get()

def update():
    global dydx, solution, x0, xn, y0, epsilon, graphic#,table
    getData()

    h, x, y_exact, y_appr = draw_graphic(float(x0), float(xn), float(step), float(y0), float(epsilon), dydx, solution)

    graphic = PhotoImage(file="Runge-Kutta/graphic.png")
    graph_label = Label(root, image=graphic)
    graph_label.place(x=225, y=0)
    

    data = [(f'{float(x[i]):.3f}', str(y_exact[int(i*h / float(step))]), str(y_appr[i]), \
             str(abs(y_appr[i] - y_exact[int(i*h / float(step))]))) \
            for i in range(0, len(x), int(float(step) / h))]
    
    '''table.delete(*table.get_children())
    for row in data:
        table.insert("", END, values=row)
    
    table.place(x=0, y=500)'''
    

    data.insert(0, ("x", "y точное", "y численное", "разница"))

    for i in range(len(data)):
        for j in range(len(data[0])):
            cell = Label(text=str(data[i][j]), relief='solid')
            cell.place(x=950 + j*130, y=i*20, width=135, height=25)



root = Tk()
root.title("Метод Рунге-Кутта")
root.geometry('900x800')

dydx = "-y**2 - x**(-4)"
solution = "(tg(1/x - 1) + x) / (x**2)"
x0 = "1"
xn = "2"
y0 = "1"
step = "0.1"
epsilon = "0.0001"
graphic = PhotoImage()
graph_label = Label()
'''
columns = ("x", "y точное", "y численное", "разница")

table = ttk.Treeview(columns=columns, show="headings", height=12)


table.heading("x", text="x")
table.heading("y точное", text="y точное")
table.heading("y численное", text="y численное")
table.heading("разница", text="разница")
'''


dydx_label = Label(text="Введите уравнение dy/dx = ")
dydx_label.pack(anchor='nw')

dydx_entry = Entry()
dydx_entry.insert(0, "-y**2 - x**(-4)")
dydx_entry.pack(anchor='nw')

solution_label = Label(text="Введите аналитическое решение y(x) = ")
solution_label.pack(anchor='nw')

solution_entry = Entry()
solution_entry.insert(0, "(tg(1/x - 1) + x) / (x**2)")
solution_entry.pack(anchor='nw')

x0_label = Label(text="Введите x0")
x0_label.pack(anchor='nw')

x0_entry = Entry()
x0_entry.insert(0, "1")
x0_entry.pack(anchor='nw')

xn_label = Label(text="Введите xn")
xn_label.pack(anchor='nw')

xn_entry = Entry()
xn_entry.insert(0, "2")
xn_entry.pack(anchor='nw')

y0_label = Label(text="Введите y0")
y0_label.pack(anchor='nw')

y0_entry = Entry()
y0_entry.insert(0, "1")
y0_entry.pack(anchor='nw')

step_label = Label(text="Введите шаг h")
step_label.pack(anchor='nw')

step_entry = Entry()
step_entry.insert(0, "0.1")
step_entry.pack(anchor='nw')

epsilon_label = Label(text="Введите погрешность")
epsilon_label.pack(anchor='nw')

epsilon_entry = Entry()
epsilon_entry.insert(0, "0.0001")
epsilon_entry.pack(anchor='nw')

draw_button = ttk.Button(text="Draw", command=update)
draw_button.pack(anchor='nw', pady=5)

exit_button = ttk.Button(text="Exit", command=finish)
exit_button.pack(anchor='nw', pady=5)

root.mainloop()