# importing libraries 
# import cv2 
# import pygame
import vlc, time
# from ffpyplayer.player import MediaPlayer
# import numpy as np 

fileName = "Demo.mp4"
windowName = "Player"

media = vlc.MediaPlayer(fileName)
media.play()

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
time.sleep(6111)
  
# getting the duration of the video
duration = player.get_length()
  
# printing the duration of the video
print("Duration : " + str(duration))
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