import os
import tkinter
import random
import time
from tkinter import messagebox

player_num = 0
gamespeed = input('게임속도를 입력하세요(1~4, 4가 가장 빠름)')
while gamespeed not in ['1', '2', '3', '4']:
    print('잘못 입력하셨습니다.')
    gamespeed = input('게임속도를 입력하세요(1~4, 4가 가장 빠름)')
gamespeed = int(gamespeed)
median = []
for i in range(1, 50):
    median.append(i)

random.shuffle(median)
unlucky = median[0:5]

class Player():
    def __init__(self, tag, locat, name, x, y, mal):
        self.tag = tag
        self.locat = locat
        self.name = name
        self.x = x
        self.y = y
        self.mal = mal

def roll(root2, player_list, canvas):
    global gamespeed
    def change_monitor():
        canvas.delete(player_list[i].tag)
        canvas.create_image(player_list[i].x, player_list[i].y, image=player_list[i].mal, tag=player_list[i].tag)
        if gamespeed == 1:
            time.sleep(1)
        elif gamespeed == 2:
            time.sleep(0.5)
        elif gamespeed == 3:
            time.sleep(0.25)

        root2.update()

    for i in range(len(player_list)):
        prev = player_list[i].locat
        dice = random.choice([1, 2, 3, 4, 5, 6])
        player_list[i].locat += dice
        if player_list[i].locat in unlucky:
            print("Player %d is unlucky!" %(i+1))
            player_list[i].locat = 1
            if i % 2 == 0:
                player_list[i].x = 70
                player_list[i].y = 470 + 10 * i
            else:
                player_list[i].x = 90
                player_list[i].y = 470 + 20 * (i // 2)

        else:
            if ((player_list[i].locat-1) // 10) != ((prev-1) // 10):
                if i % 2 == 0:
                    player_list[i].x = 70 + 65 * ((player_list[i].locat-1) % 10)
                    player_list[i].y -= 65
                else:
                    player_list[i].x = 90 + 65 * ((player_list[i].locat-1) % 10)
                    player_list[i].y -= 65
            else:
                player_list[i].x = player_list[i].x + 65 * dice
                player_list[i].y = player_list[i].y
        print('prev:', prev, 'now:', player_list[i].locat)
        change_monitor()
    print()

    for p in player_list:
        if p.locat >= 50:
            messagebox.showinfo(title='게임 오버', message=p.name + ' 승리!')
            exit(0)

def gameplay(player_num):
    print(player_num)
    global root
    player_pos = []
    player_list = []
    turn = 1

    root.destroy()
    root2 = tkinter.Tk()
    root2.title('파이썬 주사위 게임')
    root2.resizable(False, False)
    canvas = tkinter.Canvas(root2, width=800, height=600)
    canvas.pack()

    num_label = tkinter.Label(root2, text='게임 인원수: ' + str(player_num))
    num_label.place(x=0, y=0)

    roll_button = tkinter.Button(text='주사위 굴리기', command=lambda: roll(root2, player_list, canvas))
    roll_button.place(x=380, y=100)

    board = tkinter.PhotoImage(file='./board.png')
    canvas.create_image(380, 350, image=board, tag='board')

    if player_num == 1:
        m1 = tkinter.PhotoImage(file='./p1.png')
        canvas.create_image(70, 470, image=m1, tag='m1')
        p1 = Player('m1', 1, '플레이어1', 70, 470, m1)
        player_list.append(p1)

    if player_num == 2:
        m1 = tkinter.PhotoImage(file='./p1.png')
        canvas.create_image(70, 470, image=m1, tag='m1')
        m2 = tkinter.PhotoImage(file='./p2.png')
        canvas.create_image(90, 470, image=m2, tag='m2')
        p1 = Player('m1', 1, '플레이어1', 70, 470, m1)
        p2 = Player('m2', 1, '플레이어2', 90, 470, m2)
        player_list.append(p1)
        player_list.append(p2)

    if player_num == 3:
        m1 = tkinter.PhotoImage(file='./p1.png')
        canvas.create_image(70, 470, image=m1, tag='m1')
        m2 = tkinter.PhotoImage(file='./p2.png')
        canvas.create_image(90, 470, image=m2, tag='m2')
        m3 = tkinter.PhotoImage(file='./p3.png')
        canvas.create_image(70, 490, image=m3, tag='m3')
        p1 = Player('m1', 1, '플레이어1', 70, 470, m1)
        p2 = Player('m2', 1, '플레이어2', 90, 470, m2)
        p3 = Player('m3', 1, '플레이어3', 70, 490, m3)
        player_list.append(p1)
        player_list.append(p2)
        player_list.append(p3)

    if player_num == 4:
        m1 = tkinter.PhotoImage(file='./p1.png')
        canvas.create_image(70, 470, image=m1, tag='m1')
        m2 = tkinter.PhotoImage(file='./p2.png')
        canvas.create_image(90, 470, image=m2, tag='m2')
        m3 = tkinter.PhotoImage(file='./p3.png')
        canvas.create_image(70, 490, image=m3, tag='m3')
        m4 = tkinter.PhotoImage(file='./p4.png')
        canvas.create_image(90, 490, image=m4, tag='m4')
        p1 = Player('m1', 1, '플레이어1', 70, 470, m1)
        p2 = Player('m2', 1, '플레이어2', 90, 470, m2)
        p3 = Player('m3', 1, '플레이어3', 70, 490, m3)
        p4 = Player('m4', 1, '플레이어4', 90, 490, m4)
        player_list.append(p1)
        player_list.append(p2)
        player_list.append(p3)
        player_list.append(p4)

    for i in range(player_num):
        player_pos.append(1)
    root2.mainloop()


root = tkinter.Tk()
root.title("파이썬 주사위 게임")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

game_title = tkinter.PhotoImage(file='./dicewhole.png', master=root)
canvas.create_image(380, 360, image=game_title, tag = 'title')

label = tkinter.Label(root, text='게임 인원수를 고르세요.')
label.place(x=300, y=400)

button_1 = tkinter.Button(text='혼자', command=lambda: gameplay(1), master=root)
button_1.place(x=300, y=430)
button_1 = tkinter.Button(text='2명', command=lambda: gameplay(2), master=root)
button_1.place(x=340, y=430)
button_1 = tkinter.Button(text='3명', command=lambda: gameplay(3), master=root)
button_1.place(x=380, y=430)
button_1 = tkinter.Button(text='4명', command=lambda: gameplay(4), master=root)
button_1.place(x=420, y=430)

root.mainloop()
