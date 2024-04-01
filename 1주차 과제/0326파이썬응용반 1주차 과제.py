import tkinter as tkt
from tkinter.filedialog import *
from tkinter import filedialog
from tkinter import messagebox

window = tkt.Tk()
window.title('Notepad')
window.geometry('400x400+800+300')  # 400x400: 창 크기   800+300: 창이 800,300 위치에 띄워진다
window.resizable(0,0)  # 창 크기 설정 불가

window.iconbitmap("C:\\Users\\예은\\Desktop\\해달 1주차 과제 이미지\\memo.ico")
# photo = tkt.PhotoImage(file="C:\\Study\\해달\\부트캠프\\2024-1-파이썬응용\\해달로고.png")
# window.iconphoto(False, photo)

#텍스트 창 만들기 
text_area = tkt.Text(window)

#공백 설정하기 
window.grid_rowconfigure(0, weight =1)
window.grid_columnconfigure(0, weight = 1)
#텍스트 화면을 윈도우에 동서남북으로 붙인다
text_area.grid(sticky = tkt.N+tkt.E+tkt.S+tkt.W)


def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            text = text_area.get("1.0", "end-1c") 
            file.write(text)
def maker():
     window = tkt.Tk()
     window.title('만든이')
     window.geometry('400x100+800+300')
     window.resizable(0,0) 
     label = tkt.Label(window, text="예은")
     label.pack(pady=20)
def new_file():
    text_area.delete(1.0, tkt.END)


#메뉴 생성
menuMaker = tkt.Menu(window)
#첫번째 메뉴 만들기 
first_menu = tkt.Menu(menuMaker, tearoff=0)
#첫번째 메뉴의 세부메뉴 추가 및 함수 연결
first_menu.add_command(label = '새 파일', command = new_file)
first_menu.add_command(label = '저장', command = save_file)
#메뉴 바 추가 
menuMaker.add_cascade(label='파일', menu=first_menu)
first_menu.add_separator()

#메뉴 구성
window.config(menu = menuMaker)
#종료 옵션 추가하기
first_menu.add_command(label='종료', command=window.destroy)

#두번째 메뉴 추가 
second_menu = tkt.Menu(menuMaker, tearoff=0)
#세부 메뉴 추가, 함수 연결
second_menu.add_command(label = '만든 이', command=maker)

#메뉴 바 추가
menuMaker.add_cascade(label='정보', menu = second_menu)
window.mainloop() # 창 실행!