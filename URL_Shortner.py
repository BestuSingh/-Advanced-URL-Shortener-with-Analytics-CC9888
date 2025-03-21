from tkinter import *
import pyshorteners
import pyperclip

root = Tk()
root.title("URL SHORTNER")
root.configure(bg= "green")

url = StringVar()
sortUrl = StringVar()

def urlshort():
    sort_Url = url.get()
    generatedurl = pyshorteners.Shortener().tinyurl.short(sort_Url)
    sortUrl.set(generatedurl)
    
def copy():
    generatedurl = sortUrl.get()
    pyperclip.copy(generatedurl)
    
    
# We built our UI.    

Label(root,text = "URL SHORTEMER APP", font = "Arial").pack(pady = 30)
Entry(root,textvariable = url).pack(pady = 15)
Button(root,text = "Generate url", command= urlshort).pack(pady=15)
Entry(root,textvariable =sortUrl ).pack(pady = 15)
Button(root,text= "Copy url",command= copy).pack(pady=15)


root.mainloop()



