  1|;Student name: Quang Huy Tran
  2|;Student ID: 106212636
  3|;Stage 4: Graphics
  4|; SECTION 1: READ PLAYER NAME
  5|      MOV R0, #inName
  6|      STR R0, .WriteString
  7|      MOV R1, #playerName
  8|      STR R1, .ReadString
  9|      STRB R6, .WriteChar
 10|; SECTION 2: VALIDATE MATCHSTICKS (10-100)
 11|MatchInput:
 12|      MOV R0, #question
 13|      STR R0, .WriteString
 14|      LDR R3, .InputNum
 15|      CMP R3, #10
 16|      BLT InputError
 17|      CMP R3, #100
 18|      BGT InputError
 19|      MOV R8, R3
 20|      B GameStart
 21|InputError:
 22|      MOV R0, #errMsg
 23|      STR R0, .WriteString
 24|      B MatchInput
 25|; SECTION 3: MAIN GAME LOOP
 26|GameStart:
 27|      STR R3, .ClearScreen
 28|      BL DrawSystem
 29|GameLoop:
 30|      CMP R3, #0
 31|      BEQ Draw
 32|      MOV R0, #msgRemaining1
 33|      STR R0, .WriteString
 34|      MOV R0, #playerName
 35|      STR R0, .WriteString
 36|      MOV R0, #msgRemaining2
 37|      STR R0, .WriteString
 38|      STR R3, .WriteUnsignedNum
 39|      MOV R0, #msgRemaining3
 40|      STR R0, .WriteString
 41|; --- HUMAN TURN ---
 42|RemoveInput:
 43|      MOV R0, #msgRemove1
 44|      STR R0, .WriteString
 45|      MOV R0, #playerName
 46|      STR R0, .WriteString
 47|      MOV R0, #msgRemove2
 48|      STR R0, .WriteString
 49|      LDR R4, .InputNum
 50|      CMP R4, #1
 51|      BLT RemoveError
 52|      CMP R4, #7
 53|      BGT RemoveError
 54|      CMP R4, R3
 55|      BGT RemoveError
 56|      B HumanRemove
 57|RemoveError:
 58|      MOV R0, #removeErrMsg
 59|      STR R0, .WriteString
 60|      B RemoveInput
 61|HumanRemove:
 62|      SUB R3, R3, R4
 63|      MOV R0, #userremovemsg
 64|      STR R0, .WriteString
 65|      STR R4, .WriteUnsignedNum
 66|      MOV R0, #msgMatchsticks
 67|      STR R0, .WriteString
 68|      STR R3, .ClearScreen
 69|      BL DrawSystem
 70|      CMP R3, #1
 71|      BEQ HumanWins
 72|      CMP R3, #0
 73|      BEQ Draw
 74|; --- COMPUTER TURN ---
 75|      MOV R0, #msgCompTurn
 76|      STR R0, .WriteString
 77|CompRandom:
 78|      LDR R4, .Random
 79|      AND R4, R4, #7
 80|      CMP R4, #0
 81|      BEQ CompRandom
 82|      CMP R4, R3
 83|      BGT CompRandom
 84|      MOV R0, #msgCompRemove
 85|      STR R0, .WriteString
 86|      STR R4, .WriteUnsignedNum
 87|      MOV R0, #msgMatchsticks
 88|      STR R0, .WriteString
 89|      SUB R3, R3, R4
 90|      STR R3, .ClearScreen
 91|      BL DrawSystem
 92|      CMP R3, #1
 93|      BEQ HumanLoses
 94|      CMP R3, #0
 95|      BEQ Draw
 96|      B GameLoop
 97|; SECTION 4: END GAME OUTCOMES
 98|HumanWins:
 99|      MOV R0, #msgWin1
