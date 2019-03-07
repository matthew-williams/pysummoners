import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

last_time = time.time()

def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1=200,threshold2=300)
    return processed_img






while(True):
    screen = np.array(ImageGrab.grab(bbox=(10,20,640,400)))
    processed_screen = process_img(screen)
# Debugging Loop
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

# Show Screen using cv2
    cv2.imshow('Processed Image',processed_screen)
    #cv2.imshow('Python Plays Summoners War', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord('q'):  # Press Q key to exit
        cv2.destroyAllWindows()
        break