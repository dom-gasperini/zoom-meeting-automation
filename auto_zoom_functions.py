# imports
import pyautogui
import time
import pyperclip
import platform

# global variables
global os, password, meeting_id


def get_meeting_id():
    global meeting_id
    meeting_id = input('meeting id / class name / clipboard: ')
    meeting_name = 'zoom call'
    if meeting_id == 'clipboard':
        meeting_id = pyperclip.paste()
        meeting_name = 'zoom call'
    if meeting_id == 'calc':
        meeting_id = '951-444-09514'
        meeting_name = 'calculus'
    return meeting_id


def get_password():
    global password
    is_password = input('is there a password to the meeting (y / n)?: ')
    password = ''
    if is_password == 'y':
        password = input('enter the password to the meeting: ')
    return password, is_password


def get_meeting_length():
    num_of_hours = int(input('how long is the meeting going to last (in hours): '))
    meeting_length = num_of_hours * 360


def get_os():
    global os
    os = platform.system()
    if os == "Windows":
        print("looks like you're running on Windows")
    elif os == "Darwin":
        print("looks like you're running on MacOS")
    else:
        print("Unidentifiable operating system, the program cannot continue to run")
        print('exiting now')
        exit()
    return os


def search_via_command_key():
    if os == 'Darwin':
        pyautogui.hotkey('command', 'space')
        time.sleep(0.75)
    if os == 'Windows':
        pyautogui.hotkey('win')
        time.sleep(0.75)


def join():
    for i in range(30):
        pyautogui.screenshot()
        join_button = pyautogui.locateCenterOnScreen('join_button.png')
        if not join_button:
            join_attempts = 1
            print('{} failed attempts to find the join button'.format(join_attempts))
            join_attempts += 1
        if join_button is not None:
            x, y = pyautogui.locateCenterOnScreen('join_button.png')
            pyautogui.click(x, y)
            time.sleep(1)
            break
        if i == 30:
            print('error: cannot find the "join" button')
            print('exiting the program')
            exit()


def join_with_password():
    if get_password.ispassword == 'y':
        pyautogui.typewrite(password, interval=0.05)
        # join with the password
        x, y = pyautogui.locateCenterOnScreen('join_with_password_button.png')
        pyautogui.click(x, y)


def pre_join_camera():
    if get_password.ispassword == 'n':
        for i in range(30):
            pyautogui.screenshot()  # region=(700, 280, 300, 300)
            pre_join_camera_button = pyautogui.locateCenterOnScreen('pre_join_cam_off.png')
            if not pre_join_camera_button:
                join_meeting_attempts = 1
                print('{} failed attempts to find the join meeting button'.format(join_meeting_attempts))
            if pre_join_camera_button is not None:
                x, y = pyautogui.locateCenterOnScreen('join_meeting_button.png')
                pyautogui.click(x, y)
                time.sleep(1.5)
                break
            time.sleep(1)
            if i == 30:
                print('error: cannot find the "camera off" button')
                print('exiting the program')
                exit()


def join_meeting():
    for i in range(30):
        pyautogui.screenshot()  # region=(350, 140, 1555, 920)
        join_meeting_button = pyautogui.locateCenterOnScreen('join_meeting_button.png')
        if not join_meeting_button:
            join_meeting_attempts = 1
            print('{} failed attempts to find the join meeting button'.format(join_meeting_attempts))
            join_meeting_attempts += 1
        if join_meeting_button is not None:
            x, y = pyautogui.locateCenterOnScreen('join_meeting_button.png')
            pyautogui.click(x, y)
            time.sleep(1.5)
            break
        if i == 30:
            print('error: cannot find the "join meeting" button')
            print('exiting the program')
            exit()


