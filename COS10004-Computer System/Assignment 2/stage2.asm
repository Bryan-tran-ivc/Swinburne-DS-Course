;Student name: Quang Huy Tran
;Student ID: 106212636
;Stage 2: Single Player Input

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
      B GameLoop

InputError:
      MOV R0, #errMsg
      STR R0, .WriteString
      B MatchInput

; SECTION 3: MAIN GAME LOOP
GameLoop:
      CMP R3, #0
      BEQ GameOver

      MOV R0, #msgRemaining1
      STR R0, .WriteString      ; "Player "
      MOV R0, #playerName
      STR R0, .WriteString      ; <name>
      MOV R0, #msgRemaining2
      STR R0, .WriteString      ; ", there are "
      STR R3, .WriteUnsignedNum ; <X>
      MOV R0, #msgRemaining3
      STR R0, .WriteString      ; " matchsticks remaining"

RemoveInput:
      MOV R0, #msgRemove1
      STR R0, .WriteString      ; "Player "
      MOV R0, #playerName
      STR R0, .WriteString      ; <name>
      MOV R0, #msgRemove2
      STR R0, .WriteString      ; ", how many do you want to remove (1-7)? "
      LDR R4, .InputNum

      CMP R4, #1
      BLT RemoveError           ; less than 1
      CMP R4, #7
      BGT RemoveError           ; more than 7
      CMP R4, R3
      BGT RemoveError           ; more than remaining

      SUB R3, R3, R4            ; update matchstick count
      B GameLoop

RemoveError:
      MOV R0, #removeErrMsg
      STR R0, .WriteString
      B RemoveInput

GameOver:
      MOV R0, #msgGameOver
      STR R0, .WriteString      ; "Game Over"
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
msgGameOver:   .asciz "\nGame Over\n"