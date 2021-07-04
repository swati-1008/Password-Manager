from tkinter import *
from tkinter import messagebox      # messagebox is not a class, so is not imported when * was imported from tkinter
import random
import pyperclip

WHITE = "#fff"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.append([random.choice(letters) for _ in range(random.randint(8, 10))])
    password_list.append([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.append([random.choice(numbers) for _ in range(random.randint(2, 4))])

    password_list = [''.join(i) for i in password_list]

    random.shuffle(password_list)

    password = "".join(password_list)

    entry3.insert(0, password)

    pyperclip.copy(password)        # Copy the generated password to clipboard, so that it can be pasted directly to the website

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_to_file():
    website_text = entry1.get()
    email_text = entry2.get()
    password_text = entry3.get()

    # messagebox.showinfo(title = "Title", message = "Message")       # Gives a dialogbox with 'Message' as the message and an OK button

    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title = "Oops!", message = "Fields cannot be left empty")
    else:
        is_ok = messagebox.askokcancel(title = website_text, message = f"These are the details entered: \nEmail: {email_text} \nPassword: {password_text} \nIs it okay to save?")
        
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f'{website_text} | {email_text} | {password_text} \n')
                entry1.delete(0, END)
                entry3.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50, bg = WHITE, highlightthickness = 0)

canvas = Canvas(width = 200, height = 200, bg = WHITE, highlightthickness = 0)
lock_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = lock_img)
canvas.grid(row = 0, column = 1)

website = Label(text = "Website:", bg = WHITE)
website.config(padx = 5, pady = 5)
website.grid(row = 1, column = 0)

entry1 = Entry(width = 38)
entry1.focus()      # Cursor on first entry box when the application launches
entry1.grid(row = 1, column = 1, columnspan = 2)

email_username = Label(text = "Email/Username:", bg = WHITE, highlightthickness = 0)
email_username.config(padx = 5, pady = 5)
email_username.grid(row = 2, column = 0)

entry2 = Entry(width = 38)
entry2.insert(0, "swati100897@gmail.com")       # Mostly we use 1 email on all websites, so pre-populated
entry2.grid(row = 2, column = 1, columnspan = 2)

password = Label(text = "Password:", bg = WHITE, highlightthickness = 0)
password.config(padx = 5, pady = 5)
password.grid(row = 3, column = 0)

entry3 = Entry(width = 21)
entry3.grid(row = 3, column = 1, columnspan = 1)

generate_password = Button(text = "Generate Password", bg = WHITE, highlightthickness = 0, command = generate_password)
generate_password.config(padx = 5, pady = 5)
generate_password.grid(row = 3, column = 2, columnspan = 1)

add = Button(text = "Add", width = 40, bg = WHITE, highlightthickness = 0, command = save_to_file)
add.config(padx = 5, pady = 5)
add.grid(row = 4, column = 1, columnspan = 2)

window.mainloop()