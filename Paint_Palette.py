from tkinter import *


class Paint(Frame):
    win = None

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.setUI()
        self.brush_size = 10
        self.color = 'black'

    def set_color(self, new_color):
        self.color = new_color
        self.win.withdraw()

    def open_colors(self):
        self.win = Toplevel(self.parent)
        self.win.title('Палитра цветов')
        self.win.minsize(width=410, height=140)
        self.win.maxsize(width=410, height=140)

        fr_yellow = Button(self.win, width=5, height=2, bg='#FFFF99', command=lambda: self.set_color('#FFFF99'))
        fr_yellow.grid(row=0, column=0)
        fr_yellow_1 = Button(self.win, width=5, height=2, bg='#FFFF00', command=lambda: self.set_color('#FFFF00'))
        fr_yellow_1.grid(row=0, column=1)
        fr_orange = Button(self.win, width=5, height=2, bg='#FFCC00', command=lambda: self.set_color('#FFCC00'))
        fr_orange.grid(row=0, column=2)
        fr_orange_1 = Button(self.win, width=5, height=2, bg='#FF9900', command=lambda: self.set_color('#FF9900'))
        fr_orange_1.grid(row=0, column=3)
        fr_brown = Button(self.win, width=5, height=2, bg='#996633', command=lambda: self.set_color('#996633'))
        fr_brown.grid(row=0, column=4)
        fr_brown_1 = Button(self.win, width=5, height=2, bg='#663300', command=lambda: self.set_color('#663300'))
        fr_brown_1.grid(row=0, column=5)

        fr_brown_2 = Button(self.win, width=5, height=2, bg='#FF6600', command=lambda: self.set_color('#FF6600'))
        fr_brown_2.grid(row=1, column=0)
        fr_brown_3 = Button(self.win, width=5, height=2, bg='#660000', command=lambda: self.set_color('#660000'))
        fr_brown_3.grid(row=1, column=1)
        fr_red = Button(self.win, width=5, height=2, bg='#FF0000', command=lambda: self.set_color('#FF0000'))
        fr_red.grid(row=1, column=2)
        fr_red_1 = Button(self.win, width=5, height=2, bg='#990000', command=lambda: self.set_color('#990000'))
        fr_red_1.grid(row=1, column=3)
        fr_purple = Button(self.win, width=5, height=2, bg='#FF33CC', command=lambda: self.set_color('#FF33CC'))
        fr_purple.grid(row=1, column=4)
        fr_purple_1 = Button(self.win, width=5, height=2, bg='#990099', command=lambda: self.set_color('#990099'))
        fr_purple_1.grid(row=1, column=5)

        fr_purple_3 = Button(self.win, width=5, height=2, bg='#6600CC', command=lambda: self.set_color('#6600CC'))
        fr_purple_3.grid(row=2, column=0)
        fr_purple_4 = Button(self.win, width=5, height=2, bg='#330066', command=lambda: self.set_color('#330066'))
        fr_purple_4.grid(row=2, column=1)
        fr_blue = Button(self.win, width=5, height=2, bg='#000099', command=lambda: self.set_color('#000099'))
        fr_blue.grid(row=2, column=2)
        fr_blue_1 = Button(self.win, width=5, height=2, bg='#000033', command=lambda: self.set_color('#000033'))
        fr_blue_1.grid(row=2, column=3)
        fr_green = Button(self.win, width=5, height=2, bg='#00FF00', command=lambda: self.set_color('#00FF00'))
        fr_green.grid(row=2, column=4)
        fr_green_1 = Button(self.win, width=5, height=2, bg='#666633', command=lambda: self.set_color('#666633'))
        fr_green_1.grid(row=2, column=5)

    def open_sizes(self):
        self.win = Toplevel(self.parent)
        self.win.title('Размер кисти')
        self.win.minsize(width=410, height=140)
        self.win.maxsize(width=410, height=140)

        fr_1 = Button(self.win, text='1', width=5, height=2, command=lambda: self.set_brush_size(1))
        fr_1.grid(row=0, column=0)
        fr_2 = Button(self.win, text='2', width=5, height=2, command=lambda: self.set_brush_size(2))
        fr_2.grid(row=0, column=1)
        fr_3 = Button(self.win, text='3', width=5, height=2, command=lambda: self.set_brush_size(3))
        fr_3.grid(row=0, column=2)
        fr_4 = Button(self.win, text='4', width=5, height=2, command=lambda: self.set_brush_size(4))
        fr_4.grid(row=0, column=3)
        fr_5 = Button(self.win, text='5', width=5, height=2, command=lambda: self.set_brush_size(5))
        fr_5.grid(row=0, column=4)
        fr_6 = Button(self.win, text='6', width=5, height=2, command=lambda: self.set_brush_size(6))
        fr_6.grid(row=0, column=5)

        fr_7 = Button(self.win, text='7', width=5, height=2, command=lambda: self.set_brush_size(7))
        fr_7.grid(row=1, column=0)
        fr_8 = Button(self.win, text='8', width=5, height=2, command=lambda: self.set_brush_size(8))
        fr_8.grid(row=1, column=1)
        fr_9 = Button(self.win, text='9', width=5, height=2, command=lambda: self.set_brush_size(9))
        fr_9.grid(row=1, column=2)
        fr_10 = Button(self.win, text='10', width=5, height=2, command=lambda: self.set_brush_size(10))
        fr_10.grid(row=1, column=3)
        fr_11 = Button(self.win, text='11', width=5, height=2, command=lambda: self.set_brush_size(11))
        fr_11.grid(row=1, column=4)
        fr_12 = Button(self.win, text='12', width=5, height=2, command=lambda: self.set_brush_size(12))
        fr_12.grid(row=1, column=5)

        fr_13 = Button(self.win, text='13', width=5, height=2, command=lambda: self.set_brush_size(13))
        fr_13.grid(row=2, column=0)
        fr_14 = Button(self.win, text='14', width=5, height=2, command=lambda: self.set_brush_size(14))
        fr_14.grid(row=2, column=1)
        fr_15 = Button(self.win, text='15', width=5, height=2, command=lambda: self.set_brush_size(15))
        fr_15.grid(row=2, column=2)
        fr_16 = Button(self.win, text='16', width=5, height=2, command=lambda: self.set_brush_size(16))
        fr_16.grid(row=2, column=3)
        fr_17 = Button(self.win, text='17', width=5, height=2, command=lambda: self.set_brush_size(17))
        fr_17.grid(row=2, column=4)
        fr_18 = Button(self.win, text='18', width=5, height=2, command=lambda: self.set_brush_size(18))
        fr_18.grid(row=2, column=5)

    def set_brush_size(self, new_size):
        self.brush_size = new_size
        self.win.withdraw()

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):
        self.parent.title("Pythonicway PyPaint")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне
        self.columnconfigure(6,
                             weight=1)  # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1)  # То же самое для третьего ряда
        self.canv = Canvas(self, bg="white")  # Создаем поле для рисования, устанавливаем белый фон
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке,будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
        self.canv.bind('<B1-Motion>', self.draw)

        clear_btn = Button(self, text="Clear all", width=10, command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=1, sticky=W)

        color_btn = Button(self, text="Открыть палитру", width=20, command=lambda: self.open_colors())
        color_btn.grid(row=0, column=2, padx=5, sticky=W)

        size_btn = Button(self, text="Размеры кисти", width=20, command=lambda: self.open_sizes())
        size_btn.grid(row=0, column=3, padx=5, sticky=W)


