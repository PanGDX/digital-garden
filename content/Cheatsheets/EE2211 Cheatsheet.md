
A linear function needs to satisfy the properties of homogeneity and addivity

![Local picture](../Media/Pasted%20image%2020260313074546.png)
Rows of X = data points 
Columns of X = features
w value = weight for EACH FEATYRE
![Local picture](../Media/Pasted%20image%2020260313083222.png)
![Local picture](../Media/Pasted%20image%2020260313075411.png)
## Starting Definitions
Linear functions are a subset of affine functions that pass through the origin. Affine functions are $f(x_1,x_2...)=Ax_1+Bx_2+...+constant$

![Local picture](../Media/Pasted%20image%2020260308114505.png)
Thus a linear function MUST pass through the origin

Data wrangling, or data munging, is the process of cleaning, structuring, and transforming raw, messy data into a usable format for analysis, visualization, or machine learning
Data validation is the process of ensuring data is accurate, complete, and secure before it is used or stored, typically by checking that it conforms to predefined rules, formats, and ranges

argsmax/min
![Local picture](../Media/Pasted%20image%2020260308114553.png)


![Local picture](../Media/Pasted%20image%2020260124145655.png)
![Local picture](../Media/Pasted%20image%2020260308110715.png)
Regression models predict continuous numerical values where order matters (e.g., predicting temperature, price, or age)
Because regression deals with continuous numbers, it interprets the distance between numbers as meaningful. In the numerical mapping above, the model would assume that the difference between "Stop" (3) and "OK" (2) is exactly the same as the difference between "OK" (2) and "Thumbs Up" (1).

In machine learning, the distinction between supervised and unsupervised depends on whether the "right answers" (labels) are provided to the system beforehand.
- **No Pre-defined Labels:** Jack isn't being given a "training set" of stones where a teacher says, "This specific shade is called 'Ruby Red' and this one is 'Sky Blue'."
    
- **Grouping by Similarity:** Jack is looking at the stones and putting them into piles based on how similar they look to one another. Whenever you **group** data based on inherent patterns or features (like color, shape, or size) without being told what the groups are beforehand, you are performing **Clustering**.

- **Unsupervised Learning** is used when you have input data but no corresponding output labels. The system must find the underlying structure, patterns, or outliers on its own. Anomaly detection (finding data points that deviate significantly from the norm) using unlabeled data is a classic unsupervised learning task.
    
- **Supervised Learning** requires a dataset where the "answers" are provided (e.g., thousands of video clips explicitly labeled as "normal driving" or "sudden lane change" by a human).
    
- **Reinforcement Learning** involves an agent learning to make decisions by taking actions in an environment to maximize some notion of cumulative reward (like training an AI to play a game or physically steer the car), rather than just detecting patterns in static data.
Reinforcement Learning (RL) requires an active **agent** that interacts with an **environment** by taking **actions**.
- Simply observing a video feed to detect a pattern is passive. The model is just analyzing data.
- For this to be RL, the AI would actually have to be driving the car (taking actions like steering or braking) and observing how the environment changes based on what it did.
- In RL, the model learns through trial and error based on **rewards** and **punishments**.

![Local picture](../Media/Pasted%20image%2020260308110749.png)
- Inductive is probability and statistics, Deductive is rule-based reasoning


A computer program is said to learn
- from experience E
- with respect to some class of tasks T
- and performance measure P,
According to Tom Mitchell’s classic definition, a computer program is said to learn from experience **E** with respect to some class of tasks **T** and performance measure **P**, if its performance at tasks in **T**, as measured by **P**, improves with experience **E**.

For your COVID-19 prediction algorithm, these components are defined as follows:
- **Outcomes (or sample points):** These are the most basic, fundamental results of a random experiment. They are mutually exclusive and **not decomposable**. For example, if you roll a standard six-sided die, rolling a "3" is a specific, undecomposable outcome.
    
- **Events:** An event is a set (or collection) of outcomes. Because an event can contain multiple outcomes, it **is decomposable**. For example, rolling an "even number" is an event. This event can be decomposed into the simpler, fundamental outcomes: rolling a 2, rolling a 4, or rolling a 6.
#### 1. Task (T)
The specific goal or "job" the algorithm is performing.
*   **Definition:** Classifying whether a patient is COVID-19 positive or negative based on input features.
*   **Details:** Taking input data (age, health conditions, fever, cough, etc.) and outputting a prediction (Infected vs. Not Infected).

#### 2. Performance (P)
The quantitative metric used to judge how well the algorithm is doing.
*   **Definition:** The accuracy or error rate of the predictions.
*   **Details:** Common metrics would include:
    *   **Accuracy:** The percentage of total patients correctly diagnosed.
    *   **Recall (Sensitivity):** Specifically, how many actual COVID-19 cases the model successfully caught (crucial in medicine to avoid missing sick patients).
    *   **Precision:** How many of the patients predicted as "infected" actually were infected.
    *   **F1-Score:** A balance between Precision and Recall.

#### 3. Experience (E)
The data or "training material" the algorithm uses to learn.
*   **Definition:** A historical dataset of medical records.
*   **Details:** A collection of past patient files where the particulars (age, health history) and symptoms (fever, cough, headache, etc.) are already paired with a **known outcome** (e.g., the result of a PCR or ART test confirming whether they actually had COVID-19).



Causality, or causation is:
- The influence by which one event or process (i.e., cause) contributes to another (i.e. effect),
- The cause is partly responsible for the effect, and the effect is partly dependent on the cause
- There is also probable cause
- One popular way to causal data analysis is RCT - Randomized Controlled Trials
- **Causality is a statistical relationship meaning that the relationship is not deterministic. You smoke => More likely to get cancer, but not a guaranteed**

