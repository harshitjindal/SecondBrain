# GRE Quantitative Reasoning Quick Reference

> [!abstract] Overview A concise formula sheet and cheat sheet directly synthesized from the **GRE Math Review**, formatted for Obsidian.

---

# Definitions & Terminology

- **Rational vs. Irrational Numbers**: Rational numbers ($c/d$) can be represented as terminating or repeating decimals, whereas irrational numbers cannot.
- **Like Terms**: Terms with identical variables and corresponding exponents (e.g., $5z^2$ and $-z^2$)
- **Degree of a Term & Polynomial**:
    - **Term Degree**: Sum of the exponents of all variables in that term (e.g., degree of $5xy^2$ is $1 + 2 = 3$)
    - **Polynomial Degree**: The maximum degree among its terms (e.g., degree of $4x^2 + 7x^5y - 62$ is $6$)

---

# Arithmetic & Real Numbers

### Integers & Real Numbers

- **Set of Integers**: $\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$
- **Commutative Laws**: $r + s = s + r$ and $rs = sr$
- **Associative Laws**: $(r + s) + t = r + (s + t)$ and $(rs)t = r(st)$
- **Triangle Inequality**: $|r + s| \le |r| + |s|$
- **Absolute Value Product**: $|rs| = |r||s|$
- **Inequalities under Powers**:
    - If $r > 1$, then $r^2 > r$
    - If $0 < s < 1$, then $s^2 < s$




### Exponents & Radicals Properties

- **Square Root of Square**: $(\sqrt{a})^2 = a$ for $a \ge 0$, and $\sqrt{a^2} = |a|$
- **Product of Radicals**: $\sqrt{ab} = \sqrt{a}\sqrt{b}$
- **Quotient of Radicals**: $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$

---

# Algebra & Functions

### Key Algebraic Identities

- **Distributive Property**: $c(a + b) = ca + cb$ and $c(a - b) = ca - cb$
- **Square of a Sum**: $(a + b)^2 = a^2 + 2ab + b^2$
- **Square of a Difference**: $(a - b)^2 = a^2 - 2ab + b^2$
- **Difference of Squares**: $a^2 - b^2 = (a + b)(a - b)$
- **Cube of a Sum**: $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
- **Cube of a Difference**: $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$

### Rules of Exponents

- **Exponential Equality**: For positive $x \ne 1$, if $x^a = x^b$, then $a = b$
- **Negative Exponents**: $x^{-a} = \frac{1}{x^a}$
- **Product Rule**: $x^a \cdot x^b = x^{a+b}$
- **Quotient Rule**: $\frac{x^a}{x^b} = x^{a-b} = \frac{1}{x^{b-a}}$
- **Zero Exponent**: $x^0 = 1$ (where $x \ne 0$)
- **Power of a Product**: $(xy)^a = x^a y^a$
- **Power of a Quotient**: $\left(\frac{x}{y}\right)^a = \frac{x^a}{y^a}$
- **Power of a Power**: $(x^a)^b = x^{ab}$

### Function Transformations

- **Vertical Stretch**: $y = c \cdot h(x)$ stretches the graph vertically by a factor of $c$ if $c > 1$
- **Vertical Shrink**: $y = c \cdot h(x)$ shrinks the graph vertically by a factor of $c$ if $0 < c < 1$

---

# Geometry

### Lines & Angles

- **Parallel Lines & Transversals**: When two parallel lines are cut by a transversal, the angle pairs formed satisfy $x^\circ + y^\circ = 180^\circ$ for supplementary adjacent angles.

### Polygons & Triangles

- **Convex Polygon**: Interior angles are each less than $180^\circ$
- **Sum of Interior Angles**: For an $n$-sided polygon, $S = (n - 2) \times 180^\circ$
- **Regular Polygon Interior Angle**: $I = \frac{(n - 2) \times 180^\circ}{n}$
- **Triangle Exterior Angle Theorem**: An exterior angle measure equals the sum of the two remote interior angles ($z = x + y$)
- **Area of a Triangle**: $A = \frac{1}{2} b h$
- **Pythagorean Theorem**: $a^2 + b^2 = c^2$ for right triangles
- $45^\circ-45^\circ-90^\circ$ **Triangle Ratio**: Side ratio is $1 : 1 : \sqrt{2}$
- $30^\circ-60^\circ-90^\circ$ **Triangle Ratio**: Side ratio is $1 : \sqrt{3} : 2$

### Quadrilaterals & 3D Geometry

- **Area of a Trapezoid**: $A = \frac{1}{2}(b_1 + b_2)h$
- **Right Circular Cylinder Volume**: $V = \pi r^2 h$
- **Right Circular Cylinder Surface Area**: $A = 2\pi r^2 + 2\pi r h$

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

- **Standardization (**$z$**-score)**: To transform a normal distribution with mean $m$ and standard deviation $d$ to a standard normal distribution ($\mu = 0, \sigma = 1$), compute: $$z = \frac{x - m}{d}$$