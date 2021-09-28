'''
This program will make  you Healthy Pragrammer.
Program will remind you  to drink water , do eye eercise , and do physical activity.
Assume working hour = 8 hours # 9am - 5pm
'''

import datetime
import time
from pygame import mixer

current_time = time.strftime("%H:%M:%S")
work_start_time  = "11:00:00"
work_end_time = "19:00:00"
report_file_name = "Health_Report_" + str(datetime.datetime.now().date()) + "_" + time.strftime("%H:%M:%S").replace(":","-") + ".txt"

#Drink Water configuration:
water_limit = 5000 # in ml
glass_size = 200 # in ml
no_of_glass = round(water_limit / glass_size)
total_working_time = 8*60*60 # Assume 8 hours
water_interval = total_working_time / no_of_glass  # seconds
water_mp3_file = 'mp3`s/water.mp3.mp3'

# Eye Exercise Configuration:
eye_exercise_interval = 30*60  # Every 30 minutes
eye_mp3_file = 'mp3`s/jarvis_reminder_2.mp3'

# Physical Exercise Configuration:
physical_exercise_interval = 45*60 # Every 45 minutes
physical_mp3_file = 'mp3`s/vitamin_reminder.mp3'

def play_music(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

def water_drinking_reminder(glass):
    i = ''
    while(i !='drank'):
        play_music(water_mp3_file)
        print("\n", end="")
        i = input("Did you drank water ? If yes type 'Drank': ").lower()
        if i == 'drank':
            f = open(report_file_name, "a")
            f.write("[ " + str(datetime.datetime.now()) + " ] : " + "Water " + str(glass_size) + "ml" + "\n")
            f.close()
            print("Thank you !!!")
            mixer.music.stop()
            time.sleep(water_interval)
            break

def eye_exercise_reminder():
    i = ''
    while(i != 'eydone'):
        play_music(eye_mp3_file)
        print("\n", end="")
        i = input("Did you finish 'Eye Exercise' ? If yes type 'EyDone' : ").lower()
        if i == 'eydone':
            f = open(report_file_name, "a")
            f.write("[ " + str(datetime.datetime.now()) + " ] : " + "Eye Exercise" + "\n")
            f.close()
            print("Thank you !!!")
            mixer.music.stop()
            time.sleep(eye_exercise_interval)
            break

def physical_exercise_reminder():
    i = ''
    while(i !='exdone'):
        play_music(physical_mp3_file)
        print("\n", end="")
        i = input("Did you finish 'Physical Exercise' ? If yes type 'ExDone' : ").lower()
        if i == 'exdone':
            f = open(report_file_name, "a")
            f.write("[ " + str(datetime.datetime.now()) + " ] : " + "Physical Exercise" + "\n")
            f.close()
            print("Thank you !!!")
            mixer.music.stop()
            time.sleep(physical_exercise_interval)
            break


try:
    interval = 0
    glass = 0
    while(current_time!=work_end_time):
        if current_time>=work_start_time and current_time<= work_end_time:
            if glass == no_of_glass:
                pass
            else:
                water_drinking_reminder(glass)
                glass +=1
            eye_exercise_reminder()
            physical_exercise_reminder()
            current_time = time.strftime("%H:%M:%S")
except Exception as e:
    print("Somthing Wrong !!!")
