import cv2
import mediapipe as mp
import numpy as np
from tkinter import *
import random
import time

player_name = "Prateek"
speed_level = 1 # Choose between 1, 2, and 3.

# Constants ------------------------------------------------------------------------------------------------------------
head_size = 100
neck_size = 10
eye_size = 10
sholder_length = 100
body_height = 200
fingure_size = 10
Body_parts = []
draw_man = FALSE

# Canvas settings ------------------------------------------------------------------------------------------------------
tk = Tk()

WIDTH = 800
HEIGHT = 500

canvas = Canvas(tk, width = WIDTH, height = HEIGHT)
tk.title("Game")
canvas.pack()

# Pose detection -------------------------------------------------------------------------------------------------------
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture(0)

# Game pre-requisites --------------------------------------------------------------------------------------------------
if speed_level == 1:
  x_speed = 10
  y_speed = 10

if speed_level == 2:
  x_speed = 15
  y_speed = 15

if speed_level > 2:
  x_speed = 20
  y_speed = 20

stick_height = 20
stick_length = 120

score = 0

ball_1 = canvas.create_oval(50, 50, 100, 100, fill = "black")
rect = canvas.create_rectangle(stick_height, stick_height, WIDTH - stick_height, HEIGHT - stick_height)
text = canvas.create_text(WIDTH*4/5, 10, fill="darkblue", font="Times 20 italic bold", text="Player: {}".format(player_name))

canvas.mainloop()
cap.release()
cv2.destroyAllWindows()