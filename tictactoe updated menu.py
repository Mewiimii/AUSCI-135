# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:02:55 2022

"""
from tkinter import*
from tkinter.messagebox import showinfo 
global cpu
def setCPU():
    """
    This function determines if the player or CPU goes first in a one player game
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    # if the player two value is set to one then cpu equals 1 if not cpu equals zero
    global cpu
    if playerTwoCharValue.get() == '1':
        cpu = 1
    else:
        cpu = 0

    

def playerTwoX():
    playerOneCharR1.config(state = NORMAL)
    playerOneCharR2.config(state = NORMAL)

def playerTwoO():
    playerOneCharR1.config(state = NORMAL)
    playerOneCharR2.config(state = NORMAL)


def twoPlayerGame():
    """
    This function allows for the user to access only the options for a two player game in the menu
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    # when the function is called it disables five radio buttons
    difficultyR1.config(state = DISABLED)
    difficultyR2.config(state = DISABLED)
    difficultyR3.config(state = DISABLED)
    playerTwoCharR1.config(state = DISABLED)
    playerTwoCharR2.config(state =  DISABLED)
    # ensure no difficulty value is selected
    difficultyValue.set('none')
    # allows the input for player twos name to be edited and sets it to the deafult
    nameTwo.config(state = NORMAL)
    nameTwo.delete(0, 50)
    nameTwo.insert(0, 'Player 2')

    

def onePlayerGame():
    """
    This function allows for the user to access only the options for a one playerr game in the menu
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    # when the function is called it reverts the state of five radio buttons back to normal
    difficultyR1.config(state = NORMAL)
    difficultyR2.config(state = NORMAL)
    difficultyR3.config(state = NORMAL)
    playerTwoCharR1.config(state = NORMAL)
    playerTwoCharR2.config(state = NORMAL)
    # makes the deafult difficulty easy
    difficultyValue.set('Easy')
    # deletes what is in player twos name and replaces it with CPU
    nameTwo.delete(0, 50)
    nameTwo.insert(0, 'CPU')
    # makes nameTwo unchangable
    nameTwo.config(state = DISABLED)




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
        pvp.title('PvP')
        TTTBRD()
        # X and O icon
        X = Label(pvp,
                  text=player1Name)
        X.grid(row=4, column=0)

        O = Label(pvp,
                  text=player2Name)
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
                playerXO = 'O'
            else:
                cpuXO = 'O'
                playerXO = 'X'
            if cpu == 0 and S == 'O':
                cpuXO = 'X'
                playerXO = 'O'
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
        easy.title('Easy')
        TTTBRD()

        # X and O iconfor score indicators
        X = Label(easy,
                  text=player1Name)
        X.grid(row=4, column=0)

        O = Label(easy,
                  text=player2Name)
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
                playerXO = 'O'
            else:
                cpuXO = 'O'
                playerXO = 'X'
            if cpu == 0 and S == 'O':
                cpuXO = 'X'
                playerXO = 'O'
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
        med.title('Medium')
        TTTBRD()

        # X and O iconfor score indicators
        X = Label(med,
                  text=player1Name)
        X.grid(row=4, column=0)

        O = Label(med,
                  text=player2Name)
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
            playerXO = 'O'
        else:
            cpuXO = 'O'
            playerXO = 'X'
        if cpu == 0 and S == 'O':
            cpuXO = 'X'
            playerXO = 'O'
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
    hard.title('Hard')
    TTTBRD()

    # X and O iconfor score indicators
    X = Label(hard,
              text=player1Name)
    X.grid(row=4, column=0)

    O = Label(hard,
              text=player2Name)
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
    global player1Name
    global player2Name
    if playerOneCharValue.get() == 'X':
        if playerTwoCharValue.get() == '1':
            player1Name = nameOne.get()
            player2Name = nameTwo.get()
        else:
            player1Name = nameOne.get()
            player2Name = nameTwo.get()
    else: 
        if playerTwoCharValue.get() == '1':
            player2Name = nameOne.get()
            player1Name = nameTwo.get()
        else:
            player2Name = nameOne.get()
            player1Name = nameTwo.get()
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
menu.maxsize(400,400) #sets the minimum and maximum sizes for the menu window
menu.minsize(400,400)
menu.title('Menu')