100|      STR R0, .WriteString
101|      MOV R0, #playerName
102|      STR R0, .WriteString
103|      MOV R0, #msgWin2
104|      STR R0, .WriteString
105|      B PlayAgain
106|HumanLoses:
107|      MOV R0, #msgLose1
108|      STR R0, .WriteString
109|      MOV R0, #playerName
110|      STR R0, .WriteString
111|      MOV R0, #msgLose2
112|      STR R0, .WriteString
113|      B PlayAgain
114|Draw:
115|      MOV R0, #msgDraw
116|      STR R0, .WriteString
117|      B PlayAgain
118|; SECTION 5: PLAY AGAIN
119|PlayAgain:
120|      MOV R0, #msgPlayAgain
121|      STR R0, .WriteString
122|      MOV R0, #inputChar
123|      STR R0, .ReadString
124|      LDRB R9, [R0]
125|      CMP R9, #121      ; 'y'
126|      BEQ RestartGame
127|      CMP R9, #110      ; 'n'
128|      BEQ EndGame
129|      B PlayAgain
130|RestartGame:
131|      MOV R3, R8
132|      STR R3, .ClearScreen
133|      BL DrawSystem
134|      B GameLoop
135|EndGame:
136|      HALT
137|; SECTION 6: GRAPHICS
138|DrawSystem:
139|      Push {R0, R1, R2, R4, R5, R6, R9, R11, R12}
140|      MOV R0, #1
141|      MOV R1, #1
142|      MOV R6, #0
143|      MOV R11, #0
144|      MOV R12, #0
145|drawMatchStick:
146|      MOV R2, #.PixelScreen
147|      MOV R9, #.orangered
148|      LSL R4, R0, #2
149|      LSL R5, R1, #8
150|      ADD R5, R5, R4
151|      STR R9, [R2+R5]
152|      MOV R9, #.burlywood
153|      MOV R7, #3
154|bodyLoop:
155|      ADD R0, R0, #1
156|      LSL R4, R0, #2
157|      LSL R5, R1, #8
158|      ADD R5, R5, R4
159|      STR R9, [R2+R5]
160|      SUB R7, R7, #1
161|      CMP R7, #0
162|      BGT bodyLoop
163|      ADD R0, R0, #3
164|      ADD R6, R6, #1
165|      ADD R12, R12, #1
166|      CMP R6, R3
167|      BEQ EndDraw
168|      CMP R12, #10
169|      BEQ newLine
170|      B drawMatchStick
171|newLine:
172|      ADD R1, R1, #4
173|      MOV R0, #1
174|      ADD R11, R11, #1
175|      MOV R12, #0
176|      CMP R11, #10
177|      BLT drawMatchStick
178|EndDraw:
179|      Pop {R0, R1, R2, R4, R5, R6, R9, R11, R12}
180|      RET
181|; DATA
182|;Stage 1
183|inName: .asciz "Please enter your name: "
184|playerName: .block 128
185|question: .asciz "\nHow many matchsticks (10-100)? "
186|errMsg: .asciz "\nInvalid input! Please enter a number between 10 and 100\n"
187|;Stage 2
188|removeErrMsg: .asciz "\nInvalid input, please try again\n"
189|msgRemaining1: .asciz "\nPlayer "
190|msgRemaining2: .asciz ", there are "
191|msgRemaining3: .asciz " matchsticks remaining\n"
192|msgRemove1: .asciz "Player "
193|msgRemove2: .asciz ", how many do you want to remove (1-7)? "
194|;Stage 3
195|msgCompTurn: .asciz "\nComputer Player's turn\n"
196|msgCompRemove: .asciz "Computer removes "
197|userremovemsg: .asciz "\nYou chose to remove "
198|msgMatchsticks: .asciz " matchstick(s)\n"
199|msgWin1: .asciz "\nPlayer "
200|msgWin2: .asciz ", YOU WIN!\n"
201|msgLose1: .asciz "\nPlayer "
202|msgLose2: .asciz ", YOU LOSE!\n"
203|msgDraw: .asciz "\nIt's a draw!\n"
204|msgPlayAgain: .asciz "\nPlay again (y/n) ? "
205|inputChar: .block 4
