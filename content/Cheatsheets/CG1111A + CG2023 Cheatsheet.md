# CG1111A

### Tricks

Complicated circuits? A lot of battery? Weird wires that connect the middle that fucks up calculations? Thevenin Thevenin Thevenin.
A lot of batteries? Node Voltage. Together? Node Voltage + Thevenin

![[Pasted image 20240913205619.png]]
Flip it inside out
![[Pasted image 20240913190916.png]]

![[Pasted image 20240913170834.png]]

![[Pasted image 20240913171307.png]]
Suppose that we have two parallel branches. If we minimise R_B and maximise R_C+R_D, the overall resistance will be around R_B




![[Pasted image 20240910142857.png]]


	![[Pasted image 20240905151141.png|300]]![[Pasted image 20240905151451.png|300]]

![[Pasted image 20240905141139.png|300]]






## VERY IMPORTANT NOTE: $\omega = 2\pi f$ 





# Thevenin
First, always remove the load.

**Calculating the resistance:** 
- Replace battery with short circuits
- Calculate the equivalent resistance seen from the terminals where the load resistor was connected. This may be parallel.

**Calculate the voltage across the load:**
- Current may not flow. Most likely.
- Use node circuit analysis

# Node Circuit

Identify the constant, known voltages.
Slowly add in more unknown voltages as variables. 

Solve for the variables.

**Super node**
A super node can be formed from a branch or even a mini-circuit within the circuit, depending on the current in and out. If the current in and out are the same, we can make the entire thing a super node. 

**Battery**
Batteries act as a 'booster'. In a branch with only a battery, one side will be $V_1$ and the other side to be $V_{1} + battery$



# Capacitors and Inductors
![[images 4.png]]

![[Pasted image 20240913200905.png]]


### Capacitors
Unit of capacitance is Farad (F), defined as amount of charge stored per volt
### $C=\frac{Q}{V}$

![[Pasted image 20240905232810.png|300]]
![[Pasted image 20240905232914.png|200]]
![[Pasted image 20240905232927.png|200]]

**Energy stored in capacitor = $W=\frac{1}{2}CV^2$**
The stored energy can be expressed in terms of the work done in moving the charges to set up the field

![[Pasted image 20240905233234.png|300]]

**A capacitor's transient voltage in a series RC circuit is**

![[Pasted image 20240905233313.png|400]]




### Inductors
**An inductor's transient current in a series RL circuit is**

![[Pasted image 20240905233446.png|300]]
![[Pasted image 20240905233507.png|300]]

![[Pasted image 20240905233521.png|300]]
![[Pasted image 20240905233532.png|300]]

Energy stored is inductor:
$W=\frac{1}{2}LI^2$


**Steady state rules**
At steady state:
a capacitor behaves like an open-circuit
an inductor behaves like a short circuit

Cannot change instaneously:
Voltage for capacitor cannot changed instantly
Current for capacitor cannot change instantly
# AC and Phasors
**All signals must have the same frequency**
**All must be converted to sine or cosine (consistent) before taking phase angle**

**Sinusoidal**
Sinusoidal waveforms are in the form
$v(t)=V_{m}\cos(wt+\theta)$
Take note that negative will shift the graph FORWARD horizontally. 
![[Pasted image 20240831210646.png|150]]

**RMS**
RMS is defined as the equivalent values of DC voltage and current that would result in the same average power dissipation in a resistive load.
$X_{RMS}= \sqrt{ \frac{1}{T} \int^T_{0}x^2(t)dt }$
In layman terms. We have a $x(t)$ graph. We square it. We find the area under the graph for one period. We divide it by the period. Then square root the entire thing.
For sinusoidal wave, $V_{RMS}=\frac{V_{peak}}{\sqrt{ 2 }}$



**Impedance (resistance) of inductor is**
$\frac{V}{I}=\frac{wLI_{m} \angle 90 \degree }{I_{m}\angle 0}=wL \angle 90 \degree=jwL$

