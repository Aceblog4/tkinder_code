from tkinter import Tk, Label, Button, Entry, StringVar, BooleanVar, Checkbutton, Radiobutton
import threading
from functools import partial

def print_hi():
    form = Tk()
    form.title("Formulaire")

    # Define label
    name_label = Label(form, text="Name : ", width=10, height=10)
    name_value = StringVar(form)
    name_input = Entry(form, textvariable=name_value)

    surname_label = Label(form, text="Surname : ", width=10, height=10)
    surname_value = StringVar(form)
    surname_input = Entry(form, textvariable=surname_value)

    accept_condition_value = BooleanVar(form, '0')
    accept_condition_label = Label(form, text="En cliquant sur ce button vous accepter les conditions")
    accept_condition = Checkbutton(form, variable=accept_condition_value)

    sex_label = Label(form, text="Sexe : ")
    sex_choice = ['M', 'F']
    sex_value = StringVar(form, 'M')

    submit = Button(form, text="Register", command=partial(submit_form,
                                                           form, name_value,
                                                           surname_value,
                                                           accept_condition_value), padx=2, pady=2)

    # Add label to screen
    name_label.grid(column=0, row=0)
    name_input.grid(column=1, row=0)

    surname_label.grid(column=0, row=1)
    surname_input.grid(column=1, row=1)

    accept_condition.grid(column=0, row=2)
    accept_condition_label.grid(column=1, row=2)

    sex_label.grid(column=0, row=3)

    for i, val in enumerate(sex_choice):
        sex_input = Radiobutton(form, variable=sex_value, value=val, text=val)
        sex_input.grid(column=1, row=i+3)

    submit.grid(column=1, row=5)

    form.mainloop()


def submit_form(root, name_val, surname_val, condition_val):
    message = Label(root, text="Vous avez soumis le formulaire", background="green", foreground="white")
    message.grid(column=1, row=6)

    save_info(name_val.get(), surname_val.get(), condition_val.get())
    # Remove message after 30 seconds.
    timer = threading.Timer(3, message.destroy)
    timer.start()


def save_info(name, surname, condition):
    print(name, surname, condition)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
