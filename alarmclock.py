import subprocess
import time
alarm_input = input('Enter the alarm time in 24 hour format as hh:mm:ss ')
alarm = alarm_input.split(':')
current_time = time.localtime(time.time())
hour = int(alarm[0])-current_time[3]
mins = int(alarm[1])-current_time[4]
sec = int(alarm[2])-current_time[5]
diff = hour*60*60 + mins*60 + sec
print ('ALARM IS RUNNING!!!')
time.sleep(diff)
print ('TIME OVER!!!')
audio_file = 'german-shephard-daniel_simon.mp3'
subprocess.call(["afplay", audio_file])
