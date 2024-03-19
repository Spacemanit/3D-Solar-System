from tkinter.font import Font
import arrow
import matplotlib.pyplot as plt
import matplotlib.widgets as mw
from skyfield.api import load
import datetime as dt
from datetime import time
from tkinter import Button, Label, Scale, Tk, IntVar
from tkcalendar import DateEntry
import copy

root = Tk()
root.geometry("800x800")
root.title("3D solar system")
data = load("de430_1850-2150.bsp")
mercury, venus, earth, mars, jupiter, saturn, uranus, neptune, pluto, sun = [
    data[i] for i in range(1, 11)
]
planet_dict = {
    "1": ["mercury", mercury, "lightgrey"],
    "2": ["venus", venus, "khaki"],
    "3": ["earth", earth, "aqua"],
    "4": ["mars", mars, "lightsalmon"],
    "5": ["jupiter", jupiter, "olive"],
    "6": ["saturn", saturn, "gold"],
    "7": ["uranus", uranus, "turquoise"],
    "8": ["neptune", neptune, "royalblue"],
    "9": ["pluto", pluto, "slategrey"],
}
p = []
pauser = bool()
tldvar = IntVar()
pstvar = IntVar()
dpsvar = IntVar()
paused = False

def add(st, button):
    global p
    if button.cget("bg") == "red":
        button.config(bg=planet_dict[st][2])
        p.append(st)
    else:
        button.config(bg="red")
        p.remove(st)

def plotting():
    global p, paused
    planets = [["sun", sun, "yellow"]]
    for char in p:
        if planet_dict[char] not in planets:
            planets.append(planet_dict[char])
    print("started...")
    fig = plt.figure(figsize=(5, 5))
    fig.set_facecolor("navy")
    ax = fig.add_subplot(111, projection="3d")
    ax.set_facecolor("navy")
    ax.grid(color="green")

    def pausing(event):
        global paused
        paused = not paused

    axes = plt.axes((0.8, 0, 0.2, 0.05))
    pausebutton = mw.Button(axes, "Play/Pause")
    pausebutton.on_clicked(pausing)
    ts = load.timescale()
    k = sde.get_date()
    nw = dt.datetime.combine(k, time(0, 0, 0, 0))
    nw = (arrow.get(nw)).replace(tzinfo="UTC")
    tl = copy.deepcopy(nw)
    elev, azim = 30, 45
    xlim, ylim, zlim = (-10, 10), (-10, 10), (-10, 10)
    while True:
        if not paused:
            if (nw - tl).days >= tldvar.get():
                ax.cla()
                tl = nw
            nw = nw + dt.timedelta(days=(dpsvar.get() * 0.1))
            t = ts.from_datetime(nw)
            for i in planets:
                astrometric = i[1].at(t)
                x, y, z = astrometric.position.au
                ax.scatter(
                    x, y, z, s=int(pstvar.get()), marker="o", label=i[0], color=i[2]
                )
        ax.set_title(nw.date())
        ax.view_init(elev=elev, azim=azim)
        ax.set_xlim3d(xlim)
        ax.set_ylim3d(ylim)
        ax.set_zlim3d(zlim)
        if not plt.fignum_exists(fig.number):
            break
        plt.draw()
        plt.pause(0.1)
        elev, azim = ax.elev, ax.azim
        xlim, ylim, zlim = ax.get_xlim(), ax.get_ylim(), ax.get_zlim()

Mer = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["1"][0],
    command=lambda: add("1", Mer),
)
Mer.grid(row=0, column=0, padx=15, pady=10)
Ven = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["2"][0],
    command=lambda: add("2", Ven),
)
Ven.grid(row=0, column=1, padx=15, pady=10)
Ear = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["3"][0],
    command=lambda: add("3", Ear),
)
Ear.grid(row=0, column=2, padx=15, pady=10)
Mar = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["4"][0],
    command=lambda: add("4", Mar),
)
Mar.grid(row=0, column=3, padx=15, pady=10)
Jup = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["5"][0],
    command=lambda: add("5", Jup),
)
Jup.grid(row=1, column=0, padx=15, pady=10)
Sat = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["6"][0],
    command=lambda: add("6", Sat),
)
Sat.grid(row=1, column=1, padx=15, pady=10)
Ura = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["7"][0],
    command=lambda: add("7", Ura),
)
Ura.grid(row=1, column=2, padx=15, pady=10)
Nep = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["8"][0],
    command=lambda: add("8", Nep),
)
Nep.grid(row=1, column=3, padx=15, pady=10)
Plu = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text=planet_dict["9"][0],
    command=lambda: add("9", Plu),
)
Plu.grid(row=2, column=0, padx=15, pady=10)
l1 = Label(
    root,
    text="Trail length (days)",
    width=21,
    height=1,
    bg="grey",
    fg="black",
    font=Font(family="Space Odyssey", size=20),
)
l1.grid(row=3, column=0, columnspan=2)
tld = Scale(
    root,
    variable=tldvar,
    from_=0,
    to=732,
    font=Font(family="Space Odyssey", size=20),
    orient="horizontal",
)
tld.grid(row=3, column=2)
l2 = Label(
    root,
    text="Point Size",
    width=21,
    height=1,
    bg="grey",
    fg="black",
    font=Font(family="Space Odyssey", size=20),
)
l2.grid(row=4, column=0, columnspan=2)
pst = Scale(
    root,
    variable=pstvar,
    from_=0,
    to=100,
    font=Font(family="Space Odyssey", size=20),
    orient="horizontal",
)
pst.set(8)
pst.grid(row=4, column=2)
sdl = Label(
    root,
    text="Speed (days/s)",
    width=21,
    height=1,
    bg="grey",
    fg="black",
    font=Font(family="Space Odyssey", size=20),
)
sdl.grid(row=5, column=0, columnspan=2)
dps = Scale(
    root,
    variable=dpsvar,
    from_=0,
    to=200,
    font=Font(family="Space Odyssey", size=20),
    orient="horizontal",
)
dps.set(1)
dps.grid(row=5, column=2)
sdl = Label(
    root,
    text="Start Date",
    width=21,
    height=1,
    bg="grey",
    fg="black",
    font=Font(family="Space Odyssey", size=20),
)
sdl.grid(row=6, column=0, columnspan=2)
sde = DateEntry(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    date_pattern="mm/dd/yyyy",
)
sde.grid(row=6, column=2)
Strt = Button(
    root,
    width=9,
    height=1,
    bg="red",
    fg="white",
    font=Font(family="Space Odyssey", size=20),
    text="Start",
    command=lambda: plotting(),
)
Strt.grid(row=7, column=1, padx=15, pady=10)

root.mainloop()
