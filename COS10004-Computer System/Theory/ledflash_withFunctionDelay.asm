      mov R0, #.green
      mov R1, #.white
      mov R2, #1        ; 1sec delay time
flash:
      str R0,.Pixel367  ; flash on 
      LDR R3,.Time      ; start time
      push {R0}
      MOV R0, R2
      BL delay          ; call delay function
      Pop {R0}
      str R1,.Pixel367  ; flash off
      LDR R3,.Time      ; start time
      push {R0}
      MOV R0, R2
      BL delay          ; call delay function
      pop {R0}
      B flash
      halt
delay:
      push {R3,R4,R5,R6}
      MOV R3, R0        ; move delay time param into R3
      LDR R4, .Time     ; get start ime
timer:
      LDR R5, .Time     ; update time
      SUB R6, R5, R4    ; calc elapsed time
      CMP R6, R3        ; compare elapsed to delay time
      BLT timer
      pop {R3,R4,R5,R6}
      RET