**Correlation $\neq$ Causation.** (Causation is a subset of correlation).
- correlation is any statistical relationship, whether causal or not, between two random variables.
==Yes, causation is considered a subset of [correlation](https://www.google.com/search?client=ubuntu-sn&channel=fs&q=correlation&ved=2ahUKEwiZusDy86WSAxW6R2wGHVSDIpQQgK4QegQIAhAC)==. While all causal relationships are correlations (A causes B implies A and B are correlated), not all correlations are causations, as [correlations](https://www.google.com/search?client=ubuntu-sn&channel=fs&q=correlations&ved=2ahUKEwiZusDy86WSAxW6R2wGHVSDIpQQgK4QegQIAhAD) can arise from coincidence, third-variable confounding, or reverse causality


Simpson's paradox is a phenomenon in probability and statistics, in which a trend appears in several different groups of data but disappears or reverses when these groups are combined
![Local picture](../Media/Pasted%20image%2020260308112209.png)




| Type                | Data Access              | Goal                                 |
| :------------------ | :----------------------- | :----------------------------------- |
| **Supervised**      | Features $x$, Labels $y$ | Find function $f(x) \to y$           |
| **Unsupervised**    | Features $x$ only        | Clustering, Dimensionality Reduction |
| **Semi-supervised** | Mix of labeled/unlabeled | Leverage cheap unlabeled data        |

Feature extraction is a dimensionality reduction process that transforms raw, high-dimensional, or complex data (like images, audio, or text) into a smaller, manageable set of meaningful numerical features
- **Dimensionality Reduction:** It reduces the number of variables in a dataset, which helps in overcoming the "curse of dimensionality" and improves model performance.
- **Transformation, Not Selection:** Unlike feature selection, which merely picks a subset of original features, extraction creates _new_ features by combining or transforming the original data points.

![Local picture](../Media/Pasted%20image%2020260125130159.png)

You already know the resulting distribution's mean and std. You just need to know the Z value where the x landed at

## Dataset Types
(feature vectors x_i, label y_i)
- Classification
	- supervised learning
	- labels y_i are finite
	- find a function that accurately predicts labels given new samples
- Regression
	- supervised learning
	- labels y_i can be in an infinite set. This label is usually the target variable or outcome
	- Find a regressor function such that given a new x', the y' is well predicted
- clustering
	- unsupervised learning
	- no access to labels y_i
	- only feature vectors x_i
- a combination can be done. This would be considered semi-supervised

## Types of data and data processing
Two ways you can look at the data. Any data is a combination of both. 

- Numerical 
	- Discrete
	- Continuous
- Categorical
	- Nominal
		- Comes with labels like dog and cat
		- To convert it into labels that the computer can process, use one-hot encoding which converts the data into vectors of binary features
			- isDog, isCat, etc
		- **mode, frequency distribution**
	- Ordinal
		- Discrete and ordered units
		- Order matters
		- **mode, frequency distribution, median**
	- Both ratio and interval can be discrete or continuous
		- Number of people in household => Discrete, ratio
		- Credit scores in the US => continuous, interval

![Local picture](../Media/Pasted%20image%2020260308111107.png)
![Local picture](../Media/Pasted%20image%2020260308105938.png)
Temperature is an interval when measured using Celsius, but a ratio when measured with Kelvin. This is because Celsius lacks a true zero point while Kelvin does have a true zero point.
Interval data can be **both continuous and discrete**, depending on the context, although it is frequently treated as continuous


- Data wrangling
	- Binary coding => Red, Green, Blue => [1,0,0] for red, [0,1,0] for Green, etc
	- This is called one hot encoding
	- Normalizing data
	- Data cleaning: 
		- Removing outliers
		- Handling missing features like NA or 0
		- Different methods to handle this:
			- Removal
			- Using a learning algorithm to predict missing feature values
			- Data imputation
				- Option 1: Replace the missing value of a feature by an average value of this feature in the dataset:
				- Option 2: Replace the missing value with a value outside the normal range of values.
					- This is commonly used because it teaches the algorithm to learn what is best to do when the feature has a value significantly different from regular values


- SVD
	- Singular value decomposition of a matrix
	- SVD is a technique that factorize matrices into three constituent matrices, uncovering latent structures, reducing noise and compressing data
	- Very important for dimensional reduction and seeing which parameters to keep

- Normalising data
	- The scale of the data may be different. For instance, income may range in the thousands while people per household is 1-10. Models give greater importance to bigger numbers and so we have to normalize data
	- Two ways
		- Z-score scaling
			- Calculate the empirical mean and standard deviation of each feature x-i
			- Create normalized feature
			- ![Local picture](../Media/Pasted%20image%2020260201115549.png)
			- A lot of consideration due to the notion of unbiased estimator and the assumptions we need to take
		- Min-max scaling
			- ![Local picture](../Media/Pasted%20image%2020260201115657.png)
			- Simple. Straightforward

## Probability and Estimation
![Local picture](../Media/Pasted%20image%2020260308111753.png)
- Observation $\ne$ true probability
	- $$Pr(X=x_i,Y=y_i)=\frac{m_{ij}}{m} \ \ IFF \ \ m \to \inf$$
	- Take a coin toss. Toss it 3 times. The probability is NOT 0.5. It only approaches 0.5 as you toss more and more
- BUT for these observations $Pr(X=x_i, Y=y_i)$ product rule still applies
	- ![Local picture](../Media/Pasted%20image%2020260201120151.png)
- Bayes' rule
- See Stats ST2334 cheatsheet for a more comprehensive overview
$$P(y|x) = \frac{P(x|y) \times P(y)}{P(x)}$$
- CDF
	- ![Local picture](../Media/Pasted%20image%2020260201120215.png)
![Local picture](../Media/Pasted%20image%2020260201115106.png)

We describe a random experiment by describing its procedure and observations of its outcomes.
- Outcomes are mutual exclusive in the sense that only one outcome occurs in a specific trial of the random experiment. This also means an outcome is not decomposable.
- All unique outcomes form a sample space. A subset of sample space 𝑆, denoted as 𝐴, is an event in a random experiment 𝐴 ⊂ 𝑆, that is meaningful to an application.
- For Discrete random variable, the probability distribution is called PMF - probability mass function. For CRV, it is pdf - probability density function

**Maximum Likelihood Expectation**
- We do not have access to the underlying distributions
- But we do have sample data and need to generate or estimate some parameters

**Likelihood: used when you don't know the rules. Probability: used when you know the rules and distributions**
How MLE works in laymans term:
- Given the data I observe, I calculate the likelihood of each event occurring and from that I generate estimates for the mean and variance, as well as the parameter that when applied to the system has the highest likelihood that x would happen.
- You might then observe that MLE is not useful for small sample sizes because the probability is not accurate. To resolve this, use Maximum A Posteriori (MAP) to estimate an unknown quantity by finding the mode of the posterior distribution. What the fuck this means? I don't know

1.  **MLE (Maximum Likelihood Estimation):**
    *   Finds parameters that maximize the likelihood of the observed data.
    *   Best for **Large** sample sizes ($m \to \infty$).
2.  **MAP (Maximum A Posteriori):**
    *   Finds mode of the posterior distribution.
    *   Incorporates a **Prior**. Best for **Small** sample sizes.
    * parameter value $\theta$ that maximizes the posterior density
    * ![Local picture](../Media/Pasted%20image%2020260308105116.png)
    * 

## Linear Algebra The Important Stuff

a few samples = low m
m < d

### System Types ($Xw = y$)
Given matrix $X$ (size $m \times d$):
*   **Square ($m=d$, Full Rank):** Unique solution. Invertible.
*   **Overdetermined ($m > d$, "Tall"):** More equations than unknowns.
    *   Usually no exact solution.
    *   **Technique:** **Least Squares Estimation**.
    *   **Formula:** $w = (X^T X)^{-1} X^T y$
    *   *Note:* Uses **Left Inverse**. **This** means $Y$ for $YA=I$ exists
*   **Underdetermined ($m < d$, "Fat"):** Fewer equations than unknowns.
    *   Infinite solutions.
    *   **Technique:** **Least Norm Solution** (smallest length vector).
    *   **Formula:** $w = X^T (X X^T)^{-1} y$
    *   *Note:* Uses **Right Inverse**. This means $Y$ for $AY=I$ exists
![Local picture](../Media/Pasted%20image%2020260308113911.png)



### Statement 2: Given four samples of two-dimensional data points X and the corresponding target output y, the 2nd order polynomial regression system is an under-determined system.
**Answer: True**

**Explanation:**
To determine if a system is under-determined, we must compare the number of samples ($N$) to the number of parameters/features ($P$) to be learned.
*   **Number of samples ($N$):** 4 (given).
*   **Number of parameters ($P$):** For a 2nd order polynomial with 2 features $(x_1, x_2)$, the terms are:
    1.  Bias (1)
    2.  Linear terms ($x_1, x_2$)
    3.  Interaction term ($x_1x_2$)
    4.  Squared terms ($x_1^2, x_2^2$)
    *   **Total $P = 6$ parameters.**
    *   *Formula check:* $\binom{n+d}{d} = \binom{2+2}{2} = 6$.

**Conclusion:**
Since the number of samples ($N=4$) is **less than** the number of parameters ($P=6$), the system is **under-determined**. You have more unknowns than you have equations (observations).
## Linear Algebra ALL CONTENT
- Linearly independent
	- ![Local picture](../Media/Pasted%20image%2020260201122148.png)
- Basis
	- ![Local picture](../Media/Pasted%20image%2020260201122158.png)
- Null space
- Range/Column space
	- Equivalence (column rank = row rank)
- rank and dimension
- rank nullity rule

![Local picture](../Media/Pasted%20image%2020260201122217.png)
- **Nature of solutions: overdetermined and underdetermined**
	- If matrix X is square and full rank, then inverse X exist and we can solve Xy=b easily
	- BUTTTT it is often not the case!
		- Overdetermined = lots of labels y_i, few parameters
			- For instance, temperature sensors. Parameters may include cloud coverage, previous day's temperature, wind speed, etc (~10 parameters lets say) but the amount of temperature data measured can be significantly greater (hundreds in a day)
		- Underdetermined
			- Few examples, high parameters
			- Image recognition (every pixel is a parameter)
			- Natural language processing
	- So how do you handle them?
		- ![Local picture](../Media/Pasted%20image%2020260201123333.png)
		- **Rouche Capelli Theorem**
		- Step 1: Augment the matrix X
			- ![Local picture](../Media/Pasted%20image%2020260201123041.png)
		- Step 2: Compare ranks. THIS APPLIES TO ANY AND ALL MATRIX SIZES
			-   ![Local picture](../Media/Pasted%20image%2020260201123137.png)
	- Usual case:
		- Overdefined => No solution $\vec w$
			- Use least square estimation for m > d
				- X is a tall vector and overdefined
				- Try to minimize $$||X\vec w - \vec y||^2$$
				- ![Local picture](../Media/Pasted%20image%2020260201123550.png)
		- Underdefined => Infinite solutions $\vec w$
			- Use least norm solution for m < d 
				- X is a fat  vector and underdefined
				- There a infinitely many solutions. The "Least Norm" solution is the solution that has the smallest possible length
				-![Local picture](../Media/Pasted%20image%2020260201123651.png)
	- **y_pred = W_l * w*
	- Solutions of LES

![Local picture](../Media/Pasted%20image%2020260211094947.png)
det MAY be 0!




### Left and Right invertible
- If nxn, it is both left and right invertible
- If it is a tall matrix mxn where m>n, it is left invertible
	- need to check, may not exist,
	- use $X^T*X$ and calculate the DET
- If it is a wide matrix, mxn, where m<n, it is right invertible
	- use $X * X^T$ and calculate the DET



## Differentiation of Vectors and Matrices
If f(x) is a scalar function
![Local picture](../Media/Pasted%20image%2020260308114810.png)
If f(x) is a vector function
![Local picture](../Media/Pasted%20image%2020260308114846.png)

![Local picture](../Media/Pasted%20image%2020260308114936.png)
Common rules for vector-matrix differentiation
- ![Local picture](../Media/Pasted%20image%2020260308115019.png) 
## Ridge Regularization and Regression


### Statement 1: The ridge regression can be applied to multi-target regression.
**Answer: True**

**Explanation:**
Ridge regression is easily extended to multi-target (or multi-output) problems. If you have multiple target variables for each sample (i.e., $y$ is a matrix instead of a vector), the algorithm simply solves for a matrix of weights $W$. This is mathematically equivalent to running a separate ridge regression for each target variable independently, but it can be computed efficiently using the same closed-form solution: $W = (X^T X + \lambda I)^{-1} X^T Y$.

---

### Linear Regression with One or More Outputs
- Learns a model which is a LINEAR combination of features of input
- Offset term b allows line or plane to shift and better fit data
	- Helps the model fit the data more accurately
	- Bias is learnt automatically during training
	- Does not change linearity
- Objective of linear regression:
	- ![Local picture](../Media/Pasted%20image%2020260308134226.png)
- Lost function:
	- measures error for a single data point
	- $L_i = (\hat{y_i} - y_i)^2$ => Square error loss
	- There are different loss functions that can be used
- Cost function: 
	- AVERAGE of all individual losses = sum of all lost functions, divided by the number of points![Local picture](../Media/Pasted%20image%2020260308134412.png)
	- MINIMIZE THIS cost function
Loss function is for a single training sample, cost function is the average across all training samples

![Local picture](../Media/Pasted%20image%2020260308134507.png)


**Remember: X is the data, w is the weight, Y is the prediction**
![Local picture](../Media/Pasted%20image%2020260308135213.png)

- Linear regression with multiple outputs
	- ![Local picture](../Media/Pasted%20image%2020260308134825.png)



## Linear & Models for Classification

- Binary classification
	- Suppose there are two classes, positive and negative
	- ![Local picture](../Media/Pasted%20image%2020260201211508.png)
	- Use dot product to find the similarity and magnitude of similarity
		- y is true if $xw$ > 0
		- y is false if $xw$ < 0
- Multiclass classification
	- Do one hot encoding
	- ![Local picture](../Media/Pasted%20image%2020260201212245.png)
	- Given a new test sample $x_{test}$ we declare the class to be 
		- ![Local picture](../Media/Pasted%20image%2020260201212315.png)

The column of "1"s is a clever mathematical trick used to include a **bias term** (also known as the y-intercept) while keeping the math clean and simple.
- One row of x is one data sample
- A column of X is a feature. The first column is the multiplier for the weight
- A row of W is the weight for the first feature. The first row is the weight bias


![Local picture](../Media/Pasted%20image%2020260308142612.png)
![Local picture](../Media/Pasted%20image%2020260308142606.png)



- Polynomial model
	- Some datasets are not linearly separable
		- For instance XOR
	- Use nonlinear classifier by taking the products of components
	- This exponentially increases the number of features but that can be solved using kernels
![Local picture](../Media/Pasted%20image%2020260308142850.png)
![Local picture](../Media/Pasted%20image%2020260308142842.png)
![Local picture](../Media/Pasted%20image%2020260308142914.png)

![Local picture](../Media/Pasted%20image%2020260308143332.png)
4 samples = 4 rows
single feature => d = 1 => 2nd order => d x 2 = 2



Suppose we want to build a single linear regression model with three input features to predict three different classes. The model has 12 parameters to learn
- Each class has its own set of weights: one weight per feature - 3 feature per class
- 3 class = 9
- each class has 1 bias
- total: 12

### Ridge Regression
- Ridge regression is the overall linear modeling method that uses regularization to improve model generalization
	- Ridge Regularization is the technique of using $\lambda w^2$ 


- Issue: $X^T X$ is not always invertible. By doing regulization, it is ALWAYS invertible for any $\lambda > 0$
![Local picture](../Media/Pasted%20image%2020260308142422.png)

*   **Goal:** Minimize Error + Penalty on weights.
	* Shrinks the regression coefficients by penalizing large weights
*   **Cost Function:** $J(w) = ||Xw - y||^2 + \lambda ||w||^2$
*   **Closed Form Solution:**
    $$w = (X^T X + \lambda I)^{-1} X^T y$$
    *(The $\lambda I$ term ensures the matrix is invertible)*.
*   **Primal:** Focuses on $w$. Complexity depends on features ($d$).
*   **Dual:** Uses Lagrange multipliers. Complexity depends on samples ($m$).
*   **Kernel Trick:** Allows computation in infinite dimensions (e.g., RBF) without actually transforming the data, by calculating dot products directly.



![Local picture](../Media/Pasted%20image%2020260308143843.png)
- Suppose m>d (tall vector)
	- We aim to find a good weight vector $\vec w$ such that $X\vec w$ is close to $\vec y$ 
	- But it is possible that there are multiple valid $\vec w$ that gives the same error
		- ![Local picture](../Media/Pasted%20image%2020260201210827.png)
		- We want to minimize 
			- ![Local picture](../Media/Pasted%20image%2020260201210913.png)
	- The aim of ridge regularization is to force $w$ to be small
		- ![Local picture](../Media/Pasted%20image%2020260201211031.png)
	- **This stabilizes or robustify the solution as large values of w do not lead to favorable generalization on new test examples**
- Two methods
	- Primal vs Dual
		- Primal focuses on w and finds w. The compleity depends on the number of features d
		- Dual uses lagrange to rewrite the problem. The complexity depends on the dimension of the label (m)
	- ![Local picture](../Media/Pasted%20image%2020260308143832.png)
- Kernel trick
	- n dimensions? infinite dimensions? No problem, using the kernel trick I do not have to interact with higher dimensions
		- For instance, the radial basis function which maps to an infinite dimension. Without the kernel trick, it is impossible to store and compute.

![Local picture](../Media/Pasted%20image%2020260308143903.png)
Same thing for polynomial, just replace $X$ with $P$
![Local picture](../Media/Pasted%20image%2020260308143953.png)


MSE
![Local picture](../Media/Pasted%20image%2020260312130226.png)
### Metrics
*   **Accuracy:** Overall correct %.
*   **Recall (Sensitivity):** Ability to find positive cases (Crucial for medical/COVID).
*   **Precision:** Quality of positive predictions.
*   **F1-Score:** Harmonic mean of Precision and Recall.
#### Overfitting and Bias Variance Tradeoff
- Overfitting for polynomial regression
	- If we choose a model that is either too simple or too complex, predictions made on new data points (that are not part of the training set) will be bad, i.e., the MSEs of predictions on new data points will be high. 
	- **We can choose by cross-validation**
- Bias-Variance Tradeoff for Linear models with Ridge Regression
	- Least squares vs ridge regression
	- Least square has zero bias **but the variance can be very high**
	- Ridge regression has bias > 0 but it reduces bias
	- ![Local picture](../Media/Pasted%20image%2020260202220955.png)
		- Bias Variance Formula
	- The bias quantifies the error caused by simplifying assumptions in the model. For example, when we use a linear function to approximate a model which is inherently quadratic, we will suffer some bias.
	- The variance quantifies how much the estimated solution fluctuates around its mean.
	- The irreducible error quantifies the measurement noise inherent in the new test sample
*   **Bias:** Error from simplifying assumptions (Underfitting).
*   **Variance:** Error from sensitivity to small fluctuations in training set (Overfitting).
*   **Ridge Regression Effect:** Increases Bias slightly, but significantly **reduces Variance** to lower total error.

#### Examples of Loss functions and regularizers
- Loss functions and regularizers
	- ![Local picture](../Media/Pasted%20image%2020260201214350.png)
	- The most common is $l_2$ loss which is the least squared
		- $|y_t - y|^2$
	- $l_1$ loss
		- $|y1-y|$
	- ![Local picture](../Media/Pasted%20image%2020260202220755.png)

- Gradient descent
	- Choosing an optimization algorithm given a function $C:\mathbb{R}^d \to \mathbb{R}$ and we would like to find a $w$ that minimizes $C(w)$
	- We assume that C is differentiable. If it is not, there are likely techniques to approximate
		- Finite difference
		- Coordinate descent. Picking one variable and observing the change, one by one
		- Genetic algorithm
	- Step 1: Walk down the direction $-\bigtriangledown C(w)$ to 'go down' the curve the fastest way
	- From this, we only know the direction. How about 'how far' to go in this direction?
		- This is dictated by 'step size'
		- After walking a distance of $n$, stop and find another direction
	- After a while, we terminate the walk based on a specific crtieria
		- ![Local picture](../Media/Pasted%20image%2020260202221638.png)

**LOSS FUNCTION**


Training error and test error are used to evaluate how well a model fits the data. By comparing these errors, we can establish whether the model is overfitting or underfitting or just right.
The most reliable indicator of model quality is its performance on unseen data.

An overly complex model tries to capture noise or small fluctuations in data
Possible issue 1: The model is too complex for the given data
Solutions:
- Collect more training data
- Use a simpler model
- Use regularization
Possible issue 2: There are too many features and too few data points ie the system is very under-determined
- Collect more training data
- Reduce the data dimensionality (e.g., feature selection)
- Regularization



What causes underfitting
- The model is too simple
- The features are not informative enough
	- If the dataset's features lack relevance or meaning, the model will fail to learn any important patterns. Garbage in, garbage out.
		- This is where domain expertise steps in. For example, a team might want to train a model for a robot based on telemetry data of human movements. We observe that the labs themselves are primarily concerned with the QUALITY of the data - enhancing the hand tracking, the body tracking, etc - rather than just collecting more data. 



### Feature Selection
- Through feature selection, we aim to eliminate irrelevant or redundant features. This increases the data quality and improves the efficiency of training

**Method 1: Selecting features with Pearson's coefficient**
- Given features X, predict Y
- Compute Pearson's correlation coefficient between X and Y
- Rank based on the coefficient's magnitude
- Select the top N features

Feature selection procedure
- Step 1: feature selection in training set only
- Step 2: train/fit model on training set using the selected features
- Step 3: evaluate the trained model on the test set using the same selected features

### Regularization 
As we know, regularization adds a penalty cost to discourage overly complex models

### Bias Variance Tradeoff
- Suppose you have a variable X
- Bias is the average deviation of all samples from the real mean of X
- Variance is the degree of spread of all samples about the mean of the samples
![Local picture](../Media/Pasted%20image%2020260403062614.png)


Bias: Measures how far, on average, the model’s predictions are from the true
value (the center of the target).
• High bias → predictions are systematically off-target (e.g., consistently far from the center).
• Low bias → predictions are close to the center on average

Test error = $$Bias^{2}+Variance +Noise$$
**Variance refers to the variability of prediction models across different training sets**
![Local picture](../Media/Pasted%20image%2020260403062955.png)
For example, the above is a graph that plots 4th order and 2nd order polynomials fitted on randomly sampled data generated from a 2nd order polynomial (with noise added). You can see that 2nd Order polynomials have a lower variance because their spread is low. **How is variance calculated here?**

Variance is the expected square deviation of a model's prediction $\hat{f}(x)$ from its average prediction over multiple training sets:
$$
Var(\hat{f(x)}) = E[\hat{f(x)} - E[\hat{f(x)}]^2]
$$



![Local picture](../Media/Pasted%20image%2020260403063157.png)

Loss function: Measures the error for a single training example. It tells us how different the model’s prediction is from the true value for one data point.
Cost function: The cost function is built from the loss function. It is the average or total loss over the entire training dataset. It summarizes how well the model performs across all training examples.

### Optimisation
Machine learning is fundamentally an optimization problem. The model is attempting to optimize to reduce the error as far as possible without losing generalizability. 

Different model function $f$, loss function $L$, regularization $R$ give rise to different learning algorithms. For more complex $f,L,R$, the cost function can be complicated.

Gradient descent is an optimization method used to iteratively minimize the objective function to obtain the best parameters $w$

Gradient of a function is a vector of partial derivatives
![Local picture](../Media/Pasted%20image%2020260403064129.png)

Common stopping/convergence criteria:
- Maximum number of iterations is reached.
- The percentage or absolute change in cost is below a threshold.
- The percentage or absolute change in the parameters w is below a threshold
The direction and step size to move towards minimizing the cost is given by the product of the learning rate and the gradient
![Local picture](../Media/Pasted%20image%2020260403064248.png)

- What if:
	- Learning rate is too big?
		- Overshoot the local minimum
		- Slow convergence or may never converge
	- Learning rate is too small?
		- Slow convergence

- Limitations and factors that affect gradient descent outcomes
	- Initial position
		- The starting point matters significantly because it can determine whether the model will be in a local minima
	- Learning rate (step size) also matters a lot because of the reasons given above
	- The gradient descent may get stuck in the local minima and miss the global minimum
	- **Gradient descent requires the function to be differentiable or at least have a well-defined gradient to travel on. If the data is segmented and fractured or undifferentiable even through approximation, it is difficult**

### Different ML Models
- $sign(w^Tx)$ is commonly used - the value is either 1 or 0
- $\sigma (w^Tx)$ is also commonly used - the value is between 1 or 0
	- Special property:
		- If the z is large, sigmoid is ~1
		- If the z is small, sigmoid is ~0
		- Sigmoid is continuous in the middle too
	- Differentiable so we can train the model using gradient descent
	- Gives output that are probabilitistic, giving confidence in predictions rather than hard class labels
![Local picture](../Media/Pasted%20image%2020260403065211.png) 

**Different loss functions also give rise to different ML models**
- Squared error loss
	- Not good for classification
		- Squared error loss focuses on matching numerical values
			- Category labels like +1 for `Cat` and -1 for `Dog` is treated as exact mathematical targets on a number line rather than representations of two different categories. This is an issue because in classification the NUMBER doesn't matter, as much as where the number is vis-a-vis the dividing line
		- Squared error loss does not explicitly encourage classification margin
			- How `far` the value is from the `dividing line`. The `further` the better
			- Because Squared Error focuses purely on matching the number +1 or -1: It actively discourages the model from creating a large margin.
				- If the model tries to push a prediction to be "safe", Squared Error will force the model to pull the prediction back down to exactly.
- Square error loss is designed for regression




**These are better for classification tasks**
- Binary loss where the loss is 0 or 1 based on the $f$ value
	- Issue: not differentiable
- Solutions:
	- Hinge loss
	- Exponential loss
![Local picture](../Media/Pasted%20image%2020260403065519.png)
## Decision Trees
- Decision tree is a **supervised learning technique** that can be used for both classification and regression problems
	- It captures complex rules automatically
	- Works with mixed data types and does not require feature normalization
	- Easy to interpret with a diagram

![Local picture](../Media/Pasted%20image%2020260403070137.png)
Depth, Decision Node, Root Node, Terminal/Leaf Node



- The intuition behind decision trees
	- A classification decision tree is a series of YES NO questions to ask
		- Imagine you have a bunch of data on whether you will be able to go out today for a picnic. For example: temperature, how crowded the park is, the chance of rain, etc
		- The objective **is to create a model that given NEW DATA will say with a certain level of confidence that you will be able to have a picnic today**
		- Clearly, the relationships here are no linear. 
		- Instead, we use Yes No questions to evaluate whether we will be able to host a picnic
		- The problem then is that you don't know which questions to ask first!
		- Solution? **Ask the most important questions first**
		- How do you know which are the most important questions? This can be calculated statistically. This importance is called 'gain of attribute'
		- After you train the model, you will get a misclassification rate. If that rate is acceptable, it is ready to be used!
	- A regression decision tree is quite different but starts from the same concept
		- Imagine an XY plane and you need to predict that given some data, what the resulting prediction will be
		- The plane is divided into regions. Each region has an average value based on the points that are contained within it.
		- How to split the regions? Split for every feature j and threshold value s
		- Find feature j and split point s that minimizes MSE
		- ![Local picture](../Media/Pasted%20image%2020260203134911.png)


To decide HOW to split, we need to first find the node impurity
Node impurity is a measurement of how mixed the class labels are within a node. Pure nodes contain mostly one class. Decision trees are tasked with choosing the optimal split that reduces the impurity the most (`cost`) making child nodes increasingly pure

There are three ways to measure impurity:
- Gini
- Entropy
- Misclassification rate

![Local picture](../Media/Pasted%20image%2020260403113110.png)


**Gini impurity tells us how mixed up the classes are. A low score means most items are the same class. A high score means most items are jumbled together**

![Local picture](../Media/Pasted%20image%2020260403113327.png)

Note how the overall Gini uses the weighted sum (much like expected value).


**Entropy is a similar story. A low score means most items are the same class. A high score means most items are jumbled together**
![Local picture](../Media/Pasted%20image%2020260403113423.png)

Misclassification rate is the same again. Low value = mostly the same class. High value = Many classes mixed up
![Local picture](../Media/Pasted%20image%2020260403113454.png)
![Local picture](../Media/Pasted%20image%2020260403113509.png)


### Building a Classification Tree
- Objective: Low complexity (small depth value/fewer nodes), good performance (high classification accuracy)

**Greedy Solution: This generates a near-optimal tree in a reasonable amount of time. Greedy means that the model makes the locally optimal choice at each step without considering future splits.**
![Local picture](../Media/Pasted%20image%2020260403113745.png)


### Building a Regression Tree
With multiple predictors of mixed types, polynomial regression becomes cumbersome, requiring manual feature engineering. Decision trees are more suitable because they naturally handle mixed data types and threshold-based rules.
Example: Clinicians testing a new drug and determining the predicted effectiveness of the drug based on the data of the patient and how much drug they give the patient. 

The key operation for regression tree is that at each split, we select **a feature** and an **associated threshold value** that minimizes prediction error

- Predicted Value = Average of samples in the leaf node
- Predicted error = mean squared error (MSE)
![Local picture](../Media/Pasted%20image%2020260403114118.png)
Explanation: We are looking at the `dosage` feature. We plot a graph of MSE based on the threshold of the dosage and how it affects the value of MSE given the data. Then we find the threshold with the lowest MSE

Now repeat this for all features.

Here's a more detailed calculation
![Local picture](../Media/Pasted%20image%2020260403114345.png)
**Note how the average conditional MSE is calculated using weighted sum**



Classification vs Regression Tree TLDR
![Local picture](../Media/Pasted%20image%2020260403114519.png)



Benefits and Issues with Decision Tree
- Benefits
	- Easy to visualise
	- Can work with a mix of continuous and discrete data
	- Less data cleaning required
	- Makes less assumption between the relationship between feature and target
- Issues
	- Prone to overfitting 
	- Trees can be unstable as small changes in training data results in different trees. This leads to high variance

**Solutions to address overfitting for decision tree**
- Set maximum depth for the tree
- Set a minimum number of samples for splitting a leaf node so that each node is not overfitted
- Set a minimum decrease in impurity so that a leaf node is not split just to improve impurity by a negligible amount
- Randomly look at a subset of features when considering a split

**Solutions to address variance/instability for decision tree**
- Take training set and perturb training set to generate M perturbed training sets
- Train one tree for each perturbed training set
- Average prediction across M trees or majority vote decides the outcome
##### What "Perturb" means: Bootstrapping

If you have an original dataset with `N` samples, you create a perturbed training set by **sampling `N` times with replacement** from that original set.
- **Same Size:** Each of the `M` perturbed training sets has the **same number of samples (`N`) as the original dataset.**
- **With Replacement:** This is the key. Because you sample with replacement, some rows from the original data will appear multiple times in a perturbed set, and some rows will not appear at all.
- **The Math:** On average, each perturbed training set contains about **63.2%** of the unique original data points. The remaining ~36.8% are duplicates.

![Local picture](../Media/Pasted%20image%2020260403115236.png)


### Random Forests
Bootstrapped dataset is the same size as original dataset
Bootstrapped dataset might contain repeated samples
Bootstrapped dataset might not contain some samples from original dataset
![Local picture](../Media/Pasted%20image%2020260403115329.png)


What is a random forest for? Reduce overfitting and improve prediction accuracy of a single decision tree by combining many trees

- Train each tree on a different bootstrap sample
- Each split, only considers a random subset of features
- This introduces diversity among tree so when their predictions are combined, overfitting is reduced
	- Classification: Take the majority vote
	- Regression: Take the average

![Local picture](../Media/Pasted%20image%2020260403115524.png)


- What if the decision tree is trash?
	- Use random forest
		- Create many decision trees
		- Pick random features to split the data with
		- Each tree makes a prediction
		- Combine the prediction. For classification, use majority voting. For regression, use average of all predictions
	- Use gradient boosted trees
		- _Gradient boosting_ is an ensemble learning algorithm that produces accurate predictions by combining multiple decision _trees_ into a single model.
		- Unlike random forests, which build trees in parallel, GBTs train trees in series, where each new tree focuses on correcting the mistakes of the previous ensemble.
	- Use manual feature engineering
		- Instead of using X1 and X2 separately, include X1 * X2
		- This could be because the data features are clearly related in some way
			- Temperature and Cloud Cover for instance
- Shannon Entropy
	- It is the 'amount of information' in a variable
		- Shannon entropy is defined as the average rate at which information is produced by a stochastic source of data
		- Imagine several buckets of red and blue balls. ![Local picture](../Media/Pasted%20image%2020260203134159.png)
		- The first bucket guarantees that you will be able to pick out a red ball. Bucket 1 thus gives us the most amount of information because we know if we pick from it, we are guaranteed to get a red ball. This is HIGH knowledge
		- High knowledge = low entropy
			- If molecules have many possible rearrangements, then the system has high entropy, and if they have very few rearrangements, then the system has low entropy.
		- Now let's play a game show. In this game show you want to pick out the same sequence twice.
			- First pick out: RRRB => Second pick out: RRRB
			- Clearly, for bucket 1, the probability of this occurring is 1
			- A higher value shows higher predictability, thus 'knowledge' and lower 'entropy'
			- To build the entropy formula you want to do the OPPOSITE
		- ![Local picture](../Media/Pasted%20image%2020260203134443.png)
- **The tree must be:**
	- Limited in depth
	- Not all leaf nodes must be a pure node
		- What is a pure node: ALL labels are the same. This means all data samples it contains belong to the same single class
			- A node with 10 YES and 0 NO samples
		- While the main objective of the decision tree is to recursively split data into increasingly pure child nodes, IT CANNOT ALL BE PURE because that would overfit the model
	- Small changes in the dataset should not result in drastically different trees





## Cross-Validation and Performance Metrics
- **Tuning Hyperparameters**
	- Split the dataset into equal 'folds'
	- Choose a hyperparameter or model type to compare
		- For example, depth of tree, maximum number of nodes, how many layers in the neural network
	- Run k folds of experiments using one part as validation and k-1 parts as training data. Each fold will have a different validation set.
	- Within each fold, train multiple models with different parameters or model types



	- Aggregate and calculate the average MSE/evaluation metric
	- Compare ALL MSE and pick the hyperparameter with the lowest average error


![Local picture](../Media/Pasted%20image%2020260403205022.png)

**But if we are not choosing parameters or model type, we can just segment into training and test data. No validation and k-fold needed.**
### Evaluation metrics
- Regression
	- Mean square error
	- Mean Absolute Error
- Classification
![Local picture](../Media/Pasted%20image%2020260403205305.png)

Recall = TP / TP+FN
Accuracy = TP+TN / Total
Precision = TP / TP + FP

It is important to look at all these metrics because sometimes a metric can be high (like accuracy) but it does not show the whole picture.

**Cost Matrix**
![Local picture](../Media/Pasted%20image%2020260403205412.png)

- Based on the scenario and data, we can manually assert that $C_{p,n} > , <, =, C_{n,p}$
	- For example, when developing a self-driving car system
	- False negative = Car keeps going
	- False Positive = Car stops
	- Which one should have a higher cost?

- For classification, these values of TP, TN, FP, FN will change based on the threshold function



- **ROC and AUC**
	- ROC - Receiver Operating Characteristic
	- TPR = True Positive / Total Positives
	- FPR = False Positive (Mistake) / Total Negatives
	- We use TPR and FPR as the axis
		- ![Local picture](../Media/Pasted%20image%2020260203141916.png)
	- How an ROC curve is build
		- The model gives all samples a score. In this case, the probability of being positive. Sort all the samples
		- Start from infinite threshold value t. This is at (0,0) on the graph above. The model classifies nothing as positive. The range is 0<TPR<1 and 0<FPR<1
		- Walk through the sample
			- Every time the model correctly identifies a sample, move up the TPR axes. Move up 1/n where on the TPR axis where n is the number of positive samples
			- Every time the model wrongly identifies a sample, increment in the positive FPR direction. Move right.
	- What is AUC = Area under Curve of ROC
		- Integral of the ROC curve
		- The maximum is 1.0, minimum is 0.0
		- A high AUC means that you can find a threshold that has a very TPR and a low FPR, which means that the model is accurate at classifying and do not misclassify often
	- Interpretting ROC
		- The ROC curve is a menu of choices. How strict do you want to be? What are the tradeoffs you are willing to make for a higher TPR (which usually come with a higher FPR)
		- One easy way to select the sweet spot is to calculate the Euclidean distance from the (1,0) which is perfect classification
## K Mean Clustering
- An unsupervised learning method that uses dataset D
- How the algorithm works
	- Place random centroids throughout the plane. The number of centroids is K
	- For each point, calculate the distance from the data point $x_i$ to the centroid $c_i$
	- Move the $c_i$ centroid to the new center by using an equation
	- **Cost function in K mean cannot increase. It is either stuck at the local or global minimum**
	- ![Local picture](../Media/Pasted%20image%2020260203142416.png)
![Local picture](../Media/Pasted%20image%2020260430064750.png)

- k means clustering has an interesting property which is that the total loss is guaranteed not to increase. The new centroid is guaranteed to give a smaller value (if not equal which would mean no change in centroid)

- Unfortunately, k means is not guaranteed to find the global minimum, only the local minimum

There are two ways of initializing k-mean
- Forgy method which is to initialize by choosing k random centroids
- Random partition which is randomly assigning a cluster to each observation
	- Why this is better: each cluster is a random sample of the whole dataset, the initial centroids tend to be very close to the center of the data cloud. This can lead to more stable results in certain types of data
- **IN BOTH** the cluster assigned to each data point changes. The assignment is based on the actual proximity to the centroids


Hard clustering vs soft clustering
- Hard clustering is when each data point can only belong to one cluster. It is a binary choice
- Soft clustering is also known as fuzzy clustering
	- Each data point can belong to more than one cluster. 
	- An apple can be red to a certain degree and green to a certain degree
	- **These are not probability! It does not have to add up to one**


**Out of scope:**
1.  **Initialize:** Choose $k$ (number of clusters) and assign random membership weights to every point for every cluster.
2.  **Update Centroids:** Instead of taking the simple average of points in a cluster, calculate the **weighted mean**.
    *   A point with 0.9 membership in Cluster A pulls the centroid strongly.
    *   A point with 0.1 membership in Cluster A only nudges the centroid slightly.
3.  **Update Memberships:** For every point, calculate its distance to all centroids. Assign new membership weights using this logic:
    *   The closer a point is to a centroid, the higher its membership weight for that cluster.
    *   The "fuzzifier" ($m$, usually set to 2) determines how much overlap is allowed. If $m=1$, it turns back into hard K-means.
4.  **Repeat** until the weights stop changing significantly.
![Local picture](../Media/Pasted%20image%2020260430064848.png)

new centroid for group 1 = sum of all values under group 1 / number of values 


## Neural Networks

![Local picture](../Media/Pasted%20image%2020260403212012.png)


- Matrix version of chain rule
	- ![Local picture](../Media/Pasted%20image%2020260203142506.png)
	- ![Local picture](../Media/Pasted%20image%2020260203142615.png)
	- 
	- ![Local picture](../Media/Pasted%20image%2020260203142620.png)


![Local picture](../Media/Pasted%20image%2020260403212055.png)

- Relu derivative
	- Relu: $f(x)=max(0,x)$
		- < 0 gives 0
		- > 0 gives x
	- Very cheap
	- One property of the ReLU activation function is that it generates sparse matrices. Sparse matrices are matrices in which the majority of the entries are zero. Sparsity gives rise to compact models with more predictive ability and less overfitting.
	- Why is this so? Imagine you need to classify whether or not the image is a face or a toe. Suppose the image you are classifying currently is a face. The 'toe' activation for reLU would be 0 but for sigmoid it would be <0 (-1). Because it is zero, the resulting matrix optimization does not have to account it in the weights
	- Alternatives:
		- tanh
		- sigmoid - S shape squashing function
- Matrix parameters are randomized at the start for neural networks but the functions are not
- TLDR of Neural networks
	- Start with a bunch of layers and equations
	- Randomize the parameters
	- Check data in, see the loss (MSE?)
	- Apply back propagation to change parameters to reduce losses until sufficient
- When to use what functions?
	- ReLu
		- Standard, sandwiched between each function
		- ReLu makes neural networks able to comprehend non-linear relations
		- ![Local picture](../Media/Pasted%20image%2020260202223341.png)
	- Last function
		- Based on the task
			- Yes/No : Sigmoid
			- Pick : Softmax
			- Predict: Nothing


### Training and Testing of Neural Networks
- Training is done forward and backward
	- Forward: weights are fixed
		- Purpose: to compute error and responses/predictions
	- Backward: Weights are updated based on the loss function
		- Backpropagation is essentially gradient descent!
- Testing is done forward
	- Forward: (weights are fixed)
		- To estimate compute network responses
		- To predict the output labels given novel inputs

![Local picture](../Media/Pasted%20image%2020260403212151.png)

### Convolutional Neural Network
- A special type of feed forward network that significantly reduces the number of parameters in a deep neural network
- CNN is often used in image processing
- Works in a sliding window manner
	- Share the same parameter but across different locations
![Local picture](../Media/Pasted%20image%2020260403212545.png)
# Code
For your Jupyter Notebook, having a quick reference for the `numpy.linalg` module is essential. I have categorized them by how you will likely use them in Machine Learning and Linear Algebra workflows.

### 1. Solving Linear Systems
These are the primary functions for finding $x$ in $Ax = b$.

| Function | Purpose |
| :--- | :--- |
| `np.linalg.solve(A, b)` | Solves exactly $Ax = b$ for square, non-singular matrices. |
| `np.linalg.lstsq(A, b, rcond=None)` | **The ML Standard.** Solves overdetermined systems using Least Squares. Returns the solution, residuals, rank, and singular values. |

### 2. Matrix Decomposition (Factorization)
Essential for dimensionality reduction (PCA), solving complex systems, and stability analysis.

| Function | Purpose |
| :--- | :--- |
| `np.linalg.svd(A)` | **Singular Value Decomposition.** Decomposes $A = U \Sigma V^T$. Used in PCA and pseudo-inverses. |
| `np.linalg.eig(A)` | Computes eigenvalues and right eigenvectors of a square array. |
| `np.linalg.eigh(A)` | Optimized for **Hermitian** (symmetric) matrices. Faster/more stable than `eig`. |
| `np.linalg.qr(A)` | Computes the QR decomposition ($A = QR$). Useful for orthonormalizing data. |
| `np.linalg.cholesky(A)` | Computes the Cholesky decomposition ($A = LL^*$). Only works for positive-definite matrices (faster than LU). |

### 3. Inverses & Properties
Used to check if a system is solvable or to manipulate matrices algebraically.

| Function | Purpose |
| :--- | :--- |
| `np.linalg.inv(A)` | Computes the multiplicative inverse of a square matrix. |
| `np.linalg.pinv(A)` | **Moore-Penrose Pseudo-inverse.** Use this when a matrix is singular or not square. It acts as a universal solver. |
| `np.linalg.det(A)` | Calculates the determinant. If `det == 0`, the matrix is singular (not invertible). |
| `np.linalg.matrix_rank(A)` | Returns the rank of the matrix. Useful for the Rouche-Capelli theorem. |
| `np.trace(A)` | Sum of the diagonal elements (useful for regularization/norms). |

### 4. Norms (Distance & Magnitude)
Used for loss functions (L1/L2 regularization) and data normalization.

| Function | Purpose |
| :--- | :--- |
| `np.linalg.norm(x, ord=None)` | Calculates vector or matrix norms. <br>• `ord=1`: Manhattan distance (L1). <br>• `ord=2`: Euclidean distance (L2). <br>• `ord=np.inf`: Max value. |

---

### Pro-Tip: NumPy vs. SciPy
While `numpy.linalg` is perfect for learning and general operations, **if you are building production models or handling very large datasets**, you should use `scipy.linalg` instead.

**Why?**
1.  **Speed:** `scipy` is generally more highly optimized.
2.  **Safety:** `scipy.linalg` will often catch errors that `numpy.linalg` might skip.
3.  **Functionality:** `scipy.linalg` contains advanced decompositions not found in NumPy (like `lu`, `schur`, or `hessenberg`).

**Quick swap:**
```python
import scipy.linalg as la

# Example: Solve is often slightly more robust here
w = la.solve(X.T @ X, X.T @ y) 
```

**Recommendation for your Notebook:**
If you want to keep your code clean, stick to `numpy.linalg` for your definitions, but import `scipy.linalg` at the top of your notebook if you find you are hitting performance bottlenecks with larger matrices.





Based on the image provided, here is an explanation of why the statement is **True**.

### The Problem Breakdown

1.  **The Function Mapping:**
    The image defines a vector function as $f(\mathbf{x}): \mathbb{R}^3 \to \mathbb{R}^2$.
    *   **$\mathbb{R}^3$ (Input):** This means the function takes a vector $\mathbf{x}$ with 3 variables as input, e.g., $\mathbf{x} = \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix}$.
    *   **$\mathbb{R}^2$ (Output):** This means the function outputs a vector with 2 components, e.g., $f(\mathbf{x}) = \begin{bmatrix} f_1(x_1, x_2, x_3) \\ f_2(x_1, x_2, x_3) \end{bmatrix}$.

