from tkinter import *
from tkinter import messagebox


def clear_entries():
    age_entry.delete(0, 'end')
    height_entry.delete(0, 'end')
    weight_entry.delete(0, 'end')


def calculate_bmi():
    weight_kg = int(weight_entry.get())
    height_cm = int(height_entry.get())
    bmi = calculate_bmi_value(weight_kg, height_cm)
    bmi_category(bmi)


def calculate_bmi_value(weight, height):
    height_m = height / 100
    return round(weight / (height_m * height_m), 1)


def bmi_category(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'Your BMI is {bmi}: Underweight')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('BMI Calculator', f'Your BMI is {bmi}: Normal')
    elif 24.9 <= bmi < 29.9:
        messagebox.showinfo('BMI Calculator', f'Your BMI is {bmi}: Overweight')
    else:
        messagebox.showinfo('BMI Calculator', f'Your BMI is {bmi}: Obesity')


root = Tk()
root.title('BMI Calculator')
root.geometry('400x300')
root.config(bg='#686e70')

frame = Frame(root, padx=10, pady=10)
frame.pack(expand=True)

age_label = Label(frame, text="Enter Age (2 - 120)")
age_label.grid(row=1, column=1)

age_entry = Entry(frame)
age_entry.grid(row=1, column=2, pady=5)

gender_label = Label(frame, text='Select Gender')
gender_label.grid(row=2, column=1)

gender_var = StringVar()  # Variable to hold the selected gender

gender_frame = Frame(frame)
gender_frame.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(gender_frame, text='Male', variable=gender_var, value='Male')
male_rb.pack(side=LEFT)

female_rb = Radiobutton(gender_frame, text='Female', variable=gender_var, value='Female')
female_rb.pack(side=RIGHT)

height_label = Label(frame, text="Enter Height (cm)")
height_label.grid(row=3, column=1)

weight_label = Label(frame, text="Enter Weight (kg)")
weight_label.grid(row=4, column=1)

height_entry = Entry(frame)
height_entry.grid(row=3, column=2, pady=5)

weight_entry = Entry(frame)
weight_entry.grid(row=4, column=2, pady=5)

button_frame = Frame(frame)
button_frame.grid(row=5, columnspan=3, pady=10)

calculate_button = Button(button_frame, text='Calculate', command=calculate_bmi)
calculate_button.pack(side=LEFT)

clear_button = Button(button_frame, text='Clear', command=clear_entries)
clear_button.pack(side=LEFT)

exit_button = Button(button_frame, text='Exit', command=root.destroy)
exit_button.pack(side=RIGHT)

root.mainloop()
