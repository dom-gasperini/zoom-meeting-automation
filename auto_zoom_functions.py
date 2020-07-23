# imports
import pyautogui
import time
import pyperclip
import platform

# global variables
global os, password, meeting_length, meeting_name


def get_meeting_id():
    global meeting_name
    get_meeting_id.meeting_id = input('meeting id / class name / clipboard: ')
    meeting_name = 'zoom call'
    if get_meeting_id.meeting_id == 'clipboard':
        get_meeting_id.meeting_id = pyperclip.paste()
        meeting_name = 'zoom call'
    if get_meeting_id.meeting_id == 'calc':
        get_meeting_id.meeting_id = '951-444-09514'
        meeting_name = 'calculus'


def get_password():
    global password
    get_password.is_password = input('is there a password to the meeting (y / n)?: ')
    password = ''
    if get_password.is_password == 'y':
        password = input('enter the password to the meeting: ')


def get_meeting_length():
    global meeting_length
    num_of_hours = int(input('how long is the meeting going to last (in hours): '))
    get_meeting_length.meeting_length = num_of_hours * 360


def get_os():
    global os
    os = platform.system()
    if os == "Windows":
        print("looks like you're running on Windows")
    elif os == "Darwin":
        print("looks like you're running on MacOS")
    else:
        print("Unidentified operating system, the program cannot continue to run \nexiting now")
        time.sleep(0.5)
        exit()


def search_via_command_key():
    if os == 'Darwin':
        pyautogui.hotkey('command', 'space')
        time.sleep(0.75)
    if os == 'Windows':
        pyautogui.hotkey('win')
        time.sleep(0.75)


def join():
    for i in range(1, 31):
        pyautogui.screenshot()
        join_button = pyautogui.locateCenterOnScreen('join_button.png')
        if not join_button:
            print('{} failed attempts to find the join button'.format(i))
        if join_button is not None:
            x, y = pyautogui.locateCenterOnScreen('join_button.png')
            pyautogui.click(x, y)
            time.sleep(1)
            break
        if i == 30:
            print('failed to find the "join" button after {} attempts \nexiting the program'.format(i))
            exit()


def join_with_password():
    if get_password.is_password == 'y':
        pyautogui.typewrite(get_password.is_password, interval=0.05)
        for i in range(1, 31):
            pyautogui.screenshot()
            join_with_password_button = pyautogui.locateCenterOnScreen('join_with_password_button.png')
            if join_with_password_button is not None:
                x, y = pyautogui.locateCenterOnScreen('join_with_password_button.png')
                pyautogui.click(x, y)


def pre_join_camera():
    if get_password.is_password == 'n':
        for i in range(1, 31):
            pyautogui.screenshot()
            pre_join_camera_button = pyautogui.locateCenterOnScreen('pre_join_cam_off.png')
            if not pre_join_camera_button:
                print('{} failed attempts to find the join meeting button'.format(i))
            if pre_join_camera_button is not None:
                x, y = pyautogui.locateCenterOnScreen('join_meeting_button.png')
                pyautogui.click(x, y)
                time.sleep(1.5)
                break
            time.sleep(1)
            if i == 30:
                print('failed to find the "camera off" button after {} attempts \nexiting the program'.format(i))
                exit()


def join_meeting():
    for i in range(1, 31):
        pyautogui.screenshot()  # region=(350, 140, 1555, 920)
        join_meeting_button = pyautogui.locateCenterOnScreen('join_meeting_button.png')
        if not join_meeting_button:
            print('{} failed attempts to find the join meeting button'.format(i))
        if join_meeting_button is not None:
            x, y = pyautogui.locateCenterOnScreen('join_meeting_button.png')
            pyautogui.click(x, y)
            time.sleep(1.5)
            break
        if i == 30:
            print('failed to find the "join meeting" button after {} attempts \nexiting the program'.format(i))
            exit()


def join_without_video():
    for i in range(1, 31):
        pyautogui.screenshot()  # region=(350, 140, 1555, 920)
        join_without_video_button = pyautogui.locateCenterOnScreen('join_without_video_button.png')
        if not join_without_video_button:
            print('{} failed attempts to find the join without video button'.format(i))
        if join_without_video_button is not None:
            pyautogui.screenshot()  # region=(350, 140, 1555, 920)
            x, y = pyautogui.locateCenterOnScreen('join_without_video_button.png')
            pyautogui.click(x, y)
            break
        if i == 30:
            print('failed to find the "join without video" button after {} attempts \nexiting the program'.format(i))
            exit()