2.  **The Matrix of Partial Derivatives (Jacobian Matrix):**
    When taking the derivative of a vector-valued function with respect to a vector input, the result is a matrix of partial derivatives, commonly known as the **Jacobian matrix**. (Sometimes loosely referred to as the gradient in certain contexts, though strictly speaking, the gradient is for scalar functions).

    The dimensions of this matrix are determined by the number of output dimensions (rows) and input dimensions (columns).

    For our function $f(\mathbf{x})$, the Jacobian matrix $J$ is constructed by taking the partial derivative of each output component with respect to each input variable:

    $$J = \begin{bmatrix} \frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \frac{\partial f_1}{\partial x_3} \\ \frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \frac{\partial f_2}{\partial x_3} \end{bmatrix}$$

### Conclusion

*   The matrix has **2 rows** because there are 2 output components ($f_1$ and $f_2$).
*   The matrix has **3 columns** because there are 3 input variables ($x_1, x_2,$ and $x_3$).

Therefore, the resulting matrix of partial derivatives is indeed a **$2 \times 3$ matrix**. The statement in the image is correct.


### Lecture 7

# Tutorial 8 Gradient Descent shit
Notes:
- `loss_deriv = 4 * (f - y)**3 # CHANGE ME` => This is the loss function![Local picture](../Media/Pasted%20image%2020260318152124.png)

