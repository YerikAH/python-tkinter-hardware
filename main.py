from tkinter import *
from PIL import ImageTk, Image
import tkinter.font as tkFont
import random
from tkinter import messagebox
app = Tk()


# my magic
soonMagic = []
codeMagic = []

#var validation
phonebool = False
dnibool = False
moneybool = False

# styles for font
font_style = tkFont.Font(size=16, weight="bold")
font_style_small = tkFont.Font(size=10, weight="bold")

count = 0
# about us
def about_fun():

	def add_count():
		global count 
		count = count + 1
		click_num_about.configure(text=f'Clicked in the button: {count}')
	
	about_app = Toplevel()
	#config about
	about_app.title("About | The happy screw hardware store")
	about_app.config(bg="#151515")
	about_app.iconbitmap("icono.ico")
	about_app.resizable(False,False)
	#about
	logo_senati_about = Label(about_app,image=my_study,bg="#151515")
	first_text_about = Label(about_app,text="Esther small project is the course work",bg="#151515",fg="#e4e4e4")
	second_text_about = Label(about_app,text="algorithms and software programming.",bg="#151515",fg="#e4e4e4")
	second_text_about.configure(font=font_style_small)
	third_text_about = Label(about_app,text="It was developed by Harvey Vasquez Huaranga Yerik",bg="#151515",fg="#e4e4e4")
	click_num_about = Label(about_app,text=f"Clicked in the button: {count}",fg="#e4e4e4",bg="#151515")
	button_num_about = Button(about_app,text="Click me!",command=add_count,bg="#FF8F27",fg="#e4e4e4",border=0,activebackground="#FFB26A",activeforeground="#e4e4e4")
	logo_senati_about.grid(padx=20,pady=10,ipadx=10,ipady=7)
	first_text_about.grid(padx=20,pady=2,ipadx=10,ipady=2)
	second_text_about.grid(padx=20,pady=2,ipadx=10,ipady=2)
	third_text_about.grid(padx=20,pady=2,ipadx=10,ipady=2)
	click_num_about.grid(padx=20,pady=2,ipadx=10,ipady=2)
	button_num_about.grid(padx=15,pady=20,ipady=7,ipadx=20,sticky="nsew")
	
#Popup

def popup_info():
	messagebox.showinfo("Info","The secret code is a logo found in the about section.")


