# Import the tkinter module and all its functions
from tkinter import *
from tkinter import messagebox
# Import the ttk module
import tkinter.ttk
# import os module to open the text file on Windows
import os
# import platform module to check the operating system
import platform
# import subprocess module to open the text file on Mac and all other necessary modules
import subprocess
import math
import random
from datetime import date

# Create the root window
root = Tk()
root.attributes('-alpha', 0)  # Hide the root window until the login window is closed

# Check the operating system and print the result
print('Platform processor:', platform.system())

# r = Rectangle
# t = Text
# p = Polygon
# d and dd = Dropdown menu
# b = Button
# cb = Checkbutton

# Sample employee database (username: password)
employee_database = {
    "john123": "password123",
    "jane456": "qwerty456",
    "bob789": "abcxyz789",
    "admin": "admin"
}


# password and username function for login
def login():
    username = entry_username.get()
    password = entry_password.get()

    if username in employee_database and employee_database[username] == password:
        messagebox.showinfo("Login Successful", "Welcome, " + username + "!")
        open_main_window()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


# Create the login_window
login_window = Tk()
login_window.attributes('-topmost', True)
login_window.title("WallpaperCustomizer-Login")
login_window.resizable(width=False, height=False)

# Create a canvas widget to hold the button and label widgets and set its size and background color
login_window_canvas = Canvas(login_window, width=320, height=240, bg='#303030')
login_window_canvas.pack()

# Create username label and entry
label_username = tkinter.ttk.Label(login_window, text="Username:", font=("Arial", 12), background="#303030",
                                   foreground="white")
label_username.pack()
entry_username = tkinter.ttk.Entry(login_window, font=("Arial", 12))
entry_username.pack()

# Create password label and entry
label_password = tkinter.ttk.Label(login_window, text="Password:", font=("Arial", 12), background="#303030",
                                   foreground="white")
label_password.pack()
entry_password = tkinter.ttk.Entry(login_window, show="*", font=("Arial", 12))
entry_password.pack()

# Create login button
button_login = tkinter.ttk.Button(login_window, text="Login", command=login, style="TButton")
button_login.pack()

# login window shape
canvas_logo = Canvas(login_window, width=320, height=240, bg='#303030')
canvas_logo.place(x=0, y=0)

center_x = 160
center_y = 120
outer_side = 200
inner_side = 60
num_squares = 7

login_colours = ["#FFFFFF", "#D9D9D9", "#A6A6A6", "#808080"]
num_colors = len(login_colours)

for i in range(num_squares):
    side = outer_side - ((outer_side - inner_side) / num_squares) * i
    color_index = i % num_colors
    color = login_colours[color_index]
    x1 = center_x - side / 2
    y1 = center_y - side / 2
    x2 = center_x + side / 2
    y2 = center_y + side / 2
    canvas_logo.create_rectangle(x1, y1, x2, y2, fill=color, outline="", width=2)

# Create the login window title
t8 = tkinter.ttk.Label(login_window, text="WPC-LOGIN", font=("Arial", 20), background="#303030", foreground="white")
t8.place(x=80, y=105)


