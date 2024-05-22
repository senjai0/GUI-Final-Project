from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os.path 

registered_users = {}

def resize_image(event, label, original_image):
    new_width = event.width
    new_height = event.height
    resized_image = original_image.resize((new_width, new_height))
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    label.config(image=resized_image_tk)
    label.image = resized_image_tk 

def create_registration_form(root):
    global email_entry, password_entry

    root.destroy()

    def register_user():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        confirm_password = confirm_password_entry.get()
        terms_checked = terms_var.get()

        if not all((first_name, last_name, email, password, confirm_password)):
            messagebox.showerror("Error", "Please fill in all fields.")
        elif not email or "@" not in email or "." not in email:
            messagebox.showerror("Error", "Invalid email format. Please enter a valid email address.")
        elif not first_name or not last_name:
            messagebox.showerror("Error", "First name and last name are required.")
        elif any(char.isdigit() for char in first_name) or any(char.isdigit() for char in last_name):
            messagebox.showerror("Error", "First name and last name cannot contain numbers.")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
        elif not terms_checked:
            messagebox.showerror("Error", "Please accept the terms & conditions.")
        else:
            registered_users[email] = password 
            messagebox.showinfo("Success", "Registration successful!")
            registration_window.destroy()
            create_login_form()
    
    def go_back():
        registration_window.destroy()
        create_options_screen()

    registration_window = Tk()
    registration_window.title("Registration Form")
    registration_window.geometry("600x570")
    registration_window.configure(bg="white")
    registration_window.resizable(True, True)

    Label(registration_window, text="SIGN UP", font=("Arial", 22), bg="white").pack(pady=50)

    original_image = Image.open("Girl.jpg") if os.path.isfile("Girl.jpg") else Image.new("RGB", (600, 570), "white")
    resized_image = original_image.copy()
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    my_hai = Label(registration_window, image=resized_image_tk)
    my_hai.pack(fill=BOTH, expand=YES)
    my_hai.bind("<Configure>", lambda event: resize_image(event, my_hai, original_image))

    Label(registration_window, text="First Name:", font=20, bg="white").place(x=20, y=150)
    first_name_entry = Entry(registration_window, width=15, bd=1.5, font=15)
    first_name_entry.place(x=120, y=150)

    Label(registration_window, text="Last Name:",font=20, bg="white").place(x=280, y=150)
    last_name_entry = Entry(registration_window, width=15, bd=1.5, font=15)
    last_name_entry.place(x=390, y=150)

    Label(registration_window, text="Email:", font=20, bg="white").place(x=70, y=200)
    email_entry = Entry(registration_window, width=30, bd=1.5, font=15)
    email_entry.place(x=175, y=200)

    Label(registration_window, text="Password:", font=20, bg="white").place(x=70, y=250)
    password_entry = Entry(registration_window,  width=30, bd=1.5, font=15, show="•")
    password_entry.place(x=175, y=250)

    Label(registration_window, text="C-Password:", font=20, bg="white").place(x=70, y=300)
    confirm_password_entry = Entry(registration_window,  width=30, bd=1.5, font=15, show="•")
    confirm_password_entry.place(x=175, y=300)

    terms_var = BooleanVar()
    Checkbutton(registration_window, text="I accept the terms & conditions", variable=terms_var, bg="white").place(x=170, y=330)

    Button(registration_window, text="Register", font=20, bg="white", fg="black", width=11, height=2, command=register_user).place(x=320, y=380)
    Button(registration_window, text="Back", font=20, bg="white", fg="black", width=11, height=2, command=go_back).place(x=180, y=380)

    registration_window.mainloop()

def create_login_form():
    global email_entry, password_entry
    
    def login_user():
        email = email_entry.get()
        password = password_entry.get()

        if email in registered_users and registered_users[email] == password:
            messagebox.showinfo("Success", "Login successful!")
            login_window.destroy() 
            create_user_window()    
        else:
            messagebox.showerror("Error", "No account found with provided credentials.")
    
    def go_back():
        login_window.destroy()
        create_options_screen()

    login_window = Tk()
    login_window.title("Login Form")
    login_window.geometry("600x570")
    login_window.configure(bg="Black")
    login_window.resizable(True, True)

    Label(login_window, text="LOGIN", font=("Arial", 30), bg="Black", fg="White").pack(pady=50)

    original_image = Image.open("Otap.jpeg") if os.path.isfile("Otap.jpeg") else Image.new("RGB", (600, 570), "white")
    resized_image = original_image.copy()
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    my_hai = Label(login_window, image=resized_image_tk)
    my_hai.pack(fill=BOTH, expand=YES)
    my_hai.bind("<Configure>", lambda event: resize_image(event, my_hai, original_image))

    Label(login_window, text="Email:", font= 22, bg="Black", fg="White").place(x=80, y=150)
    email_entry = Entry(login_window, width=28, bd=1.5, font=15)
    email_entry.place(x=175, y=150)

    Label(login_window, text="Password:", font= 22, bg="Black", fg="White").place(x=80, y=200)
    password_entry = Entry(login_window, width= 28, bd=1.5,font=15, show="*")
    password_entry.place(x=175, y=200)

    Button(login_window, text="LOGIN", font=20, bg="Black", fg="white", width=11, height=2, command=login_user).place(x=320, y=250)
    Button(login_window, text="BACK", font=20, bg="Black", fg="white", width=11, height=2, command=go_back).place(x=180, y=250)

    login_window.mainloop()

