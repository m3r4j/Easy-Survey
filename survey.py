from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# Create the screen
root = Tk()
root.title('Survey')
root.geometry('400x450')
root.resizable(0,0)
root.iconbitmap('surveyicon.ico')

default_bg = '#%02x%02x%02x' % (240, 240, 237)
root.configure(bg=default_bg)


# Add image
survey_img = Image.open('surveyimage.png')
survey_img = survey_img.resize((210, 210), Image.ANTIALIAS)
survey_img = ImageTk.PhotoImage(survey_img)


# Add the label
survey_label = Label(root, image=survey_img, bg=default_bg)
survey_label.pack()


# Create labels / entries
name_label = Label(root, text='Name:', fg='black', bg=default_bg, font=(None, 20))
name_entry = Entry(root, width=20, font=(None, 15), fg='blue')

name_label.place(x=20, y=220)
name_entry.place(x=110, y=228)


age_label = Label(root, text='Age:', fg='black', bg=default_bg, font=(None, 20))
age_entry = Entry(root, width=20, font=(None, 15), fg='blue')

age_label.place(x=20, y=260)
age_entry.place(x=110, y=268)


color_label = Label(root, text='Color:', fg='black', bg=default_bg, font=(None, 20))
color_entry = Entry(root, width=20, font=(None, 15), fg='blue')

color_label.place(x=20, y=300)
color_entry.place(x=110, y=308)


food_label = Label(root, text='Food:', fg='black', bg=default_bg, font=(None, 20))
food_entry = Entry(root, width=20, font=(None, 15), fg='blue')

food_label.place(x=20, y=340)
food_entry.place(x=110, y=348)



# Create submit button
submit_button = Button(root, text='Submit', padx=91, fg='blue', bg=default_bg, command=lambda: messagebox.showinfo('Thanks', 'Thank you for completing this survey!'))
submit_button.place(x=107, y=390)




root.mainloop()