;Student name: Quang Huy Tran
;Student ID: 106212636
;Stage 3: Human versus Computer

; SECTION 1: READ PLAYER NAME
      MOV R0, #inName
      STR R0, .WriteString
      MOV R1, #playerName
      STR R1, .ReadString       ; save what user typed into playerName
      STRB R6, .WriteChar       ; print newline after name input

; SECTION 2: VALIDATE MATCHSTICKS (10-100)
MatchInput:
      MOV R0, #question
      STR R0, .WriteString
      LDR R3, .InputNum
      CMP R3, #10
      BLT InputError
      CMP R3, #100
      BGT InputError
      MOV R8, R3                ; R8 = save starting count for replay
      B GameLoop

InputError:
      MOV R0, #errMsg
      STR R0, .WriteString
      B MatchInput

; SECTION 3: MAIN GAME LOOP
GameLoop:
      CMP R3, #0
      BEQ Draw

      MOV R0, #msgRemaining1
      STR R0, .WriteString      ; "Player "
      MOV R0, #playerName
      STR R0, .WriteString
      MOV R0, #msgRemaining2
      STR R0, .WriteString      ; ", there are "
      STR R3, .WriteUnsignedNum
      MOV R0, #msgRemaining3
      STR R0, .WriteString      ; " matchsticks remaining"

; --- HUMAN TURN ---
RemoveInput:
      MOV R0, #msgRemove1
      STR R0, .WriteString      ; "Player "
      MOV R0, #playerName
      STR R0, .WriteString
      MOV R0, #msgRemove2
      STR R0, .WriteString      ; ", how many do you want to remove (1-7)? "
      LDR R4, .InputNum

      CMP R4, #1
      BLT RemoveError
      CMP R4, #7
      BGT RemoveError
      CMP R4, R3
      BGT RemoveError
      B HumanRemove

RemoveError:
      MOV R0, #removeErrMsg
      STR R0, .WriteString
      B RemoveInput

HumanRemove:
      SUB R3, R3, R4
      ; After human removes: if 1 left -> human wins (computer must take last)
      CMP R3, #1
      BEQ HumanWins
      ; If 0 left -> draw
      CMP R3, #0
      BEQ Draw

; --- COMPUTER TURN ---
      MOV R0, #msgCompTurn
      STR R0, .WriteString      ; "Computer Player's turn"

CompRandom:
      LDR R4, .Random           ; get random number
      AND R4, R4, #7            ; mask to range 0-7
      CMP R4, #0
      BEQ CompRandom            ; 0 is invalid, try again
      CMP R4, R3
      BGT CompRandom            ; more than remaining, try again

      MOV R0, #msgCompRemove
      STR R0, .WriteString      ; "Computer removes "
      STR R4, .WriteUnsignedNum
      MOV R0, #msgMatchsticks
      STR R0, .WriteString      ; " matchstick(s)"

      SUB R3, R3, R4
      ; After computer removes: if 1 left -> human loses (human must take last)
      CMP R3, #1
      BEQ HumanLoses
      ; If 0 left -> draw
      CMP R3, #0
      BEQ Draw
      B GameLoop

; SECTION 4: END GAME OUTCOMES
; Spec: "Player <name>, YOU WIN!"
HumanWins:
      MOV R0, #msgWin1
      STR R0, .WriteString      ; "Player "
      MOV R0, #playerName
      STR R0, .WriteString
      MOV R0, #msgWin2
      STR R0, .WriteString      ; ", YOU WIN!"
      B PlayAgain

; Spec: "Player <name>, YOU LOSE!"
HumanLoses:
      MOV R0, #msgLose1
      STR R0, .WriteString      ; "Player "
      MOV R0, #playerName
      STR R0, .WriteString
      MOV R0, #msgLose2
      STR R0, .WriteString      ; ", YOU LOSE!"
      B PlayAgain

; Spec: "It's a draw!"
Draw:
      MOV R0, #msgDraw
      STR R0, .WriteString
      B PlayAgain

; SECTION 5: PLAY AGAIN
; Spec: "Play again (y/n) ?" — restart with same settings (R8), or terminate
PlayAgain:
      MOV R0, #msgPlayAgain
      STR R0, .WriteString      ; "Play again (y/n) ? "
      MOV R0, #inputChar
      STR R0, .ReadString
      LDRB R9, [R0]             ; load first character of input
      CMP R9, #121              ; 'y'
      BEQ RestartGame
      CMP R9, #110              ; 'n'
      BEQ EndGame
      B PlayAgain               ; anything else: ask again

RestartGame:
      MOV R3, R8                ; restore original matchstick count
      B GameLoop

EndGame:
      HALT

; DATA
;Stage 1
inName:        .asciz "Please enter your name: "
playerName:    .block 128
question:      .asciz "\nHow many matchsticks (10-100)? "
errMsg:        .asciz "\nInvalid input! Please enter a number between 10 and 100\n"
;Stage 2
removeErrMsg:  .asciz "\nInvalid input, please try again\n"
msgRemaining1: .asciz "\nPlayer "
msgRemaining2: .asciz ", there are "
msgRemaining3: .asciz " matchsticks remaining\n"
msgRemove1:    .asciz "Player "
msgRemove2:    .asciz ", how many do you want to remove (1-7)? "
;Stage 3
msgCompTurn:   .asciz "\nComputer Player's turn\n"
msgCompRemove: .asciz "Computer removes "
msgMatchsticks: .asciz " matchstick(s)\n"
msgWin1:       .asciz "\nPlayer "
msgWin2:       .asciz ", YOU WIN!\n"
msgLose1:      .asciz "\nPlayer "
msgLose2:      .asciz ", YOU LOSE!\n"
msgDraw:       .asciz "\nIt's a draw!\n"
msgPlayAgain:  .asciz "\nPlay again (y/n) ? "
inputChar:     .block 4