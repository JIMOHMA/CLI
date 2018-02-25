## The tic-tac-toe game
## The X-player and the O-player


## Introduction of what the tic tac toe game is all about.
##A tic-tac-toe board is 3x3, hence our board needs to store 9 pieces of information,
## which are the inputof X's and O's. 
##A general overview of the board with its coordinate system is shown below;
##    1,1 | 2,1 | 3,1
##    ---------------
##    1,2 | 2,2 | 3,2
##    ---------------
##    1,3 | 2,3 | 3,3
##This game requires two players to play it.
## Of course there could be another version where a player plays against the
## computer, but for simplicity, we're going to stick with 2 human players.
## Since there are only 8 ways for a player to win we could define them explicitly in our
## program. The possible combinations are; i)the diagonals (1,1)(2,2)(3,3), (1,3)(2,2)(3,1)
## ii) the columns (1,1)(1,2)(1,3), (2,1)(2,2)(2,3), (3,1)(3,2)(3,3) and
## iii) the rows  (1,1)(2,1)(3,1), (1,2)(2,2)(3,2), (1,3)(2,3)(3,3)
## A player wins by getting "three in a row" and the game is over when this happens.
import random

def main():
    num_players = int(input("Enter the number players? ")) ##prompting user for number of players
    grid = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]  ## a list representation of what the board
                                                        ## will look like before the game starts.
    ## This method is used for getting the status of cells/position on the board
    def get_state(grid, row, col): 
        spot = grid[col-1][row-1] # We use col-1 & row-1 because python goes through a list
                                  # from 0. so if col& row was 2, we would get grid[1][1]
                                  # which would be the center position on the board
        if spot == 'X': 
            return 'X'
        if spot == 'O':
            return 'O'
        return ' '

    ## This method is used to set 'X' or 'O' in the correct cell(row,col)
    def set_state(grid, row, col, player):
        if player == 'X':
            spot = 'X'
        else:
            spot = 'O'
        grid[col-1][row-1] = spot

    def print_board(grid):  ## This method is responsible for displaying the board
        print_row(grid, 1)  ## first row of the board
        print('-----')
        print_row(grid, 2)  ## second row of the board
        print('-----')
        print_row(grid, 3)  ## third row of th board
        return ' '##makes sure method doesn't return any unneccessary None on the command line

        
    def print_row(grid, row): ##this is for making the rows of the matrix
        output = get_state(grid, row, 1)
        output += '|' + get_state(grid, row, 2)
        output += '|' + get_state(grid, row, 3)
        print(output)

    def winning_cond(grid): ##for checking all the possible eight possible winning situations
        ## Since the diagonals can only produce a win in just two ways,
        ## this block of if statements checks the two diagonals to see if any player has
        ## three symbols in a diagonal
        if grid[1][1] != ' ': ##this checks to see if the centre element of the board is not empty
            if grid[0][0] == grid[1][1]: ##checks to see if element in position (0,0) is same as center element
                if grid[0][0] == grid[1][1]: ## checks to see if element in position (2,2) is same as center element
                    return True
            ## checking the second diagonal
            if grid[2][0] == grid[1][1]:## checks to see if element in position (2,0) is same as center element
                if grid[0][2] == grid[1][1]: ##checks to see if element in position (0,2) is same as center element
                    return True

        ## This for loop is for checking the rows and columns to see if they have matching
        ## elements that gaurantees a win
        for i in range(0,3):  ## loop runs just three times producing i = 0,1,2
            
            ## this basically checks the entire columns to see if the elements in each column are the same
            if grid[0][i] != ' ': ## When i = 0, this checks to see if the 1st element at position (0,0) of the matrix contains no input 
                if grid[0][i] == grid[1][i]: ## When i = 0, this checks to see if the 1st element at position (1,0) is same as that in position (0,0)
                    if grid[0][i] == grid[2][i]: ## When i = 0, this checks to see if the 2nd element at position (2,0) is same as that in position (0,0)
                        return True
                    
            ## this basically checks the entire row to see if the elements in each row are the same
            if grid[i][0] != ' ': ## just like the case of the column, when i = 0 this basically checks the 1st row of the matrix [i.e (0,0),(0,1),(0,2)] to see if they are the same.
                                 ## As the loop runs through i = 1 through 2, the 2nd and 3rd rows are also checked respectively. 
                if grid[i][0] == grid[i][1]:  
                    if grid[i][0] == grid[i][2]:
                        return True
        return False ## In the case where none of the rows, columns or diagonals have no same entry,
                     ## the 'return False' takes care of the situation where there is no winner
    
    comp_player = 'O'
    def comp_move(grid):
        col = random.randint(1,3)
        row = random.randint(1,3)
        return col,row
    
    def one_user():
        Ongoing = True  ## used for running a continuous loop
        current_player = 'X' ## first player is set to X by default
        player1 = current_player
        spaces = 9    ## available number of cells before game starts
        while Ongoing:
            print_board(grid)  ## prints the state of the board before a player plays either X or O
            print(player1 + "'s turn") ## Tells user who's turn to play
            if player1 == current_player:
                coordinate = eval(input("Enter coordinate for a cell in the form (col,row)! "))
                col = coordinate[0]
                row = coordinate[1]
            elif player1 == comp_player:
                coordinate = comp_move(grid)
                col = coordinate[0]
                row = coordinate[1]
                
            current = get_state(grid, row, col) ## this gets the element in the cell which is provided by the user

            if current != ' ': ## this checks to see if the cell provided has an entry in it
                print("That cell/position is taken! or That coordinate is not on the board")
            else:  ## since the if statement fails, this else block set the corresponding 'X' or 'O'
                    ## entry in the cell
                set_state(grid,row,col, player1) ## sets the either 'X' or 'O' to the cell on the board
                spaces -= 1 ## reduces the number of available cells by 1 each time a cell is occupied 

                if winning_cond(grid): ## if this if statement is false, means we don't have a winner(a tie)
                                       ## or the game is still in progress and there is yet to be a winner
                    print(print_board(grid))  ## if a winner eventually emerge, this prints out the final
                                          ## status of the board. 
                    print(player1 + " wins")
                    Ongoing = False  ## this ends the while loop when a winner emerges

                else:  ## if there isn't a winner or the game isn't tied yet, the next player is updated
                       ## to either 'X' or 'O' depending on who the last player was
                    if player1 == 'X': 
                        player1 = comp_player

                    else:
                        player1 = current_player

                if spaces == 0:
                    print(print_board(grid))
                    print("Game is a tie!")
                    Ongoing = False

    def zero_user():
        Ongoing = True  ## used for running a continuous loop
        comp_player1 = 'X' ## first player is set to X by default
        comp_player2 = 'O'
        player1 = comp_player1
        spaces = 9    ## available number of cells before game starts
        while Ongoing:
            print_board(grid)  ## prints the state of the board before a player plays either X or O
            print(player1 + "'s turn") ## Tells user who's turn to play
            if player1 == comp_player1:
                coordinate = comp_move(grid)
                col = coordinate[0]
                row = coordinate[1]
            elif player1 == comp_player2:
                coordinate = comp_move(grid)
                col = coordinate[0]
                row = coordinate[1]
                
            current = get_state(grid, row, col) ## this gets the element in the cell which is provided by the user

            if current != ' ': ## this checks to see if the cell provided has an entry in it
                print("That cell/position is taken! or That coordinate is not on the board")
            else:  ## since the if statement fails, this else block set the corresponding 'X' or 'O'
                    ## entry in the cell
                set_state(grid,row,col, player1) ## sets the either 'X' or 'O' to the cell on the board
                spaces -= 1 ## reduces the number of available cells by 1 each time a cell is occupied 

                if winning_cond(grid): ## if this if statement is false, means we don't have a winner(a tie)
                                       ## or the game is still in progress and there is yet to be a winner
                    print(print_board(grid))  ## if a winner eventually emerge, this prints out the final
                                          ## status of the board. 
                    print(player1 + " wins")
                    Ongoing = False  ## this ends the while loop when a winner emerges

                else:  ## if there isn't a winner or the game isn't tied yet, the next player is updated
                       ## to either 'X' or 'O' depending on who the last player was
                    if player1 == 'X': 
                        player1 = comp_player2

                    else:
                        player1 = comp_player1

                if spaces == 0:
                    print(print_board(grid))
                    print("Game is a tie!")
                    Ongoing = False
        
                    
    def two_user():
        Ongoing = True  ## used for running a continuous loop
        current_player = 'X' ## first player is set to X by default
        spaces = 9    ## available number of cells before game starts
        while Ongoing:
            print_board(grid)  ## prints the state of the board before a player plays either X or O
            print(current_player + "'s turn") ## Tells user who's turn to play
            coordinate = eval(input("Enter coordinate for a cell in the form (col,row)! "))
            col = coordinate[0]
            row = coordinate[1]

            current = get_state(grid, row, col) ## this gets the element in the cell which is provided by the user

            if current != ' ': ## this checks to see if the cell provided has an entry in it
                print("That cell/position is taken! or That coordinate is not on the board")
            else:  ## since the if statement fails, this else block set the corresponding 'X' or 'O'
                    ## entry in the cell
                set_state(grid,row,col, current_player) ## sets the either 'X' or 'O' to the cell on the board
                spaces -= 1 ## reduces the number of available cells by 1 each time a cell is occupied 

                if winning_cond(grid): ## if this if statement is false, means we don't have a winner(a tie)
                                   ## or the game is still in progress and there is yet to be a winner
                    print(print_board(grid))  ## if a winner eventually emerge, this prints out the final
                                          ## status of the board. 
                    print(current_player + " wins")
                    Ongoing = False  ## this ends the while loop when a winner emerges

                else:  ## if there isn't a winner or the game isn't tied yet, the next player is updated
                   ## to either 'X' or 'O' depending on who the last player was
                    if current_player == 'X': 
                        current_player = 'O'

                    else:
                        current_player = 'X'

                if spaces == 0:
                    print(print_board(grid))
                    print("Game is a tie!")
                    Ongoing = False

        
    if num_players == 2:
        two_user()
    elif num_players == 1:
        one_user()
    elif num_players == 0:
        zero_user()

main()
    
    
