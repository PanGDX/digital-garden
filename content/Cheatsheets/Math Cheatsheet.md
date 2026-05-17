MA1511
MA1512
MA1508E
GEA1000N
CS1231


# Trig Identities
![[half-angle-formula-using-double-angle-formulas-and-semi-perimeter-1628074781.png|400]]![[Pasted image 20240909170137.png|300]]
![[Pasted image 20240909170213.png]]


# Chapter 1
**For MA1511**
$f_{xy}=f_{yx}$


**Tangent plane**
![[Pasted image 20240819160622.png|400]]

**Chain rule**
![[Pasted image 20240818195142.png|400]]


****

**Directional Derivative**
![[Pasted image 20240827225721.png|300]]
Maximum $D_{U}f(a,b) = \frac{|\nabla f(a,b)|^2}{|\nabla f(a,b)|}$ = ${|\nabla f(a,b)|}$


**Test for critical point**
We use determinant D
$D=f_{x x}(a,b)f_{y y}(a,b)-(f_{xy}(a,b))^2$

If $D<0$, it is a saddle point![[Saddle_point 1.svg|200]]
If $D>0$:
		if $f_{x x}(a,b) > 0$, minimum point
		if $f_{y y}(a,b) < 0$, maximum point

**Lagrange multiplier**
Lagrange multiplier method is **a technique for finding a maximum or minimum of a function F(x,y,z) subject to a constraint (also called side condition) of the form G(x,y,z) = 0**.
So note these keywords: 'closest', 'furthest', etc
$$
\begin{matrix}
f_{x}=\lambda g_{x} \\
f_{y}=\lambda g_{y} \\
g(x,y)=0
\end{matrix}
$$

# Chapter 2 


**Simple domain integration**
![[Pasted image 20240818203422.png]]



**Domain change**
![[Pasted image 20240908132020.png|400]]


**Polar integration**
$$\int^{\beta}_{\alpha}\int^{h(\theta)}_{g(\theta)}[f(r\cos \theta,r\sin \theta)r] d\theta$$


# Chapter 3
**Circle in parametric form**
$x=a\cos t, y=a\sin t$



**Derivative of vector-valued functions**
![[Pasted image 20240908132127.png]]
![[Pasted image 20240908132116.png]]
We can use this to derive the tangent line at point P


**Special vector chain rule**
![[Pasted image 20240908132310.png]]




**Integrating vector-valued functions**
![[Pasted image 20240908132356.png|300]]



**Arc length**
![[Pasted image 20240908132420.png|300]]
From this we can derive the case for Cartesian too, using $x=t,y=f(t)$
![[Pasted image 20240908132511.png|200]]


