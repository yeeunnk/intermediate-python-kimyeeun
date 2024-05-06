import tkinter as tkt

def on_click(number):
    entry.insert(tkt.END, number)

# 창 생성
root = tkt.Tk()
root.title("계산기")

# 아이콘 설정
# photo = tkt.PhotoImage(file="C:/Study/해달/부트캠프/2024-1-파이썬응용/2주차/윈도우계산기아이콘.png")
photo = tkt.PhotoImage(file="./윈도우계산기아이콘.png")
root.iconphoto(False, photo)

# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=35)
entry.grid(row=0, column=0, columnspan=4, pady=10)  # 0행, 0열에 배치, 4개의 열을 차지, y축에패딩(여백)추가

# 엔트리 생성 (한줄 텍스트)
entry = tkt.Entry(root, width=20, borderwidth=12, font=("Verdana", 13), justify="right")  # borderwitdh: 테두리두께
entry.grid(row=0, column=0, columnspan=4, pady=10)

def create_button(text, row, column, command, width=13, height=9, columnspan=1, rowspan=1, bg=None):
    button = tkt.Button(root, text=text, padx=width, pady=height, command=command)
    button.grid(row=row, column=column, columnspan=columnspan, rowspan=rowspan, sticky='nsew')

for number in range(9):
    create_button(str(number + 1), 4-number//3, number%3, lambda n=number+1: on_click(n)) #, bg='gainsboro')
create_button("0", 5, 0, lambda: on_click(0), columnspan=2) #, bg='gainsboro')


def on_clear():
    entry.delete(0, tkt.END)

...
def operate(operator):
    global first_num
    global 연산자
    연산자 = operator
    first_num = float(entry.get())
    entry.delete(0, tkt.END)

def on_equal():
    second_num = float(entry.get())
    entry.delete(0, tkt.END)

    if 연산자 == "+":
        entry.insert(0, first_num + second_num)
    elif 연산자 == "-":
        entry.insert(0, first_num - second_num)
    elif 연산자 == "*":
        entry.insert(0, first_num * second_num)
    elif 연산자 == "/":
        entry.insert(0, first_num / second_num)
    elif 연산자 == "%":
        if second_num == 0:
            entry.insert(0, "Error! Division by zero!")
        else:
            entry.insert(0, first_num % second_num)

def on_percent():
    num = float(entry.get())
    entry.delete(0, tkt.END)
    entry.insert(0, num / 100)

def create_button(text, row, column, command=None, **kwargs):
    button = tkt.Button(root, text=text, command=command, highlightthickness=3, **kwargs)
    button.grid(row=row, column=column, sticky='nsew')

create_button("%", 1, 2, lambda: operate("%"), bg='gray70')  # % 버튼에 % 연산을 처리하는 함수 연결
create_button("/", 1, 3, lambda: operate("/"), bg='gray70')
create_button("*", 2, 3, lambda: operate("*"), bg='gray70')
create_button("-", 3, 3, lambda: operate("-"), bg='gray70')
create_button("+", 4, 3, lambda: operate("+"), bg='gray70')
create_button("•", 5, 2, lambda: on_click('.'), bg='gainsboro')
create_button("=", 5, 3, on_equal, bg='orange')
create_button("C", 1, 0, on_clear, bg='gray70')


root.mainloop()