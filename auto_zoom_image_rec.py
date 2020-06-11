# automatic joining zoom script

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
is_password = input('is there a password to this meeting (y / n)?: ')
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
    time.sleep(0.5)
if os == 'windows':
    pyautogui.hotkey('win')
    time.sleep(0.5)


# type zoom
pyautogui.typewrite('Zoom', interval=0.15)
time.sleep(0.5)


# open zoom
pyautogui.hotkey('enter')
time.sleep(2)


# join a meeting button
pyautogui.screenshot(region=(450, 240, 300, 300))
x, y = pyautogui.locateCenterOnScreen('join_button.png')
pyautogui.click(x, y)
time.sleep(1)


# enter meeting id
pyautogui.typewrite(meeting_ID, interval=0.05)


# turn off camera pre join
if is_password == 'n':
    pyautogui.screenshot(region=(450, 240, 500, 500))
    x, y = pyautogui.locateCenterOnScreen('pre_join_cam_off.png')
    time.sleep(1)


# join meeting
pyautogui.screenshot(region=(450, 240, 300, 300))
x, y = pyautogui.locateCenterOnScreen('join_meeting_button.png')
pyautogui.click(x, y)
time.sleep(1.5)


# check if joined
pyautogui.screenshot()
in_meeting = pyautogui.locateOnScreen('leave_button.png')
if in_meeting:
    print('meeting detected')
    print('welcome to your {} meeting'.format(meeting_name))
    exit()
if not in_meeting:
    print('no meeting detected yet')


# entering password
if is_password == 'y':
    pyautogui.typewrite(password)


# join with password
if is_password == 'y':
    x, y = pyautogui.locateCenterOnScreen('join_with_password_button.png')
    pyautogui.click(x, y)
    time.sleep(3)


# join with camera prompt
pyautogui.screenshot(region=(450, 240, 500, 500))
x, y = pyautogui.locateCenterOnScreen('join_without_video_button.png')
pyautogui.click(x, y)


# microphone
pyautogui.screenshot()
ready = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
while not ready:
    pyautogui.screenshot()
    if pyautogui.locateCenterOnScreen('unmuted_microphone.png'):
        x, y = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
        pyautogui.click(x, y)
        break


# full screen
pyautogui.moveRel(50, 0, duration=1)
pyautogui.screenshot()
x, y = pyautogui.locateCenterOnScreen('full_screen_button.png')
pyautogui.click(x, y)


# all done message for password
print('welcome to your {} meeting'.format(meeting_name))
