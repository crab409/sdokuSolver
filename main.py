import tkinter 

overlap = False

app = tkinter.Tk() 
app.resizable(False, False)
app.title("sdoku-doku")

def checkB4Running() :
    global btnList
    global overlap
    global board 

    for row in range(0, 9, 1) : 
        counter = [0 for i in range(0, 9, 1)]

        for col in range(0, 9, 1) :
            if(board[row][col] != 0) : 
                counter[board[row][col]-1] += 1

        for num in range(0, 9, 1) : 
            if (counter[num] >= 2) : 
                print(f"{row}행 에서 중복 발생, {num+1}이 다수 존재")
                overlap = [0, row, num+1]
                break

        if (bool(overlap)) :
            break

    if (not overlap) :
        for col in range(0, 9, 1) :
            counter = [0 for i in range(0, 9, 1)]

            for row in range(0, 9, 1) :
                if(board[row][col] != 0) :
                    counter[board[row][col]-1] += 1

            for num in range(0, 9, 1) :
                if (counter[num] >= 2) :
                    print(f"{}열에서 중복 발생, {num+1}이 다수 존재")
                    overlap = [1, col, num+1]
                    break
            
            if (bool(overlap)) :
                break

    if (bool(overlap)) : 
        if (overlap[0] == 0) :
            for col in range(0, 9, 1) : 
                if (board[overlap[1]][col] == overlap[2]) :
                    btnList[overlap[1]][col].config(bg="#F78181")
                else : 
                    btnList[overlap[1]][col].config(bg="#F5A9A9")
        
        else : 
            for row in range(0, 9, 1) :
                if (board[row][overlap[1]] == overlap[2]) : 
                    btnList[row][overlap[1]].config(bg="#F78181")
                else : 
                    btnList[row][overlap[1]].config(bg="#F5A9A9")

    



def numIn(num, i, j, wiget) : 
    global btnList
    global board 

    board[i][j] = num
    btnList[i][j].config(text= f'{num}')


    wiget.destroy()

def btnClicked(i, j) :
    global board
    global btnList

    if(board[i][j] == 0) :
        inputBtnWiget = tkinter.Tk() 
        inputBtnWiget.title("NumberInput")
        inputBtnWiget.resizable(False, False)

        for number in range(0, 9, 1) :
            inputBtn = tkinter.Button(
                inputBtnWiget,
                text= f"{number+1}",
                font= ("Arial", 17),
                height=1,
                width=3,
                command= lambda num=number+1, i=i, j=j, wiget=inputBtnWiget : numIn(num, i, j, wiget)
            )
            inputBtn.grid(row=number%3, column=number//3)


    else : 
        board[i][j] = 0
        btnList[i][j].config(text=' ')


board = [[0 for i in range(0, 9, 1)] for i in range(0, 9, 1)]

btnList = []
for i in range(0, 9, 1) :
    btnLine = []
    for j in range(0, 9, 1) :
        btn = tkinter.Button(
            app, 
            height=2,
            width=5,
            text= ' ', 
            font= ("Arial", 18),
            command= lambda i=i, j=j:btnClicked(i, j)
        )
        btn.grid(row=i, column=j)
        btnLine.append(btn)
    btnList.append(btnLine)

startBtn = tkinter.Button(
    app, 
    text= "Start Engin",
    font= ("Arial", 20),
    fg= "#FFFFFF",
    bg= "#2E2E2E",
    command=checkB4Running
)
startBtn.grid(row=9, column=9)

app.mainloop()