# GRE Quantitative Reasoning Quick Reference

> [!abstract] Overview A concise formula sheet and cheat sheet directly synthesized from the **GRE Math Review**, formatted for Obsidian.

---

# Arithmetic & Real Numbers

### Integers & Real Numbers

> [!SUCCESS] Verified 

- **Set of Integers**: $\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$
- **Commutative Laws**: $r + s = s + r$ and $rs = sr$
- **Associative Laws**: $(r + s) + t = r + (s + t)$ and $(rs)t = r(st)$
- **Triangle Inequality**: $|r + s| \le |r| + |s|$
- **Absolute Value Product**: $|rs| = |r||s|$
- **Inequalities under Powers**:
    - If $r > 1$, then $r^2 > r$
    - If $0 < s < 1$, then $s^2 < s$

### Properties of Integers

> [!SUCCESS] Verified 

- **Even/Odd Addition**: 
	- $\text{Even} + \text{Even} = \text{Even}$
	- $\text{Odd} + \text{Odd} = \text{Even}$
	- $\text{Even} + \text{Odd} = \text{Odd}$
- **Even/Odd Multiplication**: 
	- $\text{Even} \times \text{Even} = \text{Even}$
	- $\text{Odd} \times \text{Odd} = \text{Odd}$
	- $\text{Even} \times \text{Odd} = \text{Even}$
- **Quotient and Remainder**: $c = qd + r$ (where $0 \le r < d$)

### Percents

> [!SUCCESS] Verified 

- **Percent Change**: $\frac{\text{Amount of Change}}{\text{Base (Initial Amount)}} \times 100\%$ 
*(Note: When calculating percent decrease, the base is the larger initial number; for percent increase, the base is the smaller initial number).*

### Exponents & Radicals Properties

> [!SUCCESS] Verified 

- **Square Root of Square**: $(\sqrt{a})^2 = a$ for $a \ge 0$, and $\sqrt{a^2} = |a|$
- **Product of Radicals**: $\sqrt{ab} = \sqrt{a}\sqrt{b}$
- **Quotient of Radicals**: $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$

---

# Algebra, Functions, and more...

### Definitions & Terminology

> [!SUCCESS] Verified 

- **Rational vs. Irrational Numbers**: Rational numbers ($c/d$) can be represented as terminating or repeating decimals, whereas irrational numbers cannot.
- **Like Terms**: Terms with identical variables and corresponding exponents (e.g., $5z^2$ and $-z^2$)
- **Degree of a Term & Polynomial**:
    - **Term Degree**: Sum of the exponents of all variables in that term (e.g., degree of $5xy^2$ is $1 + 2 = 3$)
    - **Polynomial Degree**: The maximum degree among its terms (e.g., degree of $4x^2 + 7x^5y - 62$ is $6$)

### Key Algebraic Identities

> [!SUCCESS] Verified 

- **Distributive Property**: $c(a + b) = ca + cb$ and $c(a - b) = ca - cb$
- **Square of a Sum**: $(a + b)^2 = a^2 + 2ab + b^2$
- **Square of a Difference**: $(a - b)^2 = a^2 - 2ab + b^2$
- **Difference of Squares**: $a^2 - b^2 = (a + b)(a - b)$
- **Cube of a Sum**: $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
- **Cube of a Difference**: $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$

### Linear Inequalities

> [!SUCCESS] Verified 

- **Sign Reversal**: When multiplying or dividing both sides of an inequality by a negative number, you **MUST** reverse the direction of the inequality sign.

### Rules of Exponents

> [!SUCCESS] Verified 

- **Exponential Equality**: For positive $x \ne 1$, if $x^a = x^b$, then $a = b$
- **Negative Exponents**: $x^{-a} = \frac{1}{x^a}$
- **Product Rule**: $x^a \cdot x^b = x^{a+b}$
- **Quotient Rule**: $\frac{x^a}{x^b} = x^{a-b} = \frac{1}{x^{b-a}}$
- **Zero Exponent**: $x^0 = 1$ (where $x \ne 0$)
- **Power of a Product**: $(xy)^a = x^a y^a$
- **Power of a Quotient**: $\left(\frac{x}{y}\right)^a = \frac{x^a}{y^a}$
- **Power of a Power**: $(x^a)^b = x^{ab}$

### Quadratic Equations & Discriminant

> [!SUCCESS] Verified 

- **Quadratic Formula**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ for $ax^2 + bx + c = 0$
- **Discriminant (**$D = b^2 - 4ac$**)**:
    - $D > 0$: 2 real roots
    - $D = 0$: 1 real root
    - $D < 0$: 2 imaginary roots

### Function Transformations

> [!SUCCESS] Verified 

- **Vertical Stretch**: $y = c \cdot h(x)$ stretches the graph vertically by a factor of $c$ if $c > 1$
- **Vertical Shrink**: $y = c \cdot h(x)$ shrinks the graph vertically by a factor of $c$ if $0 < c < 1$

### Interest & Compounding Formulas

> [!SUCCESS] Verified 

- **Annual Compound Interest**: $A = P\left(1 + \frac{r}{100}\right)^t$
- **Quarterly / Periodic Compounding**: $A = P\left(1 + \frac{r}{n \cdot 100}\right)^{nt}$ (for quarterly compounding with $n=4$, reduce rate from $r$ to $\frac{r}{n}$ and increase time from $t$ to $n \cdot t$) 

### Word Problem Shortcuts & Notes

> [!SUCCESS] Verified 

- **Combined Work Rates**: Work rates ($\text{batches}/\text{hr}$) can be added directly. Sum the rates and take the reciprocal to find combined time per batch (e.g., Machine A: 3 hrs/batch, Machine B: 2 hrs/batch $\implies \frac{1}{3} + \frac{1}{2} = \frac{5}{6}$ batch/hr $\implies \frac{6}{5}$ hrs/batch)
- **Mixture Problem Basis**: Total mixture weight equals the sum of its individual components (e.g., a 12g mixture of vinegar and oil has a total mass of 12g)


