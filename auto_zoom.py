# using more organized function references

from auto_zoom_functions import *


'''
TODO:
- fix meeting_id 
- fix password
- create function for password options 
'''

# gets meeting id
get_meeting_id()

# gets password if there is one
get_password()

# determines the operating system
get_os()

# automation start delay
time.sleep(1)

# presses os specific command key
search_via_command_key()

# typing zoom
pyautogui.typewrite('Zoom', interval=0.05)
time.sleep(1)

# opening zoom
pyautogui.hotkey('enter')

# locates and selects the join button
join()

# entering the meeting id
time.sleep(0.5)
pyautogui.typewrite(get_meeting_id.meeting_id, interval=0.05)

# locates and selects the camera off button prior to joining the meeting
pre_join_camera()

# locates and selects the join meeting button
join_meeting()

# entering the meeting password
join_with_password()

# locates and selects the join without video button
join_without_video()

# checks for a meeting
meeting_check()

# locates and selects microphone mute button
microphone()

# locates and selects the full screen button
full_screen()

seconds = 0
while seconds < meeting_length:
    # locates and selects the join breakout room button
    join_breakout()

    # locates and selects the leave breakout room button
    leave_breakout()

    # increment seconds
    seconds += 1
    time.sleep(1)

# automatic logout after 3 hours
auto_logout()