```python
import numpy as np

def generic_gradient_descent(X, y, grad_f_func, epochs=1000, lr=0.01):
    """
    X: (m, d) input matrix
    y: (m,) target vector
    grad_f_func: A function that returns partial derivative of f w.r.t w
    """
    d = X.shape[1]
    w = np.zeros(d)
    
    for _ in range(epochs):
        # Calculate f(x, w)
        # In a real scenario, we'd pass the model function too. 
        # For brevity, assuming linear inputs:
        z = np.dot(X, w)
        f = apply_activation(z, activation_type) 
        
        # Common term: 4 * (f - y)^3
        loss_deriv = 4 * (f - y)**3 # CHANGE ME
        
        # Gradient = sum(loss_deriv * grad_f)
        # grad_f is the partial derivative of the model w.r.t weights
        grad = np.sum(loss_deriv[:, np.newaxis] * grad_f_func(X, w, z), axis=0)
        
        w -= lr * grad
    return w

# --- Specific Gradients for Q3, Q4, Q5 ---

# Q3: f = x^T w  =>  df/dw = x
def grad_f_q3(X, w, z):
    return X

# Q4: f = sigmoid(x^T w) => df/dw = f(1-f) * x
def grad_f_q4(X, w, z):
    sigmoid = 1 / (1 + np.exp(-z))
    return (sigmoid * (1 - sigmoid))[:, np.newaxis] * X

# Q5: f = ReLU(x^T w) => df/dw = 1 * x (if z>0) else 0
def grad_f_q5(X, w, z):
    # Create mask where z > 0
    mask = (z > 0).astype(float)
    return (mask[:, np.newaxis] * X)
```






