from tkinter import * 
from PIL import ImageTk,Image 
import tkinter as tk
import os
import sys 


path = "C:/Users/Sharat/Desktop/Wolfhacks Howler/Howler.png"
home = "C:/Users/Sharat/Desktop/Wolfhacks Howler/Home.jpeg"

path2 = "C:/Users/Sharat/Desktop/Wolfhacks Howler/concept1.jpg"
path3 = "C:/Users/Sharat/Desktop/Wolfhacks Howler/concept2.jpg"
path4 = "C:/Users/Sharat/Desktop/Wolfhacks Howler/concept2.jpg"
def homepage():
	file = exec(open("C:/Users/Sharat/Desktop/Wolfhacks Howler/HowerHomepage.py").read())

def show_frame(frame):
	frame.tkraise()
def physical_health():
	window = tk.Tk()
	top = Toplevel()
	var1 = tk.IntVar()


	top.geometry("1000x740")
	top.title("Home")
	top.configure(background = "white")
	image = Image.open(path)
	image3 = image.resize((1000, 740), Image.ANTIALIAS)
	image4 = ImageTk.PhotoImage(image3)
	label_image4 = Label(top, image = image4, bg = "white")
	label_image4.grid(row = 0,column = 0, padx = (0,0), pady = (0,0))
	physical_label = Label(top,text = "Physical Health", font = ("Verdana",25),fg = "steelBlue3", bg = "gray2", relief = SUNKEN)
	physical_label.grid(row = 0, column = 0, padx = (0,700), pady = (0,500))


	LabelExample1 = tk.Label(top,
                        bg="azure",
                        fg="black",
                        borderwidth=4,
                        height=4,
                        width=40,
                        relief="ridge",
                        text="LEGS\n Muscles involved: Hamstrings, Glutes, Calves"
                        )

	LabelExample1.config(font=("Times", 7)),
	LabelExample2 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=6,
	                        anchor="c",
	                        relief="ridge",
	                        text="WORKOUT:\nSquats: 3x10\nWLunges: 3x10\nCalf Raises: 3x10\nSingle-Leg Box Squats: "
	                             "3x10\n Rest :30- 60 sec ")

	LabelExample2.config(font=("Times", 7)),
	LabelExample3 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=4,
	                        anchor="c",
	                        width=40,
	                        relief="ridge",
	                        text="CHEST/CORE\n Muscles involved: Abdominals, Pecs, Obliques ")
	LabelExample3.config(font=("Times", 7)),
	LabelExample4 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=9,
	                        relief="ridge",
	                        text="WORKOUT:\nPlanks: 4x60 sec\nPush Ups: 3 Sets Until\nDecline Push-Ups: \n2 Sets Until "
	                             "Failure\nJumping Jacks: 4x60 sec "
	                             "\nMountain Climbers: 3x15\nSit Ups: 3x 60 sec\nRest: 30-45 sec")
	LabelExample4.config(font=("Times", 7)),
	LabelExample5 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=4,
	                        anchor="c",
	                        width=40,
	                        relief="ridge",
	                        text="BACK\nMuscles involved: latissimus dorsi, Trapezius, \nobliques,Erector spinae")
	LabelExample5.config(font=("Times", 7)),
	LabelExample6 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="WORKOUT:\nHigh plank: 3x30 sec\nButterfly kicks 3x30 sec\nBurpees: 2x10\nTowel pullup: "
	                             "3x10\nRest: 30-60 sec ")
	LabelExample6.config(font=("Times", 7)),
	LabelExample7 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=4,
	                        anchor="c",
	                        width=40,
	                        relief="ridge",
	                        text="ARM\nMuscles involved: Biceps brachii, triceps \nbrachii, Deltoids")
	LabelExample7.config(font=("Times", 7)),
	LabelExample8 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="WORKOUT:\nArm Circles: 2x30 sec\nChair Tricep Dip: 4x15\nSide plank: 3x45 sec\nPush ups: 3 sets until failure "
	                             "\nBurpees: 3x15\nRest 30-60 sec")
	LabelExample8.config(font=("Times", 7)),

	LabelExample1.grid(column=0, row=0,  padx = (0,500), pady = (0,300))
	LabelExample2.grid(column=0, row=0,  padx = (300,0), pady = (0,300))
	LabelExample3.grid(column=0, row=0, padx = (0,500), pady = (50,100))
	LabelExample4.grid(column=0, row=0,  padx = (300,0), pady = (50,100))
	LabelExample5.grid(column=0, row=0,  padx =(0,500), pady = (300,50))
	LabelExample6.grid(column=0, row=0, padx = (300,0), pady = (300,50))
	LabelExample7.grid(column=0, row=0,  padx = (0,500), pady = (600,100))
	LabelExample8.grid(column=0, row=0, padx = (300,0), pady = (600,100))

	window.withdraw()
	window.mainloop()

