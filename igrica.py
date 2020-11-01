matrica = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]

def clear_board(matrica):
    for i in range(len(matrica)):
        for x in range(4):
            matrica[i][x] = ""
        x = 0
def print_board(matrica):
    for i in range(len(matrica)):
        print(matrica[i])

def jesu_li_jednaki(matrica):
    for i in range(len(matrica)):
        if matrica[i][0] == matrica[i][1] == matrica[i][2] == matrica[i][3] !="":
            return True
    for x in range(4):
        if matrica[0][x] == matrica[1][x] == matrica[2][x] == matrica[3][x] != "":
            return True
    if matrica[0][0] == matrica[1][1] == matrica[2][2] == matrica[3][3] != "" or matrica[3][0] == matrica[2][1] == matrica[1][2] == matrica[0][3] !="":
        return True

print_board(matrica)
turn = "X"
potezi = 0
while True:
    print("Igrac", turn,"je na redu. Unesite pozicije na koju zelite da upisete simbol: ")
    i = int(input())
    x = int(input())
    while i > 3  or x > 3 or matrica[i][x] != "":
        print("Napravili ste gresku! Unesite pozicije ponovo:")
        i = int(input())
        x = int(input())
    else:
        matrica[i][x] = turn
        potezi = potezi + 1
        if jesu_li_jednaki(matrica) :
            print("Kraj! Igrac", turn,"je pobjednik!")
            print_board(matrica)
            print("                  ")
            print("Pocinje nova runda:")
            clear_board(matrica)
            print_board(matrica)
        elif potezi == 16:
            print("Nerijeseno je! Pocinje nova partija: ")  
            clear_board(matrica) 
            print_board(matrica)    
        else:
            for i in range(len(matrica)):
                print(matrica[i])
            if turn == "X":
                turn = "Y"
            else:
                turn = "X"