imputation
==the statistical process of replacing missing or incomplete data with estimated values to create a complete dataset for analysis, thereby reducing bias and retaining sample size==
Data integrity concerns the maintenance and the assurance of data accuracy
and consistency.
**Other types of data ...?**


, One Hot Encoding (OHE) **can** be applied to a binary target, but it is generally considered redundant and, in many cases, not recommended


The polynomial model can approximate any continuous real-valued function on a closed and bounded interval to any degree of accuracy, ==a principle known as the **Weierstrass Approximation Theorem**==



![Local picture](../Media/Pasted%20image%2020260430010541.png)
**which code to use**



diction:
- learning rate


confusion matrix: for Classification

Compared with a decision tree, a random forest has lower squared bias and the
same variance? Random forest has lower variance, but squared bias stays the same


A higher training accuracy not necessarily leads to a higher test accuracy;
however, in most cases, a higher training accuracy indeed leads to a higher
validation accuracy? False

We have built a binary classifier. During testing, it is possible that the sum
of the false-positive-rate and the false-negative-rate is greater than 100%.
Imagine a binary classifier that is perfectly wrong. The sum would be 200%.


 In the naïve K-means method, the optimal K is learned automatically.
Ans: False. K is set by hand in naïve K-means. K is the number of clusters. K is a hyperparameter that must be specified by the user before the algorithm starts, requiring external heuristic methods to run and test multiple K values. 