**Impedance (resistance) of capacitor is**
$=-\frac{j}{wL}$


**Impedance (resistance) of resistor is**
$R$


Converting to $\cos$
![[Pasted image 20240905233845.png|300]]



# DC Motors
![[Pasted image 20240916233027.png|400]]
![[Pasted image 20240916233036.png|400]]
![[Pasted image 20240916233045.png|400]]



# CG2023

```latex
\documentclass[a4paper, landscape]{article}
\usepackage[top=0.6cm, bottom=0.2cm, left=0.2cm, right=0.2cm]{geometry}
\input{src/default.tex}

% Global settings
\def\subject{}
\def\semester{}
\def\author{}
\def\cols{4}

\pagestyle{empty}

\begin{document}
\cheatsheet{
    \scriptsize
    \setlength{\parindent}{0pt}
    \setlength{\parskip}{0pt}
    \setlength{\abovedisplayskip}{1pt}
    \setlength{\belowdisplayskip}{1pt}
    \setlength{\mathsurround}{0pt}

    \noindent\textbf{1. Fourier series in trigonometric form:}\\[1pt]
    \mathbox{
        x_p(t) = a_0 + 2 \cdot \sum_{k=1}^{\infty} \left( a_k \cos\left(\frac{2\pi k}{T_p}t\right) + b_k \sin\left(\frac{2\pi k}{T_p}t\right) \right)
    }
    where $a_k = (c_{-k} + c_k)/2$ and $b_k = (c_{-k} - c_k)/2$

    \vspace{2pt}\noindent\textbf{2. Spectral properties of a real signal:}\\[1pt]
    1) $x(t)$ is \underline{real}, we have $X^*(f) = X(-f)$, which leads to:\\
    $|X(f)| = |X(-f)|$ and $\angle X(f) = -\angle X(-f)$\\
    2) $x(t)$ is \underline{real and even}, we have $X(f)$ is also real and even:\\
    $X^*(f) = X(f)$ and $X(f) = X(-f)$\\
    3) $x(t)$ is \underline{real and odd}, we have $X(f)$ is imaginary and odd:\\
    $X^*(f) = -X(f)$ and $X(f) = -X(-f)$

    \vspace{2pt}\noindent\textbf{3. Properties of the Dirac-$\delta$ function:}\\[1pt]
    4) \underline{Symmetry}: $\delta(t) = \delta(-t)$\\
    5) \underline{Sampling}: $x(t)\delta(t-\lambda) = x(\lambda)\delta(t-\lambda)$\\
    6) \underline{Sifting}: $\int_{-\infty}^{\infty} x(t)\delta(t-\lambda)dt = x(\lambda)$\\
    7) \underline{Replication}: $x(t) * \delta(t-\xi) = x(t-\xi)$\\
    8) \underline{White spectrum}: $\mathcal{F}\{\delta(t)\} = \mathcal{F}^{-1}\{\delta(t)\} = 1$

    \vspace{2pt}\noindent\textbf{4. Use Fourier transform on periodic signals:}\\[1pt]
    \mathbox{
        X_p(f) = \sum_{k=-\infty}^{\infty} c_k \mathcal{F}\{e^{j 2\pi k f_p t}\}
    }
    \mathbox{
     = 
        \sum_{k=-\infty}^{\infty} c_k \cdot \delta(f - k f_p)
    }


    \vspace{2pt}\noindent\textbf{5. Fourier transform of the generating function:}\\[1pt]
    $x_p(t) = g(t) * \sum_n \delta(t-nT_p) = \sum_n g(t-nT_p)$\\
    $\rightleftharpoons X_p(f) = \sum_k f_p G(k f_p)\delta(f - k f_p)$ \quad thus $c_k = f_p G(k f_p)$

    \vspace{2pt}\noindent\textbf{6. DC value (or called average value):}\\[1pt]
    9) Original definition: $c_0 = \lim_{\tau \to \infty} \frac{1}{\tau} \int_{-\tau/2}^{\tau/2} x(t) dt = \frac{X(0)}{\infty}$.\\
    10) For periodic signal: $c_0 = \frac{1}{T_p} \int_{-0.5T_p}^{0.5T_p} x(t) dt$.\\
    11) In the frequency domain: $\frac{X(0)}{\infty} = \frac{\int_{-\infty}^{\infty} x(t) dt}{\infty} = c_0$.\\
    12) The DC value of a signal is $K$ if $X(f)$ contains a $K\delta(f)$ term.\\
    13) All bounded \underline{energy} signals have \underline{zero DC value}.\\
    14) All bounded \underline{periodic} signals are \underline{power} signals.

    \vspace{2pt}\noindent\textbf{7. Energy \& energy spectral density:}\\[1pt]
    \mathbox{
        E = \int_{-\infty}^{\infty} |x(t)|^2 dt = \int_{-\infty}^{\infty} |X(f)|^2 df = \int_{-\infty}^{\infty} E_x(f) df
    }

    \vspace{2pt}\noindent\textbf{8. Power \& power spectral density:}\\[1pt]
    $P = \lim_{T \to \infty} \frac{1}{2T} \int_{-T}^{T} |x(t)|^2 dt = \int_{-\infty}^{\infty} \lim_{T \to \infty} \frac{1}{2T} |X_T(f)|^2 df = \int_{-\infty}^{\infty} P_x(f) df$\\
    Furthermore, for periodic signals, we have:\\
    $P_x(f) = \sum_k |c_k|^2 \delta(f - k f_p)$ \quad and \quad $P = \sum_k |c_k|^2$

    \\ $c_k$ is fourier series coef

    \vspace{2pt}\noindent\textbf{9. Magnitude \& phase of a complex number:}\\[1pt]
    15) Any complex number can be expressed as $X = a + jb = |X| \cdot e^{j \angle X}$,\\
    whose magnitude is $|X| = \sqrt{X \cdot X^*} = \sqrt{a^2 + b^2}$, and whose phase can be written as $\tan \angle X = \frac{\text{Im}\{X\}}{\text{Re}\{X\}} = \frac{b}{a}$.\\
    16) In the form of $\frac{1}{a+jb}$, its magnitude is $\frac{1}{\sqrt{a^2+b^2}}$, and its phase is $-\tan^{-1}(\frac{b}{a})$.

    \vspace{2pt}\noindent\textbf{10. Properties of an LTI (linear time-invariant) system:}\\[1pt]
    17) Impulse response (in t-domain): $y(t) = x(t) * h(t)$.\\
    18) Frequency response (in f-domain): $Y(f) = X(f) \cdot H(f)$.\\
    19) With transfer function $\tilde{H}(j\omega)$, if input is $x(t) = A \cos(\omega t + \varphi)$, we have output $y(t) = A |\tilde{H}(j\omega)| \cos(\omega t + \varphi + \angle \tilde{H}(j\omega))$.

    \vspace{2pt}\noindent\textbf{11. Stability of an LTI system with poles and/or zeros:}\\[1pt]
    20) \underline{BIBO stable}: All poles lie on the left-half s-plane, i.e. $\text{Re}[s] < 0$.\\
    21) \underline{Marginally stable}: One or more poles lie on the $j\omega$ axis, the rest on the left-half s-plane.\\
    22) \underline{Unstable}: One or more poles on the right-half s-plane, or one or more repeated poles on the $j\omega$ axis.

    \vspace{2pt}\noindent\textbf{12. LTI Systems \& Stability}\\[1pt]
    \textbf{Properties:} $y(t)=x(t)*h(t) \leftrightarrow Y(f)=X(f) \cdot H(f)$.\\
    \textbf{Steady-State Sinusoidal:} If input $x(t)=A\cos(\omega_0 t+\phi)$, output $y(t)=A|\tilde{H}(j\omega_0)|\cos(\omega_0 t+\phi+\angle\tilde{H}(j\omega_0))$. Similarly, $Ae^{j(\omega_0 t+\psi)} \to A\tilde{H}(j\omega_0)e^{j(\omega_0 t+\psi)}$.\\
    \textbf{Transfer Fn:} $\tilde{H}(s) = \frac{\sum_{m=0}^M b_m s^m}{\sum_{n=0}^N a_n s^n} = K \frac{\prod (s/z_m + 1)}{\prod (s/p_n + 1)}$. Roots $p_n$ are poles, $z_m$ are zeros. Pole-zero excess = $N-M$. Zeros affect transience/shape, NOT stability.\\
    \textbf{Stability:} Depends entirely on poles Re($p$).\\
    23) \underline{BIBO}: All Re($p$)$<0$ (Left half s-plane).\\
    24) \underline{Marginal}: Re($p$)$\leq 0$, poles on imaginary axis Re($p$)$=0$ are distinct. None on right half.\\
    25) \underline{Unstable}: Any Re($p$)$>0$ (Right half) OR repeated poles on Re($p$)$=0$.\\
    \textbf{Validity of $\tilde{H}(j\omega)$:} $\tilde{H}(j\omega)|_{\omega=2\pi f} = H(f)$ everywhere if BIBO stable. If marginally stable, valid everywhere EXCEPT at the pole frequencies $\omega_o$. (e.g., $1/s$ invalid at $\omega=0$, $\sin(\omega_ot)u(t)$ invalid at $\omega=\pm\omega_o$).\\
    \textbf{DC Gain:} $\tilde{H}(0)$. Integrators $\to \infty$, Diff $\to 0$. Don't express in dB.

    \vspace{2pt}\noindent\textbf{13. Filters \& Sampling}\\[1pt]
    Total phase is (Phase of Numerator) - (Phase of Denominator). Two arctangent functions.

    \textbf{Ideal LPF:} $H(f)=K$ for $|f|<f_c$, else $0$. $H(f)=A\text{rect}(\frac{f}{2B}) \leftrightarrow h(t)=2AB\text{sinc}(2Bt)$. Cutoff=BW=$B$.\\
    \textbf{Ideal HPF:} $H(f)=K$ for $|f|>f_c$, else $0$.\\
    \textbf{Ideal BPF:} $H(f)=K$ for $f_1<|f|<f_2$, else $0$. $H(f)=A[\text{rect}(\frac{f+f_o}{B})+\text{rect}(\frac{f-f_o}{B})] \leftrightarrow h(t)=2AB\text{sinc}(Bt)\cos(2\pi f_o t)$. Center $f_o=0.5(f_u+f_l)$. BW=$B=f_u-f_l$.\\
    \textbf{Ideal Notch:} $H(f)=0$ for $f_1<|f|<f_2$, else $K$.\\
    \begin{minipage}{0.48\linewidth}
    \textbf{Ideal LPF}\\
    \includegraphics[width=\linewidth]{img/ideal_lpf.png}
    \end{minipage}
    \hfill
    \begin{minipage}{0.48\linewidth}
    \textbf{Ideal BPF}\\
    \includegraphics[width=\linewidth]{img/ideal_bpf.png}
    \end{minipage}\\
    \textbf{Reconstruction:} Perfect signal requires gain $A = T_s = 1/f_s$. Ideal $B$ is Nyquist Freq $f_s/2$. Division-by-2 needed for perfectly-overlapping BPF images.\\
    \textbf{Sampling:} Nyquist rate $f_s \geq 2f_c + B$.\\
    26) Perfectly-overlapping images: $f_s=2f_c/k$, $k=1,2,\dots,\lfloor 2f_c/B \rfloor$.\\
    27) Un-aliased: $\frac{2f_c+B}{k+1} \leq f_s \leq \frac{2f_c-B}{k}$, $k=1,2,\dots,\lfloor \frac{2f_c-B}{2B} \rfloor$.

    \vspace{2pt}\noindent\textbf{14. First \& Second Order Systems}\\[1pt]
    \textbf{1st Order DE:} $T\dot{y}+y=Kx \to \tilde{H}(s) = \frac{K}{Ts+1}$. Pole at $-1/T$.\\
    Impulse $h(t)=\frac{K}{T}e^{-t/T}u(t)$. Step $o(t)=K(1-e^{-t/T})u(t)$.\\
    \begin{minipage}{0.48\linewidth}
    \textbf{1st Order Impulse}\\
    \includegraphics[width=\linewidth]{img/first-order-unit.png}
    \end{minipage}
    \hfill
    \begin{minipage}{0.48\linewidth}
    \textbf{1st Order Step}\\
    \includegraphics[width=\linewidth]{img/first-order-step.png}
    \end{minipage}\\
    
    
    \textbf{2nd Order DE:} $\ddot{y}+2\zeta\omega_n\dot{y}+\omega_n^2 y=K\omega_n^2 x \to \tilde{H}(s) = \frac{K\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$. Poles: $s_{1,2}=-\omega_n\zeta \pm \omega_n\sqrt{\zeta^2-1}$.\\
    28) \underline{Overdamped ($\zeta>1$)}: Real/distinct poles.\\
    $h(t)=[K_1 e^{-p_1 t} + K_2 e^{-p_2 t}]u(t)$\\
    $o(t)=K[1-\frac{K_1}{p_1}e^{-p_1 t}-\frac{K_2}{p_2}e^{-p_2 t}]u(t)$\\
    $s_{1,2} = -\omega_n\zeta \pm \omega_n(\zeta^2 - 1)^{1/2}$\\
    \includegraphics[height=35mm]{img/second-order-overdamp.png}
    \includegraphics[height=35mm]{img/second-order-critical-damp.png}
    \\
    29) \underline{Critically damped ($\zeta=1$)}: Real/repeated poles.\\
    $h(t)=K\omega_n^2 t e^{-\omega_n t}u(t)$\\
    $o(t)=K[1-e^{-\omega_n t}-\omega_n t e^{-\omega_n t}]u(t)$\\
    $s_{1,2} = -\omega_n$\\
    \includegraphics[height=35mm]{img/second-order-critical-damp.png}
    \includegraphics[height=35mm]{img/second-order-underdamp.png}
    \\
    30) \underline{Underdamped ($0<\zeta<1$)}: Complex pair.\\
    $h(t)=K\frac{\omega_n^2}{\omega_d}e^{-\sigma t}\sin(\omega_d t)u(t)$\\
    $o(t)=K[1-e^{-\sigma t}(\cos(\omega_d t)+\frac{\sigma}{\omega_d}\sin(\omega_d t))]u(t)$\\
    (decay $\sigma=\omega_n\zeta$, natural $\omega_d=\omega_n\sqrt{1-\zeta^2}$).\\
    $s_{1,2} = -\omega_n\zeta \pm j\omega_n(1 - \zeta^2)^{1/2}$\\
    \\
    31) \underline{Undamped ($\zeta=0$)}: Imaginary pair $\pm j\omega_n$.\\
    $s_{1,2} = \pm j\omega_n$\\
    \includegraphics[height=35mm]{img/second-order-undamp.png}
    \\
    \textbf{Resonance:} Occurs if $\zeta < 1/\sqrt{2}$. $\omega_r$ must be real. Resonant Freq $\omega_r=\omega_n\sqrt{1-2\zeta^2}$, Peak=$K/(2\zeta\sqrt{1-\zeta^2})$.\\

    \includegraphics[width=\linewidth]{img/resonance.png}
    \\

    \vspace{2pt}\noindent\textbf{15. Bode Plots \& Asymptotics}\\[1pt]

     \includegraphics[width=\linewidth]{img/bode plot.png}
  \includegraphics[width=\linewidth]{img/asympto-bode.png}
   \includegraphics[width=\linewidth]{img/step1-bode.png}
    \includegraphics[width=\linewidth]{img/step2-bode.png}
        

    \vspace{2pt}\noindent\textbf{16. DC gain of a $N^{th}$-order LTI system:}\\[1pt]
    32) If there are more differentiators, DC gain is $\tilde{H}(0) = 0$.\\
    33) If there are more integrators, DC gain is $\tilde{H}(0) = \infty$.\\
    34) \textit{DC gain should not be expressed in dB, although dB is used for gain.}

    

    \vspace{2pt}\noindent\textbf{19. Resonance in $2^{nd}$-order systems}\\[1pt]
    Given $\tilde{H}(s) = \frac{K \omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2}$, resonance happens when $\zeta < 1/\sqrt{2}$.\\
    35) \underline{Resonant frequency}: $\omega_r = \omega_n \sqrt{1 - 2\zeta^2}$\\
    36) \underline{Resonant peak}: $M_r = |\tilde{H}(j\omega_r)| = \frac{K}{2\zeta\sqrt{1-\zeta^2}}$

    \vspace{2pt}\noindent\textbf{20. Sampling below Nyquist rate for bandpass signals}\\[1pt]
    37) \underline{Perfectly-overlapping images}: $f_s = \frac{2f_c}{k}$, where $k = 1, 2, \dots , \lfloor \frac{2f_c}{B} \rfloor$.\\
    38) \underline{Un-aliased spectral images}: $\frac{2f_c + B}{k+1} \leq f_s \leq \frac{2f_c - B}{k}$, $k = 1, 2, \dots , \lfloor \frac{2f_c - B}{2B} \rfloor$.\\
    39) The above two are only possible when $f_c \geq B$.\\
    40) \underline{Notice}: for perfectly-overlapping images, a \underline{\textbf{division-by-2}} is necessary on the reconstruction filter.

    \vspace{2pt}\noindent\textbf{21. Drawing of straight-line Bode plots:}\\[1pt]
    41) Constant $\tilde{H}(s) = K_{dc}$:\\
    \includegraphics[width=\linewidth]{img/bode_constant.png}

    42) L cascaded integrators with combined gain $\tilde{H}(s) = K_i / s^L$:\\
    \includegraphics[width=\linewidth]{img/bode_integrators.png}

    43) L cascaded differentiators with combined gain $\tilde{H}(s) = K_d \cdot s^L$:\\
    \includegraphics[width=\linewidth]{img/bode_differentiators.png}

    44) Pole factor $\tilde{H}(s) = \frac{1}{s/p_n + 1}$ with $\tilde{H}(0) = 1$:\\
    \includegraphics[width=\linewidth]{img/bode_pole.png}

    45) Zero factor $\tilde{H}(s) = \frac{s}{z_m} + 1$ with $\tilde{H}(0) = 1$:\\
    \includegraphics[width=\linewidth]{img/bode_zero.png}

    46) $2^{nd}$-order factor $\tilde{H}(s) = \frac{\omega_n^2}{s^2 + 2\zeta \omega_n s + \omega_n^2}$ with $\tilde{H}(0) = 1$:\\
    a) When $\zeta > 1$ (\textbf{over-damped}), treat as two cascaded pole factors;\\
    b) When $\zeta = 1$ (\textbf{critical-damped}), treat as two repeated pole factors;\\
    c) When $\zeta < 1$ (\textbf{under-damped}), approximate as $\zeta = 1$.\\
    For $2^{nd}$ and $3^{rd}$ case, draw the straight-line Bode plot as follows:\\
    \includegraphics[width=\linewidth]{img/bode_second_order.png}

    The rule states that the phase shift caused by a pole or zero is approximated as a straight sloping line that:
    \\ Starts exactly **one decade before** the corner frequency. /10
    \\ Ends exactly **one decade after** the corner frequency. x10

    \vspace{2mm}
    \includegraphics[width=\linewidth]{img/validity.png}
    For checking validity of $H(jw)|_{w=2\pi f}=H(f)$

    \\
    \vspace{5mm}
    
    \textbf{Transfer Function $\rightarrow$ Bode Plot (Sketching)}

    \textbf{Standardize:} Factor TF to isolate $K$, origin terms ($s$, $1/s$), and corner frequencies $(1 + s/\omega_c)$. 
    \textbf{Start (Low-Freq):} 
    \begin{itemize}
        \item Initial Slope $= [\# \text{integrators} - \# \text{differentiators}] \times (-20 \text{ dB/dec})$.
        \item Initial Phase $= [\# \text{integrators} - \# \text{differentiators}] \times (-90^\circ)$.
    \end{itemize}
    \textbf{Navigate Corners ($\omega_c$):} Change magnitude slope at each corner.
    \begin{itemize}
        \item Hit a zero: Slope bends UP by $+20L \text{ dB/dec}$ ($L=$ multiplicity).
        \item Hit a pole: Slope bends DOWN by $-20L \text{ dB/dec}$.
    \end{itemize}
    textbf{Verify End (High-Freq):} Ensure final asymptotes match total system counts.
    \begin{itemize}
        \item Final Slope $= [\# \text{total poles} - \# \text{total zeros}] \times (-20 \text{ dB/dec})$.
    \end{itemize}

\vspace{1em}

    \includegraphics[width=\linewidth]{img/translation.png}

    \vspace{1em}
    
    \textbf{
    The product of:
    Even x Even = Even |
    Odd x Odd = Even | 
    Odd x Even = Odd |
    Even/Even = Even |
    Odd/Odd = Even |
    Odd/Even = Odd |
    Even/Odd = Odd
    }
    \\
    Even: $f(-x) = f(x)$ \ \ 
    Odd: $f(-x)=-f(x)$

    \textbf{M\% Power Containment Bandwidth ($B$)}
The $M\%$ power containment bandwidth is defined as the frequency range containing a specific percentage of the signal's total power or energy.
\begin{itemize}
    \item \textbf{General Discrete Case:} $B = K f_p$
    \item $K$ is the smallest positive integer that satisfies:
    \[ \sum_{k=-K}^{K} |c_k|^2 \ge \frac{M}{100} \times P \]
    \item \textbf{Lowpass Signal $x(t)$:} The bandwidth $B$ satisfies:
    \[ \int_{-B}^{B} E_x(f) df = \frac{M}{100} \times E \]
    \item \textbf{Bandpass Signal $x(t)$:} Centered at $f_c$, the bandwidth $B$ satisfies:
    \[ \int_{f_c - 0.5B}^{f_c + 0.5B} E_x(f) df = \frac{M}{100} \times \frac{E}{2} \]
\end{itemize}

\vspace{1em}

\textbf{3dB Bandwidth Definition}
The 3dB bandwidth of a lowpass signal $x(t)$ is defined as the frequency $f_B$ where $|X(f)|$ first drops to $1/\sqrt{2}$ ($\approx -3$ dB) of its peak value.
\begin{itemize}
    \item \textbf{Magnitude Criterion:} $|X(f_B)| = \frac{|X(0)|}{\sqrt{2}} = \frac{|X(0)|}{2^{0.5}}$
    \item \textbf{Energy Spectral Density Criterion:} $\frac{E_x(f_B)}{E_x(0)} = \frac{|X(f_B)|^2}{|X(0)|^2} = \frac{1}{2}$
\end{itemize}

\vspace{1em}

\textbf{1st-Null Bandwidth}
\begin{itemize}
    \item \textbf{Fourier Transform}
    \item \textbf{Null Frequencies:} Occur where the argument of the sinc function is an integer: $f = \pm 4, \pm 8, \pm 12 \dots$ Hz.
    \item \textbf{Result:} The 1st-null bandwidth is $4$ Hz.
\end{itemize}

\vspace{1em}

\vspace{1em}

\textbf{Fourier Duality \& Properties}
\begin{itemize}
    \item \textbf{Periodic in Time $\leftrightarrow$ Discrete in Frequency:} If $x(t)$ has period $T$, spectrum consists of impulses at $k/T$.
    \item \textbf{Discrete in Time $\leftrightarrow$ Periodic in Frequency:} Sampling a signal makes its spectrum periodic.
\end{itemize}

\vspace{1em}

\textbf{Fourier Series Representations}
\begin{itemize}
    \item \textbf{Complex Exponential Fourier Series}
    \begin{itemize}
        \item \textit{Fourier Analysis (Forward):} 
        \[ c_k = \frac{1}{T_p} \int_{t_0}^{t_0+T_p} x_p(t)e^{-j2\pi kt/T_p} dt; \quad \forall \text{ integer } k \]
        \item \textit{Fourier Synthesis (Inverse):}
        \[ x_p(t) = \sum_{k=-\infty}^{\infty} c_k e^{j2\pi kt/T_p} \]
    \end{itemize}
    
    \item \textbf{Trigonometric Fourier Series}
    \begin{itemize}
        \item \textit{Fourier Analysis (Forward):}
        \[ a_k = \frac{1}{T_p} \int_{t_0}^{t_0+T_p} x_p(t)\cos(2\pi kt/T_p) dt; \quad k \ge 0 \]
        \[ b_k = \frac{1}{T_p} \int_{t_0}^{t_0+T_p} x_p(t)\sin(2\pi kt/T_p) dt; \quad k > 0 \]
        \item \textit{Fourier Synthesis (Inverse):}
        \[ x_p(t) = a_0 + 2\sum_{k=1}^{\infty} \left[ a_k \cos(2\pi kt/T_p) + b_k \sin(2\pi kt/T_p) \right] \]
    \end{itemize}
\end{itemize}

\vspace{1em}

\textbf{The DC Component (Zero Frequency)}
\begin{center}
\begin{tabular}{|l|l|}
\hline
\textbf{Perspective} & \textbf{Formula/Coefficient} \\ \hline
\textbf{Physical} & Average value over one period. \\ \hline
\textbf{Complex ($c_k$)} & $c_0$ \\ \hline
\textbf{Trig ($a_n, b_n$)} & $a_0 / 2$ \\ \hline
\textbf{Visual} & The "center line" or vertical offset of the wave. \\ \hline
\end{tabular}
\end{center}

\vspace{1em}

\textbf{Signal Properties and Periodicity}
The inverse transform is used to determine signal characteristics:
\begin{itemize}
    \item \textbf{Real Signals:} Convert complex exponentials to sin/cosine form. If any imaginary components remain, the signal is not purely real.
    \item \textbf{Periodicity:} A signal is periodic if there is a common fundamental frequency (HCF) among all components.
    \begin{itemize}
        \item The ratio of any two frequencies in the signal must be a \textbf{rational number} (a fraction of two integers).
        \item A signal becomes \textbf{completely aperiodic} when the ratio of its frequencies is \textbf{irrational}.
        \item \textbf{Note:} The HCF can be a decimal (e.g., $0.1$ or $0.01$), but it cannot be an irrational constant like $\pi$ or $\sqrt{2}$.
    \end{itemize}
\end{itemize}


\includegraphics[width=\linewidth]{img/sinesignal.png}
\includegraphics[width=\linewidth]{img/cosinesignal.png}
\includegraphics[width=\linewidth]{img/sinusoidsig.png}

\\
Sampling using $f_s$, the magnitude of the sampled signal is SCALED by the sampling frequency. This requires the ideal filter to scale down later. 
}
\end{document}
```