---

# Geometry

### Lines & Angles

> [!SUCCESS] Verified 

- **Standard Equation of Line**:  $y = m \cdot x+b$, where $m$ is the slope, and $b$ is the y-intercept.
- **Perpendicular Line Slopes**: Product of slopes $m_1 \cdot m_2 = -1$
- **Reflection across Line** $y = x$: Interchange $x$ and $y$
- **Parallel Lines & Transversals**: When two parallel lines are cut by a transversal, the angle pairs formed satisfy $x^\circ + y^\circ = 180^\circ$ for supplementary adjacent angles.

### Polygons & Triangles

> [!SUCCESS] Verified 

- **Convex Polygon**: Interior angles are each less than $180^\circ$
- **Sum of Interior Angles**: For an $n$-sided polygon, $S = (n - 2) \times 180^\circ$
- **Regular Polygon Interior Angle**: $I = \frac{(n - 2) \times 180^\circ}{n}$
- **Triangle Exterior Angle Theorem**: An exterior angle measure equals the sum of the two remote interior angles ($z = x + y$)
- **Area of a Triangle**: $A = \frac{1}{2} b h$
- **Pythagorean Theorem**: $a^2 + b^2 = c^2$ for right triangles
- $45^\circ-45^\circ-90^\circ$ **Triangle Ratio**: Side ratio is $1 : 1 : \sqrt{2}$
- $30^\circ-60^\circ-90^\circ$ **Triangle Ratio**: Side ratio is $1 : \sqrt{3} : 2$
- **Triangle Inequality Theorem**: The length of any side of a triangle must be strictly less than the sum of the lengths of the other two sides, and strictly greater than their positive difference.

### Circles

> [!SUCCESS] Verified 

- **Circle Equation**: Center $(x', y')$ with radius $r$ is $(x - x')^2 + (y - y')^2 = r^2$
- **Circumference**: $C = 2\pi r$ or $C = \pi d$
- **Area**: $A = \pi r^2$
- **Arc Length**: $\frac{\text{Central Angle}}{360^\circ} \times 2\pi r$
- **Sector Area**: $\frac{\text{Central Angle}}{360^\circ} \times \pi r^2$

### 3D Figures (Additional)

> [!SUCCESS] Verified 

- **Rectangular Solid Volume**: $V = \ell w h$
- **Rectangular Solid Surface Area**: $A = 2(\ell w + \ell h + wh)$

### Quadrilaterals & 3D Geometry

> [!SUCCESS] Verified 

- **Area of a Trapezoid**: $A = \frac{1}{2}(b_1 + b_2)h$
- **Right Circular Cylinder Volume**: $V = \pi r^2 h$
- **Right Circular Cylinder Surface Area**: $A = 2\pi r^2 + 2\pi r h$

### Parabolas

>[!QUESTION] Needs verification

- **Horizontal Parabolas**: $x = ay^2 + by + c$ (opens right if $a > 0$, opens left if $a < 0$)
- **Half-Parabolas**:
    - Upward: $\sqrt{y} = x$
    - Downward: $\sqrt{y} = -x$
    - Right-opening: $\sqrt{x} = y$
    - Left-opening: $\sqrt{x} = -y$

---

# Data Analysis & Probability

### Descriptive Statistics & Sets

- **Standard Deviation Calculation Steps**:
    1. Compute the mean of the data set
    2. Find the difference between the mean and each data value
    3. Square each difference
    4. Find the average of the squared differences
    5. Take the non-negative square root of that average
- **Inclusion-Exclusion Principle**: $|A \cup B| = |A| + |B| - |A \cap B|$
    - If $A \cap B = \emptyset$, then $|A \cup B| = |A| + |B|$
- **Multiplication Principle**: For sequential independent choices with $k$ possibilities followed by $m$ possibilities, total outcomes $= k \cdot m$
- **Permutations**: Number of unique orderings of $n$ distinct objects is $n!$

### Normal Distribution & Standardization

> [!SUCCESS] Verified 

- **Standardization (**$z$**-score)**: To transform a normal distribution with mean $m$ and standard deviation $d$ to a standard normal distribution ($\mu = 0, \sigma = 1$), compute: $z = \frac{x - m}{d}$, where $x$ is the raw data value.
### Descriptive Statistics (Additional)

- **Quartiles & IQR**: 
	- **Median ($Q2$)**: Divides the ordered data into two halves.
	- **$Q1$**: Median of the first half of the data.
	- **$Q3$**: Median of the second half of the data.
	- **Interquartile Range (IQR)**: $Q3 - Q1$ (measures the spread of the middle 50% of the data).
- **Normal Distribution Empirical Estimates**: 
	- Approx. $\frac{2}{3}$ (~68%) of data lies within $1$ standard deviation of the mean.
	- Almost all (~95%) data lies within $2$ standard deviations of the mean.

### Counting & Combinations

- **Permutations (Order matters)**: The number of ways to arrange $k$ objects from $n$ objects is $nP_k = \frac{n!}{(n-k)!}$
- **Combinations (Order does NOT matter)**: The number of ways to choose $k$ objects from $n$ objects is $nC_k = \frac{n!}{(n-k)! \cdot k!}$

### Probability Rules

- **Mutually Exclusive Events** (Cannot happen at the same time): 
	- $P(E \text{ or } F) = P(E) + P(F)$
	- $P(E \text{ and } F) = 0$
- **Independent Events** (One does not affect the other): 
	- $P(E \text{ and } F) = P(E) \times P(F)$


