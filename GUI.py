from tkinter import *
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

dream = open('/Users/Owner/Desktop/Wordcloud/DreamSpeech.txt').read()
lear = open('/Users/Owner/Desktop/Wordcloud/KingLear.txt').read()
gettysburg = open('/Users/Owner/Desktop/Wordcloud/Gettysburg.txt').read()

crown_mask = np.array(Image.open("/Users/Owner/Desktop/Wordcloud/crown_mask.jpg"))
dream_mask = np.array(Image.open("/Users/Owner/Desktop/Wordcloud/comment.png"))
getty_mask = np.array(Image.open("/Users/Owner/Desktop/Wordcloud/AL_mask.jpg"))

stopwords = STOPWORDS

root = Tk()
root.title("Create a word cloud!")

e = Entry(root, width=50, borderwidth=5)
e.insert(0, "Enter your own text")
e.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

def button_click(text,shape):
    wc = WordCloud(background_color='black',
                           contour_width=1,
                           contour_color='black',
                           stopwords=stopwords,
                           mask=shape)
    wc.generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

def button_clear():
    e.delete(0,END)

def button_enter():
    text = e.get()
    wc = WordCloud(background_color='black',
                           contour_width=1,
                           contour_color='black',
                           stopwords=stopwords)
    wc.generate(text)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()


button_Dream = Button(root, text="I have a Dream", command=lambda:button_click(dream,dream_mask))
button_Lear = Button(root, text="King Lear", command=lambda: button_click(lear,crown_mask))
button_Getty = Button(root, text="Gettysburg Address", command=lambda: button_click(gettysburg,getty_mask))
button_Clear = Button(root, text="Clear", padx=100, command=button_clear)
button_Enter = Button(root, text="Enter", padx=100, command=button_enter)

button_Dream.grid(row=1, column=0)
button_Lear.grid(row=1, column=1)
button_Getty.grid(row=1, column=2)
button_Clear.grid(row=2, column=0, columnspan=3)
button_Enter.grid(row=3, column=0, columnspan=3)

root.mainloop()
