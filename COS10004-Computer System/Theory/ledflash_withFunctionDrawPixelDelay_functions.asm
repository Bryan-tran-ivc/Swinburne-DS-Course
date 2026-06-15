      mov R2, #1        ; 1sec delay time
flash:
      MOV R0, #.green
      MOV R1, R2
      BL drawpixel      ; "flash on"
      MOV R0, #.white
      MOV R1, R2
      BL drawpixel      ; "flash off"
      B flash
      HALT
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; drawpixel function
;; inputs R0 - colour, 
;; 		  R1 - time delay in seconds
drawpixel:
      PUSH {R3,R4}
      MOV R3, R0        ; copy pixel colour to R3
      MOV R4, R1        ; copy delay time to R4
      STR R3, .Pixel367 ; draw pixel with colour
      PUSH {R0, LR}}	; backup R0 and LR before param pass and function call
      MOV R0, R4        ; pass delay time to delay function
      BL delay          ; call delay function
      Pop {R0, LR}	; restore R0 and LR after function call
      Pop {R3,R4}
      RET               ; job done
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;  delay function
;;  inputs R0 - time delay in seconds
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