def meeting_check():
    for i in range(1, 46):
        pyautogui.screenshot()
        in_meeting = pyautogui.locateOnScreen('leave_button.png')
        if in_meeting is None:
            print('no meeting detected yet')
            if i == 1:
                print('{} check for a meeting'.format(i))
            if i > 1:
                print('{} checks for a meeting'.format(i))
        if in_meeting:
            print('meeting detected')
        if i == 45:
            print('failed to find a meeting after {} checks \nexiting the program now'.format(i))
            exit()


def microphone():
    for i in range(1, 31):
        pyautogui.screenshot()
        unmuted_microphone = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
        if not unmuted_microphone:
            print('{} failed attempts to find the mute microphone button'.format(i))
        if unmuted_microphone is not None:
            x, y = pyautogui.locateCenterOnScreen('unmuted_microphone.png')
            pyautogui.click(x, y)
            break
        if i == 30:
            print('failed to find the "mute microphone" button after {} attempts \nexiting the program'.format(i))
            exit()


def full_screen():
    for i in range(1, 6):
        pyautogui.moveRel(50, 0, duration=1)
        pyautogui.screenshot()
        full_screen_button = pyautogui.locateCenterOnScreen('full_screen_button.png')
        if not full_screen_button:
            print('{} failed attempts to find the full screen button'.format(i))
        if full_screen_button is not None:
            x, y = pyautogui.locateCenterOnScreen('full_screen_button.png')
            pyautogui.click(x, y)
            break
        if i == 5:
            print('failed to find the "full screen" button after {} attempts \nexiting the program'.format(i))
            exit()


def join_breakout():
    join_breakout_attempts = 0
    while True:
        pyautogui.screenshot()
        breakout_room_join_button = pyautogui.locateCenterOnScreen('breakout_room_join_button.png')
        breakout_room_join_button_new = pyautogui.locateCenterOnScreen('breakout_room_join_button_new.png')
        if not breakout_room_join_button:
            print('{} attempts to find the join breakout room button'.format(join_breakout_attempts))
            join_breakout_attempts += 1
            time.sleep(15)
        if breakout_room_join_button or breakout_room_join_button_new is not None:
            try:
                x, y = pyautogui.locateCenterOnScreen('breakout_room_join_button.png')
            except None:
                x, y = pyautogui.locateCenterOnScreen('breakout_room_join_button_new.png')
            pyautogui.click(x, y)
            break


def leave_breakout():
    leave_breakout_attempts = 0
    while True:
        pyautogui.screenshot()
        breakout_room_return_to_main_button = pyautogui.locateCenterOnScreen('breakout_room_return_to_main_button.jpg')
        if not breakout_room_return_to_main_button:
            print('{} attempts to find the leave breakout room button'.format(leave_breakout_attempts))
            leave_breakout_attempts += 1
            time.sleep(15)
        if breakout_room_return_to_main_button is not None:
            x, y = pyautogui.locateCenterOnScreen('breakout_room_return_to_main_button.jpg')
            pyautogui.click(x, y)
            break


def auto_logout():
    for i in range(1, 31):
        pyautogui.moveRel(50, 0, duration=1)
        pyautogui.screenshot()
        leave_meeting_button = pyautogui.locateCenterOnScreen('leave_button.png')
        if leave_meeting_button is not None:
            x, y = pyautogui.locateCenterOnScreen('leave_button.png')
            pyautogui.click(x, y)
            for j in range(1, 31):
                pyautogui.screenshot()
                actually_leave_meeting_button = pyautogui.locateCenterOnScreen('actually_leave_meeting_button.png')
                if actually_leave_meeting_button is not None:
                    x, y = pyautogui.locateCenterOnScreen('actually_leave_meeting_button.png')
                    pyautogui.click(x, y)
                    break
            break

    print('automatically logged out of the meeting after {} hours \nhave a nice day!'.format(meeting_length))
