# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:02:55 2022
"""
from tkinter import Tk, Canvas, BOTH, PhotoImage, Label, Frame, Toplevel
from tkinter import StringVar, Radiobutton, Entry, DISABLED, Button, NORMAL
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
    This function allows for the user to access only the options for a one player game in the menu
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
        """
        This function allows for a two player game to be played. It creates the game board, checks for a winner, displays a
        winning/draw message and has a restart button
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        # Sets initial move
        global S
        global x
        global player1Wins
        global player2Wins
        player1Wins = 0
        player2Wins = 0
        x = S  
        # Sets and hold score
        XOscr = [0,0]
        # Creates a new game      
        def TTTBRD():
            """
            This function sets the game board back to its deafult empty state
            Parameters
            ----------
            None
            Returns 
            -------
            None
            """            
            #Resets board/memory bank
            g = [['','',''],
                 ['','',''],
                 ['','','']]
            #Scans for a winner every move made, updates score and anounces a winner 
            # while displaying the current board    
            def winner():
               """
               This function determines whether someone has one the game. After each turn the board is scanned for
               a winner and the score is updated accordingly
               Parameters
               ----------
               None
               Returns
               -------
               None
               """
               XO = ['X','O']
               XOmsg = ['X Wins!', 'O Wins!']
               XOcol = [0,2] 
               for b in range(2):
                   for r in range(3):
                    if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvpCanvas,
                                       text=XOscr[b],
                                       bg = '#262626', fg = 'white')
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                        return
                   for c in range(3):
                    if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvpCanvas,
                                       text=XOscr[b], 
                                       bg = '#262626', fg = 'white')
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                        return
                   if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvpCanvas,
                                       text=XOscr[b],
                                       bg = '#262626', fg = 'white')
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                        return
                   if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        XOscr[b] = XOscr[b] + 1
            
                        Score = Label(pvpCanvas,
                                       text=XOscr[b],
                                       bg = '#262626', fg = 'white')
                        Score.grid(row=5, column=XOcol[b])
                        
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                        return
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
                        """
                        This function places either an x or an o on the button that is clicked in the game board
                        and then scans for a winner
                        Parameters
                        ----------
                        r2=r: integer, the row that the button is in
                        c2=c: integer, the colunm the button is in
                        Returns
                        -------
                        None
                        """
                        global x
                        g[r2][c2] = x
                        if x == 'X':
                            bh = Label(pvpCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                            bu = Label(pvpCanvas, #sets the label for X
                                    image = xPic,
                                    bd = 0,)
                        if x == 'O':
                            bh = Label(pvpCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                            bu = Label(pvpCanvas, #sets the label for O
                                    image = oPic,
                                    bd = 0)
                        bh.grid(row = r2, column = c2)
                        bu.grid(row=r2, column=c2)#places both labels on clicked button
                        if x == 'X':
                            x = "O"
                        else:
                            x = 'X'
                        winner()
                        
                    bu = Button(pvpCanvas,
                                text = '',
                                bd = 0,
                                image = boardBox,
                                command = move,
                                bg = '#262626', 
                                activebackground= '#262626'
                                )
                    bu.grid(row=r, column=c)

        pvp = Toplevel()
        pvp.title('PvP')
        pvp.attributes("-topmost", True)
        pvpCanvas = Canvas(pvp, highlightthickness=0, bg = '#262626')
        pvpCanvas.pack()
        TTTBRD()
        # X and O icon
        X = Label(pvpCanvas,
                  text=player1Name,
                  bg = '#262626',
                  fg = 'white')
        X.grid(row=4, column=0)

        O = Label(pvpCanvas,
                  text=player2Name,
                  bg = '#262626',
                  fg = 'white')
        O.grid(row=4, column=2)
        # Restart button
        R = Button(pvpCanvas,
                   text='↺ ',
                   command=TTTBRD,
                   bg = '#262626',
                   fg = 'white'
                   )
        R.grid(row=4, column=1)
        #Displays X and O's initial score
        player1Score = Label(pvpCanvas,
                       text=0,
                       bg = '#262626',
                       fg = 'white')
        player1Score.grid(row=5, column=0)

        player2Score = Label(pvpCanvas,
                       text=0,
                       bg = '#262626',
                       fg = 'white')
        player2Score.grid(row=5, column=2)

        pvp.mainloop()
def startEasyGame():
        """
        This function allows for a one player game on easy to be played. It creates the game board, checks for a winner, displays a
        winning/draw message and has a restart button
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        # CPU start variable
        global cpu
        
        # Sets initial move
        global S
        global player1Wins
        global player2Wins
        player1Wins = 0
        player2Wins = 0
        global x
        x = S  
        # Sets and hold score
        
        def switch():
            """
            This switches if it is the players turn or the computers to create a new game
            Parameters
            ----------
            None
            Returns
            -------
            None
            """
            global x
            if x == 'X':
                x = "O"
            else:
                x = 'X'    
        # Creates a new game      
        def TTTBRD():
            """
            This function sets the game board back to its deafult empty state and determines which icon is assigned to each player
            Parameters
            ----------
            None
            Returns 
            -------
            None
            """   
            #sets which player is which icon
            if cpu == 1 and S == 'X' or cpu == 0 and S == 'O':
                cpuXO = 'X'
                playerXO = 'O'
            else:
                cpuXO = 'O'
                playerXO = 'X'
            #Sets board/memory bank
            g = [['','',''],
                 ['','',''],
                 ['','','']]                
            #Scans for a winner every move made, updates score and anounces a winner 
            # or stalemate while displaying the current board 
            def winner():
               """
               This function determines whether someone has won the game. After each turn the board is scanned for
               a winner and the score is upodated accordingly
               Parameters
               ----------
               None
               Returns
               -------
               None
               """
               XO = ['X','O']
               XOmsg = ['X Wins!', 'O Wins!']
               global player1Wins
               global player2Wins
               for b in range(2):
                   for r in range(3):
                    if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   for c in range(3):
                    if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
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
                """
                This function determines if the computer is playing first and if it is, completes a move
                Parameters
                ----------
                None
                Returns
                -------
                None
                """
                if cpu == 1 and S == 'X':
                    g[0][0] = cpuXO
                    bh = Label(easyCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                    bh.grid(row = 0, column = 0)
                    bu = Label(easyCanvas, 
                               image = xPic,
                               bd = 0,
                               bg = '#262626', 
                               activebackground= '#262626'
                               )
                    bu.grid(row=0, column=0)
                if cpu == 1 and S == 'O':
                    g[0][0] = cpuXO
                    bh = Label(easyCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                    bh.grid(row = 0, column = 0)
                    bu = Label(easyCanvas, 
                               image = oPic,
                               bd = 0,
                               bg = '#262626', 
                               activebackground= '#262626'
                               )
                    bu.grid(row=0, column=0)
                switch()
            
            def winCheck():
                """
                This function checks to see if there is a winner and makes the varible won global
                Parameters 
                ----------
                None
                Returns
                -------
                None
                """
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
            
            def easymode():
                """
                This function is the logic behind the easy mode computers moves, every turn the function wincheck is called
                and if there is no winer the computer makes a move using the instructions in the function
                
                Parameters
                ----------
                None
                Returns
                -------
                None
                """
                global x
                winCheck()
                x = cpuXO
                if won != 1:
                    for r in range(3):
                        for c in range(3):
                            if g[r][c] == '':
                                g[r][c] = x
                                if S == 'O' and cpu == 1 or S == 'X' and cpu == 0:
                                    bh = Label(easyCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                                    bh.grid(row = r, column = c)
                                    bu = Label(easyCanvas, #label for the O
                                            image = oPic,
                                            bd = 0,
                                            activebackground= '#262626')
                                if S == 'X' and cpu == 1 or S == 'O' and cpu == 0:
                                    bh = Label(easyCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                                    bh.grid(row = r, column = c)
                                    bu = Label(easyCanvas, #label for the X
                                            image = xPic,
                                            bd = 0, 
                                            activebackground= '#262626')                     
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
                        if S == 'O' and cpu == 0 or S == 'X' and cpu == 1:
                            bh = Label(easyCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                            bu = Label(easyCanvas, 
                                    image = oPic,
                                    bd = 0)
                        if S == 'X' and cpu == 0 or S == 'O' and cpu == 1:
                            bh = Label(easyCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                            bu = Label(easyCanvas, 
                                    image = xPic,
                                    bd = 0)
                        bh.grid(row = r2, column = c2)
                        bu.grid(row=r2, column=c2)
                        switch()
                        winner()
                        easymode()
                        
                    bu = Button(easyCanvas, 
                                image = boardBox,
                                bd = 0,
                                command = move,                                
                                bg = '#262626', 
                                activebackground= '#262626'
                                )
                    bu.grid(row=r, column=c)
            FReasy()
        #creates a window and starts a board
        easy = Toplevel()
        easy.title('Easy')
        easy.attributes("-topmost", True)
        easyCanvas = Canvas(easy, highlightthickness=0, bg = '#262626')
        easyCanvas.pack()
        TTTBRD()

        # X and O iconfor score indicators
        X = Label(easyCanvas,
                  text=player1Name,
                  bg = '#262626',
                  fg = 'white')
        X.grid(row=4, column=0)

        O = Label(easyCanvas,
                  text=player2Name,
                  bg = '#262626',
                  fg = 'white')
        O.grid(row=4, column=2)
        # Restart button
        def restart():
            """
            This function resests the game board and allows for a new game to begin
            Parameters
            ----------
            None
            Returns
            -------
            None
            """
            TTTBRD()
            switch()     
        R = Button(easyCanvas,
                   text='↺ ',
                   command=restart,
                   bg = '#262626',
                   fg = 'white'
                   )
        R.grid(row=4, column=1)
        #Displays X and O's initial score
        global player1Score
        player1Score = Label(easyCanvas,
                       text=0,
                       bg = '#262626',
                       fg = 'white')
        player1Score.grid(row=5, column=0)
        global player2Score
        player2Score = Label(easyCanvas,
                       text=0,
                       bg = '#262626',
                       fg = 'white')
        player2Score.grid(row=5, column=2)

        easy.mainloop()

def startMedGame():
        """
        This function allows for a one player game on medium to be played. It creates the game board, checks for a winner, displays a
        winning/draw message and has a restart button
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        # CPU start variable
        global cpu
 
        # Sets initial move
        global S
        global player1Wins
        global player2Wins
        player1Wins = 0
        player2Wins = 0
        global x
        x = S  
        
        def switch():
            """
            This switches if it is the players turn or the computers to create a new game
            Parameters
            ----------
            None
            Returns
            -------
            None
            """
            global x
            if x == 'X':
                x = "O"
            else:
                x = 'X'  
                
        def TTTBRD():
            """
            This function sets the game board back to its deafult empty state and determines which icon is assigned to each player
            Parameters
            ----------
            None
            Returns 
            -------
            None
            """
            #sets which player is which icon
            if cpu == 1 and S == 'X' or cpu == 0 and S == 'O':
                cpuXO = 'X'
                playerXO = 'O'
            else:
                cpuXO = 'O'
                playerXO = 'X'
            #Sets board/memory bank
            g = [['','',''],
                 ['','',''],
                 ['','','']]   
               
            #Scans for a winner every move made, updates score and anounces a winner 
            # or stalemate while displaying the current board 
            def winner():
               """
               This function determines whether someone has one the game. After each turn the board is scanned for
               a winner and the score is upodated accordingly
               Parameters
               ----------
               None
               Returns
               -------
               None
               """
               XO = ['X','O']
               XOmsg = ['X Wins!', 'O Wins!']
               global player1Wins
               global player2Wins
               for b in range(2):
                   for r in range(3):
                    if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   for c in range(3):
                    if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                   if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
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
                       
            def FRmed():
                """
                This function determines if the computer is playing first and if it is, completes a move
                Parameters
                ----------
                None
                Returns
                -------
                None
                """
                if cpu == 1 and S == 'X':
                    g[1][1] = cpuXO
                    bh = Label(medCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                    bh.grid(row = 1, column = 1)
                    bu = Label(medCanvas, 
                               image = xPic,
                               bg = '#424242')
                    bu.grid(row=1, column=1)
                if cpu == 1 and S == 'O':
                    g[1][1] = cpuXO
                    bh = Label(medCanvas, image = boardBox, bd = 0, bg = '#262626') # places a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                    bh.grid(row = 1, column = 1)
                    bu = Label(medCanvas, 
                               image = oPic,
                               bg = '#424242')
                    bu.grid(row=1, column=1)   
                switch()
            
            def winCheck():
                """
                This function checks to see if there is a winner and makes the varible won global
                Parameters 
                ----------
                None
                Returns
                -------
                None
                """
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
            
            def medmode():
                """
                This function is the logic behind the medium mode computers moves, every turn the function wincheck is called
                and if there is no winner the computer makes a move using the instructions in the function
                
                Parameters
                ----------
                None
                Returns
                -------
                None
                """
                global x
                winCheck()
                x = cpuXO
                if won != 1:
                    if S == 'O' and cpu == 0 or S == 'X' and cpu == 1:
                        bh = Label(medCanvas, image = boardBox, bd = 0, bg = '#262626') # sets a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                        bu = Label(medCanvas, image = xPic, bg = '#424242') # sets the X label
                        if g[1][1] == '':
                            g[1][1] = x
                            bh.grid(row=1, column=1)
                            bu.grid(row=1, column=1)
                        elif g[0][0] == '':
                            g[0][0] = x
                            bh.grid(row=0, column=0)
                            bu.grid(row=0, column=0)
                        elif g[2][2] == '':
                            g[2][2] = x
                            bh.grid(row=2, column=2)
                            bu.grid(row=2, column=2)
                        elif g[0][2] == '':
                            g[0][2] = x
                            bh.grid(row=0, column=2)
                            bu.grid(row=0, column=2)
                        elif g[0][1] == '':
                            g[0][1] = x
                            bh.grid(row=0, column=1)
                            bu.grid(row=0, column=1)
                        elif g[1][2] == '':
                            g[1][2] = x
                            bh.grid(row=1, column=2)
                            bu.grid(row=1, column=2)
                        elif g[2][0] == '':
                            g[2][0] = x
                            bh.grid(row=2, column=0)
                            bu.grid(row=2, column=0)
                        elif g[1][0] == '':
                            g[1][0] = x
                            bu.grid(row=1, column=0)
                            bu.grid(row=1, column=0)
                        elif g[2][1] == '':
                            g[2][1] = x
                            bu.grid(row=2, column=1)
                            bu.grid(row=2, column=1)
                    if S == 'X' and cpu == 0 or S == 'O' and cpu == 1:
                        bh = Label(medCanvas, image = boardBox, bd = 0, bg = '#262626') # sets a copy of the boardBox to prevent clicking the same button and placing a symbol over another
                        bu = Label(medCanvas, image = oPic, bg = '#424242')
                        if g[1][1] == '':
                            g[1][1] = x 
                            bh.grid(row=1, column=1)
                            bu.grid(row=1, column=1)
                        elif g[0][0] == '':
                            g[0][0] = x
                            bh.grid(row=0, column=0)
                            bu.grid(row=0, column=0)
                        elif g[2][2] == '':
                            g[2][2] = x
                            bh.grid(row=2, column=2)
                            bu.grid(row=2, column=2)
                        elif g[0][2] == '':
                            g[0][2] = x
                            bh.grid(row=0, column=2)
                            bu.grid(row=0, column=2)
                        elif g[0][1] == '':
                            g[0][1] = x
                            bh.grid(row=0, column=1)
                            bu.grid(row=0, column=1)
                        elif g[1][2] == '':
                            g[1][2] = x
                            bh.grid(row=1, column=2)
                            bu.grid(row=1, column=2)
                        elif g[2][0] == '':
                            g[2][0] = x
                            bh.grid(row=2, column=0)
                            bu.grid(row=2, column=0)
                        elif g[1][0] == '':
                            g[1][0] = x
                            bh.grid(row=1, column=0)
                            bu.grid(row=1, column=0)
                        elif g[2][1] == '':
                            g[2][1] = x
                            bh.grid(row=2, column=1)
                            bu.grid(row=2, column=1)
                        winner()


        # Every button updates the mark on the board, scans for a winner, and starts cpu's turn
            for r in range(3):
                for c in range(3):
                    def move(r2=r,c2=c):
                        global x
                        x = playerXO
                        g[r2][c2] = x                       
                        if S == 'X' and cpu == 0 or S == 'O' and cpu == 1:
                            bh = Label(medCanvas, image = boardBox, bd = 0, bg = '#262626') 
                            bu = Label(medCanvas, image = xPic, bg = '#424242')
                        if S == 'X' and cpu == 1 or S == 'O' and cpu == 0:
                            bh = Label(medCanvas, image = boardBox, bd = 0, bg = '#262626') 
                            bu = Label(medCanvas, image = oPic, bg = '#424242')
                        bh.grid(row=r2, column=c2)
                        bu.grid(row=r2, column=c2)
                        switch()
                        winner()
                        medmode()
                        
                    bu = Button(medCanvas, 
                                image = boardBox,
                                bd = 0,
                                command = move,
                                activebackground= '#262626',
                                bg = '#262626'
                                )
                    bu.grid(row=r, column=c)
            FRmed()
        #creates a window and starts a board
        med = Toplevel()
        med.title('Medium')
        med.attributes("-topmost", True)
        medCanvas = Canvas(med, highlightthickness=0, bg = '#262626' )
        medCanvas.pack()
        TTTBRD()

        # X and O iconfor score indicators
        X = Label(medCanvas,
                  text=player1Name, bg = '#262626', fg = 'white')
        X.grid(row=4, column=0)

        O = Label(medCanvas,
                  text=player2Name, bg = '#262626', fg = 'white')
        O.grid(row=4, column=2)
         
        def restart():
            """
            This function resests the game board and allows for a new game to begin
            Parameters
            ----------
            None
            Returns
            -------
            None
            """
            TTTBRD()
            switch()    
        R = Button(medCanvas,
                   text='↺ ',
                   command=restart, bg = '#242424', fg = 'white'
                   )
        R.grid(row=4, column=1)
        #Displays X and O's initial score
        player1Score = Label(medCanvas,
                       text=0, bg = '#242424', fg = 'white')
        player1Score.grid(row=5, column=0)

        player2Score = Label(medCanvas,
                       text=0, bg = '#242424', fg = 'white')
        player2Score.grid(row=5, column=2)

        med.mainloop()

def startHardGame():
    """
    This function allows for a one player game on hard to be played. It creates the game board, checks for a winner, displays a
    winning/draw message and has a restart button
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
    # CPU start variable
    global cpu
    # Sets initial move   
    global S
    global player1Wins
    global player2Wins
    player1Wins = 0
    player2Wins = 0
    global x
    x = S  
    # Sets and hold score
    global XOscr
    XOscr = [0,0]
    
    def switch():
        """
        This switches if it is the players turn or the computers to create a new game
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        global x
        if x == 'X':
            x = "O"
        else:
            x = 'X'
            
    def TTTBRD():
        """
        This function sets the game board back to its deafult empty state and determines which icon is assigned to each player
        Parameters
        ----------
        None
        Returns 
        -------
        None
        """
        #sets which player is which icon
        if cpu == 1 and S == 'X' or cpu == 0 and S == 'O':
            cpuXO = 'X'
            playerXO = 'O'
        else:
            cpuXO = 'O'
            playerXO = 'X'
        #Sets board/memory bank
        g = [['','',''],
             ['','',''],
             ['','','']]   
           
        #Scans for a winner every move made, updates score and anounces a winner 
        # or stalemate while displaying the current board 
        def winner():
            """
            This function determines whether someone has one the game. After each turn the board is scanned for
            a winner and the score is upodated accordingly
            Parameters
            ----------
            None
            Returns
            -------
            None
            """
            XO = ['X','O']
            XOmsg = ['X Wins!', 'O Wins!']
            global player1Wins
            global player2Wins
            for b in range(2):
                for r in range(3):
                    if g[r][0] == XO[b] and g[r][1] == XO[b] and g[r][2] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X': 
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                for c in range(3):
                    if g[0][c] == XO[b] and g[1][c] == XO[b] and g[2][c] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                if g[0][0] == XO[b] and g[1][1] == XO[b] and g[2][2] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
                        showinfo(message=XOmsg[b])
                        TTTBRD()
                if g[0][2] == XO[b] and g[1][1] == XO[b] and g[2][0] == XO[b]:
                        if cpu == 1 and S == 'O' or cpu == 0 and S == 'X':
                            if XO[b] == 'X':
                                player1Wins +=1
                                player1Score.configure(text = player1Wins)
                            if XO[b] == 'O':
                                player2Wins +=1
                                player2Score.configure(text = player2Wins)
                        if cpu == 0 and S == 'O' or cpu == 1 and S == 'X':
                            if XO[b] == 'X':
                                player2Wins += 1
                                player2Score.configure(text = player2Wins)
                            if XO[b] == 'O':
                                player1Wins += 1
                                player1Score.configure(text = player1Wins)
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
                  
        def FRhard():
            """
            This function determines if the computer is playing first and if it is, completes a move
            Parameters
            ----------
            None
            Returns
            -------
            None
            """
            if cpu == 1 and S == 'X':
                g[0][0] = cpuXO
                bh = Label(hardCanvas, image = boardBox, bd = 0, bg = '#262626') # sets the box label to prevent clicking same one multiple times
                bu = Label(hardCanvas, image = xPic, bg = '#424242') # sets the label to X
            if cpu == 1 and S == 'O':
                g[0][0] = cpuXO
                bh = Label(hardCanvas, image = boardBox, bd = 0, bg = '#262626')
                bu = Label(hardCanvas, image = oPic, bg = '#424242')
            bh.grid(row=0, column=0) #places both labels in the first spot
            bu.grid(row=0, column=0)
            switch()
        
        def winCheck():
            """
            This function checks to see if there is a winner and makes the varible won global
            Parameters 
            ----------
            None
            Returns
            -------
            None
            """
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
        
        def hardmode():
            """
            This function is the logic behind the hard mode computers moves, every turn the function wincheck is called
            and if there is no winner the computer makes a move using the instructions in the function
            Parameters
            ----------
            None
            Returns
            -------
            None
            """
            global x
            winCheck()
            x = cpuXO
            if won != 1:
                if S == 'X' and cpu == 1 or S == 'O' and cpu == 0:
                    bh = Label(hardCanvas, image = boardBox, bd = 0, bg = '#262626') 
                    bu = Label(hardCanvas, image = xPic, bg = '#424242')
                if S == 'O' and cpu == 1 or S == 'X' and cpu == 0:
                    bh = Label(hardCanvas, image = boardBox, bd = 0, bg = '#262626') 
                    bu = Label(hardCanvas, image = oPic, bg = '#424242')
                    #check for possible win, if so, place to block
                if g[0][0] == x and g[0][1] == x and g[0][2] == '':
                    g[0][2] = x
                    bh.grid(row=0, column=2)
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == x and g[0][1] == x and g[0][0] == '':
                    g[0][0] = x
                    bh.grid(row=0, column=0)
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == x and g[0][2] == x and g[0][1] == '':
                    g[0][1] = x
                    bh.grid(row=0, column=1)
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[1][0] == x and g[1][1] == x and g[1][2] == '':
                    g[1][2] = x
                    bh.grid(row=1, column=2)
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[1][2] == x and g[1][1] == x and g[1][0] == '':
                    g[1][0] = x
                    bh.grid(row=1, column=0)
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[1][0] == x and g[1][2] == x and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[2][0] == x and g[2][1] == x and g[2][2] == '':
                    g[2][2] = x
                    bh.grid(row=2, column=2)
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == x and g[2][1] == x and g[2][0] == '':
                    g[2][0] = x
                    bh.grid(row=2, column=0)
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == x and g[2][2] == x and g[2][1] == '':
                    g[2][1] = x
                    bh.grid(row=2, column=1)
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[0][0] == x and g[1][0] == x and g[2][0] == '':
                    g[2][0] = x
                    bh.grid(row=2, column=0)
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == x and g[1][0] == x and g[0][0] == '':
                    g[0][0] = x
                    bh.grid(row=0, column=0)
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == x and g[2][0] == x and g[1][0] == '':
                    g[1][0] = x
                    bh.grid(row=1, column=0)
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[0][0] == x and g[2][2] == x and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[0][1] == x and g[1][1] == x and g[2][1] == '':
                    g[2][1] = x
                    bh.grid(row=2, column=1)
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[1][2] == x and g[1][1] == x and g[0][1] == '':
                    g[0][1] = x
                    bh.grid(row=0, column=1)
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[0][1] == x and g[2][1] == x and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[0][2] == x and g[1][2] == x and g[2][2] == '':
                    g[2][2] = x
                    bh.grid(row=2, column=2)
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == x and g[1][2] == x and g[0][2] == '':
                    g[0][2] = x
                    bh.grid(row=0, column=2)
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[2][2] == x and g[0][2] == x and g[1][2] == '':
                    g[1][2] = x
                    bh.grid(row=1, column=2)
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[0][0] == x and g[2][2] == x and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == x and g[2][2] == x and g[0][0] == '':
                    g[0][0] = x
                    bh.grid(row=0, column=0)
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == x and g[1][1] == x and g[2][2] == '':
                    g[2][2] = x
                    bh.grid(row=2, column=2)
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[0][2] == x and g[2][0] == x and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == x and g[2][0] == x and g[0][2] == '':
                    g[0][2] = x
                    bh.grid(row=0, column=2)
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == x and g[1][1] == x and g[2][0] == '':
                    g[2][0] = x
                    bh.grid(row=2, column=0)
                    bu.grid(row=2, column=0)
                    winner()
                    return
                #Checks for a block move 
                if g[0][0] == playerXO and g[0][1] == playerXO and g[0][2] == '':
                    g[0][2] = x
                    bh.grid(row=0, column=2)
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == playerXO and g[0][1] == playerXO and g[0][0] == '':
                    g[0][0] = x
                    bh.grid(row=0, column=0)
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == playerXO and g[0][2] == playerXO and g[0][1] == '':
                    g[0][1] = x
                    bh.grid(row=0, column=1)
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[1][0] == playerXO and g[1][1] == playerXO and g[1][2] == '':
                    g[1][2] = x
                    bh.grid(row=1, column=2)
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[1][2] == playerXO and g[1][1] == playerXO and g[1][0] == '':
                    g[1][0] = x
                    bh.grid(row=1, column=0)
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[1][0] == playerXO and g[1][2] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[2][0] == playerXO and g[2][1] == playerXO and g[2][2] == '':
                    g[2][2] = x
                    bh.grid(row=2, column=2)
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == playerXO and g[2][1] == playerXO and g[2][1] == '':
                    g[2][0] = x
                    bh.grid(row=2, column=0)
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == playerXO and g[2][2] == playerXO and g[2][1] == '':
                    g[2][1] = x
                    bh.grid(row=2, column=1)
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[0][0] == playerXO and g[1][0] == playerXO and g[2][0] == '':
                    g[2][0] = x
                    bh.grid(row=2, column=0)
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[2][0] == playerXO and g[1][0] == playerXO and g[0][0] == '':
                    g[0][0] = x
                    bh.grid(row=0, column=0)
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == playerXO and g[2][0] == playerXO and g[1][0] == '':
                    g[1][0] = x
                    bh.grid(row=1, column=0)
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[0][1] == playerXO and g[1][1] == playerXO and g[2][1] == '':
                    g[2][1] = x
                    bh.grid(row=2, column=1)
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[2][1] == playerXO and g[1][1] == playerXO and g[0][1] == '':
                    g[0][1] = x
                    bh.grid(row=0, column=1)
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[0][1] == playerXO and g[2][1] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[0][2] == playerXO and g[1][2] == playerXO and g[2][2] == '':
                    g[2][2] = x
                    bh.grid(row=2, column=2)
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[2][2] == playerXO and g[1][2] == playerXO and g[0][2] == '':
                    g[0][2] = x
                    bh.grid(row=0, column=2)
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[2][2] == playerXO and g[0][2] == playerXO and g[1][2] == '':
                    g[1][2] = x
                    bh.grid(row=1, column=2)
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[0][0] == playerXO and g[2][2] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == playerXO and g[2][2] == playerXO and g[0][0] == '':
                    g[0][0] = x
                    bh.grid(row=0, column=0)
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[0][0] == playerXO and g[1][1] == playerXO and g[2][2] == '':
                    g[2][2] = x
                    bh.grid(row=2, column=2)
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[0][2] == playerXO and g[2][0] == playerXO and g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
                    bu.grid(row=1, column=1)
                    winner()
                    return
                if g[1][1] == playerXO and g[2][0] == playerXO and g[0][2] == '':
                    g[0][2] = x
                    bh.grid(row=0, column=2)
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[0][2] == playerXO and g[1][1] == playerXO and g[2][0] == '':
                    g[2][0] = x
                    bh.grid(row=2, column=0)
                    bu.grid(row=2, column=0)
                    winner()
                    return
                #Move order 
                if g[0][0] == '' and g[2][2] == '':
                    g[0][0] = x
                    bh.grid(row=0, column=0)
                    bu.grid(row=0, column=0)
                    winner()
                    return
                if g[2][2] == '' and g[0][0] == x:
                    g[2][2] = x
                    bh.grid(row=2, column=2)
                    bu.grid(row=2, column=2)
                    winner()
                    return
                if g[0][2] == '':
                    g[0][2] = x
                    bh.grid(row=0, column=2)
                    bu.grid(row=0, column=2)
                    winner()
                    return
                if g[2][0] == '':
                    g[2][0] = x
                    bh.grid(row=2, column=0)
                    bu.grid(row=2, column=0)
                    winner()
                    return
                if g[0][1] == '':
                    g[0][1] = x
                    bh.grid(row=0, column=1)
                    bu.grid(row=0, column=1)
                    winner()
                    return
                if g[1][2] == '':
                    g[1][2] = x
                    bh.grid(row=1, column=2)
                    bu.grid(row=1, column=2)
                    winner()
                    return
                if g[1][0] == '':
                    g[1][0] = x
                    bh.grid(row=1, column=0)
                    bu.grid(row=1, column=0)
                    winner()
                    return
                if g[2][1] == '':
                    g[2][1] = x
                    bh.grid(row=2, column=1)
                    bu.grid(row=2, column=1)
                    winner()
                    return
                if g[1][1] == '':
                    g[1][1] = x
                    bh.grid(row=1, column=1)
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
                    if S == 'X' and cpu == 0 or S == 'O' and cpu == 1:
                        bh = Label(hardCanvas, image = boardBox, bd = 0, bg = '#262626') # sets the box label to prevent clicking same one multiple times
                        bu = Label(hardCanvas, image = xPic, bd = 0) # sets the label to X
                    if S == 'O' and cpu == 0 or S == 'X' and cpu == 1:
                        bh = Label(hardCanvas, image = boardBox, bd = 0, bg = '#262626')
                        bu = Label(hardCanvas, image = oPic, bd = 0) # sets the label to O
                    bh.grid(row=r2, column=c2)# places both labels on clicked button
                    bu.grid(row=r2, column=c2)
                    switch()
                    winner()
                    hardmode()
                    
                bu = Button(hardCanvas, image = boardBox, command = move, bd = 0, bg = '#262626', activebackground='#262626')
                bu.grid(row=r, column=c)
        FRhard()
    #creates a window and starts a board
    hard = Toplevel()
    hard.title('Hard')
    hard.attributes("-topmost", True)
    hardCanvas = Canvas(hard, bg = '#262626', bd = 0, highlightthickness=0)
    hardCanvas.pack()
    TTTBRD()

    # X and O iconfor score indicators
    X = Label(hardCanvas, text=player1Name, bg = '#262626', fg ='white')
    X.grid(row=4, column=0)

    O = Label(hardCanvas, text=player2Name, bg = '#262626', fg = 'white')
    O.grid(row=4, column=2)
    
    def restart():
        """
        This function resests the game board and allows for a new game to begin
        Parameters
        ----------
        None
        Returns
        -------
        None
        """
        TTTBRD()
        switch()    
    R = Button(hardCanvas,text='↺ ', command=restart, bg = '#262626', fg = 'white')
    R.grid(row=4, column=1)
    #Displays X and O's initial score
    player1Score = Label(hardCanvas, text=0, bg = '#262626', fg = 'white')
    player1Score.grid(row=5, column=0)

    player2Score = Label(hardCanvas, text=0, bg = '#262626', fg = 'white')
    player2Score.grid(row=5, column=2)

    hard.mainloop()


def startGame():
    """
    This function starts the game and determines what type of game it is based on which buttons are selected
    Parameters
    ----------
    None
    Returns
    -------
    None
    """
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
boardBox = PhotoImage(file='boardbox.png')
boardBackground = PhotoImage(file='boardbackground.png')

#sets the background widget on the canvas
backgroundImage = Label(menuCanvas, image=backgroundPic, bd=0)
backgroundImage.place(x=0,y=0)


#sets the widgets for icon selection (X or O)
playerOneCharFrame = Frame(menuCanvas,
                    height = 200, width = 200, bg='#424242')
playerOneCharFrame.pack()
playerOneCharFrame.place(x = 45, y = 210)
playerOneCharValue = StringVar()
playerOneCharValue.set('X')

playerOneCharR1 =Radiobutton(playerOneCharFrame, image = xPic,
                             variable = playerOneCharValue,
                             value = 'X', bg = '#424242', activebackground= '#424242')
playerOneCharR2 =Radiobutton(playerOneCharFrame, image = oPic,
                             variable = playerOneCharValue,
                             value = 'O', bg = '#424242', activebackground= '#424242')
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
                             value = 1, command=playerTwoX, bg = '#424242', activebackground= '#424242')
playerTwoCharR2 =Radiobutton(playerTwoCharFrame, image = playerStartsPic,
                             variable = playerTwoCharValue,
                             value = 0, command = playerTwoO, bg = '#424242', activebackground= '#424242')
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
                         command = onePlayerGame, bg = '#424242', activebackground= '#424242')
gameModeR2 = Radiobutton(gameModeFrame, image = twoPlayerBox,
                         variable = gameModeValue, value = 'Two Player',
                         command = twoPlayerGame, bg = '#424242', activebackground= '#424242')
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
                         value = 'Easy', bg = '#424242', activebackground= '#424242')
difficultyR2=Radiobutton(difficultyFrame, image = mediumBox,
                         variable = difficultyValue,
                         value = 'Medium', bg = '#424242', activebackground= '#424242')
difficultyR3=Radiobutton(difficultyFrame, image = hardBox,
                         variable = difficultyValue,
                         value = 'Hard', bg = '#424242', activebackground= '#424242')
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