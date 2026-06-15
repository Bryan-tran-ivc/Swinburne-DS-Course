;Student name: Quang Huy Tran
;Student ID: 106212636
;Stage 1: Game Setup

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
      LDR R3, .InputNum         ; read number into R3
      CMP R3, #10               ; check if less than 10
      BLT Error
      CMP R3, #100              ; check if greater than 100
      BGT Error
      B PrintResults            ; both checks passed

Error:
      MOV R0, #errMsg
      STR R0, .WriteString
      B MatchInput              ; ask again

; SECTION 3: PRINT RESULTS
PrintResults:
      MOV R0, #outName
      STR R0, .WriteString      ; print "Player 1 is "
      MOV R0, #playerName
      STR R0, .WriteString      ; print player name
      MOV R0, #outMatchsticks
      STR R0, .WriteString      ; print "\nMatchsticks: "
      STR R3, .WriteUnsignedNum ; print matchstick count
      HALT

; DATA
inName:         .asciz "Please enter your name: "
playerName:     .block 128
question:       .asciz "\nHow many matchsticks (10-100)? "
errMsg:         .asciz "\nInvalid input! Please enter a number between 10 and 100\n"
outName:        .asciz "\nPlayer 1 is "
outMatchsticks: .asciz "\nMatchsticks: "