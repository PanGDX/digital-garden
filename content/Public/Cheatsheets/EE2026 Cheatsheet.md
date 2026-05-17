![[Pasted image 20250818114856.png]]

![[Pasted image 20250820144600.png]]

### Radix
the base of a system of [numeration](https://www.google.com/search?client=ubuntu-sn&hs=Ds1&sca_esv=fa8e374c3da64ae1&channel=fs&sxsrf=AE3TifOQl5xoPGCLqZrmGvq1aVnmH6b4uA:1755671580131&q=numeration&si=AMgyJEt_i95eqLH3KOj-Ut-VGJJ7JvFTgi0QzrjfdmyzUpEnsogcdYq1Q8n7tYiY6g3a4xY2AYuogSU6-v7ujyNThIvwHpU4c6jRLl5aSBNMTxBJaLgUkiE%3D&expnd=1&sa=X&ved=2ahUKEwiT5oCn4piPAxUz3TgGHcHXIJ0QyecJegQINBAS).
**Common ones include:**
- decimal (r=10)
- octal (r=8)
- hexadecimal (r=16)
- binary (r=2)

![[Pasted image 20250818115203.png]]
The notation is always 

$$(A)_2,(A)_{16},(A)_{10},etc$$
This tells us that the number A is in the form of radix = 2,16,10,etc

#### Binary/Hex/Oct to Decimal
This is the simplest one.

Start from the leftmost position and note the position. **This starts from zero**. **One digit is zero power**. Use the radix (2,8,10,16), convert to base 10 and then multiply by the radix to the power of the position. Iterate to the right position and repeat, adding the numbers one by one. The power of the position can be negative.


$$(18AB.4F)_{16}= 1\times16^3+8\times16^2+10\times16^1+11\times16^0+4\times16^{-1}+15\times16^{-2}=(6315.30859375)_{10}$$

Iterate from the leftmost position, noting the number/character's digit. 


#### Decimal to Binary/Hex/Oct

Think about how to do this.

OF COURSE! It's the reverse! Instead of multiplying and adding, we divide and subtract! **Build from the back!**

Well, how to do that?
Let's start from this.
$$6315_{10} \Rightarrow(18AB)_{16}$$

Make a table
![[Pasted image 20250911133759.png]]

| Number  | Quotient | Remainder | Remainder in Radix |
| ------- | -------- | --------- | ------------------ |
| 6315/16 | 394      | 11        | B                  |
| 394/16  | 24       | 10        | A                  |
| 24/16   | 1        | 8         | 8                  |
| 1/16    | 0        | 1         | 1                  |
WOW we got 18AB!

#### Hex/Binary/Oct <--> Hex/Binary/Oct
Binary is the simplest and the bridging for hex and oct.

**Hex <--> Binary**
- Each hex is 4 bits

![[Pasted image 20250820144529.png]]
**Oct <--> Binary**

![[Pasted image 20250820144545.png]]
**Oct <--> Hex**
Write it out in binary and then group, adding zeros **in front**
![[Pasted image 20250820144639.png]]




## Binary Arithmetic

#### Adding
Add and carry over if $\ge 2$
For instance: 0+1 = 1     
For instance: 1+1 = 0 (1 carry over)
For instance: 1+1+1 = 1 (1 carry over)

#### Multiplication

0 x 0 = 0
0 x 1 = 0
1 x 1 = 0

From this, use the same rules as decimal system (shift and add)
![[Pasted image 20250820144942.png]]

#### Subtraction
0 - 0 = 0
0 - 1 = 1 (borrow from higher position)
1 - 0 = 1
1 - 1 = 0 

#### Division

![[Pasted image 20250820145113.png]]



## Arithmetic in Digital Systems 

You might notice that we can implement multiply and divide by using add and subtract!
Subtraction can be performed by adding a negative number


## Signed and Unsigned
**Unsigned**
the MSB also represents a number
Subtraction is done through borrowing method. No need to convert unlike signed

**Signed**
Most significant bit (MSB)
0 – represents a positive number
1 – represents a negative number


**1's Complement:** The 1's complement of a binary number is found by simply inverting all of its bits
**2's Complement:** The 2's complement of a binary number is calculated in a two-step process: first, you find the 1's complement by inverting all the bits, and then you add 1 to the result

In **1's complement**, when you add two numbers, if a carry is generated from the most significant bit, it must be added back to the least significant bit of the result. This "end-around carry" adds an extra step to the calculation and complicates the hardware design

**2's complement** elegantly avoids this issue. The same addition circuitry can be used for both signed and unsigned numbers, and subtraction is performed by adding the 2's complement of the subtrahend. Any carry-out from the most significant bit is simply discarded.


- **1's Complement Range:** For an 8-bit number, the range is -127 (10000000) to +127 (01111111).
    
- **2's Complement Range:** For an 8-bit number, the range is -128 (10000000) to +127 (01111111).
![[Pasted image 20250820155014.png]]



![[Pasted image 20250820155032.png]] 



![[Pasted image 20250820155444.png]]
additional stuff:
$$AB+\overline{A}C+BC=AB+\overline{A}C$$
$$(A+B)(\overline{A}+C)(B+C)=(A+B)(\overline{A}+C)$$
Removing the redundant term. The condition is the presence of A and A'. Let us consider AB and $\overline{A}C$. Both terms are AND terms with A and complement of A as the common denominator. Now think of A as a filter with some holes. The complement of A is the opposite of that filter (a filter with the holes filled and the holes where the filter material of A was). Now B and C is the things to be passed through. Any intersection of B and C will be accounted for in the first two terms. BC may not be zero but does not provide any additional value.

$$AC=CA$$

$$$$




![[Pasted image 20250820155450.png]]


![[Pasted image 20250820155531.png]]



![[Pasted image 20250820155547.png]]


Product = AND
Addition = OR

Minterm
1. Look at a specific row in a truth table. 
2. For that row, if a variable's value is **1**, use the variable as is (e.g., A)
3. If a variable's value is **0**, use its complement (e.g., A').
4. AND all the variables together.
Example: ABC


