import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import VideoRecorder as vr
from tkinter import PhotoImage, filedialog
import socket
import tqdm
import os
import time

class App:
	def __init__(self, window, window_title="LARN Lie Detector", video_source=0):
		#creating the app
		self.window = window
		self.window.title(window_title)
		self.video_source = video_source

		#initiating the variables
		self.ok=False
		self.filename = "No File Selected"
		self.up_or_rec = 0

		# open video source (by default this will try to open the computer webcam)

		# Create a canvas that can fit the above video source size
		self.canvas = tk.Canvas(window, width = 640, height = 480)
		self.canvas.grid(column=0, row=0, columnspan=4, padx=5, pady=5)
		img = PhotoImage(file="img.png")
		self.canvas_container = self.canvas.create_image(0,0,image=img, anchor=tk.NW)

		#video control section
		self.btn_start=tk.Button(window, text='Start', command=self.open_camera)
		self.btn_start.grid(column=0, row=1, padx=5, pady=5)

		self.btn_stop=tk.Button(window, text='Stop', command=self.close_camera)
		self.btn_stop.grid(column=1, row=1, padx=5, pady=5)
		self.btn_stop["state"] = "disabled"

		self.recording_label = tk.Label(self.window, text="Not Recording", fg="green")
		self.recording_label.grid(column=3, row=1, padx=5, pady=5)

		#upload video section
		self.btn_upload=tk.Button(window, text='Upload Video', command=self.upload_video)
		self.btn_upload.grid(column=0, row=2, padx=5, pady=5)

		self.video_label = tk.Label(self.window, text="Video Selected:")
		self.video_label.grid(column=1, row=2, padx=5, pady=5)

		self.filename_label = tk.Label(self.window, text=self.filename)
		self.filename_label.grid(column=2, row=2, columnspan=2, padx=5, pady=5)

		#analyse section
		self.btn_analyse=tk.Button(window, text='Analyse', command=self.analyse)
		self.btn_analyse.grid(column=0, row=3, padx=5, pady=5)
		self.btn_analyse["state"] = "disabled"
		
		self.result_label = tk.Label(self.window, text="")
		self.result_label.grid(column=1, row=3, padx=5, pady=5)
		
		self.time_taken_label = tk.Label(self.window, text="Time Taken:")
		self.time_taken_label.grid(column=2, row=3, padx=5, pady=5)
		
		self.time_label = tk.Label(self.window, text="-")
		self.time_label.grid(column=3, row=3, padx=5, pady=5)


		# After it is called once, the update method will be automatically called every delay milliseconds

		self.window.mainloop()


	def open_camera(self):
		self.vid = vr.VideoCapture(self.video_source)
		self.ok = True

		#change button states
		self.btn_start["state"] = "disabled"
		self.btn_stop["state"] = "normal"
		self.btn_analyse["state"] = "disabled"
		self.btn_upload["state"] = "disabled"

		#changing label
		self.recording_label.configure(text="Recording", fg="red")

		#logging process in terminal
		print("Recording video ...")

		self.delay=10
		self.update()

	def analyse(self):
		self.btn_analyse["state"] = "disabled"
		
		if self.up_or_rec == 0:
			pass
		self.result_label.configure(text="Calculating...")
		SEPARATOR = "<SEPARATOR>"
		BUFFER_SIZE = 1024 * 4 #4KB
		CLIENT_ADDR = socket.gethostbyname(socket.gethostname())
		host = '127.0.0.1'
		port = 8080
		filesize = os.path.getsize(self.path)
	    # create the client socket
		s = socket.socket()
		print(f"[+] Connecting to {host}:{port}")
		s.connect((host, port))
		print("[+] Connected.")

	    # send the filename and filesize
		s.send(f"{CLIENT_ADDR}{SEPARATOR}{self.filename}{SEPARATOR}{filesize}".encode())
		# start sending the file
		progress = tqdm.tqdm(range(filesize), 
						  f"Sending {self.filename}", 
						  unit="B", unit_scale=True, 
						  unit_divisor=1024, 
						  leave=False)
		with open(self.path, "rb") as f:
			while True:
				# read the bytes from the file
				bytes_read = f.read(BUFFER_SIZE)
				if not bytes_read:
					# file transmitting is done
					break
				# we use sendall to assure transimission in 
				# busy networks
				s.sendall(bytes_read)
				# update the progress bar
				progress.update(len(bytes_read))
		# close the sockets
		s.close()
		begin = time.time()
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.bind((CLIENT_ADDR, 8040))
		data, addr = s.recvfrom(1024)
		self.result = data.decode()
		end = time.time()
		color = 'red'
		if self.result == 'Truth':
			color = 'green'
		
		time_taken = time.strftime("%Hh%Mm%Ss", time.gmtime(end-begin))
		self.result_label.configure(text=data, fg=color)
		self.time_label(text=time_taken)
		self.post_analysis_clean()
		
	def post_analysis_clean(self):
		if self.up_or_rec == 1:
			os.remove(self.filename)
		
		

	def close_camera(self):
		self.ok = False

		#updating button states
		self.btn_start["state"] = "normal"
		self.btn_stop["state"] = "disabled"
		self.btn_analyse["state"] = "normal"
		self.btn_upload["state"] = "normal"

		#changing label
		self.recording_label.configure(text="Not Recording", fg="green")

		#logging process to terminal
		print("Recording Stopped")
		print("Video Name: " + self.vid.video_name)
		
		#displaying the name of the saved video
		self.filename = self.vid.video_name + '.avi'
		self.path = self.filename
		self.filename_label.configure(text=self.filename)
		self.up_or_rec = 1
		self.vid.__del__()
		

	def upload_video(self):
		#taking the input from the user
		self.filename_upload = filedialog.askopenfilename(initialdir = "../", title = "Select a File",filetypes = [("Video Files",".avi .mp4")])
		self.path = self.filename_upload
		self.filename = os.path.basename(self.path)
		self.filename_label.configure(text=self.filename[:30])
		self.up_or_rec = -1

		#updating the button states
		self.btn_analyse["state"] = "normal"
		
		
	   
	def update(self):
		# Get a frame from the video source
		ret, frame = self.vid.get_frame()
		if self.ok:
			self.vid.out.write(cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
		else:
			return None

		if ret:
			self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
			self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
		self.window.after(self.delay,self.update)

App(tk.Tk())