def mental_health():
	window = tk.Tk()
	top = Toplevel()
	var1 = tk.IntVar()


	top.geometry("1000x740")
	top.title("Home")
	top.configure(background = "white")
	image = Image.open(path)
	image3 = image.resize((1000, 740), Image.ANTIALIAS)
	image4 = ImageTk.PhotoImage(image3)
	label_image4 = Label(top, image = image4, bg = "white")
	label_image4.grid(row = 0,column = 0, padx = (0,0), pady = (0,0))



	mental_label = Label(top,text = "Mental Peace", font = ("Verdana",25),fg = "steelBlue3", bg = "gray2", relief = SUNKEN)
	mental_label.grid(row = 0, column = 0, padx = (0,700), pady = (0,500))

	labelExample1 = tk.Label(top, bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="Have a Conversation with a fellow Astronaught \n or call someone close to you (Keep in touch).\n Expressing your feelings and conversing\n with someone can help you feel better")
	labelExample1.config(font=("Times", 8)),
	labelExample2 = tk.Label(top, bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="Stay Active, Excercise, Take a Break, Meditate \n Eat well, Drink water, Entertain yourself")
	labelExample2.config(font=("Times", 8)),
	labelExample3 = tk.Label(top, bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="Relax, take a bath, write a journal, track achievement and daily life,\n Sleep plenty ")
	labelExample3.config(font=("Times", 8)),
	labelExample4 = tk.Label(top, bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text=" Our Organization wants everyone to be happy and \n living in peace. That's why we want to host various events and celebrations for \n travellers to come together as a community and converse.\n We hope to host counselling sessions where the travellers \n can have one on one counselling sessions to talk \n about any problems or issues. This allows travellers to live with a \n with a peace of mind while travelling to a whole new world. ")
	labelExample4.config(font=("Times", 10)),
	
	labelExample1.grid(column=0, row=0,  padx = (0,400), pady = (0,300))
	labelExample2.grid(column=0, row=0,  padx = (0,400), pady = (50,100))
	labelExample3.grid(column=0, row=0,  padx = (0,400), pady = (300,50))
	labelExample4.grid(column=0, row=0,  padx = (400,0), pady = (100,50))
	window.withdraw()
	window.mainloop()

