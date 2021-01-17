# importing libraries
# import cv2
# import pygame
from socket import close
import vlc
import time
import queue
from pynput.keyboard import Key, Listener
# from ffpyplayer.player import MediaPlayer
# import numpy as np

fileName = "./media/Demo.mp4"
windowName = "Player"

player = None
moviePosition = None
videoPaused = False
closeVideo = False


def createPlayer(filename):
    global player
    player = vlc.MediaPlayer(filename)


def playVideo():
    global player
    global closeVideo

    status = player.play()

    time.sleep(2)

    if status == 0:
        while player.is_playing:
          if closeVideo:
            break


def pauseVideo():
    global moviePosition
    global player
    global videoPaused

    player.pause()

    if videoPaused:
        print('Setting player position')
        player.set_position(moviePosition)
        time.sleep(2)

    else:
        moviePosition = player.get_position()

    videoPaused = not videoPaused


def onPress(key):
    global player
    global closeVideo

    if hasattr(key, 'char'):
        if key.char == 'q':
            closeVideo = True
            exit()
    elif key == Key.space:
        pauseVideo()


def onRelease(key):
    pass


# Setup key listener
with Listener(on_press=onPress, on_release=onRelease) as listener:
    createPlayer(fileName)
    playVideo()
    listener.join()

# # creating a vlc instance
# vlc_instance = vlc.Instance()

# # creating a media player
# player = vlc_instance.media_player_new()

# # creating a media
# media = vlc_instance.media_new(fileName)

# # setting media to the player
# player.set_media(media)

# # play the video
# player.play()

# wait time
# time.sleep(6111)

# getting the duration of the video
# duration = player.get_length()

# printing the duration of the video
# print("Duration : " + str(duration))
""" 
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(fileName) 
# player = MediaPlayer('Demo.mp4')
   
# Check if camera opened successfully 
if (cap.isOpened()== False):  
  print("Error opening video  file") 

cv2.namedWindow(windowName, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(windowName, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

temp = None
flag = True

# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS) 

# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

frame_number = 0
# cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number) # optional

# Setup up audio
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(fileName)


# Read until video is completed 
while(cap.isOpened()): 
      
  # Capture frame-by-frame 
  ret, frame = cap.read() 
  # audio_frame, val = player.get_frame()
  
  if ret == True:    
    # Display the resulting frame 
    cv2.imshow('Player', frame)
    pygame.mixer.music.play() 

    frame_number = frame_number + 1
    # if val != 'eof' and audio_frame is not None:
    #   #audio
    #   img, t = audio_frame

    key = cv2.waitKey(24)

    if key == 32:
      pygame.mixer.music.pause() # Press spacebar on keyboard to pause 
      cv2.waitKey()
      key = None
      # cap.set(cv2.CAP_PROP_POS_FRAMES, 2000)
      pygame.mixer.music.unpause()
    elif key == ord('q'): # Press Q on keyboard to  exit 
        break
   
  # Break the loop 
  else:  
    break
   
# When everything done, release  
# the video capture object 
cap.release() 
   
# Closes all the frames 
cv2.destroyAllWindows()  """