def main():
    root = Tk()
    root.geometry("800x600+300+300")
    app = Paint(root)

    ##    m = Menu(root)
    ##    root.config(menu=m)
    ##
    ##    cm = Menu(m)
    ##    m.add_cascade(label = 'Цвет кисти', menu = cm)
    ##    cm.add_command(label = 'Red', command=lambda: app.set_color("red"))
    ##    cm.add_command(label = 'Green', command=lambda: app.set_color("green"))
    ##    cm.add_command(label = 'Blue', command=lambda: app.set_color("blue"))
    ##    cm.add_command(label = 'Black', command=lambda: app.set_color("black"))
    ##    cm.add_command(label = 'White', command=lambda: app.set_color("white"))
    ##
    ##    sm = Menu(m)
    ##    m.add_cascade(label = 'Размер кисти', menu = sm)
    ##    sm.add_command(label = 'Two', command=lambda: app.set_brush_size(2))
    ##    sm.add_command(label = 'Five', command=lambda: app.set_brush_size(5))
    ##    sm.add_command(label = 'Seven', command=lambda: app.set_brush_size(7))
    ##    sm.add_command(label = 'Ten', command=lambda: app.set_brush_size(10))
    ##    sm.add_command(label = 'Twenty', command=lambda: app.set_brush_size(12))
    ##    sm.add_command(label = 'Fifty', command=lambda: app.set_brush_size(15))

    root.mainloop()


if __name__ == "__main__":
    main()
