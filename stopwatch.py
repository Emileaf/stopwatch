# "Stopwatch: The Game"
# Use codeskulptor to run Python program in browser
# http://www.codeskulptor.org/

import simplegui

# define global variables
current = 0 
times_stopped = 0
whole_stopped = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if (((t % 600 - t % 10) / 10) < 10):
        return str(t / 600) + ":0" + str((t % 600 - t % 10) / 10) + "." + str(t % 10)
    else:
        return str(t / 600) + ":" + str((t % 600 - t % 10) / 10) + "." + str(t % 10)
          
# define event handlers for buttons; "Start", "Stop", "Reset"

def start():
    timer.start()

def stop():
    global times_stopped, whole_stopped
    if timer.is_running():
        timer.stop()
        times_stopped += 1
        if (current % 10 == 0):
            whole_stopped += 1
    
def reset():
    global current, times_stopped, whole_stopped
    timer.stop()
    current = 0
    times_stopped = 0
    whole_stopped = 0

# define event handler for timer with 0.1 sec interval
def increment():
    global current
    print current
    current += 1
    
# define draw handler
def draw(canvas):
    canvas.draw_text(format(current), (55, 110), 44, "white")
    canvas.draw_text(str(whole_stopped) + "/" + str(times_stopped), 
                     (150, 30), 30, "white")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 200, 200)

# register event handlers
timer = simplegui.create_timer(100, increment)
startbutton = frame.add_button("Start", start, 100)
stopbutton = frame.add_button("Stop", stop, 100)
resetbutton = frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()