Maxterm
1. Look at a specific row in a truth table.
2. For that row, if a variable's value is **0**, use the variable as is (e.g., A)    
3. If a variable's value is **1**, use its complement (e.g., A').
4. OR all the variables together.
Example: A+B+C
#### Canonical Sum of Products (SOP) Form
F = A'BC' + AB'C
This form, also known as the **minterm canonical form** or **disjunctive normal form**, represents a function as the **OR sum of all the minterms for which the function's output is 1**.


#### Canonical Product of Sums (POS) Form
F = (A+B+C) ⋅ (A+B+C')
This form, also known as the **maxterm canonical form** or **conjunctive normal form**, represents a function as the **AND product of all the maxterms for which the function's output is 0**.



### From Personal Lecture
$\overline{A}$ is not A
$\overline{A} + A= 1$
$1 \times A = A$
$\overline{A} A=0$


De Morgan (complement rule)
$\overline{+}=\times$  
$\overline{\times}=+$


### Converting Truth table to Sum of Products
![[Pasted image 20250821114627.png]]

Why is this useful?
It is useful to generate a custom F function that is specifically **true** for certain A,B and C values. (More useful for true in my opinion)

![[Pasted image 20250821114743.png]]

The same concept as above. It is useful to generate a function F that produces a false value under certain A,B,C conditions


### Reversing the process: from SOP/POS to truth table
Simply do the reverse. List out the minterms and maxterms that we want to be 1/0 and fill in the rest as 0/1
![[Pasted image 20250821114956.png]]




![[Pasted image 20250821115133.png]]

Both the Sum of Products (SOP) form and the Product of Sums (POS) form are just different ways of writing an expression for the **exact same function**. Therefore, they must produce the identical output column in a truth table.
However, they simply focus on different things. SOP focuses on answering when is this true (1). POS focuses on answering when is this false (0).



![[Pasted image 20250821115318.png]]



• Logic gate introduction
◦ AND/NAND, OR/NOR, NOT/buffer, XOR/XNOR
• Levels of abstraction: Boolean function, truth table, graphical, Verilog
• Implementation of Boolean function using gates
• Design simplification via algebraic manipulations
• Positive and negative logic
• Implementation of Boolean function with gate-level netlist




![[Pasted image 20250821115715.png]]
![[Pasted image 20250821120128.png]]
NOT/Exclusively AND
NOT/Exclusively OR


```verilog
module andgate(A,B,F);
	input A,B;
	output F;
	assign F = (A&B);
endmodule

module nandgate(A,B,F);
	input A,B;
	output F;
	assign F = ~(A&B);
endmodule

module orgate(A,B,F);
	input A,B;
	output F;
	assign F = A|B;
endmodule

module norgate(A,B,F);
	input A,B;
	output F;
	assign F = ~(A|B);
endmodule

module xorgate(A,B,F);
	input A,B;
	output F;
	assign F = (A^B);
endmodule
```


![[Pasted image 20250821120306.png]]

Simplify before gate-level implementation. Fewer gates = faster!
![[Pasted image 20250821120424.png]]




![[Pasted image 20250821120540.png]]


#### Bubble Pushing
![[Pasted image 20250821120616.png]]
- Create two bubbles and push
- Bubbles at input of gates can be pushed and transforms the gate

![[Pasted image 20250821120830.png]]
Note how the bubbles are placed at step 2. This is to indicate complement ($\overline{A}$).
Then add bubbles and shift around.



```verilog
// comment
/*
comment
*/

// Contain any sequence of letters, digits, a dollar sign '$' , and the underscore '_' symbol.


// 0 for false, 1 for true
// z/Z for high impedance value (???) usually treated as x value
// x/X represents uninitialized value/in state of change
```

Verilog is a powerful hardware description language (HDL) used to model and design electronic systems, particularly digital circuits. It provides a way to describe the behavior and structure of hardware, from simple logic gates to complex microprocessors, in a textual format. This code can then be used to simulate the circuit's behavior and synthesize it into a physical piece of hardware.

**IT IS A HARDWARE DESCRIPTION LANGUAGE!!!!**

**wire** 
used to represent an internal (physical) connection
**continuously driven by an assignment**
we should literally think of this as a wire connecting components. 

**reg**  
on LHS of an assignment, reg is updated immediately and holds its  
value until changed again 

**parameter**
use for constants

![[Pasted image 20250826210147.png|300]]

**reg**: This is the most common variable type and is used to represent data storage elements
Despite its name, a reg does not always synthesize to a physical register; it can also represent combinational logic depending on how it's used in the code.
**integer**: A 32-bit signed variable, often used for loop counters and other general-purpose calculations
**real**: Used for storing floating-point numbers
**time**: A 64-bit unsigned integer used to store simulation time, primarily for use in testbenches

**conditional operators**
- The ? conditional opreator allows to select output from a set of inputs based on a condition
	- `assign y = s ? d[1] : d[0]`
- 2:1 multiplexer MUX


**procedural assignment**
`always @`

**anything assigned in an always block must be declared as type reg**

Two assignment types: blocking vs non-blocking

![[Pasted image 20250826210925.png]]

Statements within always block are executed sequentially

Multiple always blocks run concurrently
**no assigns in always blocks**


**if-else**
![[Pasted image 20250826211354.png]]
**case**

![[Pasted image 20250826211347.png]]



**these two are the same:**
![[Pasted image 20250826211420.png]]


![[Pasted image 20250826211739.png]]![[Pasted image 20250826211841.png]]
```
// SOME FUNCTIONS
and
not
nor
xor
```




**port connection**
The dot (.) is used for a syntax called **named port connection** (or named port mapping).
![[Pasted image 20250826212130.png]]
It is the equivalent of `function(arg=...)`

```verilog
#10 //wait for 10 nano seconds

mux21 dut (sel, ip, op)

  // ---> INSTANTIATE THE DUT <---
  // Here, 'and_gate' is the module name, and 'dut' is the instance name.
  and_gate dut (
    .a (test_a),   // Connect testbench's test_a to DUT's port a
    .b (test_b),   // Connect testbench's test_b to DUT's port b
    .y (test_y)    // Connect testbench's test_y to DUT's port y
  );
```

``
- **Executes Only Once:** The code inside an initial block starts executing at the very beginning of a simulation (at time 0) and runs through its statements only one time.
Think of begin...end as the Verilog equivalent of curly braces { ... } in languages like C, C++, or Java. Its sole purpose is to group multiple statements together so they are treated as a single, sequential block.

**Putting Them Together: `initial begin ... end`**


Sequential logic circuits => The output depends on both the current state and the 'memory'

There are two types 

SR FF can store one bit of information - true or false
![[Pasted image 20250911120001.png]]NOR gate, if **any** of its inputs is 1, the output is 0. Only if **all** inputs are 0 is the output 1.
The **single most important rule for Q and Q' is that they must always be logical opposites** of each other. **it really only works when you do this. When tracing, set Q as 1/0 and then Q' as 0/1 and trace from there**
- If **Q = 1**, then **Q' must = 0**.
    
- If **Q = 0**, then **Q' must = 1**.
When we talk about the "state" of a flip-flop, we are referring to the value of its primary output, **Q**.

- If **Q = 1**, we say the flip-flop is in the **"Set" state** or the **"High" state**. It is storing a logical '1'.
    
- If **Q = 0**, we say the flip-flop is in the **"Reset" state** or the **"Low" state**. It is storing a logical '0'.





![[Pasted image 20250914090742.png]]
The output **Q flips** (or toggles) its state.

A T flip-flop is a "Toggle" flip-flop. Its behavior, as shown in the truth table, is:

- If the input **T = 0** when the active clock edge arrives, the output **Q holds** its current value (no change).
    
- If the input **T = 1** when the active clock edge arrives, the output **Q flips** to the opposite of its current value (it toggles).
![[Pasted image 20250911123814.png]]

- Clock input controls when circuit reads input/changes outputs
- Synchronous circuits only respond at transitions
	- Low -> High
	- High -> Low![[Pasted image 20250911125049.png|300]]

![[Pasted image 20250911125638.png]]
The maximum clock frequency is determined by the minimum time required for one complete clock cycle. Let's trace the signal path in a simple synchronous system, like a chain of flip-flops, which is the typical use case that limits clock speed.
**Minimum Clock Period (T) = Propagation Delay (tp) + Setup Time (tsetup)**


$t_{pHL}$ = It's the delay from the active clock edge to the moment the Q output reflects the new Low value.
```
module dff( input d, clk, output reg q);
	always @ (posedge clk)
		begin
			q=d;
		end
endmodule
```
![[Pasted image 20250911125831.png]]
Note the up array for posedge and down arrow for negedge
posedge catches 0 ->1 change
negedge catches 1 -> 0 change
![[Pasted image 20250911124029.png]]
You can imagine the usefulness of deferred assignment. It ensures that calculations are finished completely before committing the change in values. This prevents the values of x and y from affecting the circuit's behavior.


When modeling sequential logic, use nonblocking
assignments.
#2: When modeling simple combinational logic, use
continuous assignments (assign).
#3: When modeling complex combinational logic, use
blocking assignments in an always block.
#3: When modeling both sequential and combinational logic
within the same always block, use nonblocking assignments.
#4: **Do not mix blocking and nonblocking assignments in the**
**same always block.**
#5: Do not make assignments to the same variable from
more than one always block.
Digital Design Page 60



# Counters
Asynchronous : Circuit elements do not get the clock input simultaneously
Synchronous Counters: Circuit elements get the clock input simultaneously
The 4-bit counter counts from 0000 (0) → 1111(15) -> 16 distinct count states ⇒ called a mod-16 counter
**limiting frequency**
![[Pasted image 20250911131502.png]]
```
module mod8( input clk,
	output reg [2:0] q);
	wire [2:0] d;
	reg [2:0] q = 0;
	always @ (posedge clk)
		begin
			q <= d;
		end
	assign d[0] = ~q[0];
	assign d[1] = q[0] ^ q[1];
	assign d[2] = q[0]&q[1]&~q[2] | ~q[1]&q[2] | ~q[0]&q[2];
endmodule
```



The D Flip-Flop: A Data Latch
The D flip-flop, often called a "data" or "delay" flip-flop, is designed to capture and store the value present at its 'D' (data) input at the moment of a clock pulse.[1][2] This means that on the active edge of the clock signal (either rising or falling, depending on the design), the output 'Q' will assume the state of the 'D' input.[3] If the D input is high (1), the Q output will be set to high. Conversely, if the D input is low (0), the Q output will be reset to low. The output then holds this value until the next clock pulse. This behavior makes the D flip-flop ideal for creating registers, which are collections of flip-flops used to store multi-bit data, and for synchronizing signals.[4]

The T Flip-Flop: The Toggle Switch
The T flip-flop, or "toggle" flip-flop, has a single 'T' (toggle) input.[5][6] Its operation is straightforward: if the T input is high (1) when the clock pulse arrives, the output 'Q' will flip, or "toggle," to its opposite state.[7][8] If the output was 0, it becomes 1, and if it was 1, it becomes 0. If the T input is low (0) during the clock pulse, the output remains unchanged, holding its current state.[6][9][10] This toggling behavior makes the T flip-flop particularly useful in designing binary counters and frequency dividers, where the output frequency is half of the input clock frequency.[7]


**Converting from decimal to x base**
![[Pasted image 20250911141106.png|400]]
**Converting from x to decimal**
![[Pasted image 20250911141325.png]]
**Converting from x to y**
- Use binary as intermediary step. Oct = 3 bits. Hex = 4 bits. Group, convert, group.
**Unknown base**
![[Pasted image 20250911134939.png|300]]
****
0 – represents a positive number
1 – represents a negative number

Complement is only needed when the number is negative. A binary number that is being interpreted using the 2's complement system for representing signed integers
**1's Complement:** The 1's complement of a binary number is found by simply inverting all of its bits
1111010(1' s) → 00000101(magnitude) → -5
**2's Complement:** The 2's of a decimal: ignore the negative sign, convert to binary number. then, you find the 1's complement by inverting all the bits, and then you add 1 to the result. Rhe ****Most Significant Bit (MSB)**** represents the sign. To reverse the process, identify if it is negative. If it is, invert and +1 (equivalent to -1 and invert).
In addition, if bit is carried to 9th position, ignore in 8-bit arithmetic system.

**only for negative**
1. Start with the positive binary number (e.g., 01001011 for +75).
2. Starting from the **right**, copy all the bits exactly as they are until you've copied the **first 1**.
3. After that first 1, **invert** all the remaining bits to the left.
**Applying the shortcut to 00100:
- The first 1 from the right is the very first bit. So, we copy it: ...100
- Now, we invert all the bits to its left (00100): 11
- Combine them: 11100
****
Product = AND Addition = OR

Minterm
1. Look at a specific row in a truth table. 
2. For that row, if a variable's value is **1**, use the variable as is (e.g., A)
3. If a variable's value is **0**, use its complement (e.g., A').
4. AND all the variables together.
Example: ABC


Maxterm
1. Look at a specific row in a truth table.
2. For that row, if a variable's value is **0**, use the variable as is (e.g., A)    
3. If a variable's value is **1**, use its complement (e.g., A').
4. 'OR' all the variables together.
Example: A+B+C
****
- Bubble pushing for logic gates: Pairs of bubbles can be created anywhere. Bubbles represent complements
![[Pasted image 20250911141851.png]]

