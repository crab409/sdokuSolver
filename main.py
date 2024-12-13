import tkinter 

overlap = False

app = tkinter.Tk() 
app.resizable(False, False)
app.title("sdoku-doku")

def setOverlapColor() :
    global btnList 
    global overlap

    if (overlap[0] == 0) :
        for col in range(0, 9, 1) : 
            if (board[overlap[1]][col] == overlap[2]) : 
                btnList[overlap[1]][col].config(bg='#F5A9A9')
            else : 
                btnList[overlap[1]][col].config(bg="#F8E0E0")


    elif (overlap[0] == 1) :
        for row in range(0, 9, 1) : 
            if (board[row][overlap[1]] == overlap[2]) : 
                btnList[row][overlap[1]].config(bg="#F5A9A9")
            else : 
                btnList[row][overlap[1]].config(bg="#F8E0E0")

    else :
        for row in range(overlap[1][0]*3, overlap[1][0]*3+3, 1) : 
            for col in range(overlap[1][1]*3, overlap[1][1]*3+3, 1) : 
                if (board[row][col] == overlap[2]) :
                    btnList[row][col].config(bg="#F5A9A9")
                else : 
                    btnList[row][col].config(bg="#F8E0E0")


def resetColor() :
    global btnList
    global overlap

    for row in range(0, 9, 1) : 
        for col in range(0, 9, 1) : 

            if((row//3)%2==0) :
                if((col//3)%2==0) :
                    btnList[row][col].config(bg="#EFF5FB")
                else : 
                    btnList[row][col].config(bg="#FFFFFF")
            else :
                if((col//3)%2!=0) :
                    btnList[row][col].config(bg="#EFF5FB")
                else : 
                    btnList[row][col].config(bg="#FFFFFF")
    
    overlap = False



def isOverlap() : #return : [중복 종류(0:행, 1:열, 2:블럭), 중복위치, 중복값]
    global board
    global overlap 

    for row in range(0, 9, 1) :
        counter = [0 for i in range(0, 10, 1)]

        for col in range(0, 9, 1) : 
            counter[board[row][col]] += 1

        for idx in range(1, 10, 1) : 
            if (counter[idx] >= 2) :
                print(f"fun(isOverlap) : {row}행에서 중복 발생, {idx}가 다수 존재")
                overlap = [0, row, idx]
                return True

    
    for col in range(0, 9, 1) : 
        counter = [0 for i in range(0, 10, 1)]

        for row in range(0, 9, 1) : 
            counter[board[row][col]] += 1

        for idx in range(1, 10, 1) : 
            if (counter[idx] >= 2) :
                print(f"fun(isOverlap) : {col}열에서 중복 발생, {idx}가 다수 존재")
                overlap = [1, col, idx]
                return True


    for rowBlock in range(0, 3, 1) :
        for colBlock in range(0, 3, 1) : 
            counter = [0 for i in range(0, 10, 1)]

            for row in range(rowBlock*3, rowBlock*3+3, 1) :
                for col in range(colBlock*3, colBlock*3+3, 1) : 
                    counter[board[row][col]] += 1

            for idx in range(1, 10, 1) :
                if(counter[idx] >= 2) :
                    print(f"fun(isOverlap) : {rowBlock}헹 {colBlock}열 블럭에서 중복 발생, {idx}가 다수 존재")
                    overlap = [2, [rowBlock, colBlock], idx]
                    return True
    
    print("fun(isOverlap) : 중복이 발생하지 않음")
    return False



def runningEngin() : 
    global board
    global btnList

    tagetLocation =[]
    
    for row in range(0, 9, 1) : 
        for col in range(0, 9, 1) : 
            if (board[row][col] == 0) :
                tagetLocation.append([row, col])
                btnList[row][col].config(fg="#2E2EFE")

    tagetData = [1 for i in range(0, len(tagetLocation), 1)]

    while(True) : 
        for i in range(0, len(tagetData), 1) : 
            #resetColor()
            row = tagetLocation[i][0]
            col = tagetLocation[i][1]
            board[row][col] = tagetData[i]
            #btnList[row][col].config(text= f"{board[row][col]}")

        
        if(not isOverlap()) : 
            break

        #setOverlapColor()

        tagetData[0] += 1

        while (10 in tagetData) :
            for i in range(0, len(tagetData)-1, 1) : 
                if(tagetData[i] >= 10) :
                    tagetData[i+1] += 1
                    tagetData[i] = 1
            
        
        for row in range(0, 9, 1) :
            for col in range(0, 9, 1):
                print(board[row][col], end=' ')
            print()
        print()
    




def checkB4Running() :
    if (isOverlap()) :
        print("fun(checkB4Running) : 중복 발생하여 실행 취소.")
        setOverlapColor()
    
    else : 
        runningEngin()

def numIn(num, i, j, wiget) :
    global btnList
    global board 


    board[i][j] = num
    btnList[i][j].config(text= f'{num}')


    wiget.destroy()

def btnClicked(i, j) :
    global overlap  
    global board
    global btnList

    
    if (bool(overlap)) : 
        print("색상 수정 중")
        
        resetColor()

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

resetColor()

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