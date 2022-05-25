from tkinter import *

root = Tk()
root.geometry("1000x300")
Label(root, text="Python registration form" , font= 'ar 25 bold').grid(row=0, column=3)
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmethod = Label(root, text="Payment method")
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4 ,column=2)
paymentmethod.grid(row=5 ,column=2)

namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmethodvalue = StringVar

checkvalue = IntVar

nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmethodentry = Entry(root, textvariable=paymentmethodvalue)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymentmethodentry.grid(row=5,column=3)


root.mainloop()
