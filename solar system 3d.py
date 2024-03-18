from tkinter.font import Font
import matplotlib.pyplot as plt
from skyfield.api import load
import datetime as dt
from tkinter import Button, Label, Scale, Tk, IntVar

p = []
v1=IntVar

def add(st, button):
    global p
    if button.cget('bg') == "red":
        button.config(bg='green')
        p.append(st)
    else:
        button.config(bg='red')
        p.remove(st)

def plotting():
    global p
    data = load("de421.bsp")
    mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto, sun = [
        data[i] for i in range(1, 11)
    ]
    planet_dict = {
        "1": ["mercury", mercury, "grey"],
        "2": ["venus", venus, "khaki"],
        "3": ["earth", earth, "aqua"],
        "4": ["mars,", mars, "orangered"],
        "5": ["jupiter", jupiter, "olive"],
        "6": ["saturn", saturn, "gold"],
        "7": ["uranus", uranus, "turquoise"],
        "8": ["neptune", neptune, "royalblue"],
        "9": ["pluto", pluto, "slategrey"],
    }
    planets = [["sun", sun, "yellow"]]
    for char in p:
        if planet_dict[char] not in planets:
            planets.append(planet_dict[char])
    print("started...")
    fig = plt.figure(figsize=(5, 5))
    ax = fig.add_subplot(111, projection="3d")
    day = 0
    nw = dt.datetime.now(dt.timezone.utc)
    ts = load.timescale()
    xlim, ylim, zlim = (-10, 10), (-10, 10), (-10, 10)
    while True:
        day += dps.get()
        elev, azim = ax.elev, ax.azim
        if day >= int(tld.get()):
            ax.cla()
            day = 0
        nw = nw + dt.timedelta(days=(dps.get()))
        t = ts.from_datetime(nw)
        print(nw)
        for i in planets:
            astrometric = i[1].at(t)
            x, y, z = astrometric.position.au
            ax.scatter(x, y, z, s=int(pst.get()), marker="o", label=i[0], color=i[2])
        ax.view_init(elev=elev, azim=azim)
        ax.set_xlim3d(xlim)
        ax.set_ylim3d(ylim)
        ax.set_zlim3d(zlim)
        if not plt.fignum_exists(fig.number):
            break
        plt.draw()
        plt.pause(1)
        xlim, ylim, zlim = ax.get_xlim(), ax.get_ylim(), ax.get_zlim()

root = Tk()
root.geometry("800x800")
pl = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
Mer = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[0], command = lambda:add("1", Mer))
Mer.grid(row=0, column=0, padx=15, pady=10)
Ven = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[1], command = lambda:add("2", Ven))
Ven.grid(row=0, column=1, padx=15, pady=10)
Ear = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[2], command = lambda:add("3", Ear))
Ear.grid(row=0, column=2, padx=15, pady=10)
Mar = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[3], command = lambda:add("4", Mar))
Mar.grid(row=0, column=3, padx=15, pady=10)
Jup = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[4], command = lambda:add("5", Jup))
Jup.grid(row=1, column=0, padx=15, pady=10)
Sat = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[5], command = lambda:add("6", Sat))
Sat.grid(row=1, column=1, padx=15, pady=10)
Ura = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[6], command = lambda:add("7", Ura))
Ura.grid(row=1, column=2, padx=15, pady=10)
Nep = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[7], command = lambda:add("8", Nep))
Nep.grid(row=1, column=3, padx=15, pady=10)
Plu = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = pl[8], command = lambda:add("9", Plu))
Plu.grid(row=2, column=0, padx=15, pady=10)
l1 = Label(root, text = "Trail length (days)", width=21, height=1, bg="grey", fg="black", font=Font(family="Space Odyssey", size=20)) 
l1.grid(row=3, column=0, columnspan=2)
tld = Scale(root, variable = v1, from_=0, to=100, font=Font(family="Space Odyssey", size=20) , orient="horizontal")   
tld.grid(row=3, column=2)
l2 = Label(root, text = "Point Size", width=21, height=1, bg="grey", fg="black", font=Font(family="Space Odyssey", size=20)) 
l2.grid(row=4, column=0, columnspan=2)
pst = Scale(root, variable = v1, from_=0, to=100, font=Font(family="Space Odyssey", size=20) , orient="horizontal")   
pst.grid(row=4, column=2)
l3 = Label(root, text = "Speed (days/s)", width=21, height=1, bg="grey", fg="black", font=Font(family="Space Odyssey", size=20)) 
l3.grid(row=5, column=0, columnspan=2)
dps = Scale(root, variable = v1, from_=0, to=100, font=Font(family="Space Odyssey", size=20) , orient="horizontal")   
dps.grid(row=5, column=2)
Strt = Button(root, width=9, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = "Start", command = lambda:plotting())
Strt.grid(row=6, column=1, padx=15, pady=10)
openother = Button(root, width=18, height=1, bg="red", fg="white", font=Font(family="Space Odyssey", size=20) ,text = "Geocentric view", command = lambda:open("geocentric view.py"))
openother.grid(row=6, column=2, columnspan=2)
root.mainloop()