def create_profile_window():
    profile_window = Toplevel()
    profile_window.title("My Profile")
    profile_window.geometry("920x600")
    profile_window.configure(bg="black")
    profile_window.resizable(False, False)


    ech = ImageTk.PhotoImage(Image.open("jay.jpg"))
    ech1 = Label(profile_window, image=ech, height=150, width=200)
    ech1.place(x=350, y=50)

    Label(profile_window, text="PROFILE",font="arial 15", fg="white", bg="black").place(x=400 ,y=20 )
    Label(profile_window, text="Name: Chinjay D. Arbois",font="arial 11", fg="white", bg="black").place(x=350 ,y=240 )
    Label(profile_window, text="Email: ********chi@gmail.com", font="arial 11",fg="white", bg="black").place(x=350 ,y=280 )
    Label(profile_window, text="Number:   09642863674",font="arial 11",fg="White",bg="black").place(x=350, y=320)
    Label(profile_window, text="Gender: Male",font="arial 11",fg="White",bg="black").place(x=350, y=360)
    Label(profile_window, text="Country: United States ",font="arial 11",fg="White",bg="black").place(x=350, y=400)
    Label(profile_window, text="'A language that doesn’t affect the way you think about programming is not worth knowing.- Alan Perlis '",font="arial 13",fg="White",bg="black").place(x=80, y=500)

def logout():
    global email_entry, password_entry

    logout_window = Tk()
    logout_window.title("Login Form")
    logout_window.geometry("920x600")
    logout_window.configure(bg="Black")

    Label(logout_window, text="LOGIN", font=("Arial", 30), bg="Black", fg="White").pack(pady=50)

    Label(logout_window, text="Email:", font= 22, bg="Black", fg="White").place(x=250, y=150)
    email_entry = Entry(logout_window, width=28, bd=1.5, font=15)
    email_entry.place(x=330, y=150) 

    Label(logout_window, text="Password:", font= 22, bg="Black", fg="White").place(x=250, y=200)
    password_entry = Entry(logout_window, width= 28, bd=1.5,font=15, show="*")
    password_entry.place(x=330, y=200)

    Button(logout_window, text="LOGIN", font=20, bg="Black", fg="white", width=11, height=2).place(x=480, y=250)
    Button(logout_window, text="BACK", font=20, bg="Black", fg="white", width=11, height=2, command=create_options_screen).place(x=320, y=250)

    logout_window.mainloop()

    