#Login
def login_fun():
	login_app = Toplevel()
	#config login
	login_app.title("Login admin | The happy screw hardware store")
	login_app.config(bg="#151515")
	login_app.iconbitmap("icono.ico")
	login_app.resizable(False,False)

	
	def delete_label(something):
		something.grid_forget()

	def no_login():
		if name_login_entry.get() == "" or password_login_entry.get() == "":
			login_incomplete=Label(login_app,text="Please fill all the boxes", bg="#151515",fg="#F35959",anchor='w')
			login_incomplete.grid(column=1)
			login_incomplete.after(3000,lambda: delete_label(login_incomplete))
		else:
			login_incomplete=Label(login_app,text="Wrong password, try again with\n another password", bg="#151515",fg="#F35959",anchor='w')
			login_incomplete.grid(column=1)
			login_incomplete.after(3000,lambda: delete_label(login_incomplete))


	# Login

	image_login_label = Label(login_app,image=my_secu,bg="#151515")
	title_login_label = Label(login_app,text="Log in",bg="#151515",fg="#e4e4e4")
	title_login_label.configure(font=font_style)
	name_login_label = Label(login_app,text="E-mail or username",bg="#151515",fg="#e4e4e4",anchor='w')
	password_login_label = Label(login_app,text="Enter the correct password",bg="#151515",fg="#e4e4e4",anchor='w')
	name_login_entry = Entry(login_app,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
	password_login_entry = Entry(login_app,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
	try_login_button = Button(login_app,text="Log in",bg="#FF8F27",fg="#e4e4e4",border=0,activebackground="#FFB26A",activeforeground="#e4e4e4",command=no_login)
	text_login_label = Label(login_app,text="Did you forget your password?",bg="#151515",fg="#e4e4e4")

	title_login_label.grid(column=1,columnspan=1,row=0,sticky="nsew",pady=10,ipady=7)
	image_login_label.grid(column=0,rowspan=5,sticky="nsew",padx=30,ipadx=20)
	name_login_label.grid(row=1,column=1,sticky="nsew",padx=15,ipadx=60)
	name_login_entry.grid(row=2,column=1,sticky="nsew",padx=15,pady=5,ipady=5,ipadx=60)
	password_login_label.grid(row=3,column=1,sticky="nsew",padx=15,ipadx=60)
	password_login_entry.grid(row=4,column=1,sticky="nsew",padx=15,pady=5,ipady=5,ipadx=60)
	try_login_button.grid(row=5,column=1,sticky="nsew",padx=15,pady=5,ipady=5,ipadx=60)
	text_login_label.grid(row=6,column=1,sticky="nsew",padx=15,pady=5,ipady=5,ipadx=60)

#config app
app.resizable(False,False)
app.rowconfigure(0,weight=1)
app.columnconfigure(0,weight=1)
app.title("The happy screw hardware store")
app.config(bg="#151515")
app.iconbitmap("icono.ico")


# functions -- IMPORTANT

# next frame, in this case second frame
def next_pag(frame):
	frame.tkraise()

# back frame, in this case first frame
def second_change():
	next_pag(frame_first)

def third_change():
	next_pag(frame_third)
	create_element_frame_third()

# DELETE ERROR

def delete_label(something):
	something.grid_forget()

# form validation

def first_change():
	global error_incomplete
	global dni_error
	global number_error
	global number_error_phone
	global number_error_dni
	try:
		x = int(number_phone_input.get()) + 9  
		print(x)
		phonebool=False
	except ValueError:
		phonebool=True

	try:
		x = int(dni_input.get()) + 9  
		print(x)
		dnibool=False
	except ValueError:
		dnibool=True
	if name_input.get() == "" or last_name_input.get() == "" or dni_input.get() == "" or direction_input.get() == "" or number_phone_input.get() == "" :
		error_incomplete=Label(text="Please fill all the boxes", bg="#151515",fg="#F35959",anchor='w')
		error_incomplete.grid()
		error_incomplete.after(3000,lambda: delete_label(error_incomplete))
	elif len(dni_input.get()) > 8 or len(dni_input.get()) < 8:
		dni_error = Label(text="A DNI is made up of 8 digits, try again.", bg="#151515",fg="#F35959",anchor='w')
		dni_error.grid()
		dni_error.after(3000,lambda: delete_label(dni_error))
	elif len(number_phone_input.get()) > 9 or len(number_phone_input.get()) < 9:
		number_error = Label(text="A cell phone number in Peru can only have 9 digits.", bg="#151515",fg="#F35959",anchor='w')
		number_error.grid()
		number_error.after(3000,lambda: delete_label(number_error))
	elif phonebool == True:
		number_error_phone = Label(text="Just enter numbers in the phone number field.", bg="#151515",fg="#F35959",anchor='w')
		number_error_phone.grid()
		number_error_phone.after(3000,lambda: delete_label(number_error_phone))
	elif dnibool == True:
		number_error_dni = Label(text="Just enter numbers in the DNI field", bg="#151515",fg="#F35959",anchor='w')
		number_error_dni.grid()
		number_error_dni.after(3000,lambda: delete_label(number_error_dni))




	else:
		next_pag(frame_second)
		create_element_frame_second()	
	

#Logic add task, add product

#btn reset
def reset_change():
	otherFrame.grid_forget()
	name_input.delete(0,END)
	last_name_input.delete(0,END)
	dni_input.delete(0,END)
	direction_input.delete(0,END)
	number_phone_input.delete(0,END)
	soonMagic.clear()
	codeMagic.clear()
	next_pag(frame_first)


def my_magic():
	#validate form
	global code_error_third
	global count_error_third
	try :
		t =int(count_entry_third.get()) / 2
		print(t)
		moneybool= False
	except ValueError:
		moneybool= True


	if code_entry_third.get() == "" :
		code_error_third = Label(frame_third,text="Please fill al the boxes", bg="#151515",fg="#F35959",anchor='w')
		code_error_third.grid(row=4)
		code_error_third.after(3000,lambda: delete_label(code_error_third))
	elif count_entry_third.get()== "" :
		count_error_third = Label(frame_third,text="Please fill al the boxes", bg="#151515",fg="#F35959",anchor='w')
		count_error_third.grid(row=8)
		count_error_third.after(3000,lambda: delete_label(count_error_third))
	elif moneybool == True:
		count_error_third = Label(frame_third,text="Please enter only numbers in this field.", bg="#151515",fg="#F35959",anchor='w')
		count_error_third.grid(row=8)
		count_error_third.after(3000,lambda: delete_label(count_error_third))
	elif int(count_entry_third.get()) >= 100:
		count_error_third = Label(frame_third,text="Sorry we do not have that many products", bg="#151515",fg="#F35959",anchor='w')
		count_error_third.grid(row=8)
		count_error_third.after(3000,lambda: delete_label(count_error_third))
	else:
		if question_two.get() == "senati":
			price_random = random.randrange(1, 10, 2)
		else:
			price_random = random.randrange(5, 500, 54)
		code_convert =code_entry_third.get()
		count_convert =int(count_entry_third.get())
		amount_total = price_random  * count_convert
		amount_str = str(amount_total)
		soonMagic.append(amount_total)
		codeMagic.append(code_convert)
		the_frame = LabelFrame(otherFrame,bg="#2B2B2B",bd=0)
		code_frame = Label(the_frame,text=f"CODE: {code_convert}",bg="#2B2B2B",fg="#e4e4e4")
		price_frame = Label(the_frame,text=f"PRICE: ${price_random}x{count_convert}",bg="#2B2B2B",fg="#e4e4e4")
		total_frame = Label(the_frame,text=f"TOTAL: ${amount_str}",bg="#2B2B2B",fg="#e4e4e4")
		delete_frame = Button(the_frame,text="Remove product",bg="#151515",fg="#e4e4e4",border=0,activebackground="#333333",activeforeground="#e4e4e4")
		the_frame.grid(sticky="nsew")
		code_frame.grid(row=0,column=0,sticky="nsew",padx=5,ipadx=5,pady=5,ipady=5)
		price_frame.grid(row=0,column=1,sticky="nsew",padx=5,ipadx=5,pady=5,ipady=5)
		total_frame.grid(row=0,column=2,sticky="nsew",padx=5,ipadx=5,pady=5,ipady=5)
		delete_frame.grid(row=0,column=3,padx=5,ipadx=5,pady=5,ipady=5,sticky="nsew")



# Barra menu

my_menu = Menu(app)
app.config(menu=my_menu)
file_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label="Admin",menu=file_menu)
file_menu.add_command(label="Log in",command=login_fun)
file_menu.add_command(label="About us",command=about_fun)
file_menu.add_command(label="Info",command=popup_info)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=app.quit)


