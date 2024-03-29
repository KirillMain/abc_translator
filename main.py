from tkinter import *
from tkinter.scrolledtext import ScrolledText
import pyperclip
import ctypes as ct


txt = None
res = None


def rus_translate():
    abc_rus = 'йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'
    abc_eng = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'
    reply = ''
    text = txt.get("1.0", END)
    for el in text:
        try:
            ind = abc_eng.index(el)
            reply += abc_rus[ind]
        except ValueError:
            reply += el
    res.delete("1.0", END)
    res.insert(INSERT, reply[:-1])


def eng_translate():
    abc_rus = 'йцукенгшщзхъфывапролджэячсмитьбю.ёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'
    abc_eng = 'qwertyuiop[]asdfghjkl;\'zxcvbnm,./`QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'
    reply = ''
    text = txt.get("1.0", END)
    for el in text:
        try:
            ind = abc_rus.index(el)
            reply += abc_eng[ind]
        except ValueError:
            reply += el
    res.delete("1.0", END)
    res.insert(INSERT, reply[:-1])


def insert():
    txt.delete("1.0", END)
    res.delete("1.0", END)

    txt.insert(INSERT, pyperclip.paste())


def clear():
    res.delete("1.0", END)
    txt.delete("1.0", END)


def main():
    frame = Frame(
        window,
        background="#1c1c1c"
    )
    frame.pack(expand=True)


    rus_btn = Button(
        frame,
        text='Поменять на\nРусский',
        command=rus_translate,
        background="gray",  # color of button
        activebackground="dim gray",  # color of back on click
        # activeforeground="blue" # color of text
        width=20,
        height=5,
        font="14"
    )
    rus_btn.grid(row=0, column=0, pady=[0, 5], padx=10)

    eng_btn = Button(
        frame,
        text='Поменять на\nАнглийский',
        command=eng_translate,
        background="gray",  # color of button
        activebackground="dim gray",  # color of back on click
        # activeforeground="blue" # color of text
        width=20,
        height=5,
        font="14"
    )
    eng_btn.grid(row=1, column=0)

    import_btn = Button(
        frame,
        text='Вставить\nтекст',
        command=insert,
        background="gray", # color of button
        activebackground="dim gray", # color of back on click
        # activeforeground="blue" # color of text
        width=20,
        height=5,
        font="14"
    )
    import_btn.grid(row=3, column=0, pady=5)

    clear_btn = Button(
        frame,
        text='Очистить',
        command=clear,
        background="gray",  # color of button
        activebackground="dim gray",  # color of back on click
        # activeforeground="blue" # color of text
        width=20,
        height=5,
        font="14"
    )
    clear_btn.grid(row=4, column=0)


    global txt
    txt = ScrolledText(
        frame,
        width=90,
        height=17,
        wrap="word",
        font="14",
        background="#c9c9c9"
    )
    txt.grid(row=0, rowspan=2, column=1, padx=10, pady=[5, 5])

    global res
    res = ScrolledText(
        frame,
        width=90,
        height=17,
        wrap="word",
        font="14",
        background="#c9c9c9"
    )
    res.grid(row=3, rowspan=2, column=1, padx=10, pady=[15, 5])

    window.mainloop()

# ------------------------------ ЕБАНИНА ------------------------------
def dark_title_bar(window):
    window.update()
    DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    rendering_policy = DWMWA_USE_IMMERSIVE_DARK_MODE
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, rendering_policy, ct.byref(value), ct.sizeof(value))
# ------------------------------ ЕБАНИНА ------------------------------


if __name__ == "__main__":
    window = Tk()
    dark_title_bar(window)
    window["bg"] = "#1c1c1c"
    window.title("Рефактор текста")
    window.geometry('1080x720')
    # window.maxsize(width=1080, height=720)
    window.minsize(width=1080, height=720)

    main()