def nutrition():
	window = tk.Tk()
	top = Toplevel()
	var1 = tk.IntVar()


	top.geometry("1000x740")
	top.title("Home")
	top.configure(background = "white")
	image = Image.open(path)
	image3 = image.resize((1000, 740), Image.ANTIALIAS)
	image4 = ImageTk.PhotoImage(image3)
	label_image4 = Label(top, image = image4, bg = "white")
	label_image4.grid(row = 0,column = 0, padx = (0,0), pady = (0,0))
	nutrition_label = Label(top,text = "Nutrition", font = ("Verdana",25),fg = "steelBlue3", bg = "gray2", relief = SUNKEN)
	nutrition_label.grid(row = 0, column = 0, padx = (0,700), pady = (0,500))

	labelExample1 = tk.Label(top, bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="NUTRITIONAL VALUES\nCalories: 18\nWater: 95%\nProtein: 0.9 grams\nCarbs: 3.9 "
	                             "grams\nFiber: 1.2 grams\nFat: 0.2 grams\nServing: 100g")
	labelExample1.config(font=("Times", 7)),
	labelExample2 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        anchor="c",
	                        width=48,
	                        relief="ridge",
	                        text="TOMATOES\n It is usually grown in warm weather so they must be grown\nduring the "
	                             "summer months in Howler. The tomatoes need\n6-8 hours of sunlight per day with rain "
	                             "occurring every 4\ndays allowing for somewhat dry weather. The soil has a\npH of 7.1 "
	                             "to 8 and tomatoes can grow in a pH of 7.5.\nThey take 50-60 days to grow "
	                        )
	labelExample2.config(font=("Times", 7)),
	labelExample3 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        anchor="c",
	                        width=48,
	                        relief="ridge",
	                        text="ASPARAGUS\nAsparagus can tolerate major weather changes and can\nhandle both extreme "
	                             "heat and cold. This is perfect for the\nextreme weather conditions on Howler. "
	                             "Asparagus thrives\nin full sun, when it gets more than 8 hours of sunlight per \nday, "
	                             "perfect for Howlers environment. Asparagus also can\ngrow in soil with a pH of 7.5.")
	labelExample3.config(font=("Times", 7)),
	labelExample4 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="NUTRITIONAL VALUES\nCalories: 20\nWater: 94%\nProtein: 2.2 grams\nCarbs: 3.9 "
	                             "grams\nFiber: 1.8 grams\nFat: 0.2 grams\nServing: 100g")
	labelExample4.config(font=("Times", 7)),
	labelExample5 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        anchor="c",
	                        width=48,
	                        relief="ridge",
	                        text="SPINACH\nSpinach beet grow in sunny areas so can be grown on\nHowler during the summer "
	                             "months in moist conditions.\nSpinach beet requires more than 8 hours of sunlight a "
	                             "day\nfulfilling the average sunlight requirement. It grows in soil\ndwith a pH thats 7 "
	                             "or higher. Elevation doesn’t affect the \nplant and it grows in chalky soil. Another "
	                             "perfect vegetable\n to grow when inhabiting Howler.")
	labelExample5.config(font=("Times", 7)),
	labelExample6 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="NUTRITIONAL VALUES\nCalories: 18\nWater: 95%\nProtein: 0.9 grams\nCarbs: 3.9 "
	                             "grams\nFiber: 1.2 grams\nFat: 0.2 grams\nServing: 100g")
	labelExample6.config(font=("Times", 7)),
	labelExample7 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        anchor="c",
	                        width=48,
	                        relief="ridge",
	                        text="CABBAGE\nCabbage usually requires full sunlight, indicating it requires\n8 or more "
	                             "hours in sunlight. Thus it can be grown in higher "
	                             "elevations. It grows in soil with a pH of 6.5 to 7.4. A more\nstrict pH soil level "
	                             "must be taken into consideration when\ntrying to plant the cabbage. It usually grows "
	                             "in 24° C which \nis perfect for Howler.")
	labelExample7.config(font=("Times", 7)),
	labelExample8 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="NUTRITIONAL VALUES\nCalories: 25\nWater: 92%\nProtein: 1.3 grams\nCarbs: 6.0 "
	                             "grams\nFiber: 2.5 grams\nFat: 0.1 grams\nServing: 100g")
	labelExample8.config(font=("Times", 7)),

	labelExample1.grid(column=0, row=0,  padx = (300,0), pady = (0,300))
	labelExample2.grid(column=0, row=0,  padx = (0,500), pady = (0,300))
	labelExample3.grid(column=0, row=0, padx = (0,500), pady = (50,100))
	labelExample4.grid(column=0, row=0,  padx = (300,0), pady = (50,100))
	labelExample5.grid(column=0, row=0,  padx = (0,500), pady = (300,50))
	labelExample6.grid(column=0, row=0, padx = (300,0), pady = (300,50))
	labelExample7.grid(column=0, row=0,  padx = (0,500), pady = (600,100))
	labelExample8.grid(column=0, row=0, padx = (300,0), pady = (600,100))


	window.withdraw()
	window.mainloop()