def join_without_video():
    for i in range(30):
        pyautogui.screenshot()  # region=(350, 140, 1555, 920)
        join_without_video_button = pyautogui.locateCenterOnScreen('join_without_video_button.png')
        if not join_without_video_button:
            join_without_video_attempts = 1
            print('{} failed attempts to find the join without video button'.format(join_without_video_attempts))
            join_without_video_attempts += 1
        if join_without_video_button is not None:
            pyautogui.screenshot()  # region=(350, 140, 1555, 920)
            x, y = pyautogui.locateCenterOnScreen('join_without_video_button.png')
            pyautogui.click(x, y)
            break
        if i == 30:
            print('error: cannot find the "join without video" button')
            print('exiting the program')
            exit()


def meeting_check():
    for i in range(45):
        pyautogui.screenshot()
        in_meeting = pyautogui.locateOnScreen('leave_button.png')
        if in_meeting is None:
            print('no meeting detected yet')
            if i > 1:
                print('{} checks for a meeting'.format(i))
            if i == 1:
                print('{} check for a meeting'.format(i))
        if in_meeting:
            print('meeting detected')
        if i == 45:
            print('failed to find a meeting after {} checks, exiting the program now'.format(i))
            print('error: cannot detect a meeting')
            print('exiting the program')
            exit()


def microphone():
    for i in range(30):
        pyautogui.screenshot()
        unmuted_microphone = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
        if not unmuted_microphone:
            microphone_attempts = 1
            print('{} failed attempts to find the mute microphone button'.format(microphone_attempts))
            microphone_attempts += 1
        if unmuted_microphone is not None:
            x, y = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
            pyautogui.click(x, y)
            break
        if i == 30:
            print('error: cannot find the "mute microphone" button')
            print('exiting the program')
            exit()


def full_screen():
    for i in range(5):
        pyautogui.moveRel(50, 0, duration=1)
        pyautogui.screenshot()
        full_screen_button = pyautogui.locateCenterOnScreen('full_screen_button.png')
        if not full_screen_button:
            full_screen_attempts = 1
            print('{} failed attempts to find the full screen button'.format(full_screen_attempts))
            full_screen_attempts += 1
        if full_screen_button is not None:
            x, y = pyautogui.locateCenterOnScreen('full_screen_button.png')
            pyautogui.click(x, y)
            break
        if i == 5:
            print('error: cannot find the "full screen" button')
            print('exiting the program')
            exit()


def join_breakout():
    while True:
        pyautogui.screenshot()
        breakout_room_join_button = pyautogui.locateCenterOnScreen('breakout_room_join_button.png')
        if not breakout_room_join_button:
            join_breakout_attempts = 1
            print('{} attempts to find the join breakout room button'.format(join_breakout_attempts))
            join_breakout_attempts += 1
            time.sleep(15)
        if breakout_room_join_button is not None:
            x, y = pyautogui.locateCenterOnScreen('breakout_room_join_button')
            pyautogui.click(x, y)
            break


def leave_breakout():
    while True:
        pyautogui.screenshot()
        breakout_room_return_to_main_button = pyautogui.locateCenterOnScreen('breakout_room_return_to_main_button.jpg')
        if not breakout_room_return_to_main_button:
            leave_breakout_attempts = 1
            print('{} attempts to find the leave breakout room button'.format(leave_breakout_attempts))
            leave_breakout_attempts += 1
            time.sleep(15)
        if breakout_room_return_to_main_button is not None:
            x, y = pyautogui.locateCenterOnScreen('breakout_room_return_to_main_button.jpg')
            pyautogui.click(x, y)
            break


def auto_logout():
    for i in range(30):
        pyautogui.moveRel(50, 0, duration=1)
        pyautogui.screenshot()
        leave_meeting_button = pyautogui.locateCenterOnScreen('leave_meeting_button')
        if leave_meeting_button is not None:
            x, y = pyautogui.locateCenterOnScreen('')
            pyautogui.click(x, y)
            for j in range(30):
                pyautogui.screenshot()
                actually_leave_meeting_button = pyautogui.locateCenterOnScreen('')
                if actually_leave_meeting_button is not None:
                    x, y = pyautogui.locateCenterOnScreen('actually_leave_meeting_button.png')
                    pyautogui.click(x, y)
                    break
            break
    print('automatically logged out of the meeting after 3 hours \n have a nice day!')