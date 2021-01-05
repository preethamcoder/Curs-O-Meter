import speech_recognition as sr
import matplotlib.pyplot as plt
import string, sys
from pprint import pprint
from pydub import AudioSegment
from pydub.playback import play

print("Welcome to the Curs-O-Meter application!")
#print("Here are the curse words we have on file so far: ")
def textmod():
    print("Start typing whatever you want to say: ")
    data = input().lower()
    for i in possible_words:
        used_words.append(data.count(i))
        #print(used_words)
    for j in range(len(used_words)):
        if(used_words[j] > 0):
            plot_x.append(possible_words[j])
    plot_y = [i for i in used_words if i != 0]
    print("You used: ")
    for i in range(len(plot_y)):
        print(plot_x[i] + ": " + str(plot_y[i]) + " time(s)")
    xaxis = range(len(plot_x))
    plt.figure(figsize=(12, 12))
    plt.title("Curse Words You Used ")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.bar(xaxis, plot_y, width=0.5)
    plt.xticks(xaxis, plot_x)
    for a,b in zip(xaxis, plot_y):
        plt.text(a, b+8, str(b), horizontalalignment='center', verticalalignment='center')
    plt.show()
def speechmod():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak into the machine: ")
        audio = r.listen(source)
        print("Your time has elapsed. ")
        data = r.recognize_google(audio).lower()
        print("You said: " + data)
        for i in possible_words:
            used_words.append(data.count(i))
        #print(used_words)
        for j in range(len(used_words)):
            if(used_words[j] > 0):
                plot_x.append(possible_words[j])
        plot_y = [i for i in used_words if i != 0]
        if(len(plot_x)==0):
            print("Great job! You have spoken cleanly without any foul language!")
        else:
            print("You used: ", end = "\t")
        for i in range(len(plot_y)):
            print(plot_x[i] + ": " + str(plot_y[i]) + " time(s)", end = "\t\t")
        xaxis = range(len(plot_x))
        plt.figure(figsize=(12, 12))
        plt.title("Curse Words You Used ")
        plt.xlabel("Words")
        plt.ylabel("Frequency")
        plt.bar(xaxis, plot_y, width=0.5)
        plt.xticks(xaxis, plot_x)
        for a,b in zip(xaxis, plot_y):
            plt.text(a, b+8, str(b), horizontalalignment='center', verticalalignment='center')
        plt.show()
f = open("race.txt", "r")
lines = f.read().lower().split()
possible_words = []
used_words = []
plot_x = []
for line in lines:
    possible_words.append(line)
    #print(possible_words)
choice = input("Would you like to speak or type into the machine? (s/t)\t")
if choice.lower() == 't':
    textmod()
elif choice.lower() == "s":
    speechmod()
else:
    print("Invalid choice, try again!")
    
    #print(plot_y, considered_words)
        
f.close()