def status():
	window = tk.Tk()
	top = Toplevel()
	var1 = tk.IntVar()


	top.geometry("1000x740")
	top.title("Home")
	top.configure(background = "white")
	image = Image.open(path)
	image3 = image.resize((1000, 740), Image.ANTIALIAS)
	image4 = ImageTk.PhotoImage(image3)
	label_image4 = Label(top, image = image4, bg = "white")
	label_image4.grid(row = 0,column = 0, padx = (0,0), pady = (0,0))
	status_label = Label(top,text = "Howler Status", font = ("Verdana",25),fg = "steelBlue3", bg = "gray2", relief = SUNKEN)
	status_label.grid(row = 0, column = 0, padx = (0,700), pady = (0,500))

	
	LabelExample1 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=3,
	                        width=40,
	                        relief="ridge",
	                        text="WEATHER CONDITIONS"
	                        )

	LabelExample1.config(font=("Times", 7)),
	LabelExample2 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=9,
	                        anchor="c",
	                        relief="ridge",
	                        text="DESCRIPTION:\n It is important to understand \nthat Planet Howler experiences highly unstable \nweather conditions. Summer and winter climates \noccupy majority of the calender year with \ntemperatures fluctuating between -25°C to \n25°C. The planet receives rather \nlarge amount of precipitation every \n4 days consistently throughout the year.")

	LabelExample2.config(font=("Times", 7)),
	LabelExample3 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=3,
	                        anchor="c",
	                        width=40,
	                        relief="ridge",
	                        text="SOIL CONDITIONS")
	LabelExample3.config(font=("Times", 7)),
	LabelExample4 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=9,
	                        relief="ridge",
	                        text="DESCRIPTION:\n The soil found in mojaority of the aear \nmostly consists of chalky "
	                             "sediment and compact \nmatter, with organic decompostion rates. The \naverage pH leves "
	                             "between the soil range from 7.1 to \n8.0. Plants find it harder to access sufficient "
	                             "\nnutrients and adequate vitamins \nfrom the soil")
	LabelExample4.config(font=("Times", 7)),
	LabelExample5 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=3,
	                        anchor="c",
	                        width=40,
	                        relief="ridge",
	                        text="TERRIAN CONDITIONS")
	LabelExample5.config(font=("Times", 7)),
	LabelExample6 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=7,
	                        relief="ridge",
	                        text="DESCRIPTION: \nThe terrain of Planet Howler is overall \nrugged with small natural craters and hills\n it is important to understand that \nvegetation will grow at higher altitudes")

	LabelExample6.config(font=("Times", 7)),
	LabelExample7 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=3,
	                        anchor="c",
	                        width=40,
	                        relief="ridge",
	                        text="RESEARCH")
	LabelExample7.config(font=("Times", 7)),
	LabelExample8 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="DESCRIPTION:\nArriving at a new planet is a big experience, so using our app, \nwe can collect data on different elements, materials of planet Howler. \nThis allows us to learn more about planet Howler and its uses for such materials ")
	LabelExample8.config(font=("Times", 7)),

	LabelExample1.grid(column=0, row=0, padx = (0,500), pady = (0,300))
	LabelExample2.grid(column=0, row=0,  padx = (300,0), pady = (0,300))
	LabelExample3.grid(column=0, row=0,  padx = (0,500), pady = (50,100))
	LabelExample4.grid(column=0, row=0, padx = (300,0), pady = (50,100))
	LabelExample5.grid(column=0, row=0, padx = (0,500), pady = (300,50))
	LabelExample6.grid(column=0, row=0, padx = (300,0), pady = (300,50))
	LabelExample7.grid(column=0, row=0, padx = (0,500), pady = (600,100))
	LabelExample8.grid(column=0, row=0, padx = (300,0), pady = (600,100))
	
	password_lbl = Label(top,text = "Data:", font = ("Helvetica",13), bg = "white")
	password_lbl.grid(row = 0, column = 0, padx = (0,500), pady = (0,800))
	
	data_entry = Entry(top, show = "",borderwidth = 2, relief = "groove")
	data_entry.grid(row = 0, column = 0, padx = (300,0), pady = (0,800))


	window.withdraw()
	window.mainloop()

def prototype():
	window = tk.Tk()
	top = Toplevel()
	var1 = tk.IntVar()


	top.geometry("1000x740")
	top.title("Home")
	top.configure(background = "white")
	image = Image.open(path)
	image3 = image.resize((1000, 740), Image.ANTIALIAS)
	image4 = ImageTk.PhotoImage(image3)
	label_image4 = Label(top, image = image4, bg = "white")
	label_image4.grid(row = 0,column = 0, padx = (0,0), pady = (0,0))
	
	contact_label = Label(top,text = "Prototype Concept", font = ("Verdana",25),fg = "steelBlue3", bg = "gray2", relief = SUNKEN)
	contact_label.grid(row = 0, column = 0, padx = (0,600), pady = (0,500))

	image_concept1 = Image.open(path2)
	imageconcept = image_concept1.resize((140, 140), Image.ANTIALIAS)
	imagec = ImageTk.PhotoImage(imageconcept)
	label_imagec1 = Label(top, image = imagec, bg = "white")
	label_imagec1.grid(row = 0,column = 0, padx = (0,300), pady = (100,300))

	image_concept2 = Image.open(path3)
	imageconcept_1 = image_concept2.resize((140, 140), Image.ANTIALIAS)
	imagec1 = ImageTk.PhotoImage(imageconcept_1)
	label_imagec2 = Label(top, image = imagec1, bg = "white")
	label_imagec2.grid(row = 0,column = 0, padx = (0,300), pady = (300,200))

	image_concept3 = Image.open(path4)
	imageconcept_2 = image_concept3.resize((140, 140), Image.ANTIALIAS)
	imagec2 = ImageTk.PhotoImage(imageconcept_2)
	label_imagec3 = Label(top, image = imagec2, bg = "white")
	label_imagec3.grid(row = 0,column = 0, padx = (0,300), pady = (500,0))

	labelExample1 = tk.Label(top,
	                        bg="azure",
	                        fg="black",
	                        borderwidth=4,
	                        height=8,
	                        relief="ridge",
	                        text="Our Prototype is called Moonwalker, which is a small portable \n device that can be carried around. This device is compitable with \nthe Howler Software. The Moonwalker services the purpose of being a mobile essential tool\n during the travel to Howler and residence at Howler. This tool is\n an esstial guidline which will help with survival and provide prior \n knowledge before getting to Howler.")
	labelExample1.config(font=("Times", 7)),

	labelExample1.grid(column=0, row=0,  padx = (300,0), pady = (0,200))
	
	window.withdraw()
	window.mainloop()

