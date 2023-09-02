from tkinter import *
import random

root = Tk()
root.title("Random Words Generator")
root.geometry("500x500")

Generate_random_words = Label(root)

def RandomWordGenerator():
    alpha_list =["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    random_no1 = random.randint(1,26)
    random_no2 = random.randint(1,26)
    random_no3 = random.randint(1,26)
    random_no4 = random.randint(1,26)
    random_no5 = random.randint(1,26)
    random_alpha1 = alpha_list[random_no1]
    random_alpha2 = alpha_list[random_no2]
    random_alpha3 = alpha_list[random_no3]
    random_alpha4 = alpha_list[random_no4]
    random_alpha5 = alpha_list[random_no5]
    Generate_random_words["text"] = "Random words are " + str(random_alpha1) + str(random_alpha2) + str(random_alpha4) + str(random_alpha5)
    
btn = Button(root, text = "Generate Random Words", command=RandomWordGenerator, bg="orange", fg="green")

btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
Generate_random_words.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()