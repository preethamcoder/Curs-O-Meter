import matplotlib.pyplot as plt
import string, sys

print("Welcome to the Curs-O-Meter application!")
#print("Here are the curse words we have on file so far: ")

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
    print("Start typing whatever you want to say: ")
    data = input()
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
    #print(plot_y, considered_words)
        
f.close()