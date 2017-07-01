import numpy as np
from PIL import ImageGrab
import cv2
import time

last_time = time.time()

while(True):
    printscreen_pil = ImageGrab.grab(bbox=(10,20,640,400))
    #printscreen_numpy = np.array(printscreen_pil.getdata(),dtype='uint8').reshape((printscreen_pil.size[1],printscreen_pil.size[0],3))
# Debugging Loop
    print('Loop took {} seconds'.format(time.time()-last_time))
    last_time = time.time()

# Show Screen using cv2
    cv2.imshow('Python Plays Summoners War',np.array(printscreen_pil))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break