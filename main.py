import tkinter

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=300, height=160)

label1 = tkinter.Label(window, text="Enter Your Height(cm)",pady=5)
label1.pack()

height_entry = tkinter.Entry()
height_entry.pack()


label2 = tkinter.Label(window, text="Enter Your Weight (kg)",pady=5)
label2.pack()

weight_entry = tkinter.Entry()
weight_entry.pack()

def calculate():
    weight = float(weight_entry.get())
    height = float(height_entry.get())/100
    result= weight / (height**2)
    if result < 18.5:
        label3.config(text=f"Your BMI is {result} You are under weight")

    elif result >= 18.5 and result < 25:
        label3.config(text=f"Your BMI is {result} You are Normal")

    elif result >= 25 and result <=29.9:
        label3.config(text=f"Your BMI is {result} You are Over Weight")
    else:
        label3.config(text=f"Your BMI is {result} You are Obese")




button= tkinter.Button(window, text="Calculate", command=calculate)
button.pack(fill = 'y',padx = 10, pady = 10)

label3 = tkinter.Label(window, text="",pady=5)
label3.pack()




window.mainloop()