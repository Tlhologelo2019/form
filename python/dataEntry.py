import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Form")

frame = tkinter.Frame(root)
frame.pack()

#User information label frame

user_info = tkinter.LabelFrame(frame, text="User Information")
user_info.grid(row=0, column=0, padx=20, pady=20)

title_label = tkinter.Label(user_info, text="Title")
title_combobox = ttk.Combobox(user_info, values=["",  
                                                 "Mr.", 
                                                 "Mrs.", 
                                                 "Ms.", 
                                                 "Dr.", 
                                                 "Prof.", 
                                                 "Other"])
title_label.grid(row=0,  column=0)
title_combobox.grid(row=1, column=0)

userFname_label = tkinter.Label(user_info, text="First Name")
userFname_label.grid(row=0, column=1)
userLname_label = tkinter.Label(user_info, text="First Name")
userLname_label.grid(row=0, column=2)

userFname_entry = tkinter.Entry(user_info)
userFname_entry.grid(row=1, column=1)
userLname_entry = tkinter.Entry(user_info)
userLname_entry.grid(row=1, column=2)

dateOfbirth_label = tkinter.Label(user_info, text="Select your DOB: dd/mm/yyyy")
dateOfbirth_label.grid(row=2, column=0, columnspan=3)

day_spinbox = tkinter.Spinbox(user_info, from_= 1, to = 31)
day_spinbox.grid(row=3, column=0)

months = ("January", 
          "February", 
          "March", 
          "April", 
          "May", 
          "June", 
          "July",
          "August",
          "October",
          "November",
          "December")

month_combobox = ttk.Combobox(user_info, values=months)
month_combobox.grid(row=3, column=1) 

year_spinbox = tkinter.Spinbox(user_info, from_=1950 , to=2006)
year_spinbox.grid(row=3, column=2)

stateOrprovince_label = tkinter.Label(user_info, text="State/Province")
stateOrprovince_label.grid(row=4, column=0)

stateOrprovince = ("Limpopo", 
                   "Gauteng", 
                   "North West", 
                   "Eastern Cape", 
                   "Free State",
                   "KwaZulu-Natal",
                   "Mpumalanga",
                   "Northern Cape",
                   "Western Cape")
stateOrprovince_combobox = ttk.Combobox(user_info, values=stateOrprovince)
stateOrprovince_combobox.grid(row=5, column=0)

gender_label = tkinter.Label(user_info, text="Gender")
gender_label.grid(row=4, column=1)

gender = ("Male", "Female", "Other")
gender_combobox = ttk.Combobox(user_info, values=gender)
gender_combobox.grid(row=5,  column=1)

marritalStatus_label = tkinter.Label(user_info, text="Marital Status")
marritalStatus_label.grid(row=4, column=2)

marital_status = ("Single", "Married", "Divorced", "Widowed")
marital_status_combobox = ttk.Combobox(user_info, values=marital_status)
marital_status_combobox.grid(row=5, column=2)


for widget in user_info.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Course Information label frame
course_info = tkinter.LabelFrame(frame, text= "Course Information")
course_info.grid(row=1, column=0, sticky="news", padx=20, pady=20)

registered_label = tkinter.Label(course_info, text="Registration Status")
registered_label.grid(row=0, column=0)
registered_check = tkinter.Checkbutton(course_info, text="Registered")
registered_check.grid(row=1, column=0)

coursesCompleted_label = tkinter.Label(course_info, text= "#Courses Completed")
coursesCompleted_label.grid(row=0, column=1)
coursesCompleted_spinbox = tkinter.Spinbox(course_info, from_=0, to=100)
coursesCompleted_spinbox.grid(row=1, column=1)

semester_label = tkinter.Label(course_info, text= "#Semester")
semester_label.grid(row=0, column=2)
semester_spinbox = tkinter.Spinbox(course_info, from_=1, to=2)
semester_spinbox.grid(row=1, column=2)

for widget in course_info.winfo_children():
    widget.grid_configure(padx=20, pady=5)

#terms label frame
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=20)

terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.")
terms_check.grid(row=0, column=0)

button = tkinter.Button(frame, text="Submit")
button.grid(row=3, column=0)



root.mainloop()