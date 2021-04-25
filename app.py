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
	helpmenu.add_command(label='Get Help')
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
	root.iconbitmap('eye.ico')
	
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