menuCanvas = Canvas(menu, height=400, width=400, highlightthickness=0, bg = '#262626') #creates a canvas to hold the frames
menuCanvas.pack(fill=BOTH, expand=True)

#saving images found in folder to variables
onePlayerBox = PhotoImage(file='oneplayerbox.png')
twoPlayerBox = PhotoImage(file='twoplayerbox.png')
easyBox = PhotoImage(file='easybox.png')
mediumBox = PhotoImage(file='mediumbox.png')
hardBox = PhotoImage(file='hardbox.png')
startBox = PhotoImage(file='startbox.png')
xPic = PhotoImage(file='xpic.png') #0f0f0f
oPic = PhotoImage(file='opic.png')
backgroundPic = PhotoImage(file='background.png')
computerStartsPic = PhotoImage(file='computerstarts.png')
playerStartsPic = PhotoImage(file='playerstarts.png')

#sets the background widget on the canvas
backgroundImage = Label(menuCanvas, image=backgroundPic, bd=0)
backgroundImage.place(x=0,y=0)


#sets the widgets for icon selection (X or O)
playerOneCharFrame = Frame(menuCanvas,
                    height = 200, width = 200, bg='#424242')
playerOneCharFrame.pack()
playerOneCharFrame.place(x = 50, y = 220)
playerOneCharValue = StringVar()
playerOneCharValue.set('X')

playerOneCharR1 =Radiobutton(playerOneCharFrame, image = xPic,
                             variable = playerOneCharValue,
                             value = 'X', bg = '#424242')
playerOneCharR2 =Radiobutton(playerOneCharFrame, image = oPic,
                             variable = playerOneCharValue,
                             value = 'O', bg = '#424242')
playerOneCharR1.pack()
playerOneCharR2.pack()



#sets the widgets for who starts first (computer or player)
playerTwoCharFrame = Frame(menuCanvas,
                    height = 200, width = 200, bg='#424242')
playerTwoCharFrame.pack()
playerTwoCharFrame.place(x = 165, y = 220)
playerTwoCharValue = StringVar()
playerTwoCharValue.set(1)

playerTwoCharR1 =Radiobutton(playerTwoCharFrame, image = computerStartsPic,
                             variable = playerTwoCharValue,
                             value = 1, command=playerTwoX, bg = '#424242')
playerTwoCharR2 =Radiobutton(playerTwoCharFrame, image = playerStartsPic,
                             variable = playerTwoCharValue,
                             value = 0, command = playerTwoO, bg = '#424242')
playerTwoCharR1.pack()
playerTwoCharR2.pack()



#sets the widgets for game mode selection (One player or Two player)
gameModeFrame = Frame(menuCanvas,
                      height = 200, width = 200, bg = '#424242')
gameModeFrame.pack()
gameModeFrame.place(x=40,y=80)
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



# sets the widgets for the difficulty selection (Easy, Medium, or Hard)
difficultyFrame = Frame(menuCanvas,
                        height = 200, width = 200, bg = '#424242')
difficultyFrame.pack()
difficultyFrame.place(x=290,y=210)
difficultyValue = StringVar()
difficultyValue.set('Easy')

difficultyR1=Radiobutton(difficultyFrame, image = easyBox,
                         variable = difficultyValue,
                         value = 'Easy', bg = '#424242')
difficultyR2=Radiobutton(difficultyFrame, image = mediumBox,
                         variable = difficultyValue,
                         value = 'Medium', bg = '#424242')
difficultyR3=Radiobutton(difficultyFrame, image = hardBox,
                         variable = difficultyValue,
                         value = 'Hard', bg = '#424242')
difficultyR1.pack()
difficultyR2.pack()
difficultyR3.pack()


# sets the entry widgets for player names 
nameOne = Entry(menuCanvas, width = 13)
nameOne.insert(0,'Player 1')
nameOne.pack()
nameOne.place(x=200,y=90)

nameTwo = Entry(menuCanvas, width = 13)
nameTwo.insert(0, 'CPU')
nameTwo.pack()
nameTwo.place(x=200,y=115)
nameTwo.config(state = DISABLED)


# sets the widget for the start button 
startGameB = Button(menuCanvas, image = startBox, bd = 0, command=startGame, bg = '#424242', activebackground= '#424242')   
startGameB.pack()
startGameB.place(x=96,y=343)




menu.mainloop()