****
# Verilog
**wire** 
used to represent an internal (physical) connection
**continuously driven by an assignment**
we should literally think of this as a wire connecting components. 

**reg**  
on LHS of an assignment, reg is updated immediately and holds its  
value until changed again 
- Bit Indexing:
	- X[7:0]
- Concatenation
	- {X[3:0] , X[4:6]}
![[Pasted image 20250911135230.png]]


- by default passing an output is always a wire with the exception of when the output is being passed through an always block
	- `always` blocks are procedural

Comment out the $monitor and any $dumpvars or $dumpon commands in your testbench. The simulation will run much faster, and you can rely on the console output from your $display statements to verify behavior.
- The .wdb (waveform database) file will become big and slow



Of course. This is one of the most fundamental and important concepts in digital design, and understanding it is key to writing Verilog that works correctly.

The core of the issue is the difference between **Combinatorial Logic** and **Sequential Logic**, and how Verilog uses `always @(*)` and `always @(posedge clk)` to describe them.

---

### Part 1: The Two Types of Digital Logic

#### 1. Combinatorial Logic (The Job of `always @(*)`)
Think of this as **instantaneous logic**. The output is a *pure function* of the current inputs. It has no memory of what happened in the past.

*   **Real-World Analogy:** A simple calculator. If you type `2 + 3`, the answer is `5`. It doesn't matter if you calculated `1 + 1` before. The output *only* depends on the current inputs.
*   **Hardware Equivalent:** Wires and logic gates (AND, OR, NOT, multiplexers).
*   **How `always @(*)` works:** The `*` in the sensitivity list is a shortcut that tells the tool: "If *any* signal on the right-hand side of an equation inside this block changes its value, re-calculate the outputs *immediately*."