The number of terms in a polynomial of degree n with d variables is given by the combination formula
$(n+d)C(d)$
d is the bias and the weight



The ridge regression can be applied to multi-target regression
Given four samples of two-dimensional data points 𝐗 and the corresponding
target output y, the 2nd order polynomial regression system is an under-determined
system



The dimensionality $d$ refers **strictly to the original features of your data points** (in this case, $x_1$ and $x_2$, so $d=2$). You do not add 1 to $d$ for the bias. 

The mathematical formula $\binom{n+d}{d}$ is doing the heavy lifting—it **inherently accounts for the bias term** on its own. 

Here is exactly how it works:

### What the formula is actually counting
The formula $\binom{n+d}{d}$ comes from combinatorics. It counts all possible terms where the sum of the exponents of your $d$ variables is anywhere from $0$ up to $n$.

For $d=2$ (variables $x_1, x_2$) and $n=2$ (max degree 2):
*   **Sum of exponents = 2:** $x_1^2, \ x_2^2, \ x_1^1 x_2^1$ (3 terms)
*   **Sum of exponents = 1:** $x_1^1, \ x_2^1$ (2 terms)
*   **Sum of exponents = 0:** $x_1^0 x_2^0 = 1$ **(This is the bias term!)** (1 term)

Total = 3 + 2 + 1 = 6 terms.