def open_main_window():
    login_window.withdraw()  # Hide the login window

    # Create the root window and set its title and make it non-resizable
    root.attributes('-alpha', 1)
    root.attributes('-topmost', True)
    root.title('WallpaperCustomizerApp')
    root.resizable(width=False, height=False)
    # Create a canvas widget to hold the button and label widgets and set its size and background color
    main_window_canvas: Canvas = Canvas(root, width=1280, height=720)
    main_window_canvas.pack()
    main_window_canvas.config(bg='#5A5A5A')

    def place_order():
        global Customer_name, Customer_address, Customer_phone, Customer_email, order_number
        # Create the order_window
        root.attributes('-alpha', 0)  # Hide the root window until the login window is closed
        order_window = Tk()
        order_window.title("Place Order")
        order_window.resizable(width=False, height=False)
        # Create a canvas widget for the order window and set its size and background color
        canvas = Canvas(order_window, width=500, height=720, bg='#303030')
        canvas.pack()

        def edit_order():
            order_window.withdraw()  # Hide the order window
            root.attributes('-alpha', 1)  # Hide the root window until the login window is closed

        t7 = Text(order_window, width=50, height=1, font=("Arial", 12), background="#303030", foreground="white")
        t7.place(x=50, y=50)
        t7.insert(END, "Enter customer details below:")
        t7.config(state=DISABLED)

        l4 = tkinter.ttk.Label(order_window, text="Customer Name:", font=("Arial", 12), background="#303030",
                               foreground="white")
        l4.place(x=50, y=100)
        Customer_name = tkinter.ttk.Entry(order_window)
        Customer_name.place(x=250, y=100)

        l5 = tkinter.ttk.Label(order_window, text="Customer Address:", font=("Arial", 12), background="#303030",
                               foreground="white")
        l5.place(x=50, y=150)
        Customer_address = tkinter.ttk.Entry(order_window)
        Customer_address.place(x=250, y=150)

        l6 = tkinter.ttk.Label(order_window, text="Customer Phone Number:", font=("Arial", 12), background="#303030",
                               foreground="white")
        l6.place(x=50, y=200)
        Customer_phone = tkinter.ttk.Entry(order_window)
        Customer_phone.place(x=250, y=200)

        l7 = tkinter.ttk.Label(order_window, text="Customer Email:", font=("Arial", 12), background="#303030",
                               foreground="white")
        l7.place(x=50, y=250)
        Customer_email = tkinter.ttk.Entry(order_window)
        Customer_email.place(x=250, y=250)

        # Generate a random order number
        order_number = random.randint(100000, 999999)
        label_order_number = tkinter.ttk.Label(order_window, text="Order Number: {}".format(order_number),
                                               font=("Arial", 12),
                                               background='#303030', foreground='white')
        label_order_number.place(x=50, y=300)

        # Create a button widget to place the order
        b3 = tkinter.ttk.Button(order_window, text="Finalize Order", command=calculate_price, style="TButton")
        b3.place(x=50, y=350)

        # Create a button widget to go back to the main window
        b4 = tkinter.ttk.Button(order_window, text="Edit order", command=edit_order, style="TButton")
        b4.place(x=50, y=400)

        order_window.mainloop()

    def calculate_price():  # Calculate the price of the order
        global cost, total_cost, rolls_needed
        # Get the values from the entry boxes
        cost = 0.0
        total_cost = 0.0
        amount = float(amount_entry.get())
        paper_type = d2.get()
        colour = d1.get()
        lining = var4.get()
        paste = var5.get()
        wallpaper_width = 52
        wallpaper_height = 10.05
        lining_roll_length = 20  # Length of each lining paper roll in meters
        total_area = float(wallpaper_width) * float(wallpaper_height) * float(amount)

        # Determine the paper cost based on the type
        if paper_type.lower() == "standard wallpaper":
            roll_cost = 156.78
        elif paper_type.lower() == "premium wallpaper":
            roll_cost = 313.56
        else:
            roll_cost = 0

        # Determine the cost of the wallpaper
        rolls_needed = math.ceil(amount / wallpaper_height)
        cost += rolls_needed * roll_cost
        # Determine if any extra is checked
        foil = False
        glitter = False
        embossing = False
        paste_choice = "False"
        lining_choice = "False"
        # Determine id any extra is checked
        if radio_var.get() == 1:
            cost += wallpaper_height * 0.12
            foil = True

        elif radio_var.get() == 2:
            cost += wallpaper_height * 0.18
            glitter = True

        elif radio_var.get() == 3:
            cost += wallpaper_height * 0.06
            embossing = True
        else:
            cost += 0

        # Determine the lining paper cost if required
        if lining:
            cost += math.ceil(amount / lining_roll_length) * 7.63
            lining_choice = "True"
        elif lining_entry.get() != "":
            cost += float(lining_entry.get()) / 20 * 7.63  # double the cost to account for 20m rolls instead of 10.05m
            lining_choice = lining_entry
        else:
            cost += 0
            print("Unknown value entered for lining paper or none at all")

        # Determine the paste cost if required
        if paste:
            cost += math.ceil(
                amount / roll_cost) * 13.99  # calculate the number of tubs required for the amount of wallpaper
            paste_choice = "True"
        elif paste_entry.get() != "":
            cost += math.ceil(float(
                paste_entry.get()) / roll_cost) * 13.99  # calculate the number of tubs required for a custom amount of paste
            paste_choice = paste_entry.get()
        else:
            cost += 0
            print("Unknown value entered for paste or none at all")

        # Calculate the total cost
        total_cost += cost  # add the cost of the wallpaper to the total cost
        # print the order details to the console for prototype purposes
        print("___________Order Details___________")
        print("Amount: {}".format(amount) + "m")
        print("Paper Type: {}".format(paper_type))
        print("Colour: {}".format(colour))
        if foil:
            print("Extra: Foil")
        elif glitter:
            print("Extra: Glitter")
        elif embossing:
            print("Extra: Embossing")
        else:
            print("No extras added")
        if lining:
            print("Lining Paper: Yes")
        elif lining_entry.get() != "":
            print("Custom Lining Paper amount: {}".format(lining_entry.get()) + " rolls")
        else:
            print("No lining paper")
        if paste:
            print("Paste: Yes")
        elif paste_entry.get() != "":
            print("Custom Paste amount: {}".format(paste_entry.get()) + " tubs")
        else:
            print("No paste")
        print("Total Cost: £{:.2f}".format(cost))
        print("Total Area: {}m".format(total_area))
        print("Rolls Needed: {}".format(rolls_needed))
        print("___________Total Cost___________")
        print("Total Cost: £{:.2f}".format(cost))
        # Create the text file with the order details and save it to the current directory
        if platform.system() == 'Windows':
            with open("receipt.txt", "w") as file:
                file.write("Order has been placed")
                file.write("\n\n___________Customer Details___________")
                file.write("\n\nCustomer Name: {}".format(Customer_name.get()))
                file.write("\nCustomer Address: {}".format(Customer_address.get()))
                file.write("\nCustomer Phone Number: {}".format(Customer_phone.get()))
                file.write("\nCustomer Email: {}".format(Customer_email.get()))
                file.write("\n\n___________Order Details___________")
                file.write("\nAmount: {}".format(amount) + "m")
                file.write("\nTotal Area: {:.2f}m".format(round(total_area, 2)))
                file.write("\nRolls Needed: {}".format(rolls_needed))
                file.write("\nPaper Type: {}".format(paper_type))
                file.write("\nColour: {}".format(colour))
                if foil:
                    file.write("\nExtra: Foil")
                elif glitter:
                    file.write("\nExtra: Glitter")
                elif embossing:
                    file.write("\nExtra: Embossing")
                else:
                    file.write("\nNo extras added")
                if lining:
                    file.write("\nLining Paper: Yes")
                elif lining_entry.get() != "":
                    file.write("\nCustom Lining Paper amount: {}".format(lining_entry.get()) + " rolls")
                else:
                    file.write("\nNo lining paper")
                if paste:
                    file.write("\nPaste: Yes")
                elif paste_entry.get() != "":
                    file.write("\nCustom Paste amount: {}".format(paste_entry.get()) + " tubs")
                else:
                    file.write("\nNo paste")
                file.write("\n\n___________Other details___________")
                file.write("\nOrder Number: {}".format(order_number))
                file.write("\nEmployee ID: {}".format(username))
                file.write("\n\n___________Total Cost___________")
                file.write("\nTotal Cost: £{:.2f}".format(cost))
            os.startfile('receipt.txt')
        else:  # for mac and linux users (not tested)
            with open('receipt.txt', 'w') as file:
                file.write("Order has been placed")
                file.write("\n\n___________Customer Details___________")
                file.write("\n\nCustomer Name: {}".format(Customer_name.get()))
                file.write("\nCustomer Address: {}".format(Customer_address.get()))
                file.write("\nCustomer Phone Number: {}".format(Customer_phone.get()))
                file.write("\nCustomer Email: {}".format(Customer_email.get()))
                file.write("\n\n___________Order Details___________")
                file.write("\nAmount: {}".format(amount) + "m")
                file.write("\nTotal Area: {:.2f}m".format(round(total_area, 2)))
                file.write("\nRolls Needed: {}".format(rolls_needed))
                file.write("\nPaper Type: {}".format(paper_type))
                file.write("\nColour: {}".format(colour))
                if foil:
                    file.write("\nExtra: Foil")
                elif glitter:
                    file.write("\nExtra: Glitter")
                elif embossing:
                    file.write("\nExtra: Embossing")
                else:
                    file.write("\nNo extras added")
                if lining:
                    file.write("\nLining Paper: Yes")
                elif lining_entry.get() != "":
                    file.write("\nCustom Lining Paper amount: {}".format(lining_entry.get()) + " rolls")
                else:
                    file.write("\nNo lining paper")
                if paste:
                    file.write("\nPaste: Yes")
                elif paste_entry.get() != "":
                    file.write("\nCustom Paste amount: {}".format(paste_entry.get()) + " tubs")
                else:
                    file.write("\nNo paste")
                file.write("\n\n___________Other details___________")
                file.write("\nOrder Number: {}".format(order_number))
                file.write("\nEmployee ID: {}".format(username))
                file.write("\n\n___________Total Cost___________")
                file.write("\nTotal Cost: £{:.2f}".format(cost))
            subprocess.call(['open', 'receipt.txt'])

    # delete the text file when the window is closed (if it exists)
    def on_closing():
        if os.path.exists("receipt.txt"):
            os.remove("receipt.txt")
        root.destroy()

    # show assistance message
    def assistance():
        messagebox.showinfo(title="Assistance", message="Please contact us on 01234 567890 or email us at "
                                                        "Custompaper@paperpaper.com")

    # clear all the entries and reset the variables
    def clear():
        global cost
        cost = 0.0
        amount_entry.delete(0, END)
        amount_entry.insert(END, "0.00")
        d2.set("Choose wallpaper")
        var4.set(False)  # Lining
        var5.set(False)  # Paste
        lining_entry.delete(0, END)
        lining_entry.insert(END, "0.00")
        paste_entry.delete(0, END)
        paste_entry.insert(END, "0.00")
        radio_var.set(0)
        d1.set("Choose colour")

    # change colour of wallpaper and text to selected colour
    def change_color(event):
        # Get the selected color from the dropdown menu
        selected_color = d1.get()
        # Update the background color of the label
        t3.config(background=selected_color, foreground="black")
        # Update the fill color of each wallpaper colour
        for p1 in standard_wallpaper:
            main_window_canvas.itemconfig(p1, fill=selected_color)
        for r4 in premium_wallpaper_r4:
            main_window_canvas.itemconfig(r4, fill=selected_color, outline=selected_color)
        for r5 in premium_wallpaper_r5:
            main_window_canvas.itemconfig(r5, outline=selected_color)

    # change the text to nothing when clicked
    def temp_text(e):
        if lining_entry.get() == "0.00":
            lining_entry.delete(0, "end")
        if not validate_float(lining_entry.get()):
            lining_entry.delete(0, "end")

    # change the text to 0.00 when deselctected
    def reset_text(e):
        if lining_entry.get() == "":
            lining_entry.insert(0, "0.00")

    def temp_text2(e):
        if paste_entry.get() == "0.00":
            paste_entry.delete(0, "end")
        if not validate_float(paste_entry.get()):
            paste_entry.delete(0, "end")

    def reset_text2(e):
        if paste_entry.get() == "":
            paste_entry.insert(0, "0.00")

    def temp_text3(e):
        if amount_entry.get() == "0.00":
            amount_entry.delete(0, "end")
        if not validate_float(amount_entry.get()):
            amount_entry.delete(0, "end")

    def reset_text3(e):
        if amount_entry.get() == "":
            amount_entry.insert(0, "0.00")

    # check if the entry is a float
    def validate_float(entry):
        if entry == "" or entry == "0.00":
            return True
        try:
            float(entry)
            return True
        except ValueError:
            return False

    # disable entry for custom number if paste and lining paper are ticked
    def disable_entry():
        if var4.get() == 1:
            lining_entry.config(state='disabled')
        else:
            lining_entry.config(state='normal')
        if var5.get() == 1:
            paste_entry.config(state='disabled')
        else:
            paste_entry.config(state='normal')

    # Create a new tk variable to hold the state of the radio buttons
    radio_var = IntVar()
    var4 = BooleanVar(value=False)  # Lining paper
    var5 = BooleanVar(value=False)  # Paste
    var6 = BooleanVar(value=False)  # check if txt is open

    # Create new tk checkbutton widgets and set their options
    rb1 = tkinter.ttk.Radiobutton(root, text="Foil: 12p per m", variable=radio_var, value=1)
    rb1.place(x=100, y=200)

    rb2 = tkinter.ttk.Radiobutton(root, text="Glitter: 18p per m", variable=radio_var, value=2)
    rb2.place(x=100, y=230)

    rb3 = tkinter.ttk.Radiobutton(root, text="Embossing: 6p per m", variable=radio_var, value=3)
    rb3.place(x=100, y=260)

    rb4 = tkinter.ttk.Radiobutton(root, text="Deselect", variable=radio_var, value=4)
    rb4.place(x=100, y=290)

    cb4 = tkinter.ttk.Checkbutton(root, variable=var4, command=disable_entry)
    cb4.place(x=637, y=660)

    cb5 = tkinter.ttk.Checkbutton(root, variable=var5, command=disable_entry)
    cb5.place(x=637, y=690)

    # text for drop down menu colour selection
    t2 = tkinter.ttk.Label(root, text="Choose a colour:")
    t2.pack()
    t2.place(x=150, y=130)
    t3 = tkinter.ttk.Label(root, text="___________colour___________")
    t3.pack()
    t3.place(x=130, y=175)

    # Create a new tk dropdown menu widget and set its options
    d1 = StringVar(root)  # Create a StringVar object
    # Set the default value of the StringVar object
    d1.set("colour")
    # the actual dropdown menu
    dd1 = tkinter.ttk.Combobox(root, state="readonly", textvariable=d1,
                               values=["Purple", "DarkSlateGray4", "DeepSkyBlue", "LightSeaGreen", "VioletRed2",
                                       "Gold"])
    # Pack the dropdown menu
    dd1.pack()
    # Set the font of the dropdown menu
    dd1.config(font=('Helvetica bold', 12))
    # Set the position of the dropdown menu on the canvas
    dd1.place(x=100, y=150)
    # Bind the change_color function to the <<ComboboxSelected>> event of the dropdown menu
    dd1.bind('<<ComboboxSelected>>', change_color)

    # Create the labels and entry boxes for wallpaper amount, paper type, extras, lining paper, and paste
    l1 = tkinter.ttk.Label(root, text="Amount of wallpaper in meters (each roll is 10.05m):")
    l1.place(x=375, y=630)
    amount_entry: float = tkinter.ttk.Entry(root)
    amount_entry.insert(0, "0.00")
    amount_entry.bind("<FocusIn>", temp_text3)
    amount_entry.bind("<FocusOut>", reset_text3)
    amount_entry.config(validate="key", validatecommand=(root.register(validate_float), '%P'))
    amount_entry.place(x=660, y=630)

    l2 = tkinter.ttk.Label(root, text='Amount of Lining Paper (m) click button to match to wallpaper amount:')
    l2.place(x=245, y=660)
    lining_entry = tkinter.ttk.Entry(root)
    lining_entry.insert(0, "0.00")
    lining_entry.bind("<FocusIn>", temp_text)
    lining_entry.bind("<FocusOut>", reset_text)
    lining_entry.config(validate="key", validatecommand=(root.register(validate_float), '%P'))
    lining_entry.place(x=660, y=660)

    l3 = tkinter.ttk.Label(root, text='Amount of Paste (in kg) click button to match to wallpaper amount:')
    l3.place(x=265, y=690)
    paste_entry = tkinter.ttk.Entry(root)
    paste_entry.insert(0, "0.00")
    paste_entry.bind("<FocusIn>", temp_text2)
    paste_entry.bind("<FocusOut>", reset_text2)
    paste_entry.config(validate="key", validatecommand=(root.register(validate_float), '%P'))
    paste_entry.place(x=660, y=690)

    # Create a new tk button widget and set its options
    b1 = tkinter.ttk.Button(root, text="Place order", command=place_order)

    b1.pack()
    # set the position of the button on the canvas
    b1.place(x=950, y=660)

    # Create the button to ask for assistance
    b2 = tkinter.ttk.Button(root, text="Need assistance?", command=assistance)
    b2.place(x=840, y=660)

    b5 = tkinter.ttk.Button(root, text="Clear", command=clear)
    b5.place(x=950, y=690)

    def add_to_basket():
        messagebox.showerror(title="Work in progress", message="This part of the program for time constraint reasons is"
                                                               "not implemented yet.")

    b6 = tkinter.ttk.Button(root, text="Add to Basket", command=add_to_basket, style="TButton")
    b6.place(x=840, y=690)

    def logout(): # Function to logout of the program (buggy)
        root.attributes('-alpha', 0)  # Hide the root window until the login window is closed
        login_window.deiconify()  # Show the login window

    b7 = tkinter.ttk.Button(root, text="Logout", command=logout)
    b7.place(x=100, y=690)

    # All shapes and text for UI design
    r1 = main_window_canvas.create_rectangle(80, 120, 380, 400, outline="black", width=5, fill="#c0c0c0")
    t1 = main_window_canvas.create_text((350, 50), text="Wallpaper Customizer", fill='white',
                                        font=('Helvetica bold', 36))
    r2 = main_window_canvas.create_rectangle(80, 620, 1080, 1070, outline="black", width=5, fill="#c0c0c0")
    r3 = main_window_canvas.create_rectangle(620, 80, 1080, 530, outline="black", width=8, fill="#c0c0c0")

    # display logged-in username on canvas
    username = entry_username.get()
    t4 = main_window_canvas.create_text((530, 100), text="USER: " + username, fill='white', font=('Helvetica bold', 12))

    Platform = platform.system()
    t5 = main_window_canvas.create_text((530, 120), text="Platform: " + Platform, fill='white',
                                        font=('Helvetica bold', 12))

    time = date.today()
    t6 = main_window_canvas.create_text((530, 140), text="Date: " + str(time), fill='white',
                                        font=('Helvetica bold', 12))

    # t9 = canvas.create_text(530, 160, text="Wallpaper cost: £{:.2f}".format(cost), fill='white',font=('Helvetica bold', 12))
    # standard wallpaper design
    # standard wallpaper design cords
    x1, y1 = 400, 300
    x2, y2 = 800, 300
    x3, y3 = 700, 150
    x4, y4 = 500, 150
    # Create wallpaper 1 using create_polygon
    standard_wallpaper = []
    for i in range(4):
        for j in range(10):
            # Create the trapezoid using the create_polygon method
            p1 = main_window_canvas.create_polygon(x1, y1, x2, y2, x3, y3, x4, y4, fill="purple", outline='black',
                                                   width=3)

            # Scale down the trapezoids to make them smaller
            main_window_canvas.scale(p1, 0, 0, 0.25, 0.25)

            # Move the trapezoids to the right position
            main_window_canvas.move(p1, 585 + i * 80, 70 + j * 37)
            # Add the trapezoid to the list of trapezoids
            standard_wallpaper.append(p1)

    # premium wallpaper design
    # Create wallpaper 2 using create_rectangle

    # Create two separate lists for premium_wallpaper_r4 and premium_wallpaper_r5
    premium_wallpaper_r4 = []
    premium_wallpaper_r5 = []

    # premium wallpaper cords
    x1, y1 = 50, 50
    x2, y2 = 100, 100
    x3, y3 = 50, 50
    x4, y4 = 100, 100
    # Loop to create 9 rectangles diagonally connected to the bottom right
    for a in range(9):
        if a % 2 == 0:  # Check if the index is even
            fill_color = "purple"
        else:
            fill_color = ""  # Transparent fill color
        # Create the rectangle with the modified coordinates and fill color
        r4 = main_window_canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="", width=3)
        main_window_canvas.move(r4, 390, 20)
        main_window_canvas.scale(r4, 0, 0, 1.5, 1.5)
        # Increase the coordinates for the next rectangle
        x1 += 25
        x2 += 25
        y1 += 25
        y2 += 25

        premium_wallpaper_r4.append(r4)

        # Loop to create 9 rectangles diagonally connected to the bottom left
        r4 = main_window_canvas.create_rectangle(x3, y3, x4, y4, fill=fill_color, outline="purple", width=3)
        main_window_canvas.move(r4, 590, 20)
        main_window_canvas.scale(r4, 0, 0, 1.5, 1.5)
        # Increase the coordinates for the next rectangle
        x3 -= 25
        x4 -= 25
        y3 += 25
        y4 += 25

        premium_wallpaper_r4.append(r4)

    x1, y1 = 50, 50
    x2, y2 = 100, 100
    x3, y3 = 50, 50
    x4, y4 = 100, 100

    for b in range(9):
        if b % 2 == 0:  # Check if the index is even
            fill_color = ""
        else:
            fill_color = "white"  # Transparent fill color

        # Create the rectangle with the modified coordinates and fill color
        r5 = main_window_canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline="purple", width=3)
        main_window_canvas.move(r5, 390, 20)
        main_window_canvas.scale(r5, 0, 0, 1.5, 1.5)

        # Increase the coordinates for the next rectangle
        x1 += 25
        x2 += 25
        y1 += 25
        y2 += 25

        premium_wallpaper_r5.append(r5)

        # Loop to create 9 rectangles diagonally connected to the bottom left
        r5 = main_window_canvas.create_rectangle(x3, y3, x4, y4, fill=fill_color, outline="purple", width=3)
        main_window_canvas.move(r5, 590, 20)
        main_window_canvas.scale(r5, 0, 0, 1.5, 1.5)
        # Increase the coordinates for the next rectangle
        x3 -= 25
        x4 -= 25
        y3 += 25
        y4 += 25
        premium_wallpaper_r5.append(r5)

        # done for hierarchy reasons

        r5 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="white", outline="purple", width=3)
        main_window_canvas.move(r5, 930, 490)
        main_window_canvas.scale(r5, 0, 0, 0.75, 0.75)
        premium_wallpaper_r5.append(r5)

        r5 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="white", outline="purple", width=3)
        main_window_canvas.move(r5, 1230, 490)
        main_window_canvas.scale(r5, 0, 0, 0.75, 0.75)
        premium_wallpaper_r5.append(r5)

        # outer colour changing squares for wallpaper 2
        r4 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="purple", outline="purple", width=3)
        main_window_canvas.move(r4, 980, 240)
        main_window_canvas.scale(r4, 0, 0, 0.75, 0.75)
        premium_wallpaper_r4.append(r4)

        r4 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="purple", outline="purple", width=3)
        main_window_canvas.move(r4, 1180, 240)
        main_window_canvas.scale(r4, 0, 0, 0.75, 0.75)
        premium_wallpaper_r4.append(r4)

        r4 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="purple", outline="purple", width=3)
        main_window_canvas.move(r4, 980, 440)
        main_window_canvas.scale(r4, 0, 0, 0.75, 0.75)
        premium_wallpaper_r4.append(r4)

        r4 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="purple", outline="purple", width=3)
        main_window_canvas.move(r4, 1180, 440)
        main_window_canvas.scale(r4, 0, 0, 0.75, 0.75)
        premium_wallpaper_r4.append(r4)

        # middle white square

        r5 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="white", outline="purple", width=3)
        main_window_canvas.move(r5, 1030, 290)
        main_window_canvas.scale(r5, 0, 0, 0.75, 0.75)
        premium_wallpaper_r5.append(r5)

        r5 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="white", outline="purple", width=3)
        main_window_canvas.move(r5, 1130, 290)
        main_window_canvas.scale(r5, 0, 0, 0.75, 0.75)
        premium_wallpaper_r5.append(r5)

        r5 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="white", outline="purple", width=3)
        main_window_canvas.move(r5, 1030, 390)
        main_window_canvas.scale(r5, 0, 0, 0.75, 0.75)
        premium_wallpaper_r5.append(r5)

        r5 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="white", outline="purple", width=3)
        main_window_canvas.move(r5, 1130, 390)
        main_window_canvas.scale(r5, 0, 0, 0.75, 0.75)
        premium_wallpaper_r5.append(r5)

        # colour changing Square in the center of wallpaper 2
        r4 = main_window_canvas.create_rectangle(0, 0, 100, 100, fill="purple", outline="purple", width=3)
        main_window_canvas.move(r4, 1080, 340)
        main_window_canvas.scale(r4, 0, 0, 0.75, 0.75)
        premium_wallpaper_r4.append(r4)

    # Define a function to toggle the state of wallpapers
    def chosen_wallpaper(event):
        wallpaper_choice = d2.get()
        if wallpaper_choice == "Standard wallpaper":
            state = main_window_canvas.itemcget(standard_wallpaper[0], "state")
            if state == "normal":
                state = "hidden"
            else:
                state = "normal"
            for p1 in standard_wallpaper:
                main_window_canvas.itemconfigure(p1, state=state)

            # Hide the Choice 2 wallpaper
            for r4 in premium_wallpaper_r4:
                main_window_canvas.itemconfigure(r4, state="hidden")
            for r5 in premium_wallpaper_r5:
                main_window_canvas.itemconfigure(r5, state="hidden")

        elif wallpaper_choice == "Premium wallpaper":
            state = main_window_canvas.itemcget(premium_wallpaper_r4[0], "state")
            if state == "normal":
                state = "hidden"
            else:
                state = "normal"
            for r4 in premium_wallpaper_r4:
                main_window_canvas.itemconfigure(r4, state=state)
            for r5 in premium_wallpaper_r5:
                main_window_canvas.itemconfigure(r5, state=state)

            # Hide the Choice 1 wallpaper
            for p1 in standard_wallpaper:
                main_window_canvas.itemconfigure(p1, state="hidden")

    # Set initial state to hidden for both wallpapers
    for p1 in standard_wallpaper:
        main_window_canvas.itemconfigure(p1, state="hidden")
    for r4 in premium_wallpaper_r4:
        main_window_canvas.itemconfigure(r4, state="hidden")
    for r5 in premium_wallpaper_r5:
        main_window_canvas.itemconfigure(r5, state="hidden")

        # Create a combobox (dropdown menu) to toggle which wallpaper is shown
        d2 = StringVar(root)
        d2.set("Choose wallpaper")
        dd2 = combobox = tkinter.ttk.Combobox(root, textvariable=d2, state="readonly",
                                              values=["Premium wallpaper", "Standard wallpaper"])
        dd2.config(font=("Helvetica bold", 12))
        dd2.pack()
        combobox.pack()
        combobox.bind("<<ComboboxSelected>>", chosen_wallpaper)
        combobox.place(x=640, y=500)

    # to delete text file from system
    root.protocol("WM_DELETE_WINDOW", on_closing)
    # Run the main event loop
    # Start the main event loop to display the window
    root.mainloop()


# run the Login window's main loop
login_window.mainloop()
