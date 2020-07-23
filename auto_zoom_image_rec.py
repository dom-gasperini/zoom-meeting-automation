# automatic zoom call join script

import pyautogui
import time
import pyperclip
import platform

# getting the meeting id
meeting_ID = input('meeting id / class name / clipboard: ')
meeting_name = 'zoom'
if meeting_ID == 'clipboard':
    meeting_ID = pyperclip.paste()
    meeting_name = 'zoom'
if meeting_ID == 'calc':
    meeting_ID = '951-444-09514'
    meeting_name = 'calculus'

# getting the meeting password
is_password = input('is there a password to the meeting (y / n)?: ')
password = ''
if is_password == 'y':
    password = input('enter the password to the meeting: ')

# getting meeting length
num_of_hours = int(input('how long is the meeting going to last (in hours): '))
meeting_length = num_of_hours * 360

# determine user os
os = platform.system()
if os == "Windows":
    print("looks like you're running on Windows")
elif os == "Darwin":
    print("looks like you're running on MacOS")
else:
    print("Unidentified operating system, the program cannot continue to run \nexiting now")
    time.sleep(0.5)
    exit()

# automation start delay
time.sleep(1)

# pressing search hot key
if os == 'Darwin':
    pyautogui.hotkey('command', 'space')
    time.sleep(0.75)
if os == 'Windows':
    pyautogui.hotkey('win')
    time.sleep(0.75)

# typing zoom
pyautogui.typewrite('Zoom', interval=0.05)
time.sleep(1)

# opening zoom
pyautogui.hotkey('enter')

# find and click the join a meeting button
for i in range(30):
    pyautogui.screenshot()
    join_button = pyautogui.locateCenterOnScreen('join_button.png')
    if join_button is not None:
        x, y = pyautogui.locateCenterOnScreen('join_button.png')
        pyautogui.click(x, y)
        time.sleep(1)
        break

# entering the meeting id
time.sleep(0.5)
pyautogui.typewrite(meeting_ID, interval=0.05)

# find and select the turn off camera pre-join
if is_password == 'n':
    pyautogui.screenshot()  # region=(700, 280, 300, 300)
    x, y = pyautogui.locateCenterOnScreen('pre_join_cam_off.png')
    time.sleep(1)

# find and select the join meeting
for i in range(30):
    pyautogui.screenshot()  # region=(350, 140, 1555, 920)
    join_meeting_button = pyautogui.locateCenterOnScreen('join_meeting_button.png')
    if join_meeting_button is not None:
        x, y = pyautogui.locateCenterOnScreen('join_meeting_button.png')
        pyautogui.click(x, y)
        time.sleep(1.5)
        break

# entering the meeting password
if is_password == 'y':
    pyautogui.typewrite(password, interval=0.05)

    # join with password
    x, y = pyautogui.locateCenterOnScreen('join_with_password_button.png')
    pyautogui.click(x, y)

# find and click the join with camera prompt
for i in range(30):
    pyautogui.screenshot()  # region=(350, 140, 1555, 920)
    join_without_video_button = pyautogui.locateCenterOnScreen('join_without_video_button.png')
    if join_without_video_button is not None:
        pyautogui.screenshot()  # region=(350, 140, 1555, 920)
        x, y = pyautogui.locateCenterOnScreen('join_without_video_button.png')
        pyautogui.click(x, y)
        break

# check if user has joined the meeting
for i in range(45):
    pyautogui.screenshot()
    in_meeting = pyautogui.locateOnScreen('leave_button.png')
    if in_meeting:
        print('meeting detected')
        # microphone
        for z in range(30):
            pyautogui.screenshot()
            unmuted_microphone = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
            if unmuted_microphone is not None:
                x, y = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
                pyautogui.click(x, y)
                break
        # find and select the full screen button
        for j in range(3):
            pyautogui.moveRel(50, 0, duration=1)
            pyautogui.screenshot()
            full_screen_button = pyautogui.locateCenterOnScreen('full_screen_button.png')
            if full_screen_button is not None:
                x, y = pyautogui.locateCenterOnScreen('full_screen_button.png')
                pyautogui.click(x, y)
                break
        # all done message for joined meeting
        print('welcome to your {} meeting'.format(meeting_name))
        exit()  # remove when breakout room shit is done!!!
    if in_meeting is None:
        print('no meeting detected yet')
        if i > 1:
            print('{} checks for a meeting'.format(i))
        if i == 1:
            print('{} check for a meeting'.format(i))
        # failed to find a meeting message
        if i == 45:
            print('failed to find a meeting after {} checks, exiting the program now'.format(i))

seconds = 0
while seconds < meeting_length:
    # entering breakout rooms mid-meeting
    while True:
        pyautogui.screenshot()
        breakout_room_join_button = pyautogui.locateCenterOnScreen('breakout_room_join_button.png')
        breakout_room_join_button_new = pyautogui.locateCenterOnScreen('breakout_room_join_button_new.png')
        if breakout_room_join_button or breakout_room_join_button_new is not None:
            try:
                x, y = pyautogui.locateCenterOnScreen('breakout_room_join_button.png')
            except None:
                x, y = pyautogui.locateCenterOnScreen('breakout_room_join_button_new.png')
            pyautogui.click(x, y)
            break
    # exiting breakout rooms mid-meeting
    while True:
        pyautogui.screenshot()
        breakout_room_join_button = pyautogui.locateCenterOnScreen('breakout_room_return_to_main_button.')
        if breakout_room_join_button is not None:
            x, y = pyautogui.locateCenterOnScreen('breakout_room_return_to_main_button.jpg')
            pyautogui.click(x, y)
            break
    # meeting auto logout adding timer
    seconds += 1
    time.sleep(1)

# auto logout of meeting after timer
for i in range(30):
    pyautogui.moveRel(50, 0, duration=1)
    pyautogui.screenshot()
    leave_meeting_button = pyautogui.locateCenterOnScreen('leave_button.png')
    if leave_meeting_button is not None:
        x, y = pyautogui.locateCenterOnScreen('leave_button.png')
        pyautogui.click(x, y)
        for j in range(30):
            pyautogui.screenshot()
            actually_leave_meeting_button = pyautogui.locateCenterOnScreen('actually_leave_meeting_button.png')
            if actually_leave_meeting_button is not None:
                x, y = pyautogui.locateCenterOnScreen('actually_leave_meeting_button.png')
                pyautogui.click(x, y)
                break
        break

print('automatically logged out of the meeting after 3 hours \nhave a nice day!')
