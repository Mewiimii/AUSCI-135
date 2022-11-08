# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:02:55 2022

"""
from tkinter import*
from tkinter.messagebox import showinfo 
global cpu
def setCPU():
    global cpu
    if playerTwoCharValue.get() == '1':
        cpu = 1
    else:
        cpu = 0

def playerOneX():
    selection = 'Player starting is ' +playerOneCharValue.get()
    playerOneCharLabel.config(text = selection)
    playerTwoCharR1.config(state = NORMAL)
    playerTwoCharR2.config(state = NORMAL)  

def playerOneO():
    selection = 'Player starting is ' +playerOneCharValue.get()
    playerOneCharLabel.config(text = selection)
    playerTwoCharR1.config(state = NORMAL)
    playerTwoCharR2.config(state = NORMAL)
    

def playerTwoX():
    #selection = 'CPU starts: True'
    #playerTwoCharLabel.config(text = selection)
    playerOneCharR1.config(state = NORMAL)
    playerOneCharR2.config(state = NORMAL)

def playerTwoO():
    #selection = 'CPU starts: False'
    #playerTwoCharLabel.config(text = selection)
    playerOneCharR1.config(state = NORMAL)
    playerOneCharR2.config(state = NORMAL)


def twoPlayerGame():
    #selection = gameModeValue.get()+' Game'
    #gameModeLabel.config(text = selection)
    difficultyR1.config(state = DISABLED)
    difficultyR2.config(state = DISABLED)
    difficultyR3.config(state = DISABLED)
    difficultyValue.set('none')
    difficultyText = ' '
    difficultyLabel.config(text = difficultyText)
    

def onePlayerGame():
    #selection = gameModeValue.get()+' Game'
    #gameModeLabel.config(text = selection)
    difficultyR1.config(state = NORMAL)
    difficultyR2.config(state = NORMAL)
    difficultyR3.config(state = NORMAL)
    difficultyValue.set('Easy')


def difficulty():
    selection = 'The Difficulty Is Set To '+difficultyValue.get()
    #difficultyLabel.config(text = selection)

def startTwoPlayerGame():
    # Sets initial move
        global S
        global x
        x = S  
        # Sets and hold score
        XOscr = [0,0]
        # Creates a new game      
        def TTTBRD():
            
            #Resets board/memory bank
            g = [['','',''],
                 ['','',''],
                 ['','','']]
            #Scans for a winner every move made, updates score and anounces a winner 
            # while displaying the current board    
            def winner():
               XO = ['X','O']
               XOmsg = ['X Wins!', 'O Wins!']
               XOcol = [0,2] 
               for b in range(2):
                   for r in range(3):
                    if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvp,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   for c in range(3):
                    if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvp,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvp,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvp,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   elif c == 2 and b == 1:
                       st = ['','','']
                       for r in range(3):
                           if '' not in g[r]:
                               st[r] = 'x' 
                               if '' not in st:
                                   showinfo(message="Stalemate")
                                   TTTBRD()     
                    


        # Every button updates the mark on the board, scans for a winner, and changes player
            for r in range(3):
                for c in range(3):
                    def move(r2=r,c2=c):
                        global x
                        g[r2][c2] = x
                        bu = Label(pvp, 
                                   text = g[r2][c2],
                                   padx = 15
                                   )
                        bu.grid(row=r2, column=c2)
                        if x == 'X':
                            x = "O"
                        else:
                            x = 'X'
                        winner()
                        
                    bu = Button(pvp, 
                                text = g[r][c],
                                padx = 20,
                                command = move
                                )
                    bu.grid(row=r, column=c)

        pvp = Tk()
        TTTBRD()
        # X and O icon
        X = Label(pvp,
                  text='X')
        X.grid(row=4, column=0)

        O = Label(pvp,
                  text='O')
        O.grid(row=4, column=2)
        # Restart button
        R = Button(pvp,
                   text='↺ ',
                   command=TTTBRD
                   )
        R.grid(row=4, column=1)
        #Displays X and O's initial score
        Xscore = Label(pvp,
                       text=0)
        Xscore.grid(row=5, column=0)

        Oscore = Label(pvp,
                       text=0)
        Oscore.grid(row=5, column=2)

        pvp.mainloop()

def startEasyGame():
        # CPU start variable
        global cpu
        
        # Sets initial move
        global S
        
        global x
        x = S  
        # Sets and hold score
        XOscr = [0,0]
        #switches player
        def switch():
            global x
            if x == 'X':
                x = "O"
            else:
                x = 'X'    
        # Creates a new game      
        def TTTBRD():
            #sets which player is which icon
            if cpu == 1 and S == 'X':
                cpuXO = 'X'
            else:
                cpuXO = 'O'
            if cpu == 1 and S == 'X':
                playerXO = 'O'
            else:
                playerXO = 'X'
            #Sets board/memory bank
            g = [['','',''],
                 ['','',''],
                 ['','','']]   
               
            #Scans for a winner every move made, updates score and anounces a winner 
            # or stalemate while displaying the current board 
            def winner():
               XO = ['X','O']
               XOmsg = ['X Wins!', 'O Wins!']
               XOcol = [0,2] 
               for b in range(2):
                   for r in range(3):
                    if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(easy,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   for c in range(3):
                    if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(easy,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(easy,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(easy,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   elif c == 2 and b == 1:
                       st = ['','','']
                       for r in range(3):
                           if '' not in g[r]:
                               st[r] = 'x' 
                               if '' not in st:
                                   winCheck()
                                   if won != 1:
                                       showinfo(message="Stalemate")
                                       TTTBRD()
            #checks if cpu goes first and plays            
            def FReasy():
                if cpu == 1:
                    g[0][0] = cpuXO
                    bu = Label(easy, 
                               text = g[0][0],
                               padx = 15
                               )
                    bu.grid(row=0, column=0)
                switch()
            #checks if there is a winner
            def winCheck():
                global won
                won = 0
                XO = ['X','O']
                for b in range(2):
                    for r in range(3):
                     if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                         won = 1
                    for c in range(3):
                     if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                         won = 1
                    if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                         won = 1
                    if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        won = 1
            #every cycle makes a play on the board if there is no winner.
            def easymode():
                global x
                winCheck()
                x = cpuXO
                if won != 1:
                    for r in range(3):
                        for c in range(3):
                            if g[r][c] == '':
                                g[r][c] = x
                                bu = Label(easy, 
                                           text = g[r][c],
                                           padx = 15
                                           )
                                bu.grid(row=r, column=c)
                                winner()
                                return


        # Every button updates the mark on the board, scans for a winner, and starts cpu's turn
            for r in range(3):
                for c in range(3):
                    def move(r2=r,c2=c):
                        global x
                        x = playerXO
                        g[r2][c2] = x
                        bu = Label(easy, 
                                   text = g[r2][c2],
                                   padx = 15
                                   )
                        bu.grid(row=r2, column=c2)
                        switch()
                        winner()
                        easymode()
                        
                    bu = Button(easy, 
                                text = g[r][c],
                                padx = 20,
                                command = move
                                )
                    bu.grid(row=r, column=c)
            FReasy()
        #creates a window and starts a board
        easy = Tk()
        TTTBRD()

        # X and O iconfor score indicators
        X = Label(easy,
                  text='X')
        X.grid(row=4, column=0)

        O = Label(easy,
                  text='O')
        O.grid(row=4, column=2)
        # Restart button
        def restart():
            TTTBRD()
            switch()     
        R = Button(easy,
                   text='↺ ',
                   command=restart
                   )
        R.grid(row=4, column=1)
        #Displays X and O's initial score
        Xscore = Label(easy,
                       text=0)
        Xscore.grid(row=5, column=0)

        Oscore = Label(easy,
                       text=0)
        Oscore.grid(row=5, column=2)

        easy.mainloop()

def startMedGame():
        # CPU start variable
        global cpu
 
        # Sets initial move
        global S

        global x
        x = S  
        # Sets and hold score
        XOscr = [0,0]
        # Creates a new game
        def switch():
            global x
            if x == 'X':
                x = "O"
            else:
                x = 'X'       
        def TTTBRD():
            #sets which player is which icon
            if cpu == 1 and S == 'X':
                cpuXO = 'X'
            else:
                cpuXO = 'O'
            if cpu == 1 and S == 'X':
                playerXO = 'O'
            else:
                playerXO = 'X'
            #Sets board/memory bank
            g = [['','',''],
                 ['','',''],
                 ['','','']]   
               
            #Scans for a winner every move made, updates score and anounces a winner 
            # or stalemate while displaying the current board 
            def winner():
               XO = ['X','O']
               XOmsg = ['X Wins!', 'O Wins!']
               XOcol = [0,2] 
               for b in range(2):
                   for r in range(3):
                    if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(med,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   for c in range(3):
                    if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(med,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(med,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(med,
                                       text=XOscr[b])
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   elif c == 2 and b == 1:
                       st = ['','','']
                       for r in range(3):
                           if '' not in g[r]:
                               st[r] = 'x' 
                               if '' not in st:
                                   winCheck()
                                   if won != 1:
                                       showinfo(message="Stalemate")
                                       TTTBRD()
            #checks if cpu goes first and plays            
            def FRmed():
                if cpu == 1:
                    g[1][1] = cpuXO
                    bu = Label(med, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                switch()
            #checks if there is a winner
            def winCheck():
                global won
                won = 0
                XO = ['X','O']
                for b in range(2):
                    for r in range(3):
                     if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                         won = 1
                    for c in range(3):
                     if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                         won = 1
                    if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                         won = 1
                    if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        won = 1
            #every cycle makes a play on the board if there is no winner.
            def medmode():
                global x
                winCheck()
                x = cpuXO
                if won != 1:
                    if g[1][1] == '':
                        g[1][1] = x
                        bu = Label(med, 
                                   text = g[1][1],
                                   padx = 15
                                   )
                        bu.grid(row=1, column=1)
                        winner()
                    elif g[0][0] == '':
                         g[0][0] = x
                         bu = Label(med, 
                                    text = g[0][0],
                                    padx = 15
                                    )
                         bu.grid(row=0, column=0)
                         winner()
                    elif g[2][2] == '':
                         g[2][2] = x
                         bu = Label(med, 
                                    text = g[2][2],
                                    padx = 15
                                    )
                         bu.grid(row=2, column=2)
                         winner()
                    elif g[0][2] == '':
                         g[0][2] = x
                         bu = Label(med, 
                                    text = g[0][2],
                                    padx = 15
                                    )
                         bu.grid(row=0, column=2)
                         winner()
                    elif g[0][1] == '':
                         g[0][1] = x
                         bu = Label(med, 
                                    text = g[0][1],
                                    padx = 15
                                    )
                         bu.grid(row=0, column=1)
                         winner()
                    elif g[1][2] == '':
                         g[1][2] = x
                         bu = Label(med, 
                                    text = g[1][2],
                                    padx = 15
                                    )
                         bu.grid(row=1, column=2)
                         winner()
                    elif g[2][0] == '':
                         g[2][0] = x
                         bu = Label(med, 
                                    text = g[2][0],
                                    padx = 15
                                    )
                         bu.grid(row=2, column=0)
                         winner()
                    elif g[1][0] == '':
                         g[1][0] = x
                         bu = Label(med, 
                                    text = g[1][0],
                                    padx = 15
                                    )
                         bu.grid(row=1, column=0)
                         winner()
                    elif g[2][1] == '':
                         g[2][1] = x
                         bu = Label(med, 
                                    text = g[2][1],
                                    padx = 15
                                    )
                         bu.grid(row=2, column=1)
                         winner()


        # Every button updates the mark on the board, scans for a winner, and starts cpu's turn
            for r in range(3):
                for c in range(3):
                    def move(r2=r,c2=c):
                        global x
                        x = playerXO
                        g[r2][c2] = x
                        bu = Label(med, 
                                   text = g[r2][c2],
                                   padx = 15
                                   )
                        bu.grid(row=r2, column=c2)
                        switch()
                        winner()
                        medmode()
                        
                    bu = Button(med, 
                                text = g[r][c],
                                padx = 20,
                                command = move
                                )
                    bu.grid(row=r, column=c)
            FRmed()
        #creates a window and starts a board
        med = Tk()
        TTTBRD()

        # X and O iconfor score indicators
        X = Label(med,
                  text='X')
        X.grid(row=4, column=0)

        O = Label(med,
                  text='O')
        O.grid(row=4, column=2)
        # Restart button 
        def restart():
            TTTBRD()
            switch()    
        R = Button(med,
                   text='↺ ',
                   command=restart
                   )
        R.grid(row=4, column=1)
        #Displays X and O's initial score
        Xscore = Label(med,
                       text=0)
        Xscore.grid(row=5, column=0)

        Oscore = Label(med,
                       text=0)
        Oscore.grid(row=5, column=2)

        med.mainloop()

def startHardGame():
    # CPU start variable

    # Sets initial move   

    x = S  
    # Sets and hold score
    XOscr = [0,0]
    # Creates a new game
    def switch():
        global x
        if x == 'X':
            x = "O"
        else:
            x = 'X'       
    def TTTBRD():
        #sets which player is which icon
        if cpu == 1 and S == 'X':
            cpuXO = 'X'
        else:
            cpuXO = 'O'
        if cpu == 1 and S == 'X':
            playerXO = 'O'
        else:
            playerXO = 'X'
        #Sets board/memory bank
        g = [['','',''],
             ['','',''],
             ['','','']]   
           
        #Scans for a winner every move made, updates score and anounces a winner 
        # or stalemate while displaying the current board 
        def winner():
           XO = ['X','O']
           XOmsg = ['X Wins!', 'O Wins!']
           XOcol = [0,2] 
           for b in range(2):
               for r in range(3):
                if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                    XOscr[b] = XOscr[b] + 1
        
                    Score = Label(hard,
                                   text=XOscr[b])
                    Score.grid(row=5, column=XOcol[b])
                    
                    showinfo(message=XOmsg[b])
                    TTTBRD()
               for c in range(3):
                if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                    XOscr[b] = XOscr[b] + 1
        
                    Score = Label(hard,
                                   text=XOscr[b])
                    Score.grid(row=5, column=XOcol[b])
                    
                    showinfo(message=XOmsg[b])
                    TTTBRD()
               if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                    XOscr[b] = XOscr[b] + 1
        
                    Score = Label(hard,
                                   text=XOscr[b])
                    Score.grid(row=5, column=XOcol[b])
                    
                    showinfo(message=XOmsg[b])
                    TTTBRD()
               if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                    XOscr[b] = XOscr[b] + 1
        
                    Score = Label(hard,
                                   text=XOscr[b])
                    Score.grid(row=5, column=XOcol[b])
                    
                    showinfo(message=XOmsg[b])
                    TTTBRD()
               elif c == 2 and b == 1:
                   st = ['','','']
                   for r in range(3):
                       if '' not in g[r]:
                           st[r] = 'x' 
                           if '' not in st:
                               winCheck()
                               if won != 1:
                                   showinfo(message="Stalemate")
                                   TTTBRD()
        #checks if cpu goes first and plays            
        def FRhard():
            if cpu == 1:
                g[0][0] = cpuXO
                bu = Label(hard, 
                           text = g[0][0],
                           padx = 15
                           )
                bu.grid(row=0, column=0)
            switch()
        #checks if there is a winner and updates the won value
        def winCheck():
            global won
            won = 0
            XO = ['X','O']
            for b in range(2):
                for r in range(3):
                 if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                     won = 1
                for c in range(3):
                 if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                     won = 1
                if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                     won = 1
                if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                    won = 1
        #every cycle makes a play on the board if there is no winner.
        def hardmode():
            global x
            winCheck()
            x = cpuXO
            if won != 1:
                #check for possible win
                if g[0][0] == x and g[0][1] == x and g[0][2] == '':
                    g[0][2] = x
                    bu = Label(hard, 
                               text = g[0][2],
                               padx = 15
                               )
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == x and g[0][1] == x and g[0][0] == '':
                    g[0][0] = x
                    bu = Label(hard, 
                               text = g[0][0],
                               padx = 15
                               )
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == x and g[0][2] == x and g[0][1] == '':
                    g[0][1] = x
                    bu = Label(hard, 
                               text = g[0][1],
                               padx = 15
                               )
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[1][0] == x and g[1][1] == x and g[1][2] == '':
                    g[1][2] = x
                    bu = Label(hard, 
                               text = g[1][2],
                               padx = 15
                               )
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[1][2] == x and g[1][1] == x and g[1][0] == '':
                    g[1][0] = x
                    bu = Label(hard, 
                               text = g[1][0],
                               padx = 15
                               )
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[1][0] == x and g[1][2] == x and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[2][0] == x and g[2][1] == x and g[2][2] == '':
                    g[2][2] = x
                    bu = Label(hard, 
                               text = g[2][2],
                               padx = 15
                               )
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == x and g[2][1] == x and g[2][0] == '':
                    g[2][0] = x
                    bu = Label(hard, 
                               text = g[2][0],
                               padx = 15
                               )
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == x and g[2][2] == x and g[2][1] == '':
                    g[2][1] = x
                    bu = Label(hard, 
                               text = g[2][1],
                               padx = 15
                               )
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[0][0] == x and g[1][0] == x and g[2][0] == '':
                    g[2][0] = x
                    bu = Label(hard, 
                               text = g[2][0],
                               padx = 15
                               )
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == x and g[1][0] == x and g[0][0] == '':
                    g[0][0] = x
                    bu = Label(hard, 
                               text = g[0][0],
                               padx = 15
                               )
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == x and g[2][0] == x and g[1][0] == '':
                    g[1][0] = x
                    bu = Label(hard, 
                               text = g[1][0],
                               padx = 15
                               )
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[0][0] == x and g[2][2] == x and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[0][1] == x and g[1][1] == x and g[2][1] == '':
                    g[2][1] = x
                    bu = Label(hard, 
                               text = g[2][1],
                               padx = 15
                               )
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[1][2] == x and g[1][1] == x and g[0][1] == '':
                    g[0][1] = x
                    bu = Label(hard, 
                               text = g[0][1],
                               padx = 15
                               )
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[0][1] == x and g[2][1] == x and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[0][2] == x and g[1][2] == x and g[2][2] == '':
                    g[2][2] = x
                    bu = Label(hard, 
                               text = g[2][2],
                               padx = 15
                               )
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == x and g[1][2] == x and g[0][2] == '':
                    g[0][2] = x
                    bu = Label(hard, 
                               text = g[0][2],
                               padx = 15
                               )
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[2][2] == x and g[0][2] == x and g[1][2] == '':
                    g[1][2] = x
                    bu = Label(hard, 
                               text = g[1][2],
                               padx = 15
                               )
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[0][0] == x and g[2][2] == x and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == x and g[2][2] == x and g[0][0] == '':
                    g[0][0] = x
                    bu = Label(hard, 
                               text = g[0][0],
                               padx = 15
                               )
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == x and g[1][1] == x and g[2][2] == '':
                    g[2][2] = x
                    bu = Label(hard, 
                               text = g[2][2],
                               padx = 15
                               )
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[0][2] == x and g[2][0] == x and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == x and g[2][0] == x and g[0][2] == '':
                    g[0][2] = x
                    bu = Label(hard, 
                               text = g[0][2],
                               padx = 15
                               )
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == x and g[1][1] == x and g[2][0] == '':
                    g[2][0] = x
                    bu = Label(hard, 
                               text = g[2][0],
                               padx = 15
                               )
                    bu.grid(row=2, column=0)
                    winner()
                    return
                #Checks for a block move 
                if g[0][0] == playerXO and g[0][1] == playerXO and g[0][2] == '':
                    g[0][2] = x
                    bu = Label(hard, 
                               text = g[0][2],
                               padx = 15
                               )
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == playerXO and g[0][1] == playerXO and g[0][0] == '':
                    g[0][0] = x
                    bu = Label(hard, 
                               text = g[0][0],
                               padx = 15
                               )
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == playerXO and g[0][2] == playerXO and g[0][1] == '':
                    g[0][1] = x
                    bu = Label(hard, 
                               text = g[0][1],
                               padx = 15
                               )
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[1][0] == playerXO and g[1][1] == playerXO and g[1][2] == '':
                    g[1][2] = x
                    bu = Label(hard, 
                               text = g[1][2],
                               padx = 15
                               )
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[1][2] == playerXO and g[1][1] == playerXO and g[1][0] == '':
                    g[1][0] = x
                    bu = Label(hard, 
                               text = g[1][0],
                               padx = 15
                               )
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[1][0] == playerXO and g[1][2] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[2][0] == playerXO and g[2][1] == playerXO and g[2][2] == '':
                    g[2][2] = x
                    bu = Label(hard, 
                               text = g[2][2],
                               padx = 15
                               )
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == playerXO and g[2][1] == playerXO and g[2][1] == '':
                    g[2][0] = x
                    bu = Label(hard, 
                               text = g[2][0],
                               padx = 15
                               )
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == playerXO and g[2][2] == playerXO and g[2][1] == '':
                    g[2][1] = x
                    bu = Label(hard, 
                               text = g[2][1],
                               padx = 15
                               )
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[0][0] == playerXO and g[1][0] == playerXO and g[2][0] == '':
                    g[2][0] = x
                    bu = Label(hard, 
                               text = g[2][0],
                               padx = 15
                               )
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == playerXO and g[1][0] == playerXO and g[0][0] == '':
                    g[0][0] = x
                    bu = Label(hard, 
                               text = g[0][0],
                               padx = 15
                               )
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == playerXO and g[2][0] == playerXO and g[1][0] == '':
                    g[1][0] = x
                    bu = Label(hard, 
                               text = g[1][0],
                               padx = 15
                               )
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[0][1] == playerXO and g[1][1] == playerXO and g[2][1] == '':
                    g[2][1] = x
                    bu = Label(hard, 
                               text = g[2][1],
                               padx = 15
                               )
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[2][1] == playerXO and g[1][1] == playerXO and g[0][1] == '':
                    g[0][1] = x
                    bu = Label(hard, 
                               text = g[0][1],
                               padx = 15
                               )
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[0][1] == playerXO and g[2][1] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[0][2] == playerXO and g[1][2] == playerXO and g[2][2] == '':
                    g[2][2] = x
                    bu = Label(hard, 
                               text = g[2][2],
                               padx = 15
                               )
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == playerXO and g[1][2] == playerXO and g[0][2] == '':
                    g[0][2] = x
                    bu = Label(hard, 
                               text = g[0][2],
                               padx = 15
                               )
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[2][2] == playerXO and g[0][2] == playerXO and g[1][2] == '':
                    g[1][2] = x
                    bu = Label(hard, 
                               text = g[1][2],
                               padx = 15
                               )
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[0][0] == playerXO and g[2][2] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == playerXO and g[2][2] == playerXO and g[0][0] == '':
                    g[0][0] = x
                    bu = Label(hard, 
                               text = g[0][0],
                               padx = 15
                               )
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == playerXO and g[1][1] == playerXO and g[2][2] == '':
                    g[2][2] = x
                    bu = Label(hard, 
                               text = g[2][2],
                               padx = 15
                               )
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[0][2] == playerXO and g[2][0] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == playerXO and g[2][0] == playerXO and g[0][2] == '':
                    g[0][2] = x
                    bu = Label(hard, 
                               text = g[0][2],
                               padx = 15
                               )
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == playerXO and g[1][1] == playerXO and g[2][0] == '':
                    g[2][0] = x
                    bu = Label(hard, 
                               text = g[2][0],
                               padx = 15
                               )
                    bu.grid(row=2, column=0)
                    winner()
                    return
                #Move order 
                if g[0][0] == '' and g[2][2] == '':
                     g[0][0] = x
                     bu = Label(hard, 
                                text = g[0][0],
                                padx = 15
                                )
                     bu.grid(row=0, column=0)
                     winner()
                     return
                if g[2][2] == '' and g[0][0] == x:
                     g[2][2] = x
                     bu = Label(hard, 
                                text = g[2][2],
                                padx = 15
                                )
                     bu.grid(row=2, column=2)
                     winner()
                     return 
                if g[0][2] == '':
                     g[0][2] = x
                     bu = Label(hard, 
                                text = g[0][2],
                                padx = 15
                                )
                     bu.grid(row=0, column=2)
                     winner()
                     return
                if g[2][0] == '':
                     g[2][0] = x
                     bu = Label(hard, 
                                text = g[2][0],
                                padx = 15
                                )
                     bu.grid(row=2, column=0)
                     winner()
                     return
                if g[0][1] == '':
                     g[0][1] = x
                     bu = Label(hard, 
                                text = g[0][1],
                                padx = 15
                                )
                     bu.grid(row=0, column=1)
                     winner()
                     return
                if g[1][2] == '':
                     g[1][2] = x
                     bu = Label(hard, 
                                text = g[1][2],
                                padx = 15
                                )
                     bu.grid(row=1, column=2)
                     winner()
                     return
                
                if g[1][0] == '':
                     g[1][0] = x
                     bu = Label(hard, 
                                text = g[1][0],
                                padx = 15
                                )
                     bu.grid(row=1, column=0)
                     winner()
                     return
                if g[2][1] == '':
                     g[2][1] = x
                     bu = Label(hard, 
                                text = g[2][1],
                                padx = 15
                                )
                     bu.grid(row=2, column=1)
                     winner()
                     return
                if g[1][1] == '':
                    g[1][1] = x
                    bu = Label(hard, 
                               text = g[1][1],
                               padx = 15
                               )
                    bu.grid(row=1, column=1)
                    winner()
                    return 

    # Every button updates the mark on the board, scans for a winner, and starts cpu's turn
        for r in range(3):
            for c in range(3):
                def move(r2=r,c2=c):
                    global x
                    x = playerXO
                    g[r2][c2] = x
                    bu = Label(hard, 
                               text = g[r2][c2],
                               padx = 15
                               )
                    bu.grid(row=r2, column=c2)
                    switch()
                    winner()
                    hardmode()
                    
                bu = Button(hard, 
                            text = g[r][c],
                            padx = 20,
                            command = move
                            )
                bu.grid(row=r, column=c)
        FRhard()
    #creates a window and starts a board
    hard = Tk()
    TTTBRD()

    # X and O iconfor score indicators
    X = Label(hard,
              text='X')
    X.grid(row=4, column=0)

    O = Label(hard,
              text='O')
    O.grid(row=4, column=2)
    # Restart button 
    def restart():
        TTTBRD()
        switch()    
    R = Button(hard,
               text='↺ ',
               command=restart
               )
    R.grid(row=4, column=1)
    #Displays X and O's initial score
    Xscore = Label(hard,
                   text=0)
    Xscore.grid(row=5, column=0)

    Oscore = Label(hard,
                   text=0)
    Oscore.grid(row=5, column=2)

    hard.mainloop()


def startGame():
    global S
    global cpu
    if gameModeValue.get() == 'Two Player':
        S = playerOneCharValue.get()
        startTwoPlayerGame()
    else:
        if difficultyValue.get() == 'Easy':
            S = playerOneCharValue.get()
            setCPU()
            startEasyGame()
        elif difficultyValue.get() == 'Medium':
            S = playerOneCharValue.get()
            setCPU()
            startMedGame()
        elif difficultyValue.get() == 'Hard':
            S = playerOneCharValue.get()
            setCPU()
            startHardGame()
            

            

menu = Tk()
menu.title('Menu')

menuCanvas = Canvas(menu, height=500, width=500, highlightthickness=0, bg = '#424242')
menuCanvas.pack(fill='both', expand = True)
#change to proper file grabs
onePlayerBox = PhotoImage(file='oneplayerbox.png')
twoPlayerBox = PhotoImage(file='twoplayerbox.png')
easyBox = PhotoImage(file='easybox.png')
mediumBox = PhotoImage(file='mediumbox.png')
hardBox = PhotoImage(file='hardbox.png')
startBox = PhotoImage(file='startbox.png')
xPic = PhotoImage(file='xpic.png') #0f0f0f
oPic = PhotoImage(file='opic.png')


playerOneCharFrame = Frame(menuCanvas,
                    height = 200, width = 200, bg='#424242')

playerOneCharFrame.pack(side = LEFT)

playerOneCharValue = StringVar()

playerOneCharValue.set('X')

playerOneCharR1 =Radiobutton(playerOneCharFrame, image = xPic,
                             variable = playerOneCharValue,
                             value = 'X', command=playerOneX, bg = '#424242')

playerOneCharR2 =Radiobutton(playerOneCharFrame, image = oPic,
                             variable = playerOneCharValue,
                             value = 'O', command = playerOneO, bg = '#424242')


playerOneCharR1.pack()
playerOneCharR2.pack()


playerOneCharLabel = Label(playerOneCharFrame, text = ' ', bg = '#424242')
playerOneCharLabel.pack()
playerOneCharLabel.config(text = 'Starting player is X')

playerTwoCharFrame = Frame(menuCanvas,
                    height = 200, width = 200, bg='#424242')


playerTwoCharLabel = Label(playerTwoCharFrame, text = ' ', bg = '#424242')
playerTwoCharLabel.pack()
playerTwoCharLabel.config(text = 'Choose who goes first:')


playerTwoCharFrame.pack(side = RIGHT)

playerTwoCharValue = StringVar()

playerTwoCharValue.set('True')

playerTwoCharR1 =Radiobutton(playerTwoCharFrame, text = 'Computer Starts',
                             variable = playerTwoCharValue,
                             value = 1, command=playerTwoX, bg = '#424242')

playerTwoCharR2 =Radiobutton(playerTwoCharFrame, text = 'Player Starts',
                             variable = playerTwoCharValue,
                             value = 0, command = playerTwoO, bg = '#424242')


playerTwoCharR1.pack()
playerTwoCharR2.pack()


gameModeFrame = Frame(menuCanvas,
                      height = 200, width = 200, bg = '#424242')

gameModeLabel = Label(gameModeFrame, text = ' ', bg = '#424242')
gameModeLabel.pack()
gameModeLabel.config(text = 'How many players?')

gameModeFrame.pack(side = TOP)

gameModeValue = StringVar()

gameModeValue.set('One Player')

gameModeR1 = Radiobutton(gameModeFrame, image = onePlayerBox,
                         variable = gameModeValue, value = 'One Player',
                         command = onePlayerGame, bg = '#424242')
gameModeR2 = Radiobutton(gameModeFrame, image = twoPlayerBox,
                         variable = gameModeValue, value = 'Two Player',
                         command = twoPlayerGame, bg = '#424242')
gameModeR1.pack()
gameModeR2.pack()


difficultyFrame = Frame(menuCanvas,
                        height = 200, width = 200, bg = '#424242')

difficultyLabel = Label(difficultyFrame, text = ' ', bg = '#424242')
difficultyLabel.pack()
difficultyLabel.config(text = 'Difficulty:')

difficultyFrame.pack(side = BOTTOM)

difficultyValue = StringVar()

difficultyValue.set('Easy')

difficultyR1=Radiobutton(difficultyFrame, image = easyBox,
                         variable = difficultyValue,
                         value = 'Easy', command=difficulty, bg = '#424242')
difficultyR2=Radiobutton(difficultyFrame, image = mediumBox,
                         variable = difficultyValue,
                         value = 'Medium', command=difficulty, bg = '#424242')
difficultyR3=Radiobutton(difficultyFrame, image = hardBox,
                         variable = difficultyValue,
                         value = 'Hard', command=difficulty, bg = '#424242')

difficultyR1.pack()
difficultyR2.pack()
difficultyR3.pack()


startGameB = Button(menuCanvas, image = startBox, bd = 0, command=startGame, bg = '#424242', activebackground= '#424242')
    
              
startGameB.pack()

menu.mainloop()



