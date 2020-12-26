from tkinter import *
from random import shuffle
from time import sleep

def onClick(event):
    global buttons, cb
    grid_info = event.widget.grid_info()
    x = grid_info['column']
    y = grid_info['row']
    buttons[y][x].config(image = images[7 * y + x])
    buttons[y][x].update_idletasks()
    cb.append([x, y])
    
    if len(cb) == 2:
        sleep(0.8)
        if image_addresses[7 * cb[0][1] + cb[0][0]] == image_addresses[7 * cb[1][1] + cb[1][0]]:            
            buttons[cb[0][1]][cb[0][0]].unbind('<Button-1>')
            buttons[cb[1][1]][cb[1][0]].unbind('<Button-1>')           
        else:           
            buttons[cb[0][1]][cb[0][0]].config(image = secret_image)
            buttons[cb[1][1]][cb[1][0]].config(image = secret_image)
        cb = []

def about():
    messagebox.showinfo('О программе', 'Игру написала Алия Какабаева. Электронная почта: a.kakabaeva@yandex.ru')

def rules():
    messagebox.showinfo('Правила игры', '''Суть игры очень проста. Карточки выкладываются на стол рубашкой вверх.
	Далее по очереди каждый игрок открывает две любые карточки, показывая их всем.
	Если на них изображены одинаковые рисунки, он забирает их себе, и вскрывает следующую пару.
	Однако, если изображения разные, то он возвращает эти карточки взакрытую обратно на свои места, а ход переходит следующему игроку.
	Когда все карточки будут разобраны, выбирается победитель – тот, кто правильно открыл наибольшее количество карточек.
    В Memory можно играть и одному, но тогда, для интереса, можно засекать, за какое время вы раскроете все пары.
	Впрочем, таких версий игры в интернете очень много – играй не хочу :)''')
        
board = Tk()
board.title("Memory")
board.iconbitmap('images/icon.ico')
board.resizable(width = False,  height = False)

main_menu = Menu(board)
board.config(menu = main_menu)
help_menu = Menu(main_menu, tearoff = 0)
about_menu = Menu(main_menu, tearoff = 0)
mainmenu.add_command(label = 'Правила игры', command = rules)
mainmenu.add_command(label = 'О программе', command = about)

secret_image = PhotoImage(file = 'images/awesome-memory-icon.gif')
image_addresses_copy = ['blue', 'dragon', 'bruni', 'grogu', 'owl', 'cat', 'fury', 
						'bambi', 'dog', 'wolf', 'fox', 'kitten', 'barn_owl', 'httyd']
image_addresses = []
images = []
for image_address in image_addresses_copy:
    image_addresses.append('images/' + image_address + '.gif')
	image_addresses.append('images/' + image_address + '.gif')
shuffle(image_addresses)
for image_address in image_addresses:
    images.append(PhotoImage(file = image_address))

buttons = []
for row in range(4):
    row_buttons = []
    for col in range(7):
        button = Button(image = secret_image)
        button.grid(row = row, column = col, padx = 3, pady = 3)
        button.bind('<Button-1>', onClick)
        row_buttons.append(button)
buttons.append(row_buttons)
cb = [] #clicked buttons

board.mainloop()
