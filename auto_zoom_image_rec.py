# automatic joining zoom script

# TODO:
"""

fix the pre-join camera off image search
optimize pre-join camera off image search time
perfect the time for meeting detection while loop

"""

import pyautogui
import time
import pyperclip

# getting meeting id
meeting_ID = input('meeting id / class name / clipboard: ')
meeting_name = 'zoom'
if meeting_ID == 'clipboard':
    meeting_ID = pyperclip.paste()
    meeting_name = 'zoom'
if meeting_ID == 'calc':
    meeting_ID = '951-444-09514'
    meeting_name = 'calculus'

# getting password
is_password = input('is there a password to the meeting (y / n)?: ')
password = ''
if is_password == 'y':
    password = input('enter the password to the meeting: ')

# determine os
os = input('which operating system are you using (windows / mac)?: ')

# automation
time.sleep(1)

# search for zoom
if os == 'mac':
    pyautogui.hotkey('command', 'space')
    time.sleep(0.75)
if os == 'windows':
    pyautogui.hotkey('win')
    time.sleep(0.75)

# type zoom
pyautogui.typewrite('Zoom', interval=0.05)
time.sleep(1)

# open zoom
pyautogui.hotkey('enter')

# join a meeting button
while True:
    pyautogui.screenshot()
    join_button = pyautogui.locateCenterOnScreen('join_button.png')
    if join_button is not None:
        x, y = pyautogui.locateCenterOnScreen('join_button.png')
        pyautogui.click(x, y)
        time.sleep(1)
        break

# enter meeting id
pyautogui.typewrite(meeting_ID, interval=0.05)

# turn off camera pre-join
if is_password == 'n':
    pyautogui.screenshot(region=(700, 280, 300, 300))
    x, y = pyautogui.locateCenterOnScreen('pre_join_cam_off.png')
    time.sleep(1)

# join meeting
pyautogui.screenshot(region=(350, 140, 1555, 920))
x, y = pyautogui.locateCenterOnScreen('join_meeting_button.png')
pyautogui.click(x, y)
time.sleep(1.5)

# entering password
if is_password == 'y':
    pyautogui.typewrite(password, interval=0.05)

# join with password
if is_password == 'y':
    x, y = pyautogui.locateCenterOnScreen('join_with_password_button.png')
    pyautogui.click(x, y)

# join with camera prompt
while True:
    pyautogui.screenshot(region=(350, 140, 1555, 920))
    join_without_video_button = pyautogui.locateCenterOnScreen('join_without_video_button.png')
    if join_without_video_button is not None:
        pyautogui.screenshot(region=(350, 140, 1555, 920))
        x, y = pyautogui.locateCenterOnScreen('join_without_video_button.png')
        pyautogui.click(x, y)
        break

# check if joined
i = 0
while i < 30:
    pyautogui.screenshot()
    in_meeting = pyautogui.locateOnScreen('leave_button.png')
    if in_meeting:
        print('meeting detected')
        # microphone
        while True:
            pyautogui.screenshot()
            unmuted_microphone = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
            if unmuted_microphone is not None:
                x, y = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
                pyautogui.click(x, y)
                break

        # full screen
        while True:
            pyautogui.moveRel(50, 0, duration=1)
            pyautogui.screenshot()
            full_screen_button = pyautogui.locateCenterOnScreen('full_screen_button.png')
            if full_screen_button is not None:
                x, y = pyautogui.locateCenterOnScreen('full_screen_button.png')
                pyautogui.click(x, y)
                break

        # all done message for password
        print('welcome to your {} meeting'.format(meeting_name))
        exit()
    if in_meeting is None:
        print('no meeting detected yet')
        print('{} checks for meeting'.format(i))
        i += 1
