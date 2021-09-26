import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import VideoRecorder as vr
from tkinter import filedialog

class App:
    def __init__(self, window, window_title="LARN", video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.ok=False
        self.time = 0
        self.timer_texts = ["Recording[|]", "Recording[/]", "Recording[-]", "Recording[\]"]
        self.filename = "No File Selected"

        # open video source (by default this will try to open the computer webcam)
        self.vid = vr.VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas.grid(column=0, row=0, columnspan=4, padx=5, pady=5)

        #video control buttons
        self.btn_start=tk.Button(window, text='Start', command=self.open_camera)
        self.btn_start.grid(column=0, row=1, padx=5, pady=5)

        self.btn_stop=tk.Button(window, text='Stop', command=self.close_camera)
        self.btn_stop.grid(column=1, row=1, padx=5, pady=5)
        self.btn_stop["state"] = "disabled"

        self.label_timer=tk.Label(self.window, text="%ss"%self.time)
        self.label_timer.grid(column=2, row=1, padx=5, pady=5)

        self.timer_animation = tk.Label(self.window, text="Not Recording")
        self.timer_animation.grid(column=3, row=1, padx=5, pady=5)

        # quit button
        
        self.btn_upload=tk.Button(window, text='Upload Video', command=self.upload_video)
        self.btn_upload.grid(column=0, row=2, padx=5, pady=5)

        self.filename_label = tk.Label(self.window, text=self.filename)
        self.filename_label.grid(column=1, row=2, padx=5, pady=5)

        self.btn_analyse=tk.Button(window, text='Analyse', command=self.analyse)
        self.btn_analyse.grid(column=0, row=3, padx=5, pady=5)
        self.btn_analyse["state"] = "disabled"
        


        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay=10
        self.update()

        self.window.mainloop()


    def open_camera(self):
        self.ok = True
        self.btn_start["state"] = "disabled"
        self.btn_stop["state"] = "normal"
        print("Recording video ...")

        self.time = 0

        self.label_timer=tk.Label(self.window, text="%ss"%self.time)
        self.label_timer.grid(column=2, row=1, padx=5, pady=5)

        self.timer_animation = tk.Label(self.window, text=self.timer_texts[0])
        self.timer_animation.grid(column=3, row=1, padx=5, pady=5)

        self.label_timer.after(1000, self.timer)
        
    
    def timer(self):
        self.time += 1
        self.label_timer.configure(text="%ss"%self.time)
        self.timer_animation.configure(text=self.timer_texts[self.time%3])
        self.label_timer.after(1000, self.timer)

    def analyse(self):
        #video_name = self.vid.video_name
        pass

    def close_camera(self):
        self.ok = False
        self.btn_start["state"] = "normal"
        self.btn_stop["state"] = "disabled"
        self.btn_analyse["state"] = "normal"
        print("Recording Stopped")
        print("Video Name: " + self.vid.video_name)
        print("Video Length: %ss"%self.time)
        
        self.label_timer.destroy()
        self.timer_animation.destroy()

        self.label_timer=tk.Label(self.window, text="%ss"%self.time)
        self.label_timer.grid(column=2, row=1, padx=5, pady=5)

        self.timer_animation = tk.Label(self.window, text="Not Recording")
        self.timer_animation.grid(column=3, row=1, padx=5, pady=5)

        self.filename = "Live Recording Selected"
        self.filename_label.configure(text=self.filename)

    def upload_video(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File",filetypes = [("Video Files",".avi .mp4")])
        self.filename_label.configure(text=self.filename)

        self.btn_analyse["state"] = "normal"
        
        
       
    def update(self):

        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if self.ok:
            self.vid.out.write(cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tk.NW)
        self.window.after(self.delay,self.update)

App(tk.Tk())