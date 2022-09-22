import json
import tkinter
import random


class tk:
    label1 = None
    label2 = None
    allWords = None

    def next(self):
        r = random.randint(0, len(self.allWords))
        self.label1["text"] = self.allWords[r]['headWord']
        self.label2["text"] = self.allWords[r]['content']['word']['content']['trans'][0]['tranCn']

    def init_window(self, all_words):
        self.allWords = all_words
        self.main_window = tkinter.Tk()
        self.main_window.title("Auto Check")
        self.main_window.geometry("200x100")
        self.label1 = tkinter.Label(self.main_window, text="")
        self.label1.pack()
        self.label2 = tkinter.Label(self.main_window, text="")
        self.label2.pack()
        self.next()
        button1 = tkinter.Button(self.main_window, text="next", command=lambda: self.next())
        button1.pack()
        self.main_window.mainloop()


if __name__ == '__main__':
    path = 'CET4luan_1.json'
    all_words = []
    f = open(path, encoding='utf-8')
    for line in f.readlines():
        data = json.loads(line)
        all_words.append(data)
    m = tk()
    m.init_window(all_words)