### Summary:
*   **$d$** is just the input dimension. If the problem says "two-dimensional," $d=2$. 
*   **$n$** is the max polynomial degree.
*   The formula $\binom{n+d}{d}$ calculates the final number of parameters, and the math automatically includes the "Degree 0" combination, which is your bias.


Adding regularization (e.g., L2 norm) to the cost function ==typically **slows down** the absolute optimization speed== by introducing a trade-off between fitting training data and keeping weights small, rather than speeding up convergence to the absolute minimum.


Suppose we are minimizing a cost function C(w) with respect to w using a
gradient descent algorithm. We observe the following: At iteration 1, C(w) is 11. At
iteration 2, C(w) becomes 10.9. At iteration 3, C(w) becomes 10.7. At iteration 4,
C(w) becomes 10.6. At iteration 5, C(w) becomes 10.55. Which of the following is
true? Note that there might be more than one true option. If so, you should select
all the correct options in order to get all the marks.
(1) Decreasing the learning rate will speed up the optimization further
(2) Increasing the learning rate will speed up the optimization further
(3) Adding a regularization to the cost function will speed up the optimization
further
(4) Insufficient information in the question to tell which option is true
Ans: (4) Even though the cost function is decreasing slowly, it’s entirely possible that
we were lucky and initialized near the local minimum, so hard to say without further
experimentation.



