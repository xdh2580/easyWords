import json
import threading
import time
import tkinter
import random

path = None
all_words = []


class tk:
    radioBtnA = None
    radioBtnB = None
    radioBtnC = None
    radioBtnD = None
    button_start = None
    label1 = None
    label2 = None
    button_next = None
    button_auto = None
    label3 = None
    allWords = None
    vocabulary = None

    def __init__(self):
        self.main_window = tkinter.Tk()

    def start(self):
        self.button_start.forget()
        self.radioBtnA.pack_forget()
        self.radioBtnB.pack_forget()
        self.radioBtnC.pack_forget()
        self.radioBtnD.pack_forget()
        self.label1.pack()
        self.label2.pack()
        self.button_next.pack()
        self.label3.pack()
        self.button_auto.pack()
        if m.vocabulary.get() == "CET4_1":
            path = 'CET4luan_1.json'
        elif m.vocabulary.get() == "CET4_2":
            path = 'CET4luan_2.json'
        elif m.vocabulary.get() == "CET6_1":
            path = 'CET6luan_1.json'
        elif m.vocabulary.get() == "CET6_2":
            path = 'CET6_2.json'
        f = open(path, encoding='utf-8')
        for line in f.readlines():
            data = json.loads(line)
            all_words.append(data)
        # print(len(all_words))
        self.next()
        self.main_window.geometry("200x100")
        pass

    def next(self):
        r = random.randint(0, len(self.allWords)-1)
        self.label1["text"] = self.allWords[r]['headWord']
        self.label3["text"] = self.allWords[r]['content']['word']['content']['usphone']
        self.label2["text"] = self.allWords[r]['content']['word']['content']['trans'][0]['pos']+" "+self.allWords[r]['content']['word']['content']['trans'][0]['tranCn']

    def auto(self):
        self.button_next.forget()
        self.button_auto.forget()
        while True:
            try:
                self.next()
            except Exception as e:
                print(e)
            time.sleep(2)


    def init_window(self, all_words):
        self.allWords = all_words
        self.main_window.title("Easy Words")
        self.main_window.geometry("200x150")
        self.vocabulary = tkinter.StringVar(value="CET4_1")  # 默认四级高频词汇
        self.radioBtnA = tkinter.Radiobutton(self.main_window, text="四级核心", variable=self.vocabulary, value="CET4_1")
        self.radioBtnA.pack()
        self.radioBtnB = tkinter.Radiobutton(self.main_window, text="四级全部", variable=self.vocabulary, value="CET4_2")
        self.radioBtnB.pack()
        self.radioBtnC = tkinter.Radiobutton(self.main_window, text="六级核心", variable=self.vocabulary, value="CET6_1")
        self.radioBtnC.pack()
        self.radioBtnD = tkinter.Radiobutton(self.main_window, text="六级全部", variable=self.vocabulary, value="CET6_2")
        self.radioBtnD.pack()
        self.button_start = tkinter.Button(self.main_window, text="start", command=lambda: self.start())
        self.button_start.pack()
        self.label1 = tkinter.Label(self.main_window, text="")
        # self.label1.pack()
        self.label2 = tkinter.Label(self.main_window, text="")
        # self.label2.pack()
        self.button_next = tkinter.Button(self.main_window, text="next", command=lambda: self.next())
        self.button_auto = tkinter.Button(self.main_window, text="auto", command=lambda: threading.Thread(target=self.auto).start())
        # button1.pack()
        self.label3 = tkinter.Label(self.main_window, text="")
        # self.label3.pack()
        self.main_window.mainloop()


if __name__ == '__main__':
    m = tk()
    m.init_window(all_words)