**Line integral**
$$\int f(x,y,z, \dots)\sqrt{ [x'(t)]^{2}+ [y'(t)]^{2}+ [z'(t)]^2 } $$



**Parametric surfaces**
![[Pasted image 20240908132550.png|300]]

To find the normal, simply use $r_u$ and $r_v$ and cross-multiply them




# Chapter 4

**Vector field definition**
![[Pasted image 20240908132722.png]]
Unlike normal vectors, a vector field DOES rely on the initial position

An example of this is the gradient field.


**Line integral of vector fields**
This is known as work done. We can consider the vector field F to represent a changing force.
![[Pasted image 20240908132958.png|200]]
We can calculate this work done using:
![[Pasted image 20240908133013.png|300]]

### MOST IMPORTANT EQUATION 
![[Pasted image 20240908133100.png|350]]


**Conservative vector fields**
![[Pasted image 20240908133213.png|400]]
TLDR: Vector field F is conservative when $\vec F = \nabla f$ and $f$ exists. 
This means that: For $\vec F = P(x,y)\vec i + Q(x,y)\vec j$, $f_x=P(x,y)$ and $f_y=Q(x,y)$


**Conservative vector fields are path independent**
Work done =$f(x_1) - f(x_2)$ for conservative fields




**Test for a conservative field**

![[Pasted image 20240908134106.png|400]]





**Green's Theorem**

**Note : Green's theorem applies only with two-dimensional vector fields**
Green's Theorem is useful when finding the area bounded by several curves. Instead of calculating one by one,![[Pasted image 20240824154502.png|400]]
We simply calculate by using Green's Theorem

Positively orientated: single counter-clockwise traversal
Simple: No intersection
Closed: closed

![[Pasted image 20240908134236.png|400]]

**Curl**
Just remember using cross-product
![[Pasted image 20240908134444.png|300]] = ![[Pasted image 20240908134458.png|300]]

**Divergence**
Just remember using dot product
![[Pasted image 20240908134526.png|300]] = ![[Pasted image 20240908134531.png|300]]
# Chapter 5

### Arithmetic Sequences and Sum

#### $$a_{n} = a_{0}+(n-1)d,n \in R^+$$
#### $$S_n=\frac{n}2{(2a+(n-1d))}=\frac n 2 (a_1+a_n)$$

### Geometric Sequences

**Geometric Sequence**
#### $$g_{n}=g_{n}(r)^{n-1} $$
**Geometric Series**
#### $$S_n=g_1(\frac{1-r^n}{1-r})$$
**Infinite sum**
#### $S_n=\frac{g_1}{1-r}$





**Limits laws**

![[Pasted image 20240825101603.png|400]]

![[Pasted image 20240908135106.png|350]]


**Limit tricks**
If both the nominator and the denominator are infinite, divide by the largest power of n throughout







**Unique series**
$$\sum^n_{k=1}k=\frac{1}{2}n(n+1)$$
$$\sum^n_{k=1}k^2=\frac{n(n+1)(2n+1)}{6}$$



**nth Term Test**
$n$ approaches infinity, this means that the sequence is divergent.
However, if the sequence does not diverge, this does not mean it converges too. It can bounce around 1 and 2 forever, for example.


**p-test**
Only used for this form $\frac{1}{k^p}$
![[Pasted image 20240825102543.png|300]]


**Power series and root and ratio tests**
![[Pasted image 20240825104437.png|400]]


![[Pasted image 20240908135517.png|400]]

The key here is the < and > 1. This exist because if < 1, each additional term multiplied together is smaller and smaller, eventually converging. 
If there is only one point of convergence, the radius of convergence is infinite.
If there is no points, then radius is zero. 




![[maclaurin-expansion-table.png]]
**Final Radius of Convergence**: Once you have the radii of convergence for the different parts, the overall radius of convergence of the series is determined by taking the **minimum** of the radii of convergence of the individual parts. This is because the series will only converge where all parts converge.











# Question(able)

![[Pasted image 20240909170843.png]]


### Tricks
Partial fraction trick: Cover Up Method
![[1_r-IgiBcBrK3jTn01koJpCQ.png|400]]
To calculate $R_3$, use $x=3$ and substitute into the equation while excluding $x-3$

### Definitions and Equations



##### Separable Differential Equation
$$g(y)\frac{dy}{dx}=f(x)$$
##### Integration by parts
$$\int uv \ dx= u\int v\ dx - \int u'(\int v \ dx)\ dx$$
##### Integrating factors
$$\frac{dy}{dx} + f(x)y=q(x)$$
$$u=e^{\int f(x)\ dx}$$
$$(uy)' = uq$$
##### Bernoulli differential equation
$$y'+p(x)y=q(x)y^n$$
Substitute $v=y^{1-n}$ into the equation
Becomes
$$v'+v(1-n)p(x)=q(x)(1-n)$$
Proceed to solve using method of integrating factors

##### Directional/Slope Field
![[Pasted image 20241026105216.png|200]]
##### Radioactive Decay
$$\frac{dN}{dt}=-kN$$
$k$ is the decay constant
$k=\frac{\ln(2)}{t_{\frac{1}{2}}}$ where $t_{\frac{1}{2}}$ is the half life

![[Pasted image 20241013165033.png|300]]

![[halflif5.png|300]]
##### Newton's Equations


Newton's Second Law of Motion:  $F=ma$
Newton's Law of Cooling: $\frac{dy}{dt}=k(y-T_{ambient})$
Newton's Law of Cooling Solution: $y=(y_0-T_{amb})e^{-kt}+T_{amb}$

##### Malthusian model
$\frac{dy}{dt}=ky$
##### Verhulst model/Logistic Growth
$$\frac{dy}{dt}= ky\left( 1-\frac{y}{c} \right) $$
Where $k$ is a constant and $c$ is the carrying capacity

Solution:
$$y(t)=\frac{c}{1+Ae^{-kt}}$$
Substitute $y_0$ initially/other values to find $A$
##### Verhulst model with harvest

##### Finding General Solutions for Linear Homogeneous Differential Equations of nth Degree
1. Convert the equation into a characteristic equation by substituting $y(x)=e^{\lambda x}$
		For example:
$$y^4-4y'''+6y''-4y'+y=0$$
		becomes (after all $e^{\lambda x}$ terms cancel out)
$$m^4-4m^3+6m^2-4m+0=0$$


2. Solve for $m$
3. There are four possibilities
	1. $m$ are real and distinct
		- Solution: $e^{mx}$
	2. $m$ are real and repeating
		- How many times $m$ is repeated = Multiplicity $r$
		- Solution: $e^{mx}, xe^{mx}, x^2e^{mx},...x^{r-1}e^{mx}$
	3. $m$ are complex and complementary
		- For $m=e^{(\alpha+i\beta)x}$
		- Solution: $e^{\alpha x}\cos \beta x$, $e^{\alpha x}\sin \beta x$
	4. $m$ are complex, complementary and repeating
		- How many times $m$ is repeated = Multiplicity $r$
		- Solution: 
			- $e^{\alpha x}\cos \beta x$, $e^{\alpha x}\sin \beta x$
			- $xe^{\alpha x}\cos \beta x$, $xe^{\alpha x}\sin \beta x$
			- ...
			- $x^{r-1}e^{\alpha x}\cos \beta x$, $x^{r-1}e^{\alpha x}\sin \beta x$
4. Put it all together using Superposition Principle
		For linear homogeneous differential equations, any combination of solutions is also a solution
		$y(x)=c_1y_1(x)+c_2y_2(x)+...c_ny_n(x)$

##### Method of Undetermined Coefficient (finding particular solution)
Guess a solution based off the form of the particular solution $f(x)$
If the term of the guess solution is already in the general solution (usually $e^{kx}$), multiply by $x$ until it is not.

![[maxresdefault 3.jpg|400]]

##### Variation of parameters (finding particular solution)
Suppose the particular solution is $f(x)$
The homogeneous solution is 
$$y(x)=C_1y_{1(x)}+C_2y_2(x)$$
For this method, we change the constants to be functions of x
$$y(x)=u(x)y_{1(x)}+v(x)y_2(x)$$
Functions are:
$$u(x)=-\int \frac{y_2f(x)}{y_1y_2'-y'_1y_{2}} \ dx$$
$$v(x)=\int \frac{y_1f(x)}{y_1y_2'-y'_1y_{2}} \ dx $$



##### Simple Harmonic Motion (SHM)
A particle is said to be in simple harmonic motion if its acceleration is directly proportional to its displacement:
$\frac{d^2x}{dt^2}=-w^2x$   where $w$ is the angular frequency of the oscillation

Solution: 
Characteristic equation: $$\lambda^2=-w^2$$
$$\lambda=\pm wi$$
$$x(t)=A\cos wt+B\sin wt=R\cos(wt-\psi)$$
Where $R=\sqrt{A^2+B^2}$ and $\psi=\tan(\frac{B}{A})$
It can also be expressed using $\sin$ but using a different $\psi$

##### SHM with damping
$\ddot x=-w^{2}x - 2\gamma \dot x$
Solving for the characteristic equation $m^{2}+2\gamma m+w^2=0$
We get $m= \gamma \pm \sqrt{\gamma ^{2}- w^2}$
Using the discriminant: $D=\gamma ^{2}-m^2$, we determine the type of damping

**Underdamped: D<0**
For $m=\alpha+\beta i$
$x(t)=c_1e^{\alpha t}\cos\beta t+c_{2}e^{\alpha t}\sin\beta t$
**Critically damped: D=0**
$x(t)=c_1e^{m t}+c_{2}te^{mt}$
**Overdamped: D>0**
$x(t)=c_1e^{m_1 t}+c_{2}e^{m_2 t}$
##### SHM with Resonance
$\ddot x=-w^{2}x+F\cos\psi t$
Resonance occurs when driving force = angular frequency, ie $\psi = w$


Use $Ce^{iwt}$ instead of $A\cos wt+B\sin wt$ because it simplifies the working. To do this, we simply use $Re(x)$ to only consider the real elements but do the workings with imaginary numbers too.



## Laplace Transforms
Defined by: 
$$L(f(t))=F(s)=\lim \int^h_0f(t)e^{-st}dt$$
$$f(t)=L^{-1}[F(s)]$$
We use the $s$ in the integral as a constant
**It possesses the properties**
- Linearity
$$L[af(t)+bg(t)]=aL[f(t)]+bL[g(t)]$$
- First Shifting Theorem
$$L[e^{at}\times f(t)]=F(s-a)$$
- Derivatives
$$L[f^{(n)}(t)]=s^nL[f(t)]+s^{n-1}f(0)+s^{n-2}f'(0)+...+sf^{(n-2)}(0)+f^{(n-1)}(0)$$
		How to remember: The power add up to $n-1$
- Differentiation Property
$$L[t^nf(t)]=(-1)^nF^{(n)}(s)$$


**Unit Step and Unit Impulse**
- Unit Step function
$$
u(t-c) = \begin{cases} 
      0, & t<c \\
      1, & t>c
   \end{cases}
$$
- Unit Impulse Function
	- The area it 'covers' sums up to one
$$
f(t) = \begin{cases} 
      \frac{1}{\varepsilon}, & 0<t<\varepsilon \\
      0, & t>\varepsilon
   \end{cases}
$$

- Unit Step Laplace Transform
$$L(u(t-c))=\frac{e^{-cs}}{s}$$
- Unit Impulse Function
$$L[\delta (t-c)]=e^{-cs}$$
- Second Shifting Theorem
$$L[f(t-c)u(t-c)]=e^{-sc}F(s), \ \ F(s)=L[f(t)]$$
- Converting a Piece-Wise function to a bunch of unit step functions
We can rewrite $f(t)$ by taking the products of the function’s values with the corresponding difference of unit step functions:
$$
f(t) = \begin{cases} 
      2, & 0 < t < 1, \\
      \frac{t^2}{2}, & 1 < t < \frac{\pi}{2}, \\
      \cos t, & t > \frac{\pi}{2}.
   \end{cases}
$$
Into
$$f(t) = 2 \left(1 - u(t - 1)\right) + \frac{t^2}{2} \left[u(t - 1) - u\left(t - \frac{\pi}{2}\right)\right] + \cos t \cdot u\left(t - \frac{\pi}{2}\right)$$

	
![[lt.jpg]]



# Partial Differential Equation (PDE)
A partial differential equation is an equation involving two or more partial derivatives of a function that is based on two or more variables.
In general, there are many solutions and it can be entirely different.
**A partial differential equation is linear if it is of first degree in the unknown function**
##### Homogeneous vs Non-Homogeneous PDE
$$a(x,y){\frac{dU}{dx}} +b(x,y)\frac{dU}{dx}=0$$
All the terms have ${\frac{dU}{dx}}$. This is homogeneous
For non-homogeneous, the equation will have terms without $\frac{dU}{dx}$
$$a(x,y){\frac{dU}{dx}} +b(x,y)\frac{dU}{dx}=f(x,y)$$

**For homogeneous solutions, solutions can be added together**
$$u(x,y)=c_1u_1(x,y)+c_2u_{2(x,y)}$$
$c_1,c_2$ are any real number

#### Steps to solve:
Suppose a solution exists in the form $u(x,y)=X(x)Y(y)$
Replace all terms with $X,Y$ and their derivatives
Separate all terms involving $x,y$ into LHS and RHS, equating both sides with a constant $k$
Solve the $X_{all \ \ eq}(x) = k$ and $Y_{all \ \ eq}(y)=k$
Merge back into $u(x,y)$
**Note: $k$ can be negative**




# Trigonometry
![[Pasted image 20241102105825.png]]
![[Pasted image 20241102105837.png]]
![[Pasted image 20241102105843.png]]

![[Pasted image 20241102115405.png]]



### Completing the Squares
![[Pasted image 20241102115817.png]]
For this question, the optimal method is to substitute $u=y+x$ and then $t=u+2$. The first is clear but the substitution for $t$ is not obvious. The reason behind this is because after substituing $u$, we get $\frac{2u^2+8u+10}{(u+3)^2}$. Completing the square for the numerator gets us $2(u+2)^2+2$ . Since $u+3$ is in a bracket entirely, it is not a big concern. The issue is the numerator, so we substitute $t=u+2$ to simplify the numerator






![[Pasted image 20250427153323.png]]
**Best and foolproof method: $span(S) \subseteq span(T)$ and $span(T) \subseteq span(S)$ which will show independence too**

**ALWAYS show linear independence**
# Table of Content
- ==Consistent -> Has a solution. The solution may not be unique. For instance,==
- ==Let A be a square matrix of order n. The following statements are equivalent.==
- ==The linear system is inconsistent when the last column, the answer column, is the pivot column.==
- ==Inversing==
- ==RREF and non-square matrix==
- ==**Elementary matrix**==
- ==**Determinants**==
- ==Cramer Rule==
- ==Basis/Sets==
- ==Dot Product and Span==
- ==**Relationship between spans** ==
- ==**Subspace conditions**==
- ==**Linear independence Theorem**==
- ==**Dimension**==
- ==**Relative Coordinates: Express vector V in terms of non-standard basis vectors**==
- ==Checking for Basis==
- ==Row Space and Column Space==
- ==The nullspace of m x n ==
- ==**Rank-nullity theorem**==
- ==**Full-rank**==
- ==Orthogonal and linear equation defining V==
- ==Orthogonal set and orthonormal set==
- ==Checking vector for orthogonality (to span)==
- ==Orthogonal Complement==
- ==Orthogonal Bases General Property==
- ==Projection of Vector on a Subspace==
- ==**Orthogonal matrix**==
- ==**More random orthogonal-related theorem!**==
- ==**Orthogonal Projection Theorem**==
- ==**Best approximation theorem**==
- ==Gram-Schmidt Process==
- ==Least Square Approximation==
- ==Eigenvalue and eigenvector==
- ==Multiplicity==
- ==**Diagonalisation**==
- ==Orthogonal Diagonalisation==
- ==Steady-state vector/stochastic matrix==
- ==First-Order Homogeneous Linear System==
- ==**Wronskian**==
- ==Key stuff to be used in solving first-order homogeneous linear system==
- ==**Fundamental solution set**==
- ==two obstructions to diagonalization==
- ==complex eigenvalues==
- ==Generalized eigenvectors==
# Content


![[Pasted image 20250426195615.png|300]]

==Consistent -> Has a solution. The solution may not be unique. For instance,==
$$ \begin{bmatrix}
1 & 0 & 1 & 1 \\
0 & 1 & 1 & -1 \\
0 & 0 & 0 & 0 
\end{bmatrix}  $$
is consistent.

Invertible  <-> non-singular

==Let A be a square matrix of order n. The following statements are equivalent.==
1. A is invertible
2. $A^T$ is invertible
3. Rows and columns are **linearly independent**
4. Rows and columns form a basis for $\mathbb{R}^n$
5. RREF(A) = I
6. There is a matrix such that AB = I = BA
7. A can be expressed as a product of elementary matrices
8. Homogeneous system $Ax=0$ has only the trivial solution
9. For any b in system $Ax=b$, there is a unique solution
10. **The determinant of A is nonzero, determinant != 0**

IMPORTANT AND USEFUL: linearly independent = invertible = determinant is not zero

==The linear system is inconsistent when the last column, the answer column, is the pivot column.==


==Inversing==
![[Pasted image 20250118160021.png]]

==RREF and non-square matrix==
![[Pasted image 20250426192527.png]]

==**Elementary matrix**==
A square matrix E of order n is called an elementary matrix if it can be obtained from the identity matrix I by performing a single elementary row operation

**Note that E is applied IN FRONT of A. So B = EA where B is the resultant matrix**
![[Pasted image 20250119104657.png]]



==**Determinants**==

![[Pasted image 20250118160421.png]]
![[Pasted image 20250119114536.png|300]]![[Pasted image 20250119114553.png|300]]
$$det(A)=det(A^T)$$
$$det(AB)=det(A)det(B) \text{ for square matrix}$$ 

==Cramer Rule==
![[Pasted image 20250314153736.png]]



==Basis/Sets==
**Any set containing the zero vector is linearly dependent.**


==Dot Product and Span==
$u \cdot v = |u||v|\cos\theta$
$u\cdot v=0$ means perpendicular
Normalise: $\frac{u}{|u|}$
Distance: $d(u,v)=|u-v|$
Span of $u_1,u_2...u_n$ is the subset of $\mathbb{R}^n$ that contains all linear combinations of $u_n$

$v \in span\{ u_1...u_n\}$ if an only if 
$$ \begin{bmatrix}
u_1...u_n|v
\end{bmatrix}  $$
is consistent

==**Relationship between spans** ==
For $span(S) \subseteq span(T)$, $(T | S)$ must be consistent
Thus, for $span(S) = span(T)$, $(T|S)$ and $(S|T)$ must both be consistent


==**Subspace conditions**==
For subset V of $\mathbb{R}^n$ to be a subspace:
$V$ contains zero vector or is non-empty
$V$ is closed under linear combination : $\alpha u + \beta v \in V$


==**Linear independence Theorem**==
The opposite of the above. V is still a subspace of $\mathbb{R}^n$. S is a subset of linearly independent vectors under V. If S spans V, then S is the basis for V. If not, then new linearly independent vectors can be added to S. Eventually, S will span V

==**Dimension**==
The dimension of V (dim(V)) is defined by the number of linearly independent vectors in any basis of V
**For any matrix A, the dimension (Dim) of column space of A is equal to the dimension of row space. This is true.**


==**Relative Coordinates: Express vector V in terms of non-standard basis vectors**==
![[Pasted image 20250130151413.png]]
![[Pasted image 20250130151440.png]]
==Checking for Basis==
![[Pasted image 20250130151122.png]]


==Row Space and Column Space==
Row operations preserve row space
Row space is a subspace of R^n and column space is a subspace of R^m.

IF matrix R is in RREF, the non-zero rows form the **basis for the row space**
Suppose R is the RREF(A). The columns in A corresponding to pivot columns in R form the basis for column space of A.

$Ax=v$ is equivalent to asking is $\bar v$ is in column space of A. It is only such if $\bar v$ can be expressed as a linear combination of the columns of A.

==The nullspace of m x n ==
matrix A is the solution space to $Ax=0$ 

$$\text{Null(A)} = \{ v \in \mathbb{R}^n | Av=0 \}$$

**Note that null space can never be empty because zero vector is always a solution - Null(A) = {0} minimally**
**Note that number of zero rows does not say anything about the number of vectors in the basis of the null space. Use rank-nullity theorem instead**



==**Rank-nullity theorem**==
Let A be a mxn matrix.

Rank-nullity theorem states that 
$$\text{rank(A)} + \text{Null(A)} = \text{n}$$
**Note how it is n, NOT m**

==**Full-rank**==
Suppose you have an mxn matrix. What is the maximum rank?
The maximum rank is the minimum of m or n.

IE
$$\text{Max rank(A)} = \text{minimum(m,n)}$$
This is called full rank.

For a matrix A of size mxn
1. A is full-rank, rank(A) = n (number of columns) 
	- We can imagine this as a tall matrix
2. Columns are linearly independent
3. Rows span $\mathbb{R}^m$

| If full_rank(A) = m (m>n) => Wide matrix                                        | If full_rank(A) = n (n<m) => Tall matrix                                                                                              |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Rows are linearly independent                                                   | Columns                                                                                                                               |
| Columns span $\mathbb{R}^m$                                                                                                                                                                                             |
| $AA^T$ is invertible ($A^T$ is nxm) => Results in invertible matrix of size mxm | $A^TA$ is invertible ($A^T$ is                                                                                                        |
| A has a right inverse<br>$AB = I = (AA^T)(AA^T)^{-1}$ => B = $A^T(AA^T)^{-1}$   | A has a left inv                                                                                                                      |
| Ax=b is c Ax= 0 only has trivial solution x = 0 => Null(A) = {0} => no non-trivial combination of columns can result in zero vector ult in zero   ult in zero   ult in zero   n result in   on of  on of  on of  on of  |


==Orthogonal and linear equation defining V==
![[Pasted image 20250315151038.png|400]]

==Orthogonal set and orthonormal set==
Note that **the zero vector is the only vector that is orthogonal to itself**. In fact, the zero vector is orthogonal to every vector v∈V
Orthogonal set can contain zero vector. Orthonormal set cannot contain zero vector.


==Checking vector for orthogonality (to span)==
How do you quickly check if $w$ is orthogonal to V?

Suppose you have set S that spans V (span(S) = V). $S = \{ u_1, u_2, ..., u_k\}$
$w$ is orthogonal to V if and only if $w$ is in the nullspace of $A^T$ where A = $(u_1 \ \ u_2 \ \ ... \ \ u_k)$![[Pasted image 20250425200542.png]]


==Orthogonal Complement==
Orthogonal complement of subspace V (subspace of $\mathbb{R}^n$) is the set of all vectors that are orthogonal to V
This is denoted $V ^{\perp}$ 

Suppose you have set S that spans V (span(S) = V). $S = \{ u_1, u_2, ..., u_k\}$
$w$ is orthogonal to V if and only if $w$ is in the null space of $A^T$ where A = $(u_1 \ \ u_2 \ \ ... \ \ u_k)$
This can be written as 
$V^ {\perp}= \text{Null}(A^T)$ 


**We can prove**
**$\text{Row}(A^{\perp}) = \text{Null}(A)$**
This is because:
- Every vector $r$ in row space is a linear combination of the row vectors in A
- Using the orthogonal complement's definition - set of all vectors that are orthogonal to V, ie set of all vectors $w$ such as $w \cdot r = 0$ for all $r \in \text{Row(A)}$
- A vector lies in the nullspace of A if and only if $Av=0$
	- Written line by line, this means that $a_i \cdot v = 0$ where $a_i$ is the row vector of A
![[Pasted image 20250302212103.png|400]]

Since A is symmetric, it is diagonalizable, and since it has only 2 eigenvalues, it must be that the geometric multiplicity of eigenvalue 2 is 2 too. Lastly, since A is symmetric, the **eigenspaces must are orthogonal to each other**, that is, E2 ⊥ E1


==Orthogonal Bases General Property==
- All orthonormal sets are linearly independent
- Almost all orthogonal sets are linearly independent
	- The only case is when the zero vector is in the set. Then they are not linearly independent
	- **In this course, we consider orthogonal sets linearly independent

==Projection of Vector on a Subspace==

![[Pasted image 20250302213519.png]]

If S is an orthonormal basis, this becomes simpler,
$$v = (v\cdot u_1)u_1 + (v\cdot u_2)u_2 + ... + (v \cdot u_k)u_k$$

==**Orthogonal matrix**==
A nxn square matrix A is orthogonal if $$A^T=A^{-1}$$
A is an orthogonal matrix if and only if the columns/rows form an **orthonormal** basis for $R^N$

==**More random orthogonal-related theorem!**==
$$u \cdot v = [u]_s \cdot [v]_s$$
$$||u-v|| = ||[u]_s -[v]_s||$$
==**Orthogonal Projection Theorem**==
Let V be a subspace of $R^n$. Every vector w in $R^n$ can be expressed using $w=w_p+w_n$
$$w_p \text{ is the vector in V}$$
$$w_n \text{ is orthogonal to V}$$




==**Best approximation theorem**==
Let $w_p$ be the projection of $w$ onto V. $w_p$ is the closest vector in V to $w$.
$$||w_p-w||\le ||w-v|| \text{ for } \forall v\in V$$


==Gram-Schmidt Process==

- To compute the projection of w on V, we need to first **find the orthonormal/orthogonal basis of V.**
- Suppose we have S, which is a basis for V. However, it is not orthonormal. The Gram-Schmidt Process converts it **to be orthnormal**
- Given a linear independent set {u1, u2, ..., uk }, we want to find an orthogonal set {v1, v2, ..., vk } such that span{u1, u2, ..., uk } = span{v1, v2, ..., vk }.

Here are the steps.
- Let $v_1 = u_1$. Clearly, span( {v1} ) = span( {u1} )
- Let $v_2 = u_2 - u_2'$ where $u_2'$ is a projection of $u_2$ on span{v1}. 
	- $v_2 \perp v_1$
	- span({v1,v2}) = span({u1,u2})
- repeat for $v_{i+1} = u_{i+1} - u_{i+1}'$ 
- Put into {v1,v2,v3...} and then normalise.
![[Pasted image 20250414105230.png|400]]

==Least Square Approximation==
$Ax=b$ but What if b is not in A?
We can still find the **b'** that is closest to b. This is basically finding $u$ to minimise $||Au-b||$

**Note: Suppose u is a solution to Ax = b. Is u a least square solution to Ax = b. YES**
**This works for non squared matrix**

- $Au$ ($b'$) has to be a projection of b onto column space of A. Then we solve for $u$
- **$A^T A u = A^T b$ must be satisfied.** 


u is a least square solution to Ax = b if and only if it is a solution to $A^T Ax = A^T b$.
**Let V be a subspace of Rn and S = {u1, u2, ..., uk } be a basis for V . Then the orthogonal projection of a vector w onto V is**
$$w_p = A(A^TA)^{-1}A^Tw$$
where A = (u1 u2 u3 u4 ...)
Note: Least square solutions may not be unique, but projection is unique.



![[Pasted image 20250315142136.png]]
![[Pasted image 20250315142416.png]]


![[Pasted image 20250427110440.png]]


==Eigenvalue and eigenvector==
$$Av=\lambda v$$
Note that it is possible for eigenvalues to be zero  but not eigenvector.


==Multiplicity==
- **Algebraic multiplicity** of eigenvalue λ:  
    - How many times λ appears as a root of the characteristic polynomial.
    
- **Geometric multiplicity** of λ:  
    - the number of linearly independent eigenvectors corresponding to λ

==**Diagonalisation**==
Invertible matrix P such that it is a diagonal matrix AND
$$P^{-1}AP=D$$
For **diagonalizability**, the geometric multiplicity must **equal** the algebraic multiplicity **for each eigenvalue**.
A **diagonalization** (or an **orthogonal diagonalization**) is not affected by multiplying one of the eigenvectors by -1. 
Any nonzero scalar multiple of an eigenvector is still a valid eigenvector, so flipping signs in one or more columns of the matrix does not invalidate the diagonalization.


==Orthogonal Diagonalisation==

Suppose P is a square matrix such that $P^T = P^{−1}$. Then P is an orthogonal matrix
A is orthgonally diagonalizable if and only if A is symmetric.
**Real symmetric matrices not only have real eigenvalues, they are always diagonalizable.**



Since **A is symmetric, it is diagonalizable**, and since it has only 2 eigenvalues, it must be that the geometric multiplicity of eigenvalue 2 is 2 too. **Lastly, since A is symmetric, the eigenspaces must are orthogonal** to each other, that is, E2 ⊥ E1
![[Pasted image 20250401144327.png]]
==Steady-state vector/stochastic matrix==
![[Pasted image 20250401144603.png]]
A stochastic matrix is **a square matrix whose columns/rows are probability vectors**
![[Pasted image 20250401160436.png]]

==First-Order Homogeneous Linear System==
![[Pasted image 20250411145736.png]]



==**Wronskian**==
do det on **(v1, v2, v3)** (fundamental set of solution -> sub t=0 for instance, only need to prove that one value of t is such that det != 0)
If det(v matrix) != 0, this is a fundamental set of solutions


==Key stuff to be used in solving first-order homogeneous linear system==
$$
v=v_r+iv_i \text{ for vectors with complex entries}
$$

$$
e^{i\theta} = \cos\theta + i\sin \theta
$$

**Real solutions from complex solution**
$$x_r(t)=e^{\lambda_rt}(\cos(\lambda_it)v_r -\sin(\lambda_it)v_i)$$
$$
x_i(t) = e^{\lambda_rt}(\cos(\lambda_it)v_i + \sin(\lambda_it)v_r)
$$

==**Fundamental solution set**==
Similar concept to a basis. It is the set of solutions from which the general solution form can is derived
![[Pasted image 20250411145703.png]]
==two obstructions to diagonalization==
(i) the characteristic polynomial does not factorize into real linear factors,
Solution: allow complex eigenvalues
(ii) the geometric multiplicity of an eigenvalue is strictly less than the algebraic multiplicity.
Solution: use generalized eigenvectors

==complex eigenvalues==
**Real solutions from complex solution**
$$x_r(t)=e^{\lambda_rt}(\cos(\lambda_it)v_r -\sin(\lambda_it)v_i)$$
$$
x_i(t) = e^{\lambda_rt}(\cos(\lambda_it)v_i + \sin(\lambda_it)v_r)
$$
*   **Eigenvalue $\lambda_2 = 1 + 2i$**:
    *   Eigenvector: $\mathbf{v}_3 = \begin{pmatrix} 1 \\ 0 \\ 1+i \\ i \end{pmatrix}$ (satisfies $A\mathbf{v}_3 = (1+2i)\mathbf{v}_3$)
*   **Eigenvalue $\lambda_3 = 1 - 2i$**:
    *   Since **A** is real, the conjugate eigenvalue exists.
    *   Eigenvector: $\mathbf{v}_4 = \overline{\mathbf{v}_3} = \begin{pmatrix} 1 \\ 0 \\ 1-i \\ -i \end{pmatrix}$ (satisfies $A\mathbf{v}_4 = (1-2i)\mathbf{v}_4$)
**Conjunction!!!**


==Generalized eigenvectors==
![[Pasted image 20250411153437.png]]
$$(A - \lambda I) \mathbf{v}_2 = \mathbf{v}_1 \text{ where v1 is the eigenvector}$$ 

# Tricks and Tips
==Use DET==
**Sometimes using DET to solve to find variables is faster than solving the actual equation**
![[Pasted image 20250314133319.png]]

==Vector subspace definition==
![[Pasted image 20250426194350.png]]



==Okay, let's break down the conversion step-by-step.==

1.  **Start with the definition of V:**
    The set V contains all vectors $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix}$ that satisfy the single linear equation:
    $\frac{1}{2}x_1 - x_3 - \frac{1}{2}x_4 = 1$

2.  **Identify Free and Dependent Variables:**
    *   This equation relates $x_1, x_3,$ and $x_4$.
    *   Notice that $x_2$ does not appear in the equation. This means $x_2$ can be any real number without affecting whether the vector is in V. So, $x_2$ is a *free variable*.
    *   We have one equation relating three variables ($x_1, x_3, x_4$). We can choose one variable to express in terms of the others. It's usually easiest to solve for the variable with the "lowest" index, which is $x_1$. The other variables involved ($x_3, x_4$) will also be treated as *free variables*.
    *   So, the free variables are $x_2, x_3, x_4$. The dependent variable is $x_1$.

3.  **Solve for the Dependent Variable:**
    Rearrange the equation to solve for $x_1$:
    $\frac{1}{2}x_1 = 1 + x_3 + \frac{1}{2}x_4$
    Multiply by 2:
    $x_1 = 2 + 2x_3 + x_4$

4.  **Introduce Parameters for Free Variables:**
    Since $x_2, x_3, x_4$ are free, we can represent them with parameters. Let:
    *   $x_2 = r$
    *   $x_3 = s$
    *   $x_4 = t$
    where $r, s, t$ can be any real numbers ($r, s, t \in \mathbb{R}$).

5.  **Express the Vector in Terms of Parameters:**
    Substitute the parameter expressions back into the vector $\mathbf{x}$:
    $\mathbf{x} = \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 2 + 2x_3 + x_4 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} = \begin{pmatrix} 2 + 2s + t \\ r \\ s \\ t \end{pmatrix}$

6.  **Separate the Vector into Parts:**
    Now, decompose this vector into a constant part (the particular solution) and parts corresponding to each parameter (spanning the null space/homogeneous solution):
    $\begin{pmatrix} 2 + 2s + t \\ r \\ s \\ t \end{pmatrix} = \begin{pmatrix} 2 \\ 0 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ r \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 2s \\ 0 \\ s \\ 0 \end{pmatrix} + \begin{pmatrix} t \\ 0 \\ 0 \\ t \end{pmatrix}$

7.  **Factor out the Parameters:**
    Factor out $r, s,$ and $t$ from the respective vectors:
    $\begin{pmatrix} 2 \\ 0 \\ 0 \\ 0 \end{pmatrix} + r \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} 2 \\ 0 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix}$

8.  **Write the Explicit Set Notation:**
    This expression represents any vector $\mathbf{x}$ in V. So, we can write V explicitly as the set of all such vectors:
    $V = \left\{ \begin{pmatrix} 2 \\ 0 \\ 0 \\ 0 \end{pmatrix} + r \begin{pmatrix} 0 \\ 1 \\ 0 \\ 0 \end{pmatrix} + s \begin{pmatrix} 2 \\ 0 \\ 1 \\ 0 \end{pmatrix} + t \begin{pmatrix} 1 \\ 0 \\ 0 \\ 1 \end{pmatrix} \, \middle| \, r, s, t \in \mathbb{R} \right\}$

This matches the explicit form given in the solution. The process involves identifying free variables, solving for the dependent variable(s), introducing parameters, and decomposing the general vector solution.



Okay, let's solve part (b).

**Understanding the Problem:**

We are given two bases for the subspace V:
1.  $S = \{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$
2.  $T = \{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ (We assume $a$ is such that this is indeed a basis, as per the result of part (a)).

We are given the coordinate vector of a vector $\mathbf{w} \in V$ with respect to basis $S$:
$[\mathbf{w}]_S = \begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix}$
This means:
$\mathbf{w} = 3\mathbf{u}_1 + 1\mathbf{u}_2 + 2\mathbf{u}_3$

We want to find the coordinate vector of $\mathbf{w}$ with respect to basis $T$:
$[\mathbf{w}]_T = \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}$
This means:
$\mathbf{w} = c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + c_3\mathbf{v}_3$

**Using the Change-of-Basis Matrix:**

We can relate the coordinate vectors using the change-of-basis matrix from $T$ to $S$, denoted as $P_{S \leftarrow T}$. The columns of this matrix are the coordinate vectors of the basis vectors in $T$ relative to the basis $S$.

From the problem statement:
$\mathbf{v}_1 = 1\mathbf{u}_1 + (a+1)\mathbf{u}_2 - a\mathbf{u}_3 \implies [\mathbf{v}_1]_S = \begin{pmatrix} 1 \\ a+1 \\ -a \end{pmatrix}$
$\mathbf{v}_2 = a\mathbf{u}_1 + 2\mathbf{u}_2 - a\mathbf{u}_3 \implies [\mathbf{v}_2]_S = \begin{pmatrix} a \\ 2 \\ -a \end{pmatrix}$
$\mathbf{v}_3 = -1\mathbf{u}_1 + (a+1)\mathbf{u}_2 - 1\mathbf{u}_3 \implies [\mathbf{v}_3]_S = \begin{pmatrix} -1 \\ a+1 \\ -1 \end{pmatrix}$

So, the change-of-basis matrix is:
$P_{S \leftarrow T} = \begin{pmatrix} [\mathbf{v}_1]_S & [\mathbf{v}_2]_S & [\mathbf{v}_3]_S \end{pmatrix} = \begin{pmatrix} 1 & a & -1 \\ a+1 & 2 & a+1 \\ -a & -a & -1 \end{pmatrix}$

The relationship between the coordinate vectors is:
$[\mathbf{w}]_S = P_{S \leftarrow T} [\mathbf{w}]_T$

**Solving for $[\mathbf{w}]_T$:**

We have the equation:
$\begin{pmatrix} 3 \\ 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 1 & a & -1 \\ a+1 & 2 & a+1 \\ -a & -a & -1 \end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix}$

This is a system of linear equations for $c_1, c_2, c_3$:
1.  $c_1 + a c_2 - c_3 = 3$
2.  $(a+1)c_1 + 2 c_2 + (a+1)c_3 = 1$
3.  $-a c_1 - a c_2 - c_3 = 2$

We can solve this system using substitution or elimination, or by finding the inverse of the matrix $P_{S \leftarrow T}$. Let's use elimination.

Subtract (3) from (1):
$(1 - (-a))c_1 + (a - (-a))c_2 + (-1 - (-1))c_3 = 3 - 2$
$(1+a)c_1 + 2a c_2 = 1 \quad (*)$

Add $a$ times (1) to (3):
$(-a+a)c_1 + (-a+a^2)c_2 + (-1-a)c_3 = 2+3a$
$a(a-1)c_2 - (a+1)c_3 = 2+3a \quad (**)$

From (1), $c_3 = c_1 + a c_2 - 3$. Substitute this into (2):
$(a+1)c_1 + 2 c_2 + (a+1)(c_1 + a c_2 - 3) = 1$
$(a+1)c_1 + 2 c_2 + (a+1)c_1 + a(a+1)c_2 - 3(a+1) = 1$
$2(a+1)c_1 + (2 + a(a+1))c_2 = 1 + 3(a+1)$
$2(a+1)c_1 + (a^2+a+2)c_2 = 1 + 3a + 3$
$2(a+1)c_1 + (a^2+a+2)c_2 = 3a + 4 \quad (***)$

Now we have a system of two equations for $c_1, c_2$:
(*) $(1+a)c_1 + 2a c_2 = 1$
(***) $2(a+1)c_1 + (a^2+a+2)c_2 = 3a + 4$

Multiply (*) by 2:
$2(1+a)c_1 + 4a c_2 = 2$

Subtract this from (***):
$(2(a+1) - 2(a+1))c_1 + ((a^2+a+2) - 4a)c_2 = (3a + 4) - 2$
$(a^2 - 3a + 2)c_2 = 3a + 2$
$(a-1)(a-2)c_2 = 3a + 2$
$c_2 = \frac{3a+2}{(a-1)(a-2)}$ (Assuming $a \neq 1, a \neq 2$, which must be true if T is a basis, from part (a))

Substitute $c_2$ back into (*):
$(1+a)c_1 = 1 - 2a c_2$
$(1+a)c_1 = 1 - 2a \frac{3a+2}{(a-1)(a-2)}$
$(1+a)c_1 = \frac{(a-1)(a-2) - 2a(3a+2)}{(a-1)(a-2)}$
$(1+a)c_1 = \frac{(a^2 - 3a + 2) - (6a^2 + 4a)}{(a-1)(a-2)}$
$(1+a)c_1 = \frac{a^2 - 3a + 2 - 6a^2 - 4a}{(a-1)(a-2)}$
$(1+a)c_1 = \frac{-5a^2 - 7a + 2}{(a-1)(a-2)}$
$c_1 = \frac{-5a^2 - 7a + 2}{(a+1)(a-1)(a-2)}$

Finally, find $c_3$ using $c_3 = c_1 + a c_2 - 3$:
$c_3 = \frac{-5a^2 - 7a + 2}{(a+1)(a-1)(a-2)} + a \frac{3a+2}{(a-1)(a-2)} - 3$
$c_3 = \frac{-5a^2 - 7a + 2 + a(a+1)(3a+2) - 3(a+1)(a-1)(a-2)}{(a+1)(a-1)(a-2)}$
$c_3 = \frac{-5a^2 - 7a + 2 + a(3a^2+5a+2) - 3(a+1)(a^2-3a+2)}{(a+1)(a-1)(a-2)}$
$c_3 = \frac{-5a^2 - 7a + 2 + 3a^3+5a^2+2a - 3(a^3-3a^2+2a+a^2-3a+2)}{(a+1)(a-1)(a-2)}$
$c_3 = \frac{3a^3 - 5a + 2 - 3(a^3-2a^2-a+2)}{(a+1)(a-1)(a-2)}$
$c_3 = \frac{3a^3 - 5a + 2 - 3a^3+6a^2+3a-6}{(a+1)(a-1)(a-2)}$
$c_3 = \frac{6a^2 - 2a - 4}{(a+1)(a-1)(a-2)}$
$c_3 = \frac{2(3a^2 - a - 2)}{(a+1)(a-1)(a-2)}$
Factor $3a^2 - a - 2 = (3a+2)(a-1)$:
$c_3 = \frac{2(3a+2)(a-1)}{(a+1)(a-1)(a-2)}$
$c_3 = \frac{2(3a+2)}{(a+1)(a-2)}$ (Assuming $a \neq 1$)

**Result:**

The coordinate vector $[\mathbf{w}]_T$ is:
$[\mathbf{w}]_T = \begin{pmatrix} c_1 \\ c_2 \\ c_3 \end{pmatrix} = \begin{pmatrix} \frac{-5a^2 - 7a + 2}{(a+1)(a-1)(a-2)} \\ \frac{3a+2}{(a-1)(a-2)} \\ \frac{2(3a+2)}{(a+1)(a-2)} \end{pmatrix}$

We can also express this using the determinant found in part (a), $\det(P_{S \leftarrow T}) = -(a+1)(a-1)(a-2)$.
$[\mathbf{w}]_T = \frac{1}{-(a+1)(a-1)(a-2)} \begin{pmatrix} -(-5a^2 - 7a + 2) \\ -(a+1)(3a+2) \\ - (a-1) 2(3a+2) \end{pmatrix}$
$[\mathbf{w}]_T = \frac{1}{(a+1)(a-1)(a-2)} \begin{pmatrix} 5a^2 + 7a - 2 \\ (a+1)(3a+2) \\ 2(a-1)(3a+2) \end{pmatrix}$
Checking calculation:
Row 1: $5a^2+7a-2$. Previous result: $-5a^2-7a+2$. Sign flip. Let's recheck $c_1$.
$(1+a)c_1 = \frac{-5a^2 - 7a + 2}{(a-1)(a-2)}$. Correct.
$c_1 = \frac{-5a^2 - 7a + 2}{(a+1)(a-1)(a-2)}$. Correct.

Row 2: $c_2 = \frac{3a+2}{(a-1)(a-2)}$. The expression should be $\frac{(a+1)(3a+2)}{(a+1)(a-1)(a-2)}$. Correct.

Row 3: $c_3 = \frac{2(3a+2)}{(a+1)(a-2)}$. The expression should be $\frac{2(3a+2)(a-1)}{(a+1)(a-1)(a-2)}$. Correct.

So the final answer derived through solving the system is:
$[\mathbf{w}]_T = \begin{pmatrix} \frac{-(5a^2 + 7a - 2)}{(a+1)(a-1)(a-2)} \\ \frac{(a+1)(3a+2)}{(a+1)(a-1)(a-2)} \\ \frac{2(a-1)(3a+2)}{(a+1)(a-1)(a-2)} \end{pmatrix}$

Final Answer:
$[\mathbf{w}]_T = \frac{1}{(a+1)(a-1)(a-2)} \begin{pmatrix} -5a^2 - 7a + 2 \\ (a+1)(3a+2) \\ 2(a-1)(3a+2) \end{pmatrix}$




==Sample of Solving First Homogeneous ==

Okay, let's solve part (d).

**1. Recap Information about Eigenvalues and Eigenvectors/Generalized Eigenvectors:**

From the previous parts and the problem statement, we have gathered the following for the 4x4 real matrix **A**:

*   **Eigenvalue $\lambda_1 = 0$**:
    *   Eigenvector: $\mathbf{v}_1 = \begin{pmatrix} 0 \\ 1 \\ 2 \\ 3 \end{pmatrix}$ (satisfies $A\mathbf{v}_1 = \mathbf{0}$)
    *   Generalized Eigenvector: $\mathbf{v}_2 = \begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix}$ (satisfies $A\mathbf{v}_2 = \mathbf{v}_1$)
    This corresponds to a Jordan block of size 2 for $\lambda=0$.

*   **Eigenvalue $\lambda_2 = 1 + 2i$**:
    *   Eigenvector: $\mathbf{v}_3 = \begin{pmatrix} 1 \\ 0 \\ 1+i \\ i \end{pmatrix}$ (satisfies $A\mathbf{v}_3 = (1+2i)\mathbf{v}_3$)

*   **Eigenvalue $\lambda_3 = 1 - 2i$**:
    *   Since **A** is real, the conjugate eigenvalue exists.
    *   Eigenvector: $\mathbf{v}_4 = \overline{\mathbf{v}_3} = \begin{pmatrix} 1 \\ 0 \\ 1-i \\ -i \end{pmatrix}$ (satisfies $A\mathbf{v}_4 = (1-2i)\mathbf{v}_4$)

**2. Construct the General Real Solution:**

The general solution to $\mathbf{y}'(t) = \mathbf{A}\mathbf{y}(t)$ is built from these components:

*   **For $\lambda_1 = 0$ (repeated with a generalized eigenvector):**
    The contribution to the solution is $c_1 e^{0t}\mathbf{v}_1 + c_2 e^{0t}(t\mathbf{v}_1 + \mathbf{v}_2) = c_1 \mathbf{v}_1 + c_2(t\mathbf{v}_1 + \mathbf{v}_2)$.

*   **For the complex conjugate pair $\lambda = 1 \pm 2i$:**
    We use the real and imaginary parts of $e^{\lambda_2 t} \mathbf{v}_3 = e^{(1+2i)t} \mathbf{v}_3$.
    $e^{(1+2i)t} \mathbf{v}_3 = e^t e^{i2t} \begin{pmatrix} 1 \\ 0 \\ 1+i \\ i \end{pmatrix}$
    $= e^t (\cos(2t) + i\sin(2t)) \left( \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} + i \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix} \right)$
    $= e^t \left[ \left( \cos(2t)\begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} - \sin(2t)\begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix} \right) + i \left( \sin(2t)\begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} + \cos(2t)\begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix} \right) \right]$
    $= e^t \begin{pmatrix} \cos(2t) \\ 0 \\ \cos(2t) - \sin(2t) \\ -\sin(2t) \end{pmatrix} + i e^t \begin{pmatrix} \sin(2t) \\ 0 \\ \sin(2t) + \cos(2t) \\ \cos(2t) \end{pmatrix}$
    Let $\mathbf{y}_{Re}(t) = \text{Re}(e^{\lambda_2 t} \mathbf{v}_3) = e^t \begin{pmatrix} \cos(2t) \\ 0 \\ \cos(2t) - \sin(2t) \\ -\sin(2t) \end{pmatrix}$
    Let $\mathbf{y}_{Im}(t) = \text{Im}(e^{\lambda_2 t} \mathbf{v}_3) = e^t \begin{pmatrix} \sin(2t) \\ 0 \\ \cos(2t) + \sin(2t) \\ \cos(2t) \end{pmatrix}$
    The contribution from the complex pair is $c_3 \mathbf{y}_{Re}(t) + c_4 \mathbf{y}_{Im}(t)$.

*   **General Real Solution:**
    $\mathbf{y}(t) = c_1 \mathbf{v}_1 + c_2(t\mathbf{v}_1 + \mathbf{v}_2) + c_3 \mathbf{y}_{Re}(t) + c_4 \mathbf{y}_{Im}(t)$
    $\mathbf{y}(t) = c_1 \begin{pmatrix} 0 \\ 1 \\ 2 \\ 3 \end{pmatrix} + c_2 \left( t \begin{pmatrix} 0 \\ 1 \\ 2 \\ 3 \end{pmatrix} + \begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} \right) + c_3 e^t \begin{pmatrix} \cos(2t) \\ 0 \\ \cos(2t) - \sin(2t) \\ -\sin(2t) \end{pmatrix} + c_4 e^t \begin{pmatrix} \sin(2t) \\ 0 \\ \cos(2t) + \sin(2t) \\ \cos(2t) \end{pmatrix}$

**3. Apply the Initial Conditions:**

We are given $\mathbf{y}(0) = \begin{pmatrix} 0 \\ 0 \\ -1 \\ -3 \end{pmatrix}$. Set $t=0$ in the general solution:
$\cos(0)=1, \sin(0)=0, e^0=1$.
$\mathbf{y}(0) = c_1 \begin{pmatrix} 0 \\ 1 \\ 2 \\ 3 \end{pmatrix} + c_2 \left( 0 \begin{pmatrix} 0 \\ 1 \\ 2 \\ 3 \end{pmatrix} + \begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} \right) + c_3 e^0 \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} + c_4 e^0 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix}$
$\begin{pmatrix} 0 \\ 0 \\ -1 \\ -3 \end{pmatrix} = c_1 \begin{pmatrix} 0 \\ 1 \\ 2 \\ 3 \end{pmatrix} + c_2 \begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} + c_3 \begin{pmatrix} 1 \\ 0 \\ 1 \\ 0 \end{pmatrix} + c_4 \begin{pmatrix} 0 \\ 0 \\ 1 \\ 1 \end{pmatrix}$
$\begin{pmatrix} 0 \\ 0 \\ -1 \\ -3 \end{pmatrix} = \begin{pmatrix} -c_2 + c_3 \\ c_1 + c_2 \\ 2c_1 + c_3 + c_4 \\ 3c_1 + c_4 \end{pmatrix}$

**4. Solve for the Coefficients:**

This leads to the system of linear equations:
1.  $-c_2 + c_3 = 0 \implies c_3 = c_2$
2.  $c_1 + c_2 = 0 \implies c_1 = -c_2$
3.  $2c_1 + c_3 + c_4 = -1$
4.  $3c_1 + c_4 = -3$

Substitute $c_3=c_2$ and $c_1=-c_2$ into (3):
$2(-c_2) + c_2 + c_4 = -1$
$-2c_2 + c_2 + c_4 = -1$
$-c_2 + c_4 = -1 \quad (*)$

Substitute $c_1=-c_2$ into (4):
$3(-c_2) + c_4 = -3$
$-3c_2 + c_4 = -3 \quad (**)$

Subtract (*) from (**):
$(-3c_2 + c_4) - (-c_2 + c_4) = -3 - (-1)$
$-2c_2 = -2$
$c_2 = 1$

Now find the others:
$c_3 = c_2 = 1$
$c_1 = -c_2 = -1$
From (*): $c_4 = c_2 - 1 = 1 - 1 = 0$

So the coefficients are $c_1 = -1, c_2 = 1, c_3 = 1, c_4 = 0$.

**5. Write the Specific Solution:**

Substitute these coefficients back into the general solution:
$\mathbf{y}(t) = (-1) \mathbf{v}_1 + (1)(t\mathbf{v}_1 + \mathbf{v}_2) + (1) \mathbf{y}_{Re}(t) + (0) \mathbf{y}_{Im}(t)$
$\mathbf{y}(t) = -\mathbf{v}_1 + t\mathbf{v}_1 + \mathbf{v}_2 + \mathbf{y}_{Re}(t)$
$\mathbf{y}(t) = (t-1)\mathbf{v}_1 + \mathbf{v}_2 + \mathbf{y}_{Re}(t)$
$\mathbf{y}(t) = (t-1) \begin{pmatrix} 0 \\ 1 \\ 2 \\ 3 \end{pmatrix} + \begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} + e^t \begin{pmatrix} \cos(2t) \\ 0 \\ \cos(2t) - \sin(2t) \\ -\sin(2t) \end{pmatrix}$
$\mathbf{y}(t) = \begin{pmatrix} 0 \\ t-1 \\ 2t-2 \\ 3t-3 \end{pmatrix} + \begin{pmatrix} -1 \\ 1 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} e^t \cos(2t) \\ 0 \\ e^t(\cos(2t) - \sin(2t)) \\ -e^t \sin(2t) \end{pmatrix}$
$\mathbf{y}(t) = \begin{pmatrix} -1 + e^t \cos(2t) \\ (t-1)+1 \\ (2t-2) + e^t(\cos(2t) - \sin(2t)) \\ (3t-3) - e^t \sin(2t) \end{pmatrix}$

**Final Solution for (d):**

The solution to the initial value problem is:
$\mathbf{y}(t) = \begin{pmatrix} -1 + e^t \cos(2t) \\ t \\ 2t - 2 + e^t \cos(2t) - e^t \sin(2t) \\ 3t - 3 - e^t \sin(2t) \end{pmatrix}$



==Show Span equality==
Let B be the basis found in part (c). Since T has 3 vectors which is
equals to the dimension of W , suffice to show either one of the following
i. B ⊆ span(T ), T ⊆ span(B), and T is linearly independent;
ii. T is linearly independent and T ⊆ span(B); or
iii. B ⊆ span(T ).


==Substituting y1==
![[Pasted image 20250427145609.png]]


![[Pasted image 20250429143510.png]]

![[Pasted image 20250429173244.png]]
Trick for (B):
$$
(A | I) --> rref --> (R | P)
$$





Simpson's Paradox -> implies presence of confounders


Simpson's Paradox occurs when the association between two variables (Program and Outcome) reverses or disappears when a third variable (Age) is controlled for. This third variable acts as a confounder.

Confounder MUST have association with outcome AND independent variable.

While subgroup analysis is necessary to understand Simpson's Paradox, its conclusions are only reliable if the standard requirements for statistical inference are met within each subgroup.



==The ecological fallacy occurs when inferences about individuals are made based on group-level data, while the atomistic fallacy (also known as the "fallacy of division") occurs when inferences about groups are made based on individual-level data==


Okay, let's break this down using the formulas for the slope and intercept in a simple linear regression equation Y = a + bX.

The estimated equation is given as Y = X. Comparing this to the standard form Y = a + bX, we can see:

- The estimated intercept a = 0.
    
- The estimated slope b = 1.
Now let's recall the formulas for the estimated slope and intercept:

- Slope b = r * (SD_Y / SD_X)
    
- Intercept a = Mean_Y - b * Mean_X
- r is the correlation coefficient between X and Y.
    
- SD_Y is the standard deviation of Y.
    
- SD_X is the standard deviation of X.
    
- Mean_Y is the mean of Y.
    
- Mean_X is the mean of X.


The **Base Rate Fallacy** (also known as base rate neglect or base rate bias) is a cognitive error where people tend to **ignore or underweight general statistical information (the "base rate" or "prior probability")** and focus instead on specific, often vivid or compelling, information (the "individuating information") when making judgments or estimating probabilities.

In simpler terms: People often get distracted by specific details about a particular case or person and forget to consider how common or rare that situation or characteristic is in the overall population.

1. **What the Data Shows:** The study provides data aggregated at the **group level (schools)**. It correlates the average IQ of graduates from a school with the average income of graduates from that same school.
    
2. **What the Researcher Concludes:** The researcher draws a conclusion about the **individual level**. They infer that an individual graduate's high IQ will cause or lead to that individual having a higher income.
    
3. **The Mistake (Ecological Fallacy):** This jump from group-level findings (averages for schools) to individual-level conclusions is the definition of the **Ecological Fallacy**. Just because schools with higher average IQs also have higher average incomes doesn't automatically mean that within any given school, or across the population of all graduates treated as individuals, IQ is the driving factor for income.



Approx: (0 - 0.3 weak, 0.3 - 0.7 moderate, 0.7 - 1 strong)


Extrapolation of linear regression: Prediction beyond the observed range is dangerous (Not advisable)



==Permutations deal with ordered arrangements, while combinations focus on selecting groups without regard to order==. Permutations consider the order of elements, making ABC, BAC, and CAB distinct arrangements. Combinations, however, consider only the members of a group, so ABC, BAC, and CAB are all the same combination.

When Simpson’s Paradox is observed, analysing data by subgroups (e.g., age groups) can help reveal relationships that may be misrepresented in the combined data. However, the validity of such subgroup analyses also depends on having sufficiently large and representative samples within each subgroup


![[Pasted image 20250422110700.png]]
Take a look at the row vs column and calculate conditional rate.

Confounding conditions, or confounding variables, are ==factors that distort the relationship between an independent and dependent variable in a study==
MUST BE NON-ZERO FOR BOTH.




![[Pasted image 20250125150849.png|100]]![[Pasted image 20250125150837.png|100]]![[Pasted image 20250125152751.png|100]]
![[Pasted image 20250125164012.png|400]]
**WEIRD THEOREM**
$\neg \forall x \in D \ \  P(x)$ <-> $\exists x \in D \ \ \neg P(x)$
$\neg \exists x \in D \ \ P(x)$ <-> $\forall x \in D \ \ \neg P(x)$
**The order of quantifiers matter**
**Witnesses**
$\exists x \ \ P(x)$
Produce an object $z$ such that $P(z)$ is true.

**Proving a conditional directly**
For instance, to prove p->q is true (square of any even integer is even)
Assume p is true then prove that q is also true.
For instance, $n=2x$ , $n^2 = (2x)^2 = 2(2x^2)$

**Proof by contraposition**
p -> q
Prove: ~q -> ~p

**Equivalence**
Prove: p<->q
Prove both p -> q and q->p

**Splitting into cases**
**Exhaust all cases**

![[Pasted image 20250125154325.png]]



![[Pasted image 20250125172927.png|00]]
![[Pasted image 20250125173001.png|00]]
![[Pasted image 20250125173006.png|00]]
![[Pasted image 20250125173011.png|00]]

![[Pasted image 20250125173233.png|00]]

![[Pasted image 20250125173237.png|00]]

![[Pasted image 20250125173242.png|00]]



![[Pasted image 20250311202208.png|300]]

## Chapter 4
$\emptyset$ is an empty set. NOT an empty element

$\subset$ is subset, $\subseteq$ is subset + equivalent

Roster rotation!
![[Pasted image 20250310162338.png|400]]

##### Power Sets P

Let A be a set. The set of all subsets of A, P(A), is the power set of A

For instance, P( {1,2} ) = { $\varnothing$, {1}, {2}, {1,2} }
P( $\emptyset$ ) = { $\emptyset$ }

 So the only subset of ∅ is ∅

![[Pasted image 20250221210715.png]]


![[Pasted image 20250221210633.png]]
$\bar B$ is B complement  


Union: $A\cup B$ = $\{ x : x \in A \text{ or } x \in B \}$ 
Intersection: $A \cap B$ = $\{ x : x \in A \text{ and } x \in B \}$ 
Complement: $A / B$ = $\{ x : x \in A \text{ and } x \notin B  \}$
Respectively: ![[Pasted image 20250221210429.png|100]] 
##### Set-builder notation
$$\{x\in U | P(x)\}$$

U is a set. x is any element from U. P(x) is the predicate that is true
For instance
$$\{ x\in \mathbb{Z}_{\geq 0} | \text {x is even}\}$$

##### Replacement notation
Similar to the set-builder, except instead of $x$ being the elements in the set, $t(x)$ are the elements in the set instead

$$\{ t(x) | x \in A  \}$$
Set contains all objects of the form $t(x)$ where $x$ ranges over the elements of A is donated
Can also be read as 'the set of all $t(x)$ where $x\in A$


##### The unique set that satisfies a property: empty set
- For all sets A, B, if both A and B have no element, then A = B



### Set equality = 
Two sets are equal if they have the same elements. $$\forall z (z\in A \Leftrightarrow  z\in B)$$
#### Quick Question Answers:
From Proposition 4.2.7, we know ∅ ⊆ A. So ∅ ∈ P(A) by the definition of P(A).
This implies P(A)̸ = ∅ as ∅ has no element

**Last resort: Use Truth Table**
![[Pasted image 20250310192718.png|400]]

**When in doubt, use distributive property**


## Chapter 5

(x,y) is an ordered tuple. The order matters. (1,2) $\neq$ (2,1)

Cartesian product of two sets: {x,y} and {1,2,3,4}:
$$\{x,y\} \times \{ \text{1,2,3} \} = \{(a,1), (a,2),(a,3),(b,1),(b,2),(b,3)\}$$
#### Composition
![[Pasted image 20250223134930.png|400]]

Let R be a relation from A to B. Let S be a relation from B to C.
$S \circ R$ is defined as { (x,z) |  (x,y) $\in$ R and (y,z) $\in$ S for some y $\in$ B}
Note how the set B has to be the same.
**Note the order: S composed with R (S $\circ$ R), not the other way. Composition is not generally commutative.**

**S composed with R**
Example: (Q is all rational numbers)
![[Pasted image 20250223135358.png|300]]
(4.8, 2) is in $S \circ R$. 4 is in Z such that (4.8,4) is in R (since floor x = y) and (4, 2) is in S (condition: y=z^2).

We can sometimes merge the conditions for speed:
![[Pasted image 20250223140424.png]]


##### Inverse
Let R be the relation from A to B.
Let relation $R^{-1}$ be the inverse of R, from B to A.

$R^{-1}$ = { (y,x) $\in$ B $\times$ A : (x,y) $\in$ R }

![[Pasted image 20250223140654.png]]

##### Composition with Inversion
Much like matrices, when composition is inversed, some orders of operations are changed.

Let R be a relation from A to B. Let S be a relation from B to C.
$$(S\circ R)^{-1} = R^{-1}\circ S^{-1}$$ 

![[Pasted image 20250223141017.png|400]]
##### 

### Graphs representing graphs

##### Directed Graphs

![[Pasted image 20250223141819.png]]
Reading in D as: {from, to}. Order matters because this is a directed graph
 **directed graph (V, D)**

##### Undirected graph
**undirected graph (W, E)**


![[Pasted image 20250223141808.png]]
Reading similar to D. Put both sides instead of {B,P and {P,B}}
Note the {} instead of ()



![[Pasted image 20250310205428.png]]
x is (the name of) a student who is enrolled in the course y
$S \cdot R$ => A to C (reverse order)

Let $(a,b) \in R^{-1}$ . Then $(b,a) \in R$

a-b = 2x
b-a = 2(-x) => also even


![[Pasted image 20250310213353.png]]
Explanation for linking $T \cdot (S \cdot R)$ together

## Chapter 6
The first option is reflexive. The second is symmetric. The last is transitivity.
![[Pasted image 20250223142236.png|300]]


##### Reflexivity
$$\forall x \in A (x R x)$$
##### Symmetry 
$$\forall x,y \in A (x R y \rightarrow yRx)$$
x being R related to y implies that y is R-related to x.
Note: can we surmise that all symmetric relations are reflexive? No. The reflexive relation may not exist at all. But if it does, it is obviously symmetric.

##### Transitivity
$∀x, y , z ∈ A (x R y ∧ y R z ⇒ x R z)$
![[Pasted image 20250223154058.png]]
##### Equivalence classes

A equivalence relation is a relation that is reflexive, symmetric and transitive.
	![[Pasted image 20250223153744.png|100]]
### Equivalence Classes
![[Pasted image 20250312200749.png]]
x is related to?
$[x]_{~}$ is the set of all elements of A that x is ~-related to
We can see from the arrow drawing
![[Pasted image 20250312200956.png|100]]
b is connected to c and vice versa. a is only connected to itself



### Partitions
Call C a partition of a set A if
(0) C is a set of nonempty subsets of A;
(1) every element of A is in some element of C ; and
(2) if two elements of C have a nonempty intersection, then they are equal
![[Pasted image 20250312200604.png|300]]

C is a set of nonempty subsets S ⊆ A such that every element of A is in exactly one
S ∈ C 
C is a set of mutually disjoint nonempty subsets of A whose union is A.
### Partial orders and total orders



A/~ is called the quotient of A by ~. It is the set of all equivalence classes with respect to ~
A/~ = {[x] : x $\in$ A}
For instance, A/= <=> {{x} : x $\in$ A}

![[Pasted image 20250223220105.png]]


![[Pasted image 20250223215809.png]]

Theorem 6.2.5. Let ∼ be an equivalence relation on a set A. For all x, y ∈ A,
x ∼ y ⇔ [x] = [y].

![[Pasted image 20250223215831.png]]

**S is not symmetric because (1, 1) S (2, 2) but (2, 2) /S (1, 1), for instance**
##### Antisymmetry and totality

R is antisymmetric if ∀x, y ∈ A (x R y ∧ y R x ⇒ x = y)
This means that for relation R on A, 

Partial order if R is reflexive, antisymmetric, and transitive.
Graphically, you can picture a relation R as a directed graph whose vertices are the elements of A, and where there is a directed edge from x to y if $xRy$ For an antisymmetric relation, whenever there is a directed edge from x to y and also from y to x, those two points must actually be the same vertex. In other words, you never see two different vertices with arrows going back and forth between them.

**It is not antisymmetric because, for example, we have (a, b) ∈ R and (b, a) ∈ R, but 
a != b.**

**A total order is always a partial order.**

R is a (non-strict) total order or a (non-strict) linear order if R is a partial order and
every pair of elements is comparable, i.e.,
∀x, y ∈ A (x R y ∨ y R x)
When you represent a total (or linear) order as a directed graph, you can arrange the elements in a single “line” (a chain). Every pair of distinct elements xxx and yyy is connected in one direction or the other, so for any two nodes there is exactly one edge between them (pointing from the smaller to the larger).


##### Well-Ordering Principle

The **well-ordering principle** (often stated in the context of the set of natural numbers N\mathbb{N}) is the assertion that:

> Every nonempty subset of the natural numbers has a least (smallest) element.

In other words, if you take any nonempty set S⊆NS\subseteq \mathbb{N}, there is some element m∈Sm \in S such that m≤sm \leq s for all s∈Ss \in S.

This principle is closely related to the principle of mathematical induction. In fact, they are logically equivalent in standard treatments of number theory (the Peano axioms).


![[Pasted image 20250311203350.png]]

![[Pasted image 20250311203221.png]]





### Proving
**Reflexive**
Prove (x,y) R (x,y)

**Symmetric**
Prove x R y => y R x
Prove (x,y) R (z,w) => (z,w) R (x,y)

**Antisymmetric**
Let $(x_1,y_1)R(x_2,y_2)$ and $(x_2,y_2)R(x_1,y_1)$. Prove that $x_1 = x_2$ and $y_1 = y_2$

**Transitive**
Let $$(x_1,y_1),(x_2,y_2),(x_3,y_3) \text{ such that } (x_1,y_1)R(x_2,y_2) \text{ and } (x_2,y_2)R(x_3,y_3)$$
Show that $$(x_1,y_1)R(x_3,y_3)$$



Here’s one concrete example:

- Let A=Z (the set of all integers).
- Define the relation ∼  on Z  by saying x∼y if and only if x−y is divisible by 3.

This is an equivalence relation. Then
$$A/\sim \;=\;\{\,[x] \,:\, x \in \mathbb{Z}\}\,$$

is the set of equivalence classes (sometimes called _cosets_). Concretely, there are three distinct equivalence classes:
$$[0] = \{\dots, -6, -3, 0, 3, 6, \dots \}$$
$$[1] = \{\dots, -5, -2, 1, 4, 7, \dots \}$$
$$[2] = \{\dots, -4, -1, 2, 5, 8, \dots \}$$

$$A/\sim \;=\;\{\, [0], [1], [2] \}.$$
The symmetry of a relation R on A states that ∀x, y ∈ A (x R y ⇒ y R x). The
attempt claims that this implies ∀x, y ∈ A (x R y ∧ y R x). This is not justified
(and actually not true)

![[Pasted image 20250312211543.png]]

Reflexive = Transitive and Symmetric 

##### Some relations
Let R denote the divisibility relation on Z+, i.e., for all x, y ∈ Z+,
x R y ⇔ x | y.
Then R is reflexive, not symmetric, but transitive.



Let S denote the subset relation on a set U of sets, i.e., for all x, y ∈ U ,
x S y ⇔ x ⊆ y.
Then S is reflexive, may not be symmetric (when U contains x, y such that x ⊊ y), but is
transitive


x R1 y ⇔ x ⩽ y. => Reflexive, not symmetric, transitive
x R2 y ⇔ x<y => not reflexive, not symmetric, transitive

One counterexample is the relation R = {(0, 0), (1, 1)} on the set A = {0, 1}
**This is equivalent to drawing out the arrow diagram and making it into set**