```latex
\documentclass[8pt,landscape,a4paper]{extarticle}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=0.15in]{geometry}
\usepackage{multicol}
\usepackage{amsmath}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{xcolor}
\usepackage{graphicx}

% Minimize whitespace
\setlength{\columnsep}{6pt}
\setlength{\columnseprule}{0.1pt}
\setlist{leftmargin=8pt, nosep, itemsep=1pt}
\titlespacing{\section}{0pt}{2pt}{2pt}
\titlespacing{\subsection}{0pt}{1pt}{1pt}

% Custom section styling
\titleformat{\section}{\color{blue}\bfseries\scriptsize\uppercase}{}{0em}{}
\titleformat{\subsection}{\bfseries\tiny}{}{0em}{\underline}

\pagestyle{empty}
\begin{document}
\tiny

\begin{multicols*}{4}

% --- SECTION 1 ---
\section{1. OS \& Architecture}
\subsection{OS Fundamentals}
\textbf{Resource Allocator:} Manages/allocates resources. \\
\textbf{Control Program:} Controls execution \& I/O. \\
\textbf{Kernel:} The one program always running. 
\begin{itemize}
    \item \textbf{Monolithic:} 1 big program (Unix, Win). Fast, crashy.
    \item \textbf{Microkernel:} Minimized (IPC/Mem only). Services run as user procs. Secure, stable, slow. 
\end{itemize}
\textbf{Hypervisors:}
\begin{itemize}
    \item \textbf{Type 1 (Bare Metal):} Replaces OS (Enterprise).
    \item \textbf{Type 2 (Host OS):} Runs on OS (VirtualBox).
\end{itemize}

\subsection{Real-Time Systems (RTOS)}
Must satisfy bounded response time; correctness relies on output \textit{and} timeliness. 
\begin{itemize}
    \item \textbf{Focus:} Time-critical (schedulers guarantee execution upper-bound/deadline), reliable, sensor/actuator ops.
    \item \textbf{Response Time:} Time from input to output. 
\end{itemize}

% --- SECTION 2 ---
\section{2. Interrupts \& Polling}
\subsection{Polling vs Interrupts}
\textbf{Polling Cons:} CPU busy-waits, wastes energy. \\
\textbf{Interrupt System:} OS is interrupt-driven (idles if none).
\begin{itemize}
    \item Device buffer $\to$ CPU cache. Device controller fires int.
    \item \textbf{Flow:} Request $\to$ CPU gets int number $\to$ Look up address in \textbf{Interrupt Vector} $\to$ Execute ISR.
\end{itemize}

\subsection{Interrupt Handling}
\begin{itemize}
    \item OS saves Registers \& PC (preserve CPU state).
    \item OS determines int type; executes specific ISR code.
    \item OS restores context \& resumes tasks. 
\end{itemize}
\textbf{Interrupt Response Time ($T_D$):} Latency + Processing. 
\begin{itemize}
    \item RT req: $T_D <$ Time between interrupts.
    \item High-priority ints increase latency of low-priority ones.
\end{itemize}
\textbf{Split Processing:} 
ISR does minimal work (copy data, reset HW) $\to$ Queues pointer to defer main work to dedicated task (avoids missing deadlines).

\subsection{System Calls}
Escalates user prog to OS functions (slow/intensive). \\
\textbf{Flow:} User invokes $\to$ Lib puts syscall \# in Reg $\to$ \textbf{TRAP} (switch to Kernel mode) $\to$ Handle $\to$ Return.

% --- SECTION 3 ---
\section{3. Processes \& Threads}
\textbf{Program:} Static entity. \textbf{Process:} Executing pgm. \\
\textbf{Context Switch:} Save old state, load new. Pure overhead. \\
\textbf{Process Model:} Simplifies concurrent design.

\subsection{Process States}
\begin{itemize}
    \item \textbf{Created:} PCB init. Waits for minimal resources. 
    \item \textbf{Ready:} Competes for CPU. (RTOS: must not disrupt timing of active system).
    \item \textbf{Running:} Actively executing on CPU.
    \item \textbf{Blocked:} Waiting for I/O or Sync. Not competing.
    \item \textbf{Terminated:} Done/Error. PCB kept for data retrieval.
\end{itemize}
\textbf{Running $\to$ Ready Transitions:}
\textit{Pre-emption} (Involuntary: scheduler forces out) vs \textit{Yield} (Voluntary: process asks OS to reschedule).

\subsection{Process Creation}
\begin{itemize}
    \item \textbf{fork():} Exact clone. Ret 0 to child, PID to parent. Inherits PC, Code, Data/Stack copy, Open Files. 
    \item \textbf{exec():} Replaces memory/code with new pgm.
    \item \textbf{wait(status):} Parent blocks until child exits. 
\end{itemize}

\subsection{Threads}
Unit of execution inside a process. \\
\textbf{Shared:} Heap, Data (Globals), Files, Code. \\
\textbf{Private:} Stack, Registers (PC/SP), Thread ID.
\begin{itemize}
    \item \textbf{User Threads:} Managed by Lib. Fast. OS blind (if 1 blocks on I/O, whole process blocks). No true SMP.
    \item \textbf{Kernel Threads:} Managed by OS. Slower. HW-aware (True SMP). Schedulable by OS.
    \item \textbf{Hybrid:} User threads multiplexed on Kernel threads.
\end{itemize}
\textbf{Pthreads:} \texttt{pthread\_t} (TID), \texttt{pthread\_attr} (Attrs).

% --- SECTION 4 ---
\section{4. Context \& Memory}
\subsection{Hardware Context}
\textbf{PC (Program Counter):} Address of next instruction. \\
\textbf{SP (Stack Pointer):} Top (1st unused loc) of stack. \\
\textbf{FP (Frame Pointer):} Fixed loc in stack frame to access local vars via displacement. \\
\textbf{Register Spilling:} If GPR exhausted, save to RAM temporarily.

\subsection{Calling Convention \& Layout}
Standard protocol for Setup/Teardown of stack frames. 
Stacks typically grow \textbf{upwards} (lowest addr at bottom, highest at top, incrementing SP). \\
\textbf{Memory:} \textbf{Text} (Instrs) $\to$ \textbf{Data} (Globals) $\to$ \textbf{Heap} (Dynamic) $\uparrow$ $\downarrow$ \textbf{Stack} (Func invocations). 

% --- SECTION 5 ---
\section{5. CPU Scheduling}
\textbf{Goal:} Decide who runs and for how long. \\
\textbf{Metrics:}
\begin{itemize}
    \item \textbf{WCET (C):} Worst-Case Execution Time.
    \item \textbf{Deadline (D):} Max time allowed from release to completion.
    \item \textbf{WCRT (R):} Worst-Case Response Time (actual).
\end{itemize}
\textbf{Nonpreemptive:} Task holds CPU till yield/I/O. \\
\textbf{Preemptive:} CPU can be taken by OS anytime. \\
\textbf{Interactive Sched:} Focus on response/predictability. Uses timer interrupts (1-10ms) \& Time Quantums. 

\subsection{RTOS Scheduling Algorithms}
\textbf{Fixed Priority:} Priorities assigned manually, never change.
\begin{itemize}
    \item \textbf{RMS (Rate Monotonic):} Optimal fixed scheme. Shorter Period = Higher Priority.
\end{itemize}
\textbf{Dynamic Priority:} 
\begin{itemize}
    \item \textbf{EDF (Earliest Deadline First):} Closest deadline gets highest priority.
\end{itemize}

\subsection{Schedulability Analysis}
\textbf{Utilization ($U$):} Sum of (C / Period) for all tasks.
\begin{itemize}
    \item $U > 1.0$: Failed (Overloaded).
    \item $U \le$ LL-Bound: Passed (Guaranteed).
    \item $LL < U \le 1.0$: \textbf{Critical Instance Analysis}.
\end{itemize}
\textbf{Critical Instance Analysis:} Worst case scenario is all tasks release at $t=0$. 
\begin{itemize}
    \item Step 1: Calc total WCET = $t$. 
    \item Step 2: Tasks may release during $t$. Add new compute recursively. 
    \item Step 3: Repeat until $t >$ Max Period (fail) or converges (pass). 
\end{itemize}
\textit{Note: Can try RMS even if LL bound fails, use Critical Analysis.}

\subsection{Round Robin \& Priority}
\textbf{Round Robin (RR):} FIFO + Time Quantum. Fast response. Cons: Fails RTOS timing/fragile, no priority. \\
\textbf{RR w/ Interrupts:} Tasks polled, but ISR handles time-critical ints. Cons: Data processing delayed. \\
\textbf{Priority Sched:} Highest priority runs. Preemptive vs Non.

\section*{1. Inter-Process Communication (IPC)}
\begin{itemize}
    \item \textbf{Shared Memory}: Efficient but requires synchronization.
    \begin{itemize}
        \item \textit{POSIX Syscalls}: \texttt{shmget()} (create), \texttt{shmat()} (attach), \texttt{shmdt()} (detach), \texttt{shmctl()} (destroy).
        \item \textit{Master Code}:\\
        \texttt{shmid = shmget(IPC\_PRIVATE, 40,}\\
        \texttt{\quad \quad \quad IPC\_CREAT | 0600);}\\
        \texttt{shm = (int*) shmat(shmid, NULL, 0);}
    \end{itemize}
    \item \textbf{Message Passing}: OS handles memory; portable, easier sync, but inefficient.
    \begin{itemize}
        \item \textit{Naming}: \textbf{Direct} (\texttt{Send(P2, Msg)}) vs. \textbf{Indirect} via Mailbox/Port (\texttt{Send(MB, Msg)}).
        \item \textit{Synchronization}: \textbf{Blocking} (Synchronous) vs. \textbf{Non-Blocking} (Asynchronous).
    \end{itemize}
    \item \textbf{Unix Pipes}: Circular bounded byte buffer. Implicit sync (writers wait if full, readers if empty). Half/Full-duplex.
    \begin{itemize}
        \item \textit{Syscall}: \texttt{pipe(int fd[])}. \texttt{fd[0]} = read end, \texttt{fd[1]} = write end.
        \item \textit{Code}:\\
        \texttt{pipe(fd);}\\
        \texttt{if(fork() \textgreater{} 0) \{}\\
        \texttt{\quad close(fd[0]); write(fd[1], str, len);}\\
        \texttt{\} else \{}\\
        \texttt{\quad close(fd[1]); read(fd[0], buf, len);}\\
        \texttt{\}}
        \item \textit{Redirection}: \texttt{dup()}, \texttt{dup2()}.
    \end{itemize}
    \item \textbf{Unix Signals}: Asynchronous event notification.
    \begin{itemize}
        \item \textit{Code}: \texttt{if (signal(SIGSEGV, myHandler) == SIG\_ERR) \{ ... \}}
    \end{itemize}
\end{itemize}

\section*{2. Memory Abstraction \& Allocation}
\begin{itemize}
    \item \textbf{Base + Limit Registers}: Hardware abstraction. $\text{Actual} = \text{Base} + \text{Adr}$. Must check $\text{Actual} < \text{Limit}$.
    \item \textbf{Contiguous Memory Allocation}:
    \begin{itemize}
        \item \textbf{Fixed-Size Partition}: Fast, easy. Causes \textbf{Internal Fragmentation} (wasted space inside partition).
        \item \textbf{Variable-Size Partition}: Flexible. Causes \textbf{External Fragmentation} (holes between partitions).
        \item \textbf{Algorithms}: \textbf{First-Fit} (first hole large enough), \textbf{Best-Fit} (smallest hole large enough), \textbf{Worst-Fit} (largest hole).
    \end{itemize}
    \item \textbf{Buddy System}: Efficient splitting/coalescing using powers of 2 ($2^k$).
    \begin{itemize}
        \item Blocks $B$ and $C$ are buddies if their $S^{th}$ bit is a complement and leading bits are identical.
        \item Maintains an array of linked lists \texttt{A[0...K]} for free blocks of size $2^J$.
    \end{itemize}
\end{itemize}

\section*{3. Virtual Memory Management}
\begin{itemize}
    \item \textbf{Memory Access Time}: \\
    $T_{access} = (1 - p) \times T_{mem} + p \times T_{page\_fault}$ \\
    (where $p$ = page fault probability).
    \item \textbf{Paging}: Splits logical memory into pages, physical memory into frames. 
    \begin{itemize}
        \item \textit{Page Fault}: Trap to OS when accessing a non-memory resident page.
    \end{itemize}
    \item \textbf{Page Table Structures}:
    \begin{itemize}
        \item \textbf{Direct Paging}: Single table. Huge memory overhead (e.g., 32-bit addr, 4KiB page = 2MiB table).
        \item \textbf{2-Level Paging}: Splits table into a Page Directory + smaller Page Tables. Saves space because empty directory entries mean unallocated page tables.
        \item \textbf{Inverted Page Table}: One table for \textit{all} processes, ordered by physical frame. Entry = \texttt{\textless{}PID, Page\#\textgreater{}}. Huge memory savings, but slow translation (requires search/hashing).
    \end{itemize}
    \item \textbf{Page Replacement Algorithms} (Triggered when physical memory is full):
    \begin{itemize}
        \item \textbf{OPT (Optimal)}: Replace page not used for the longest future time. Unrealizable benchmark.
        \item \textbf{FIFO}: Evict oldest loaded page. Suffers from \textbf{Belady's Anomaly} (more frames = \textit{more} page faults).
        \item \textbf{LRU (Least Recently Used)}: Exploits temporal locality. 
        \begin{itemize}
            \item \textit{Implementations}: \textbf{Counter} (search for smallest time, overflow risk) or \textbf{Stack} (move referenced to top, evict bottom; hard to do in HW).
        \end{itemize}
        \item \textbf{CLOCK (Second-Chance)}: FIFO with a \texttt{reference bit}. If bit=0, replace. If bit=1, set to 0 (give 2nd chance) and move to next.
    \end{itemize}
    \item \textbf{Thrashing \& Working Set}:
    \begin{itemize}
        \item \textbf{Thrashing}: Heavy I/O from constant page faults.
        \item \textbf{Working Set Model}: $W(t, \Delta)$ = active pages in interval $\Delta$. Allocate enough frames for the working set to prevent thrashing.
        \item \textbf{Local vs Global Replacement}: Global allows stealing frames from other processes (can cause cascading thrashing). Local restricts a process to its own frames.
    \end{itemize}
\end{itemize}

\section*{4. Synchronization}
\begin{itemize}
    \item \textbf{Critical Section (CS) Properties}: 
    1. Mutual Exclusion, 2. Progress - if nothing is in critical section, process is granted access, 3. Bounded Wait - after p\_i request entry, exist an upperbound number of times other processes can enter before p\_i, 4. Independence - processes never block each other.
    \item \textbf{Deadlock} = no progress | \textbf{livelock} = not blocked but no progress because deadlock avoidance | \textbf{starvation} - process is blocked forever
    \item \textbf{Hardware Level}: \texttt{TestAndSet Reg, MemLoc}. Atomic instruction.
    \begin{itemize}
        \item \textit{Code}: \texttt{while(TestAndSet(Lock) == 1);}
    \end{itemize}
    \item \textbf{Semaphore}: Integer + waiting list. No busy waiting.
    \begin{itemize}
        \item \texttt{Wait(S)} / \texttt{P()}: If $S \le 0$, block/sleep. Decrement S.
        \item \texttt{Signal(S)} / \texttt{V()}: Increment S. Wake up one sleeping process. Never blocks.
    \end{itemize}
    \item \textbf{Producer-Consumer (Blocking Code)}:
    \begin{itemize}
        \item \textit{Producer}:\\
        \texttt{wait(notFull); wait(mutex);}\\
        \texttt{add\_to\_buffer;}\\
        \texttt{signal(mutex); signal(notEmpty);}
        \item \textit{Consumer}:\\
        \texttt{wait(notEmpty); wait(mutex);}\\
        \texttt{remove\_from\_buffer;}\\
        \texttt{signal(mutex); signal(notFull);}
    \end{itemize}
    \item \textbf{Readers-Writers}: Writer needs exclusive access; readers can share.
    \item \textbf{Pthreads}: \texttt{pthread\_mutex\_lock()}, \texttt{pthread\_cond\_wait()}, \texttt{pthread\_cond\_broadcast()}.
\end{itemize}

\section*{5. File System}
\begin{itemize}
    \item \textbf{File Data Structure \& Access}:
    \begin{itemize}
        \item \textit{Fixed Length Records}: Easy jump. $\text{Offset} = \text{Size} \times (N-1)$.
        \item \textit{Access Methods}: \textbf{Sequential} (read in order) vs \textbf{Random/Direct} (\texttt{read(offset)} or \texttt{seek(offset)}).
    \end{itemize}
    \item \textbf{Directory Structures}:
    \begin{itemize}
        \item \textit{Single-Level} vs \textit{Tree-Structured} (Absolute/Relative paths).
        \item \textit{DAG (Directed Acyclic Graph)}: Allows file sharing.
        \begin{itemize}
            \item \textbf{Hard Link}: Multiple directory pointers to the same disk file. Pros: Low overhead. Cons: Deletion orphans (if owner deletes, link breaks).
            \item \textbf{Symbolic Link}: Special file containing the path. Pros: Simple deletion. Cons: Disk space overhead.
        \end{itemize}
    \end{itemize}
    \item \textbf{Disk Organization}: MBR $\rightarrow$ Partitions $\rightarrow$ [OS Boot Block | Partition Details | Directory Structure | Files Info | File Data].
    \item \textbf{File Block Allocation}:
    \begin{itemize}
        \item \textbf{Contiguous}: Directory stores \texttt{start} \& \texttt{length}. Pros: Fast, simple. Cons: External fragmentation, file size fixed.
        \item \textbf{Linked List}: Block stores data + pointer to next. Directory stores \texttt{start} \& \texttt{end}. Pros: No fragmentation. Cons: Slow random access, pointer overhead.
        \item \textbf{FAT (Linked List V2)}: Moves pointers to a File Allocation Table in RAM. Pros: Fast random access.
        \item \textbf{Indexed}: Directory points to an \textit{Index Block} (array of block addresses). Pros: Fast direct access. Cons: Max file size limited by index block size.
        \item \textbf{Unix Inode (Combined)}: Uses direct blocks, single indirect, double indirect, and triple indirect pointers for massive files.
    \end{itemize}
    \item \textbf{Free Space Management}:
    \begin{itemize}
        \item \textbf{Bitmap}: 1 bit per block (0=occupied, 1=free). Fast manipulations, but takes up RAM.
        \item \textbf{Linked List}: Blocks store pointers to next free block. Low memory overhead, but slow.
    \end{itemize}
    \item \textbf{Disk I/O Scheduling}:
    \begin{itemize}
        \item \textit{Time} = \texttt{Seek Time} (move head to track) + \texttt{Rotational Latency} (wait for sector) + \texttt{Transfer Time}.
        \item \textit{Algorithms}: \textbf{FCFS} (First Come First Serve), \textbf{SSF} (Shortest Seek First), \textbf{SCAN} (Elevator: Bi-directional innermost $\leftrightarrow$ outermost). Focus is on reducing \textit{Seek Time}.
    \end{itemize}
\end{itemize}

\section{Real-time Schedulability}
The iterative equation for task response time $t_i$ is defined as:
\[ t_i = \sum_{k=1}^{n \text{ tasks}} (\text{WCET of } k\text{th task}) \left\lceil \frac{t_{i-1}}{\text{period}} \right\rceil \] 
\[ \text{ where } t_0 = \sum \text{WCET} \]

\subsection{Schedulability Regions (Utilization $U$)}
\begin{itemize}
    \item \textbf{Not Schedulable:} Occurs when $U > 1$.
    \item \textbf{Necessary Condition:} $U \le 1$.
    \item \textbf{May or may not be schedulable:} The region where $n(2^{1/n} - 1) < U \le 1$.
    \item \textbf{Sufficient Condition:} $U \le n(2^{1/n} - 1)$.
    \item \textbf{Schedulable:} Guaranteed when the utilization is within the sufficient condition range.
\end{itemize}

\section{Function Call Conventions}
\subsection{On executing function call}
\begin{itemize}
    \item \textbf{Caller:} Pass arguments with registers and/or stack.
    \item \textbf{Caller:} Save Return PC on stack.
    \item Transfer control from caller to callee.
    \item \textbf{Callee:} Save registers used by callee. Save old Frame Pointer (FP) and Stack Pointer (SP).
    \item \textbf{Callee:} Allocate space for local variables of callee on stack.
    \item \textbf{Callee:} Adjust SP to point to new stack top.
\end{itemize}

\subsection{On returning from function call}
\begin{itemize}
    \item \textbf{Callee:} Restore saved registers, FP, and SP.
    \item Transfer control from callee to caller using saved PC.
    \item \textbf{Caller:} Continues execution in caller.
\end{itemize}

\section{Exception/Interrupt Handler Illustration}
\subsection{Process Flow}
\begin{enumerate}
    \item \textbf{Exception/Interrupt occurs:}
    \begin{itemize}
        \item Control transfers to a handler routine automatically.
    \end{itemize}
    \item \textbf{Return from handler routine:}
    \begin{itemize}
        \item Program execution resumes.
        \item May behave as if nothing happened.
    \end{itemize}
\end{enumerate}

\subsection{Handler Routine Steps}
\begin{enumerate}
    \item Save Register/CPU state.
    \item Perform the handler routine.
    \item Restore Register/CPU state.
    \item Return from interrupt.
\end{enumerate}

\section{Process Creation using \texttt{fork()}}
\begin{verbatim}
int main() {
    pid_t pid = fork();
    if (pid == 0) {// Child process}
    else if (pid > 0) {// Parent process}
}
\end{verbatim}

\begin{verbatim}
int pthread_create(
    pthread_t *tidCreated,
    const pthread_attr_t *threadAttributes,
    void* (*startRoutine) (void*),
    void *argForStartRoutine
);
void pthread_exit( void* exitValue );
int pthread_join( pthread_t threadID, void **status );
\end{verbatim}

% --- ADDED CONTENT START ---

\section{Key Pointers}

\subsection{1. Synchronization \& Interrupts}
\begin{itemize}
    \item \textbf{Disabling Interrupts:} Not a good choice for locking. Breaks quantum-based process switching (timer interrupts fail), misses important wakeup signals from ISRs, and can hang the entire system.
    \item \textbf{Pipes as Binary Semaphores (Locks):}
    \begin{itemize}
        \item \texttt{fd[0]} for read, \texttt{fd[1]} for write used via \textbf{"Token"} concept.
        \item \textbf{1 byte in pipe} = Lock is Available. \textbf{0 bytes} = Lock is Held.
        \item \textbf{Acquire:} \texttt{read()} blocks until a byte is present, ensuring only one thread gets the token (Atomic).
        \item \textbf{Release:} \texttt{write()} returns the byte, unblocking one waiting thread.
    \end{itemize}
\end{itemize}

\subsection{2. Process \& Memory Mgmt}
\begin{itemize}
    \item \textbf{Context Switching:} Saves the state of a running process. Requires: (1) Flushing the TLB (or using ASIDs to prevent unauthorized memory access), (2) Loading the new page table, (3) Setting the PT base register.
    \item \textbf{Preemptive vs. Non-preemptive:} Preemptive OSs (Interactive) can forcibly interrupt processes. Non-preemptive (Real-time) cannot.
    \item \textbf{Memory Partitions:} \textbf{Fixed-Size:} Fast/simple, static, causes \textbf{Internal Frag}. \textbf{Variable-Size:} Flexible, causes \textbf{External Frag}.
    \item \textbf{Segmentation:} Out-of-bounds access is catchable via Segment Limit. A process's \textbf{Heap} does not create a new segment when it grows; the OS simply increases the limit of the existing heap segment.
\end{itemize}

\subsection{3. Virtual Memory \& Paging}
\begin{itemize}
    \item \textbf{Page Faults \& Limits:} Incorrect memory access in paging is \textit{not} inherently catchable by boundary limits unless it hits an "Invalid" (Valid Bit = 0) page.
    \item \textbf{Multi-level Paging:} Split memory so every page table fits \textit{exactly} into one physical page frame.
    \item \textbf{Inverted Page Table:} One global table for the OS. One entry per physical frame (Index = Frame). Matches using \texttt{[PID | p | d]}.
    \item \textbf{Page Replacement Algorithms:} \textbf{OPT} (Benchmark), \textbf{FIFO} (Oldest out, Belady's Anomaly), \textbf{LRU} (Least Recently Used), \textbf{CLOCK} (Circular FIFO, skips reference bit = 1).
    \item \textbf{Working Set Model \& Thrashing:} Used to allocate frames and prevent thrashing. Adjust the window ($L$ or $\Delta$) based on page fault frequency (High freq = $\Delta$ too small; low freq + low CPU = $\Delta$ too large).
\end{itemize}

\subsection{4. fork(), exec(), and CoW}
\begin{itemize}
    \item \textbf{CoW Logic:} \texttt{fork()} initially shares physical frames between Parent and Child, marking them Read-Only ($W=0$).
    \item \textbf{Write Attempt (Trap):} If a child modifies a RAM variable, a Memory Violation occurs. The OS catches this, copies the frame to a new physical location, and sets $W=1$ so the child has a private copy.
    \item \textbf{\texttt{exec()} vs \texttt{write()}:} If the child calls \texttt{exec()}, it discards the parent's memory entirely (no CoW needed). Writing to a file descriptor (\texttt{write()}) does \textit{not} trigger memory CoW unless the memory buffer itself is altered.
\end{itemize}

\subsection{5. File Systems \& I/O}
\begin{itemize}
    \item \textbf{File Descriptors (FD):} Non-negative integers serving as handles for an OS array (0 = stdin, 1 = stdout, 2 = stderr). Using \texttt{open()} gives an FD, saving the OS from expensive disk searches on every read/write.
    \item \textbf{Redirection (\textgreater):} To redirect standard output, the OS closes \texttt{fd=1} and points it to the new file's entry.
    \item \textbf{Inodes:} Store metadata and pointers to disk blocks. 
    \item \textbf{Triply Indirect Pointers:} If a file grows into the triple-indirect range, writing just \textit{1 byte} requires \textbf{4 disk writes} (3 index blocks + 1 data block).
    \item \textbf{Free Space:} Managed by Bitmaps (fast but takes RAM) or Linked Lists.
\end{itemize}

\section{Key Equations}

\subsection{1. Address Mapping \& Offsets}
\begin{itemize}
    \item \textbf{Base + Limit Mapping:} $\text{Actual\_Physical} = \text{Base} + \text{Offset}$ \textit{(Must check: Offset $<$ Limit)}
    \item \textbf{Buddy System Mapping:} $\text{Physical} = \text{Start\_of\_}2^k\text{\_Block} + \text{Offset}$ \textit{(Must check: Offset $< 2^k$)}
    \item \textbf{File Fixed-Length Records:} $\text{Offset} = \text{Record\_Size} \times (N - 1)$
\end{itemize}

\subsection{2. Memory Architecture Calculations}
\begin{itemize}
    \item \textbf{Number of Frames:} $\text{Physical\_Address\_Space} \div \text{Frame\_Size}$
    \item \textbf{Number of Pages:} $\text{Logical\_Address\_Space} \div \text{Page\_Size}$
    \item \textbf{Total Page Table Entries (PTEs):} $\text{Number\_of\_Pages}$
    \item \textbf{Single-Level Page Table Size:} $\text{Number\_of\_Pages} \times \text{PTE\_Size}$
    \item \textbf{Entries per Multi-Level Table:} $\text{Frame\_Size} \div \text{Entry\_Size}$
\end{itemize}

\subsection{3. Performance \& Access Times}
\begin{itemize}
    \item \textbf{Effective Access Time ($T_{access}$):} \\
    $T_{access} = (1 - p) \times T_{mem} + p \times T_{page\_fault}$ \\
    \textit{(where $p$ is probability of page fault)}
    \item \textbf{TLB Miss Time (n-level paging):} \\
    $T_{total} = T_{TLB\_miss} + (\text{Levels} \times T_{table\_access}) + T_{mem\_access}$ \\
    \textit{(Example: 4-level paging = $20 + 100 + 100 + 100 + 100 + 100 = 520$ ns)}
\end{itemize}

% --- ADDED CONTENT END ---

\includegraphics[width=0.5\linewidth]{img/arm.png}
\includegraphics[width=0.5\linewidth]{img/deadlines.png}
\includegraphics[width=0.5\linewidth]{img/dir.png}
\includegraphics[width=0.5\linewidth]{img/file-descriptors.png}
\includegraphics[width=0.5\linewidth]{img/inode.png}
\includegraphics[width=0.5\linewidth]{img/invert-table.png}
\includegraphics[width=0.5\linewidth]{img/memoryframe.png}
\includegraphics[width=0.5\linewidth]{img/os.png}
\includegraphics[width=0.5\linewidth]{img/page-segment-1.png}
\includegraphics[width=0.5\linewidth]{img/page-segment.png}
\includegraphics[width=0.5\linewidth]{img/page.png}
\includegraphics[width=0.5\linewidth]{img/process-table.png}
\includegraphics[width=0.5\linewidth]{img/process.png}
\includegraphics[width=0.5\linewidth]{img/replacement-algo.png}
\includegraphics[width=0.5\linewidth]{img/schedule-sequence.png}
\includegraphics[width=0.5\linewidth]{img/segment.png}
\includegraphics[width=0.5\linewidth]{img/stack.png}
\includegraphics[width=0.5\linewidth]{img/tlb-fault-handler.png}

Multiples of Bytes
\\
1000 kB = kilobyte
\\
1024 KiB = $2^{10}$ bytes  |   MiB = $2^{20}$   |  GiB = $2^{30}$
\\
- Arrival time: point of time at which a process enters the ready queue.
\\
- Waiting time: amount of time spent by a process waiting in the ready queue for getting the CPU.
\\
- Response time: amount of time after which a process gets the CPU for the first time after entering the ready queue.
\\
- execution time or running time: amount of time required by a process for executing on CPU.
\\
- Completion time: point of time at which a process completes its execution on the CPU and takes exit from the system.
\\
- Turn Around Time: total amount of time spent by a process in the system.
\\
too small: may miss pages in current locality
\\
too big: may contain pages from different locality
\\
110101 << 1 = 1101010
\\
W(t,l) = start from t-l to t inclusive

\end{multicols*}
\end{document}
```