# ** How does a Program is executed?**

## **Compilation:**
```C
int main() {
    int a = 5;
    int b = 3;
    int c = a + b;
    printf("%d", c);
}
```

### 1. The above program is stored in SSD as add.c.
### 2. When it is compiled, the compiler converts every line of code into assembly level language.
### 3. The assembler converts the code in assembly to machine code.
### 4. A new file as ``add.exe`` is created with machine level instructions, data & meta data.
### 5. The file ``add.exe`` is stored in SSD.

## **Execution:**
### ``When you double click the add.exe.``

### 1. The instructions & data in add.exe are loaded from SSD to RAM.
### 2. The Control unit places the address of instruction into the Program Counter (PC).
### 3. After executing the instruction in the Instruction Register (IR).
### 4. Control unit places the address of instruction from PC into IR and increments the PC.
### 5. Control unit checks if the address is present in L1 Cache. If yes execute that instruction present in the address. If not check in L2 -> L3 -> RAM.
### 6. When the address is found in RAM, then Control unit copies the necessary instructions of program and place them into the L1 Cache.
### 7. And the Decoder decodes the instruction in the CPU decides if it needs ALU or other units to execute the instruction.
### 8. Next, the instruction gets executed by either ALU or other units.
### 9. When the instructions are about storing the data then CPU stores them in the Registers and that data is fetched from the registers when needed.
### 10. This cycle repeats from 3 to 9.

## CPU never knows what are the variables, functions, libraries, etc. It only knows instructions, bits, memory addresses, etc.