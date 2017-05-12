import CHIP_IO.GPIO as GPIO
import time
import subprocess

MUSIC_FILE = 'yodel.mp3'
PIN = "XIO-P1"

# setting up input
GPIO.setup(PIN, GPIO.IN)

# create new fifo file for mplayer control
subprocess.Popen(['rm',  '-f', '/tmp/mplayer-control'])
subprocess.Popen(['mkfifo', '/tmp/mplayer-control'])

# control music
def play_music():
    subprocess.Popen(['mplayer', '-slave',  '-input', 'file=/tmp/mplayer-control',  MUSIC_FILE])

def stop_music():
    f = open('/tmp/mplayer-control', 'w')
    f.write('quit\n')
    f.close()
    
# application loop
is_playing = False

while True:
    time.sleep(1)

    # photoresistor thinks it's dark
    if GPIO.input(PIN):
        print("HIGH")        
        if is_playing:
            is_playing = False            
            stop_music()
    
    # photoresistor thinks it's light
    else:
        print("LOW")
        if not is_playing:
            is_playing = True             
            play_music()




