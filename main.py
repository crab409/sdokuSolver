import tkinter


app = tkinter.Tk()
app.resizable()
app.title("sudoku-doku")

# 버튼 클리하면 보드드에 +1 되는 함수
def btnClicked(row, col) :
    global btnList 
    global board 

    board[row][col] = (board[row][col]+1)%10
    btnList[row][col].config(text=board[row][col])
    if board[row][col]==0:btnList[row][col].config(text=' ')


# 색깔 좀 이쁘게 만드는 함수
def resetColor() :
    global btnList

    for row in range(9) :
        for col in range(9) :
            btnList[row][col].config(fg="#000000")

            if row//3%2==0 :
                if col//3%2==0:
                    btnList[row][col].config(bg="#E5EFFB")
                else :
                    btnList[row][col].config(bg="#FFFFFF")
            else : 
                if col//3%2==0:
                    btnList[row][col].config(bg="#FFFFFF")
                else :
                    btnList[row][col].config(bg="#E5EFFB")


# 계산을 시작하는 함수 
def start() :
    global board 
    global btnList

    if sum(map(sum, board))==0:return 

    while (True) :
        cnt = 0 
        for row in range(9) : 
            for col in range(9) :
                if board[row][col] != 0 : continue
                print(f"row: {row}, col: {col}번째 보드 연산중...")
                ans = isOkNumber(
                    blockCheck(row, col),
                    rowCheck(col),
                    colCheck(row)
                )
                print(ans)

                if len(ans) > 1 : continue
                cnt+=1 
                data = ans[0]
                board[row][col] = data
                btnList[row][col].config(text=data, fg="#3D2EDA")

        if cnt==0 : break


# 블럭 단위로 존재하는 숫자 체크 
def blockCheck(row, col) :
    global board 
    arr = [0 for i in range(9)]
    bRow = row//3
    bCol = col//3 

    for line in board[bRow*3:bRow*3+3] :
        for data in line[bCol*3:bCol*3+3] : 
            if data==0: continue
            arr[data-1] = 1
    
    return arr 

# 행 단위로 존재하는 숫자 체크
def rowCheck(col) :
    global board 
    arr = [0 for i in range(9)]

    for row in range(9) :
        data = board[row][col]
        if data == 0 : continue 
        arr[data-1] = 1
    
    return arr

# 열 단위로 존재하는 숫자 체크 
def colCheck(row) :
    global board 
    arr = [0 for i in range(9)]

    for col in range(9) :
        data = board[row][col]
        if data == 0 : continue 
        arr[data-1] = 1

    return arr


# 존재하는 숫자를 제외해 가능한 숫자를 추려내는 함수
def isOkNumber(block, rowLine, colLine) :
    arr = [0 for i in range(9)]

    for i in range(9) : 
        data = block[i]+rowLine[i]+colLine[i]
        arr[i] = 0 if data==0 else 1

    result = []
    for i in range(9) :
        if arr[i] == 0 : 
            result.append(i+1)

    return result



board = [
    [0 for i in range(9)] for j in range(9)
]

btnList = []
for row in range(9) :
    btnLine = []
    for col in range(9) :
        btn = tkinter.Button(
            app, 
            height=2,
            width=5,
            text= ' ', 
            font= ("Arial", 18),
            command=lambda row=row, col=col:btnClicked(row, col)
        )
        btn.grid(row=row, column=col)
        btnLine.append(btn)
    btnList.append(btnLine)

startBtn = tkinter.Button(
    app, 
    text="start",
    command=start
)

startBtn.grid(row=10, column=10)

resetColor()
app.mainloop()