window = tk.Tk()
top = Toplevel()
var1 = tk.IntVar()

top.geometry("1000x740")
top.title("Howler")
top.configure(background = "white")


image = Image.open(path)
image3 = image.resize((1000, 740), Image.ANTIALIAS)
image4 = ImageTk.PhotoImage(image3)
label_image3 = Label(top, image = image4, bg = "black")
label_image3.grid(row = 0,column = 0, padx = (0,0), pady = (0,0))

def home_window():
	window = tk.Tk()
	top = Toplevel()
	var1 = tk.IntVar()


	top.geometry("1000x740")
	top.title("Home")
	top.configure(background = "white")
	image = Image.open(path)
	image3 = image.resize((1000, 740), Image.ANTIALIAS)
	image4 = ImageTk.PhotoImage(image3)
	label_image4 = Label(top, image = image4, bg = "white")
	label_image4.grid(row = 0,column = 0, padx = (0,0), pady = (0,0))

	home_msg = "Our Mission is to travel to the planet Howler, \nand discover a new home, habitable for all humans. \nHowler, or our organization works towards creating a\n system that people can use to guide themselves for the Howler Voyage. \nThe different environment is a lot to adjust to, the low gravity, different weather \nconditions, food differences,etc. There’s a lot of factors\n that play in when travelling to Howler, and we hope to account for those factors\n and educate travellers on them to ensure they have a healthy trip. We also hope to educate \ntravellers about Howler in order to give them a sense of what\n to avoid and what to look out for. We hope to learn more about the planet \nHowler and make it our new home for which reason we hope to explore \nand study the contents of Howler. "
	home_button = Label(top,text = "Home", font = ("Helvetica",15),fg = "gray3", bg = "antique white", relief = SUNKEN)
	home_button.grid(row = 0, column = 0, padx = (0,800), pady = (0,400))

	nutrition_button = Button(top,text = "Nutrition", font = ("Helvetica",15),fg = "antique white", bg = "gray3", relief = SUNKEN, command = nutrition)
	nutrition_button.grid(row = 0, column = 0, padx = (0,500), pady = (0,400))

	mentalhealth_button = Button(top,text = "Mental Peace", font = ("Helvetica",15),fg = "antique white", bg = "gray3", relief = SUNKEN, command = mental_health)
	mentalhealth_button.grid(row = 0, column = 0, padx = (0,150), pady = (0,400))

	physical_button = Button(top,text = "Physical Health", font = ("Helvetica",15),fg = "antique white", bg = "gray3", relief = SUNKEN, command = physical_health)
	physical_button.grid(row = 0, column = 0, padx = (300,50), pady = (0,400))

	status_button = Button(top,text = "Howler Status", font = ("Helvetica",15),fg = "antique white", bg = "gray3", relief = SUNKEN, command = status)
	status_button.grid(row = 0, column = 0, padx = (600,0), pady = (0,400))

	prototype_button = Button(top,text = "Prototype", font = ("Helvetica",15),fg = "antique white", bg = "gray5", relief = SUNKEN, command = prototype)
	prototype_button.grid(row = 0, column = 0, padx = (900,0), pady = (0,400))

	home_label = Label(top,text = "Our Mission", font = ("Verdana",25),fg = "steelBlue3", bg = "gray2", relief = SUNKEN)
	home_label.grid(row = 0, column = 0, padx = (0,700), pady = (0,200))

	info_label =  Label(top,text = home_msg , font = ("Verdana",10),fg = "steelBlue3", bg = "gray2", relief = SUNKEN)
	info_label.grid(row = 0, column = 0, padx = (0,350), pady = (200,50))


	window.withdraw()
	window.mainloop()

Welcome_label = Label(top,text = "Welcome to Howler", font = ("Verdana",50,"italic"), fg = "antique white", bg = "gray5")
Welcome_label.grid(row = 0, column = 0, padx = (0,0), pady = (0,200))
continue_button = Button(top,text = "Continue", font = ("Helvetica",25),fg = "antique white", bg = "gray3", relief = SUNKEN, command = home_window)
continue_button.grid(row = 0, column = 0, padx = (0,0), pady = (230,0))



window.withdraw()
window.mainloop()