from tkinter import*
from tkinter import messagebox
from random import*
from time import*

lst=[]

def OnClick(event):
    global buttons, images, clicked, lst
    t=event.widget.grid_info()
    x=t['column']
    y=t['row']
    buttons[7*y+x].config(image=images2[7*y+x])
    buttons[7*y+x].update_idletasks()
    clicked[7*y+x]=True
    
    if clicked.count(True)==2:
        for i in range(len(images)):
            if clicked[i]==True:
                lst.append(i)
                
        if images[lst[0]]==images[lst[1]]:            
            buttons[lst[0]].unbind('<Button-1>')
            buttons[lst[1]].unbind('<Button-1>')            
            lst=[]
            clicked=[False]*28           
        else:
            sleep(0.8)            
            buttons[lst[0]].config(image=secret_image)
            buttons[lst[1]].config(image=secret_image)
            lst=[]
            clicked=[False]*28

def about():
    messagebox.showinfo('О программе','Игру написала Алия Какабаева. Адрес: Ставропольский край, Александровский район, Село Северное, ул Восточная(2), дом 52. Электронная почта: a.kakabaeva@yandex.ru')

def rool():
    messagebox.showinfo('Правила игры','''Суть игры очень простая. Эти карточки выкладываются на стол «рубашкой» вверх. Далее по очереди каждый игрок открывает две любые карточки, показывая их всем. Если на них изображены одинаковые рисунки, он забирает их себе, и вскрывает следующую пару. Однако, если изображения разные, то он возвращает эти карточки взакрытую обратно на свои места, а ход переходит следующему игроку. Когда все карточки будут разобраны, выбирается победитель – тот, кто набрал наибольшее количество карточек.
    В Memory можно играть и одному, но тогда, для интереса, можно засекать, за какое время вы раскроете все пары. Впрочем, таких версий игры в интернете очень много – играй, не хочу :)''')
        
a=Tk()
a.title("Memory")
a.iconbitmap('images/icon.ico')
a.resizable(width=False,  height=False)

mainmenu=Menu(a)
a.config(menu=mainmenu)
help_menu=Menu(mainmenu,tearoff=0)
about_menu=Menu(mainmenu,tearoff=0)
mainmenu.add_command(label='Правила игры',command=rool)
mainmenu.add_command(label='О программе',command=about)

clicked=[False]*28

secret_image=PhotoImage(file='images/awesome-memory-icon.gif')

images=['images/blue.gif','images/dragon.gif','images/bruni.gif',
        'images/grogu.gif','images/owl.gif','images/cat.gif',
        'images/fury.gif','images/bambi.gif','images/dog.gif',
        'images/wolf.gif','images/fox.gif','images/kitten.gif',
        'images/barn_owl.gif','images/httyd.gif',
        'images/blue.gif','images/dragon.gif','images/bruni.gif',
        'images/grogu.gif','images/owl.gif','images/cat.gif',
        'images/fury.gif','images/bambi.gif','images/dog.gif',
        'images/wolf.gif','images/fox.gif','images/kitten.gif',
        'images/barn_owl.gif','images/httyd.gif']


images2=[]

print(len(images))

shuffle(images)

for i in range(len(images)):
    images2.append(PhotoImage(file=images[i]))

    
buttons=[]


row=0
col=0

for i in range(4):
    for j in range(7):
        button=Button(image=secret_image)
        button.grid(row=row,column=col,padx=3,pady=3)
        button.bind('<Button-1>',OnClick)
        buttons.append(button)
        col+=1
    if col>6:
        col=0
        row+=1

a.mainloop()