#### 2. Sequential Logic (The Job of `always @(posedge clk)`)
Think of this as logic with **memory**. The output depends on the current inputs *and* the system's previous state. It changes in discrete steps, synchronized to a clock.

*   **Real-World Analogy:** A person counting button clicks with a pen and paper. They remember the current count (the "state"). When you click the button (the "clock edge"), they look at their paper, add one, and write down the new number. They ignore everything happening *between* clicks.
*   **Hardware Equivalent:** **Flip-flops**. These are the fundamental memory elements in an FPGA. A flip-flop holds a value and will only update it to a new value on a clock edge.
*   **How `always @(posedge clk)` works:** The `posedge clk` in the sensitivity list tells the tool: "Create flip-flops for the registers assigned in this block. No matter how the inputs change, do not update the value of these registers until the exact moment the clock signal goes from low to high."

---

### Part 2: How `always @(*)` Caused Your Specific Errors

You were trying to describe **sequential logic** (a state machine that remembers a position and a counter) using a **combinatorial block**. This mismatch between intent and syntax caused two major problems.

#### Error 1: The "Teleporting" Circle (Combinatorial Feedback Loop)

This was caused by your FSM that updates the circle's position:
```verilog
// The flawed code
always @(*) begin
    //...
    future_x_circle_center = x_circle_center + _x_movement; // Reads the old position
    //...
    x_circle_center = future_x_circle_center; // Tries to write the new position
end
```
Let's trace what the hardware tries to do with this:
1.  The `always @(*)` block is sensitive to `x_circle_center`.
2.  Inside the block, you calculate a *new* value for `x_circle_center`.
3.  Because this is a combinatorial block, the tool tries to make the update happen *instantaneously*.
4.  The moment the output `x_circle_center` is updated, the input `x_circle_center` has changed.
5.  This change **immediately re-triggers the sensitivity list (`*`)**, and the block executes again.

