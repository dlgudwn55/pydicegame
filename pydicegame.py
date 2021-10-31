import tkinter

player_num = 0
player_list = []

def get_player_num():
    global player_num
    txt = entry.get()
    while (txt not in ['1', '2', '3', '4']):
        button_for_player_num['text'] = '잘못 입력하셨습니다.'
        txt = entry.get()
    player_num = int(txt)



root = tkinter.Tk()
root.title("파이썬 주사위 게임")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()

game_title = tkinter.PhotoImage(file='./dicewhole.png')
canvas.create_image(380, 400, image=game_title, tag = 'title')

label = tkinter.Label(root, text='게임 인원 수를 숫자로 적으세요(1~4).')
label.place(x=300, y=10)

entry = tkinter.Entry(width=1)
entry.place(x=350, y=30)

button_for_player_num = tkinter.Button(text='입력', command=get_player_num)
button_for_player_num.place(x=360, y=30)

# 메인화면으로 전환
board = tkinter.PhotoImage(file='./board.png')
canvas.create_image(380, 300, image=board, tag='board')
root.mainloop()

print(player_num)
