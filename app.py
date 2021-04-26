# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 20:56:32 2021

@author: Arjun
"""
import PIL
from PIL import ImageTk
import PIL.Image
import cv2
import tkinter as tk

def show_menu():
	#menu
	menubar = tk.Menu(root)
	filemenu = tk.Menu(menubar, tearoff=0)
	
	filemenu.add_command(label='Check Status', command=show_status)
	filemenu.add_separator()
	filemenu.add_command(label="Quit",command=root.destroy)
	menubar.add_cascade(label="File", menu=filemenu)
	
	helpmenu = tk.Menu(menubar, tearoff=0)
	helpmenu.add_command(label='About App', command=about_app)
	helpmenu.add_command(label='Get Help', command=help_app)
	menubar.add_cascade(label="Help", menu=helpmenu)
		
	root.config(menu=menubar)

def show_frame():
	_, frame = cap.read()
	frame = cv2.flip(frame, 1)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = PIL.Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)
	lmain.grid(row=0, column=0, sticky = tk.W, pady=20, padx=20, columnspan=2)
	
def show_status():
	status = tk.Toplevel()
	root.iconbitmap('eye.ico')
	status.title('Check Status')
	
	if cap.isOpened():
		video_status_text = 'Online'
	else:
		video_status_text = 'Offline'
		
	video_label = tk.Label(status, text = "Video Input Status: \t" + video_status_text)
	video_label.grid(row=1, column=0, sticky = tk.W, pady=20, padx=5)

def stop_detect():
	global timer, timer_time
	stop_detector.grid_forget()
	timer.destroy()
	timer_time = 0
	timer = tk.Label(root, text= str(timer_time) + 's')
	start_detector.grid(row=1, column=0, pady=10)
	view_result.grid(row=1, column=1, pady=10)

def lie_detect():
	global timer_time
	timer_time = 0
	start_detector.grid_forget()
	view_result.grid_forget()
	show_timer()
	stop_detector.grid(row=1, column=0, pady=10)
	
def view_results():
	pass

def show_timer():
	global timer_time 
	timer_time += 1
	timer.configure(text = str(timer_time) + 's')
	timer.after(1000, show_timer)
	timer.grid(row=1, column=1)
	
	
def about_app():
	about = tk.Toplevel()
	about.iconbitmap('eye.ico')
	
	heading = tk.Label(about, text='About Us', font=("Arial", 14))
	heading.grid(row=0, column=0, columnspan=2, pady=10)
	
	team = tk.Label(about, text='Team - LARN2121', font=("Arial", 11))
	team.grid(row=1, column=0, columnspan=2, pady=5)
	
	
	team1 = tk.Label(about, text='Arjun\nChengappa\nStudent PESU, Bangalore', font=("Arial", 10))
	team1.grid(row=2, column=0, padx=5, pady=5)

	team2 = tk.Label(about, text='Lavitra\nKsitij Madan\nStudent PESU, Bangalore', font=("Arial", 10))
	team2.grid(row=2, column=1, padx=5, pady=5)
	
	team3 = tk.Label(about, text='Nishta\nVarshney\nStudent PESU, Bangalore', font=("Arial", 10))
	team3.grid(row=3, column=0, padx=5, pady=5)
	
	team4 = tk.Label(about, text='Ritik\nHariani\nStudent PESU, Bangalore', font=("Arial", 10))
	team4.grid(row=3, column=1, padx=5, pady=5)
	
	description = tk.Label(about, text='Created by LARN2121 for Capstone Project(2022) under mentorship of\nProf. Ramamurty Srinath. Inteded for educational use only.')
	description.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

	copyright_ = tk.Label(about, text='©PES University, Bangalore', font=("Arial", 8))
	copyright_.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
	
	
def help_app():
	help_app = tk.Toplevel()
	help_app.iconbitmap('eye.ico')
	
	heading = tk.Label(help_app, text='HELP', font=("Arial", 15))
	heading.grid(row=0, column=0, pady=10)
	
	heading_1 = tk.Label(help_app, justify=tk.LEFT, text='Directions of Use', font=("Arial", 13))
	heading_1.grid(row=1, column=0, pady=5)
	
	running = tk.Label(help_app, justify=tk.LEFT, text='Running the Lie Detector:', font=("Arial", 11))
	running.grid(row=2, column=0, pady=2)
	
	running_ins = tk.Label(help_app, font=("Arial", 10), justify=tk.LEFT, text='- To Start the Lie Detector, click on "Start Detector".\n- A timer will start running. This timer shows the number\n  of seconds the detector has been running.\n- To stop the Lie Detector, click on "Stop Detector".\n- To view the results of the detector, click on "View Results".')
	running_ins.grid(row=3, column=0, pady=1)
	
	status = tk.Label(help_app, justify=tk.LEFT, text='Viewing the sensor status:', font=("Arial", 11))
	status.grid(row=4, column=0, pady=3)
	
	status_ins = tk.Label(help_app, font=("Arial", 10), justify=tk.LEFT, text='- To view the status of the camera, the microphone and other\n  sensors, click on the "File" on the Menu Bar.\n- Then click on "Check Status" in the dropdown menu.\n- This will open a new window displaying the status of all the\n  sensors.')
	status_ins.grid(row=5, column=0, pady=1)
	
	feedback = tk.Label(help_app, font=("Arial", 10), justify=tk.LEFT, text='Please feel free to raise an issue to the development team or\nsuggest changes.')
	feedback.grid(row=6, column=0, pady=3, padx=3)
	
	name_label = tk.Label(help_app, font=("Arial", 10), text='Enter Your Name and issue details')
	name_label.grid(row=7, column=0, pady=2, padx=4, sticky=tk.W)
	
	name = tk.Entry(help_app, width=20, )
	name.insert(0, 'Anonymous')
	name.grid(row=8, column=0, pady=2, padx=4, sticky=tk.W)
	
	details = tk.Text(help_app, width=35, height=4)
	details.insert(tk.INSERT, 'Raise an Issue or Suggest a change')
	details.grid(row=9, column=0, pady=2, padx=4, sticky=tk.W)
	
	def submit_issue():
		username = name.get()
		issue = details.get("1.0", tk.END)
		log = ",".join([username, issue])
		logs = open('logs', 'a')
		logs.write(log)
		logs.close()
		
		
	submit = tk.Button(help_app, text='Submit')
	submit.grid(row=10, column=0, pady=2, padx=4, sticky=tk.W)
	submit.configure(command=submit_issue)
	
	
	
	
width, height = 300, 150
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


root = tk.Tk()
root.iconbitmap('eye.ico')
root.title('LARN - Lie Detector')

show_menu()
lmain = tk.Label(root)
show_frame()

start_detector = tk.Button(root, text='Start Lie Detector', command=lie_detect)
start_detector.grid(row=1, column=0, pady=10)

stop_detector = tk.Button(root, text='Stop Lie Detector', command=stop_detect)

view_result = tk.Button(root, text='View Results', command=view_results)

timer_time = 0
timer = tk.Label(root, text= str(timer_time) + 's', pady=10)

root.mainloop()
cap.release()