Consider the cost function C(w) = DataLoss(w) + λRegularization(w). Assume that
the global minimum of C(w) when λ = 2 is 12. Now we change λ to be equal to 20
and again minimize C(w). Assuming we attain the global minimum, the new optimal
cost function value C
(1) will be higher than before
(2) will be lower than before
(3) will stay the same
(4) Insufficient information in the question to tell which option is true

Answer is 4 because the change in total cost depends on the trade off between data loss and regularization term. Think of it as the 'shape' of the map is now different, thus the global minimum cannot be guaranteed to be higher or lower
**Data Loss increases:** Because the model is now "less flexible" (it is restricted by the larger penalty), it will likely fit the training data worse than it did before.
**Regularization term decreases:** Because the weights are smaller




uppose in a 2-class classification problem, our decision tree algorithm
achieves 52% accuracy on our training set, and also 52% accuracy on our test set.
Which of the following modification might potentially improve our algorithm's test
accuracy? Note that there might be more than one true option. If so, you should
select all the correct options in order to get all the marks.
(1) Increase maximum depth of tree
(2) Decrease maximum depth of tree
(3) Increase minimum number of samples for splitting a leaf node
(4) Decrease minimum number of samples for splitting a leaf node
(5) Try random forest instead of decision tree
Ans: Underfitting regime, so (1) Increase maximum tree depth and (4) Decrease
minimum number of samples for splitting a leaf node. Although we are in the underfitting
regime, but since we are increasing model complexity, we can use try random forest to
decrease variance, so (5) is true as well.
**If it is an overfitting regime, you would DEFINITELY want to use random forest. Random forest decreases the variance of decision trees. A single tree may be overfitted and sensitive to particular noise in the training data but an aggregate of trees will reduce this issue**


violates the most fundamental rule of machine learning: **The test set must remain unseen until the very end.**
If you use the test set to choose your model, you are essentially "training" on your test set. Here is why this is a major problem:
### 1. Data Leakage (Information Contamination)

The test set is intended to be a proxy for **unseen, future, real-world data**. If you use it to compare Model A, Model B, and Model C, and then pick the winner based on those scores, your "final" choice is now biased toward the specific quirks, noise, and patterns present in the test set.



MCQ10.3 Which of the following statement(s) is/are true about ROC curve? Note
that there might be more than one true option. If so, you should select all the correct
options in order to get all the marks.
(a) ROC curve is a widely used evaluation metric.
(b) Area Under the Curve (AUC) is lower-bounded by 0 and upper-bounded by 1.
(c) Given a fixed dataset, a higher Gini coefficient of ROC curve usually indicates
better performance.
(d) None of the others
a,b,c



Gradient is given by 2 sin(𝑤) cos(w)
At w = 3, gradient = 2*sin(3)*cos(3) = -0.279415498
After first round of gradient descent, updated value of w = 3 - (-0.279415498)*0.1 =
3.027942
NOTE THAT IT IS - step * gradient



![Local picture](../Media/Pasted%20image%2020260430034810.png)



![Local picture](../Media/Pasted%20image%2020260430063923.png)