# All create frames

frame_first = Frame(app,bg="#151515")
frame_second = Frame(app,bg="#151515")
frame_third = Frame(app,bg="#151515")

frame_first.grid_propagate(True)
frame_second.grid_propagate(True)
frame_third.grid_propagate(True)
for frame in (frame_first,frame_second,frame_third):
	frame.grid(row=0,column=0,sticky="nsew")
# Images
my_logo = ImageTk.PhotoImage(
	Image.open("./logo.png")
)
my_pay = ImageTk.PhotoImage(
	Image.open("./payimg.png")
)
my_secu = ImageTk.PhotoImage(
	Image.open("./login.png")
)
my_study = ImageTk.PhotoImage(
	Image.open("./senati.png")
)
#Frame number one || Frame one
# Label start
name_label = Label(frame_first,text="First name",bg="#151515",fg="#e4e4e4",anchor='w')
last_name_label = Label(frame_first,text="Last name",bg="#151515",fg="#e4e4e4",anchor='w')
dni_label = Label(frame_first,text="DNI",bg="#151515",fg="#e4e4e4",anchor='w')
direction_label = Label(frame_first,text="Direction",bg="#151515",fg="#e4e4e4",anchor='w')
number_phone_label = Label(frame_first,text="Phone number",bg="#151515",fg="#e4e4e4",anchor='w')
logo_label = Label(frame_first,image=my_logo,bg="#151515")
# Input start
name_input = Entry(frame_first,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
last_name_input = Entry(frame_first,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
dni_input = Entry(frame_first,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
direction_input = Entry(frame_first,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
number_phone_input = Entry(frame_first,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
# Button start
button_next = Button(frame_first,bg="#FF8F27",fg="#e4e4e4",text="Next",border=0,activebackground="#FFB26A",activeforeground="#e4e4e4",command=first_change)
# packaging with grid "css" of python
# Label
logo_label.grid(row=0,column=0,columnspan=2,padx=20,pady=30,ipady=7,ipadx=20,sticky="nsew")
name_label.grid(row=1,column=0,sticky="nsew")
last_name_label.grid(row=1,column=1,sticky="nsew")
dni_label.grid(row=3,column=0,columnspan=2,sticky="nsew")
direction_label.grid(row=5,column=0,columnspan=2,sticky="nsew")
number_phone_label.grid(row=7,column=0,columnspan=2,sticky="nsew")
# Input
name_input.grid(row=2,column=0,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")
last_name_input.grid(row=2,column=1,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")
dni_input.grid(row=4,column=0,columnspan=2,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")
direction_input.grid(row=6,column=0,columnspan=2,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")
number_phone_input.grid(row=8,column=0,columnspan=2,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")
# Button
button_next.grid(row=9,column=0,columnspan=2,padx=15,pady=20,ipady=7,ipadx=20,sticky="nsew")
# End Frame one
# Frame two label, buton and label || Frame 2
def create_element_frame_second():
	global question_two
	title_label = Label(frame_second,text="¡Almost ready!",bg="#151515",fg="#FF8F27")
	title_label.configure(font=font_style)
	imgae_label =  Label(frame_second,image=my_pay,bg="#151515")
	question_pay = Label(frame_second,text="Do you have any secret code?",bg="#151515",fg="#e4e4e4",anchor='w')
	advice_label = Label(frame_second,text="Please enter the correct amount and check if the data you\n sent is correct, then there will be no going back.",bg="#151515",fg="#AEAEAE",justify=LEFT,anchor='w')
	question_two = Entry(frame_second,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
	button_modal = Button(frame_second,bg="#FF8F27",fg="#e4e4e4",text="Next",border=0,activebackground="#FFB26A",activeforeground="#e4e4e4",command=third_change)
	button_back = Button(frame_second,bg="#FF7B00",fg="#e4e4e4",text="Back",border=0,activebackground="#FF8F27",activeforeground="#e4e4e4",command=second_change)
	# Grid
	title_label.grid(row=0,column=0,padx=15,pady=10,ipady=7,ipadx=100)
	imgae_label.grid(row=1,column=0,sticky="ns",padx=15,pady=10,ipady=7,ipadx=20)
	question_pay.grid(row=2,column=0,sticky="nsew",padx=15,ipadx=20)
	question_pay.configure(font=font_style_small)
	advice_label.grid(row=3,column=0,padx=15,ipadx=15,sticky="nsew")
	question_two.grid(row=4,column=0,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")
	button_modal.grid(row=5,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")
	button_back.grid(row=6,padx=15,pady=10,ipady=7,ipadx=20,sticky="nsew")

# Frame three  label, buton and label || Frame 3
def create_element_frame_third():
	global code_entry_third
	global count_entry_third
	global otherFrame
	logo_label_third = Label(frame_third,image=my_logo,bg="#151515")
	code_label_third = Label(frame_third,text="Product code",bg="#151515",fg="#e4e4e4",justify=LEFT,anchor='w')
	code_label_third.configure(font=font_style_small)
	code_help_label_third = Label(frame_third,text="You can enter any number, example of some\n codes: 253, 894, 509, 764, 924, 204, 346, or you can even write letters.",bg="#151515",fg="#AEAEAE",justify=LEFT,anchor='w')
	count_label_third = Label(frame_third,text="Amount",bg="#151515",fg="#e4e4e4",justify=LEFT,anchor='w')
	count_label_third.configure(font=font_style_small)
	count_help_label_third = Label(frame_third,text="How many will you take, from the product code you entered.",bg="#151515",fg="#AEAEAE",justify=LEFT,anchor='w')
	show_task_label_third = Label(frame_third,text="Below are all the products you entered.",bg="#151515",fg="#e4e4e4",justify=LEFT,anchor='w')
	show_task_label_third.configure(font=font_style_small)
	code_entry_third = Entry(frame_third,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)
	count_entry_third = Entry(frame_third,bg="#222222",fg="#f1f1f1",borderwidth="0",justify=LEFT)

	task_button_third = Button(frame_third,bg="#FF7B00",fg="#e4e4e4",text="Add product",border=0,activebackground="#FFB26A",activeforeground="#e4e4e4",command=my_magic)
	print_button_third = Button(frame_third,text="Print list",bg="#FF8F27",fg="#e4e4e4",border=0,activebackground="#FFB26A",activeforeground="#e4e4e4",command=print_list)
	reset_button_third = Button(frame_third,text="Reset",bg="#FF7B00",fg="#e4e4e4",border=0,activebackground="#FFB26A",activeforeground="#e4e4e4",command = reset_change)

	logo_label_third.grid(row=0,column=0,sticky="nsew",ipadx=100,pady=20,ipady=20)
	code_label_third.grid(row=1,column=0,sticky="nsew",padx=15)
	code_help_label_third.grid(row=2,column=0,sticky="nsew",padx=15)
	code_entry_third.grid(row=3,column=0,sticky="nsew",padx=15,pady=10,ipady=10)
	count_label_third.grid(row=5,column=0,sticky="nsew",padx=15)
	count_help_label_third.grid(row=6,column=0,sticky="nsew",padx=15)
	count_entry_third.grid(row=7,column=0,sticky="nsew",padx=15,pady=10,ipady=10)
	task_button_third.grid(row=9,column=0,padx=15,pady=5,ipady=7,ipadx=20,sticky="nsew")
	print_button_third.grid(row=10,column=0,padx=15,pady=5,ipady=7,ipadx=20,sticky="nsew")
	reset_button_third.grid(row=11,column=0,padx=15,pady=5,ipady=7,ipadx=20,sticky="nsew")
	show_task_label_third.grid(row=12,column=0,padx=15,pady=5,ipady=7,ipadx=20,sticky="nsew")

	otherFrame = LabelFrame(frame_third,bg="#2B2B2B",bd=0)
	otherFrame.grid()
	
#print list

def print_list():
	
	print_app = Toplevel()
	print_app.title("Print | The happy screw hardware store")
	print_app.config(bg="#e4e4e4")
	print_app.iconbitmap("icono.ico")
	print_app.resizable(False,False)

	count_temporal= 0
	word_temporal = ""
	myvar = 0
	for t in soonMagic:
		count_temporal =  count_temporal + t
		myvar = myvar + 1
	for h in codeMagic:
		word_temporal = f"{word_temporal} | {h}"
	#Montage 
	name_local_print = name_input.get()
	last_local_print = last_name_input.get()
	dni_local_print = dni_input.get()
	number_local_print= number_phone_input.get()
	direction_local_print= direction_input.get()

	fullname_local = f"FULLNAME: {name_local_print} {last_local_print}"
	number_local = f"NUMBER: {number_local_print}"
	dni_local = f"DNI: {dni_local_print}"
	directaion_local= f"DIRECTION: {direction_local_print}"
	total_local = f"TOTAL: ${count_temporal}"
	count_local = f"COUNT PRODUCT: {myvar}"
	count_word_local = f"LIST PRODUCT: {word_temporal}"

	full_name_print = Label(print_app,text=fullname_local,justify=LEFT,anchor='w')
	number_print = Label(print_app,text=number_local,justify=LEFT,anchor='w')
	dni_print = Label(print_app,text=dni_local,justify=LEFT,anchor='w')
	direction_print = Label(print_app,text=directaion_local,justify=LEFT,anchor='w')
	total_print = Label(print_app,text=total_local,justify=LEFT,anchor='w')
	product_count_print = Label(print_app,text=count_local,justify=LEFT,anchor='w')
	product_description_print = Label(print_app,text=count_word_local,justify=LEFT,anchor='w')
	
	full_name_print.grid(row=0,column=0,sticky="nsew")
	number_print.grid(row=0,column=1,sticky="nsew")
	dni_print.grid(row=1,column=0,sticky="nsew")
	direction_print.grid(row=1,column=1,sticky="nsew")
	product_description_print.grid(row=2,column=0,sticky="nsew",columnspan=1)
	product_count_print.grid(row=3,column=0,sticky="nsew")
	total_print.grid(row=3,column=1,sticky="nsew")
	myvar = 0


# show frame number one
next_pag(frame_first)


app.mainloop()