def create_user_window():

    def show_anime_window(anime):
        anime_window = Tk()
        anime_window.title(anime)
        anime_label = Label(anime_window, text=anime, font="Arial 20")
        anime_label.pack(pady=20)
        anime_window.mainloop()

    def search_anime():
        query = search_entry.get()
        if query in ["AOT", "Attack on Titan"]:
            show_anime_window("Attack on Titan")
        elif query in ["Haikyuu", "Haikyu"]:
            show_anime_window("Haikyuu")
        elif query == "Slayer":
            show_anime_window("Demon Slayer")
        elif query == "Your Name":
            show_anime_window("Your Name")
        elif query in ["Detective Conan", "Conan"]:
            show_anime_window("Detective Conan")
        elif query == "Naruto":
            show_anime_window("Naruto Shippuden")
        elif query == "One Piece":
            show_anime_window("One Piece")
        elif query == "Black Clover":
            show_anime_window("Black Clover")
        elif query == "Chainsaw Man":
            show_anime_window("Chainsaw Man")
        else:
            messagebox.showerror("Error", "Anime not found.")

    user_window = Tk()
    user_window.title("Movies")
    user_window.geometry("920x600")
    user_window.configure(bg="black")

    frame = Frame(user_window, bg="black")
    frame.pack(fill=BOTH, expand=YES)

    canvas = Canvas(frame, bg="black")
    canvas.pack(side=LEFT, fill=BOTH, expand=YES)

    scrollbar = Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(int(-1*(event.delta/120)), "units"))

    content_frame = Frame(canvas, bg="black")
    canvas.create_window((0, 0), window=content_frame, anchor=NW)

    search_entry = Entry(user_window, width=20, bd=1.5, font=12)
    search_entry.place(x=380, y=30)

    Label(user_window, text="ANIME", font="Broadway 25", fg="White", bg="black").place(x=11, y=10)

    search_button = Button(user_window, text="Search", font=12, bg="black", fg="white", command=search_anime, width=6, height=1)
    search_button.place(x=580, y=28)

    Button(user_window, text="Profile", font=5, bg="black", fg="White", command=create_profile_window, width=5, height=1).place(x=830, y=10)
    Button(user_window, text="Logout", font=5, bg="black", fg="White",command=logout, width=5, height=1).place(x=830, y=40)

    Label(user_window, text="Search:", font="arial 12", fg="White", bg="black").place(x=300, y=30)

    AOT = ImageTk.PhotoImage(Image.open("AOT1.jpg"))
    AOT1 = Label(user_window, image=AOT, height=150, width=200)
    AOT1.place(x=50, y=140)

    chain = ImageTk.PhotoImage(Image.open("Chain.jpeg"))
    chain1 = Label(user_window, image=chain, height=150, width=200)
    chain1.place(x=350, y=140)

    haik = ImageTk.PhotoImage(Image.open("haiky.jpg"))
    haik1 = Label(user_window, image=haik, height=150, width=200)
    haik1.place(x=50, y=360)

    one = ImageTk.PhotoImage(Image.open("onepiece1.jpg"))
    one1 = Label(user_window, image=one, height=150, width=200)
    one1.place(x=350, y=360)
    
    nar = ImageTk.PhotoImage(Image.open("naruto.jpeg"))
    nar1 = Label(user_window, image=nar, height=150, width=200)
    nar1.place(x=650, y=140)

    clo = ImageTk.PhotoImage(Image.open("clover.jpg"))
    clo1 = Label(user_window, image=clo, height=150, width=200)
    clo1.place(x=650, y=360)

    nam = ImageTk.PhotoImage(Image.open("name.jpeg"))
    nam1 = Label(user_window, image=nam, height=150, width=200)
    nam1.place(x=650, y=570)

    sla = ImageTk.PhotoImage(Image.open("slay.jpeg"))
    sla1 = Label(user_window, image=sla, height=150, width=200)
    sla1.place(x=50, y=570)

    con = ImageTk.PhotoImage(Image.open("conan.jpeg"))
    con1 = Label(user_window, image=con, height=150, width=200)
    con1.place(x=350, y=570)


    Label(user_window, text="Attach on Titan",font="arial 12",fg="White",bg="black").place(x=50, y=300)

    Label(user_window, text="Chainsaw Man", font="arial 12",fg="White", bg="black").place(x=350, y=300)

    Label(user_window, text="Naruto: Shippuden", font="arial 12",fg="White", bg="black").place(x=650, y=300)

    Label(user_window, text="Haikyuu", font="arial 12",fg="White",bg="black").place(x=50, y=515)

    Label(user_window, text="One Piece", font="arial 12", fg="White", bg="black").place(x=350, y=515)

    Label(user_window, text="Black Clover", font="arial 12", fg="White", bg="black").place(x=650, y=515)

    Label(user_window, text="Demon Slayer", font="arial 12", fg="White", bg="black").place(x=50, y=585)

    Label(user_window, text="Detective Conan", font="arial 12", fg="White", bg="black").place(x=350, y=585)

    Label(user_window, text="Your Name", font="arial 12", fg="White", bg="black").place(x=650, y=585)
    
    user_window.mainloop()


def create_options_screen():
    global root
    
    try:
        root.destroy()
    except:
        pass
    
    root = Tk()
    root.title("Registration and Login")
    root.geometry("600x570")
    root.configure(bg="white")
    root.resizable(True, True)

    Label(root, text="ANIME MOVIES", font="arial 25", bg="white").pack(pady=10)

    original_image = Image.open("haikyuu.jpeg") if os.path.isfile("haikyuu.jpeg") else Image.new("RGB", (600, 570), "white")
    resized_image = original_image.copy()
    resized_image_tk = ImageTk.PhotoImage(resized_image)
    my_hai = Label(root, image=resized_image_tk)
    my_hai.pack(fill=BOTH, expand=YES)
    my_hai.bind("<Configure>", lambda event: resize_image(event, my_hai, original_image))

    option = Label(root, text="Select options:", font=("arial 16"), bg="white")
    option.place(x=225, y=100)

    r = Button(root, text="Register Account", font=20, bg="white", fg ="black", width=15, height=2, command=lambda: create_registration_form(root))
    r.place(x=226, y=170)
    l = Button(root, text="Login ", font=20, bg="white", fg="black", width=15, height=2, command= create_login_form)
    l.place(x=226, y=240)

    root.mainloop()

create_options_screen()