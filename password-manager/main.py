from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

#password_list = []

password_list = [random.choice(letters) for _ in range(nr_letters)]
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))

# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
password_list += [random.choice(symbols) for _ in range(nr_symbols)]

# for char in range(nr_numbers):
#   password_list += random.choice(numbers)

password_list += [random.choice(numbers) for _ in range(nr_numbers)]

random.shuffle(password_list)

password = "".join(password_list)

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = webiste_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any fields empty !")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                      f"\nPassword: {password} \nIs it ok to save ? ")

        if is_ok :
            with open("data.txt", "a") as data:
                data.write(f"{website} | {email} | {password} \n")
                webiste_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg='#FFFDF6')
canvas = Canvas(width=200, height=200, bg='#FFFDF6', highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo_img)
canvas.grid(row=0, column=1)

#Labels
website_labels = Label(text="Website:", bg='#FFFDF6')
website_labels.grid(row=1, column=0)

email_user_label = Label(text="Email/Username:", bg='#FFFDF6')
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg='#FFFDF6')
password_label.grid(row=3, column=0)

#Entry
webiste_entry = Entry(width=35, bg='#FFFDF6')
webiste_entry.grid(row=1, column=1, columnspan=2)
webiste_entry.focus()

email_user_entry = Entry(width=35, bg='#FFFDF6')
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_entry.insert(0, "fmdoums14@gmail.com")

password_entry = Entry(width=21, bg='#FFFDF6')
password_entry.grid(row=3, column=1)

#Btn
generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, command=save)
add_btn.grid(row=4, column=1, columnspan=2)



window.mainloop()