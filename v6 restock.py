import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sys

super_dude = 8
lizard_man = 12
water_woman = 3
comics_sold = 0
super_sold = 0
lizard_sold = 0
water_sold = 0

# Baseline code
class Master(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, Sell, Stock, Restock):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew") # Allignment + stretch
        
        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Comic Book Store", font="Arial 30 bold")
        label.grid(row=0, column=1, columnspan=10, pady=10, padx=50)

        SellButton = ttk.Button(self, text="Sell Comic Area", command=lambda: controller.show_frame(Sell)) #lambda stops auto run upon load
        SellButton.grid(row=1, column=1, padx=25, pady=25, ipady=50, ipadx=50)

        StockButton = ttk.Button(self, text="Stock Level Information", command=lambda: controller.show_frame(Stock)) #lambda stops auto run upon load
        StockButton.grid(row=1, column=2, padx=25, pady=25, ipady=50, ipadx=50)

        RestockButton = ttk.Button(self, text="Restock Comic Area", command=lambda: controller.show_frame(Restock)) #lambda stops auto run upon load
        RestockButton.grid(row=1, column=3, padx=25, pady=25, ipady=50, ipadx=50)

class Sell(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Sell Comic Area", font="Arial 30 bold")
        label.pack(pady=10, padx=10)

        BackButton = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage)) #lambda stops auto run upon load
        BackButton.place(x=15,y=15)

# Functions to sell product
        def clicked_superdude():
            global super_dude, comics_sold, super_sold
            super_dude -= 1
            comics_sold += 1
            super_sold += 1
            print(super_dude, comics_sold)
        
        def clicked_lizardman():
            global lizard_man, comics_sold, lizard_sold
            lizard_man -= 1
            comics_sold += 1
            lizard_sold += 1
            print(lizard_man, comics_sold)

        def clicked_waterwoman():
            global water_woman, comics_sold, water_sold
            water_woman -= 1
            comics_sold += 1
            water_sold += 1
            print(water_woman, comics_sold)

# Functions to show on out of stock
        def clickedsuper():
            if super_dude <= 0:
                messagebox.showinfo("Error", "Out of Stock")
                return
            messagebox.showinfo("Alert", "Comic Purchased!")
            clicked_superdude()

        def clickedlizard():
            if lizard_man <= 0:
                messagebox.showinfo("Error", "Out of Stock")
                return
            messagebox.showinfo("Alert", "Comic Purchased!")
            clicked_lizardman()

        def clickedwater():
            if water_woman <= 0:
                messagebox.showinfo("Error", "Out of Stock")
                return
            messagebox.showinfo("Alert", "Comic Purchased!")
            clicked_waterwoman()

# Buy item buttons
        super_btn = ttk.Button(self, text="BUY ITEM #super", command=clickedsuper)
        super_btn.place(x=65,y=120)

        lizard_btn = ttk.Button(self, text="BUY ITEM #lizard", command=clickedlizard)
        lizard_btn.place(x=350,y=120)

        water_btn = ttk.Button(self, text="BUY ITEM #water", command=clickedwater)
        water_btn.place(x=600,y=120)

# Comic book labels
        super_dude_label = tk.Label(self, text="Super Dude Comic!", font="arial 15 bold")
        super_dude_label.place(x=15,y=75)

        lizard_man_label = tk.Label(self, text="Lizard Man Comic!", font="arial 15 bold")
        lizard_man_label.place(x=300,y=75)

        water_woman_comic = tk.Label(self, text="Water Woman Comic!", font="arial 15 bold")
        water_woman_comic.place(x=550,y=75)

class Stock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Stock Level Information", font="Arial 30 bold")
        label.pack(pady=10, padx=10)

        BackButton = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage)) #lambda stops auto run upon load
        BackButton.place(x=15,y=15)

        def show_sold():
            stock_sentence = f"ITEMS LEFT IN STOCK:\n{super_dude} Super Dude Comic's\n {lizard_man} Lizard Man Comic's\n {water_woman} Water Woman Comic's"
            current_stock = tk.Label(self, text=stock_sentence, font="arial 18 bold")
            current_stock.place(x=80,y=110)

            stock_sold_sentence = f"ITEMS SOLD:\n{super_sold} Super Dude Comic's\n {lizard_sold} Lizard Man Comic's\n {water_sold} Water Woman Comic's"
            stock_sold = tk.Label(self, text=stock_sold_sentence, font="arial 18 bold")
            stock_sold.place(x=400,y=110)

        info_btn = ttk.Button(self, text="Generate/Refresh Stock Information", command=show_sold)
        info_btn.pack()

class Restock(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Restock Comic Area", font="Arial 30 bold")
        label.pack(pady=10, padx=10)

        BackButton = ttk.Button(self, text="< Back", command=lambda: controller.show_frame(HomePage)) #lambda stops auto run upon load
        BackButton.place(x=15,y=15)


# Drop Down Box

        def show():
            aLabel = Label(root, text=clicked.get()).pack()

        clicked = tk.StringVar()
        clicked.set("Select...")

        options = [
            "Super Dude",
            "Lizard Man",
            "Water Woman"
        ]

        drop = tk.OptionMenu(self, clicked, *options)
        drop.pack()

# SUPER ENTRY BOX
        super_entry = tk.Entry(self, width=10, bg="white")
        super_entry.pack()
        super_entry.get()
    
        def onClick():
            myLabel = tk.Label(self, text=super_entry.get())
            myLabel.pack()
            if super_entry == super_dude:
                print("ok")


        myButton = ttk.Button(self, text="Enter restock", command=onClick)
        myButton.pack()


app = Master()
app.title("Comic Book Store")
app.mainloop()