This creates an **infinite, zero-delay feedback loop**. In simulation, this loop runs thousands of times in a single time-step, causing the `x_circle_center` value to increment uncontrollably, making it look like it "teleported" across the screen.

When you try to synthesize this for a real FPGA, the tool sees this impossible loop and either throws an error or, as in your case, infers latches which lead to unpredictable, unstable behavior.

**The Fix:** Using `always @(posedge clk)` breaks this loop. The update `x_circle_center <= future_x_circle_center` only happens on a clock edge. The block then "sleeps" until the next clock edge, giving the system a stable, predictable update rate and preventing the infinite loop.

#### Error 2: The Stuck Movement State (Unintentional Latch)

This was caused by your button-press logic:
```verilog
// The flawed code
always @(*) begin
    if (btn[0])      _current_movement = _direction_up;
    else if (btn[1]) _current_movement = _direction_left;
    // ... and so on ...
    // BUT WHAT HAPPENS IF NO BUTTON IS PRESSED?
end
```
A fundamental rule for combinatorial logic is that you **must specify an output for every possible input combination**.

Your code specified what `_current_movement` should be if `btn[0]` is pressed, if `btn[1]` is pressed, etc. But it never specified what should happen when **no buttons are pressed** (when `btn` is `4'b0000`).

When the synthesis tool sees this, it asks itself, "The designer didn't tell me what to do. What should I build?" Its only logical assumption is that you want to **preserve the last known value**. The hardware component that stores a value without a clock is called a **latch**.

Latches are highly undesirable in modern FPGA design because their timing is difficult to analyze, and they can be susceptible to glitches. Your code was unintentionally creating a latch that "held on" to the last direction forever.

**The Fix:** When we moved this logic to a clocked block, we were explicitly telling the synthesizer to create a flip-flop. A flip-flop is *designed* to hold its value between clock edges. This is intentional, predictable memory, which is exactly what you wanted for your "sticky" movement state.

### Summary

| Feature | `always @(*)` (Combinatorial) | `always @(posedge clk)` (Sequential) |
| :--- | :--- | :--- |
| **Purpose** | To describe logic that is instantaneous. | To describe logic that has memory and changes in steps. |
| **Synthesizes to** | Logic Gates, Multiplexers | **Flip-Flops** + Logic Gates |
| **Analogy** | A simple calculator | A state machine, a counter, a memory register |
| **Your Error** | You used it for a state machine, creating **infinite loops** and **unwanted latches**. | This is the **correct construct** for state machines, counters, and updating positions over time. |

In short, `always @(*)` describes **what a circuit *is*** right now based on its inputs. `always @(posedge clk)` describes **how a circuit's state *changes* over time**.