// Set up Interrupt handling
      MOV R0,#flash
      STR R0,.ClockISR
      MOV R0,#1000
      STR R0,.ClockInterruptFrequency
      MOV R0,#1
      STR R0,.InterruptRegister //Enable all interrupts
      MOV R3, #0        // register keeps track of state of LED
mainProgram: B mainProgram //Here, just an empty loop!
flash:
      PUSH {R0,R1}
      CMP R3, #0        // check state
      BNE off
      MOV R3, #1        // if R3 0, then 1
      MOV R0, #.white
      B drawpixel
off:
      MOV R3, #0        // if R3 1, then 0
      MOV R0, #.green
drawpixel:
      STR R0, .Pixel367 // draw the pixel
      POP {R0,R1}
      RFE

