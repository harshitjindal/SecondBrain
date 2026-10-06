# GRE Quantitative Reasoning Quick Reference (v2)

> [!abstract] Overview A concise formula sheet and cheat sheet directly synthesized from the **GRE Math Review**, formatted for Obsidian.

---

# Arithmetic & Number Properties

### Integers & Real Numbers

> [!SUCCESS] Verified

- **Set of Integers**: $\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$
- **Commutative Laws**: $r + s = s + r$ and $rs = sr$
- **Associative Laws**: $(r + s) + t = r + (s + t)$ and $(rs)t = r(st)$
- **Triangle Inequality**: $|r + s| \le |r| + |s|$
- **Absolute Value Product**: $|rs| = |r||s|$
- **Inequalities under Powers**:
    - If $r > 1$, then $r^2 > r$
    - If $0 < s < 1$, then $s^2 < s$

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

### Primes, Factors & Multiples

> [!NOTE] New

- **Prime**: an integer $> 1$ whose only positive divisors are $1$ and itself. $2$ is the only even prime. $1$ is **not** prime.
- **Primes below 30**: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29$
- **Prime factorization**: every integer $> 1$ factors uniquely into primes, e.g. $360 = 2^3 \cdot 3^2 \cdot 5$
- **Number of positive divisors**: if $n = p^a q^b r^c \cdots$ then the count is $(a+1)(b+1)(c+1)\cdots$
- **GCD and LCM**: GCD uses the *smaller* power of each shared prime, LCM uses the *larger* power of every prime. For positive integers: $\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab$
- **Divisibility rules**:
    - $2$: last digit even
    - $3$: digit sum divisible by $3$
    - $4$: last two digits divisible by $4$
    - $5$: last digit $0$ or $5$
    - $6$: divisible by both $2$ and $3$
    - $8$: last three digits divisible by $8$
    - $9$: digit sum divisible by $9$
    - $10$: last digit $0$
    - $11$: alternating sum of digits divisible by $11$
- **Sign rules**: product or quotient of two numbers with the same sign is positive; with different signs, negative. $0$ is neither positive nor negative.
- **Consecutive integers**: $n, n+1, n+2, \dots$ (consecutive evens/odds: $n, n+2, n+4, \dots$). Sum of $k$ consecutive integers has mean equal to the middle value.

### Fractions, Decimals, Ratios & Order of Operations

> [!NOTE] New

- **Order of operations (PEMDAS)**: Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right)
- **Adding fractions**: $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$
- **Dividing by a fraction**: $\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}$
- **Ratio** $a : b$ means $\frac{a}{b}$. If a quantity is split in ratio $a : b$, the parts are $\frac{a}{a+b}$ and $\frac{b}{a+b}$ of the total.
- **Proportion**: $\frac{a}{b} = \frac{c}{d} \iff ad = bc$
- **Useful approximations**: $\sqrt{2} \approx 1.41$, $\sqrt{3} \approx 1.73$, $\sqrt{5} \approx 2.24$, $\pi \approx 3.14$
- **Perfect squares** $1$ to $20$: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400$
- **Perfect cubes** $1$ to $10$: $1, 8, 27, 64, 125, 216, 343, 512, 729, 1000$
- **Common fraction-percent pairs**: $\frac{1}{8} = 12.5\%$, $\frac{1}{6} \approx 16.7\%$, $\frac{1}{5} = 20\%$, $\frac{1}{4} = 25\%$, $\frac{1}{3} \approx 33.3\%$, $\frac{3}{8} = 37.5\%$

### Percents

> [!WARNING] Corrected

- **Percent**: $x\%$ means $\frac{x}{100}$; "$x\%$ of $y$" is $\frac{x}{100} \cdot y$
- **Percent Change**: $\frac{\text{Amount of Change}}{\text{Original Amount}} \times 100\%$ *(The base is always the **original** value. For a decrease the original is the larger number; for an increase it is the smaller number.)*
- **Successive percent changes multiply**: a $p\%$ increase followed by a $q\%$ decrease gives a factor $\left(1 + \frac{p}{100}\right)\left(1 - \frac{q}{100}\right)$. They do **not** simply add or cancel (a $20\%$ increase then a $20\%$ decrease leaves $96\%$ of the original).
- **Percent vs. percentage points**: going from $40\%$ to $50\%$ is $+10$ percentage points, which is a $25\%$ increase.

### Exponents & Radicals

> [!WARNING] Corrected

- **Square Root of Square**: $(\sqrt{a})^2 = a$ for $a \ge 0$, and $\sqrt{a^2} = |a|$
- **Product of Radicals**: $\sqrt{ab} = \sqrt{a}\sqrt{b}$ **for $a, b \ge 0$**
- **Quotient of Radicals**: $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$ **for $a \ge 0,\ b > 0$**
- **Fractional exponents**: $x^{1/n} = \sqrt[n]{x}$ and $x^{m/n} = \left(\sqrt[n]{x}\right)^m$
- **Warning**: $\sqrt{x}$ always means the **non-negative** root. Even roots of negative numbers are not real.
- **Warning**: $\sqrt{a + b} \ne \sqrt{a} + \sqrt{b}$ in general.

### Absolute Value

> [!NOTE] New

- **Definition**: $|x| = x$ if $x \ge 0$, and $|x| = -x$ if $x < 0$. Always $|x| \ge 0$.
- $|x| = a$ (with $a > 0$) $\iff x = a$ or $x = -a$
- $|x| < a \iff -a < x < a$
- $|x| > a \iff x < -a$ or $x > a$
- $|x - c|$ is the distance between $x$ and $c$ on the number line.

---

# Algebra, Functions & Word Problems

### Definitions & Terminology

> [!SUCCESS] Verified

- **Rational vs. Irrational Numbers**: Rational numbers ($c/d$) can be represented as terminating or repeating decimals, whereas irrational numbers cannot.
- **Like Terms**: Terms with identical variables and corresponding exponents (e.g., $5z^2$ and $-z^2$)
- **Degree of a Term & Polynomial**:
    - **Term Degree**: Sum of the exponents of all variables in that term (e.g., degree of $5xy^2$ is $1 + 2 = 3$)
    - **Polynomial Degree**: The maximum degree among its terms (e.g., degree of $4x^2 + 7x^5y - 62$ is $6$)

### Key Algebraic Identities

> [!SUCCESS] Verified

- **Distributive Property**: $c(a + b) = ca + cb$ and $c(a - b) = ca - cb$
- **Square of a Sum**: $(a + b)^2 = a^2 + 2ab + b^2$
- **Square of a Difference**: $(a - b)^2 = a^2 - 2ab + b^2$
- **Difference of Squares**: $a^2 - b^2 = (a + b)(a - b)$
- **Cube of a Sum**: $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
- **Cube of a Difference**: $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$

### Factoring

> [!NOTE] New

- **Common factor**: $ab + ac = a(b + c)$
- **Trinomial**: $x^2 + (p + q)x + pq = (x + p)(x + q)$. Find two numbers whose sum equals the $x$-coefficient and whose product equals the constant.
- **Never divide by a variable that could be $0$**; factor and use the zero-product property instead: $ab = 0 \implies a = 0$ or $b = 0$.

### Linear Inequalities

> [!SUCCESS] Verified

- **Sign Reversal**: When multiplying or dividing both sides of an inequality by a negative number, you **MUST** reverse the direction of the inequality sign.

### Rules of Exponents

> [!SUCCESS] Verified

- **Exponential Equality**: For positive $x \ne 1$, if $x^a = x^b$, then $a = b$
- **Negative Exponents**: $x^{-a} = \frac{1}{x^a}$
- **Product Rule**: $x^a \cdot x^b = x^{a+b}$
- **Quotient Rule**: $\frac{x^a}{x^b} = x^{a-b} = \frac{1}{x^{b-a}}$
- **Zero Exponent**: $x^0 = 1$ (where $x \ne 0$)
- **Power of a Product**: $(xy)^a = x^a y^a$
- **Power of a Quotient**: $\left(\frac{x}{y}\right)^a = \frac{x^a}{y^a}$
- **Power of a Power**: $(x^a)^b = x^{ab}$

### Quadratic Equations & Discriminant

> [!WARNING] Corrected

- **Quadratic Formula**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$ for $ax^2 + bx + c = 0$
- **Discriminant ($D = b^2 - 4ac$)**:
    - $D > 0$: 2 distinct real roots
    - $D = 0$: 1 real root (a repeated root)
    - $D < 0$: **no real roots** (the parabola does not cross the $x$-axis)
- **Sum and product of roots** (Vieta): $x_1 + x_2 = -\frac{b}{a}$ and $x_1 x_2 = \frac{c}{a}$
- **Vertex of $y = ax^2 + bx + c$**: at $x = -\frac{b}{2a}$. Opens upward if $a > 0$ (minimum), downward if $a < 0$ (maximum).

### Systems of Equations

> [!NOTE] New

- **Substitution**: solve one equation for a variable and substitute into the other.
- **Elimination**: add or subtract multiples of the equations to cancel a variable.
- **Number of solutions** of two linear equations: one (lines intersect), none (parallel lines), or infinitely many (same line).
- **Shortcut**: GRE questions often ask for an expression such as $x + y$ or $x - y$. Try adding or subtracting the equations directly before solving for each variable.

### Functions & Transformations

> [!WARNING] Corrected

- **Function**: each input $x$ gives exactly one output $f(x)$. **Domain** = allowed inputs; **range** = resulting outputs. Watch for division by zero and square roots of negatives.
- **Vertical Stretch**: $y = c \cdot h(x)$ stretches the graph vertically by a factor of $c$ if $c > 1$
- **Vertical Shrink**: $y = c \cdot h(x)$ shrinks the graph vertically by a factor of $c$ if $0 < c < 1$
- **Vertical Shift**: $y = h(x) + c$ moves the graph up $c$ units ($c > 0$), down if $c < 0$
- **Horizontal Shift**: $y = h(x + c)$ moves the graph **left** $c$ units ($c > 0$); $y = h(x - c)$ moves it **right** $c$ units
- **Reflection across the $x$-axis**: $y = -h(x)$
- **Reflection across the $y$-axis**: $y = h(-x)$
- **Reflection across the line $y = x$**: interchange $x$ and $y$ (this gives the inverse relation)

### Sequences

> [!NOTE] New

- **Arithmetic** (common difference $d$): $a_n = a_1 + (n - 1)d$; sum of the first $n$ terms $S_n = \frac{n(a_1 + a_n)}{2}$
- **Geometric** (common ratio $r$): $a_n = a_1 r^{\,n-1}$; sum of the first $n$ terms $S_n = \frac{a_1(1 - r^n)}{1 - r}$ for $r \ne 1$

### Interest & Compounding Formulas

> [!WARNING] Corrected

- **Simple Interest**: $I = P \cdot \frac{r}{100} \cdot t$, so the total is $A = P\left(1 + \frac{rt}{100}\right)$
- **Annual Compound Interest**: $A = P\left(1 + \frac{r}{100}\right)^t$
- **Periodic Compounding**: $A = P\left(1 + \frac{r}{n \cdot 100}\right)^{nt}$ ($n$ compounding periods per year; for quarterly compounding $n = 4$: divide the rate by $4$ and multiply the number of years by $4$)

### Rate, Work, Distance & Mixture Problems

> [!WARNING] Corrected

- **Distance**: $d = r \cdot t$
- **Average speed** $= \frac{\text{total distance}}{\text{total time}}$. This is **not** the average of the two speeds unless the times are equal.
- **Combined Work Rates**: Work rates ($\text{batches}/\text{hr}$) can be added directly. Sum the rates and take the reciprocal to find combined time per batch (e.g., Machine A: 3 hrs/batch, Machine B: 2 hrs/batch $\implies \frac{1}{3} + \frac{1}{2} = \frac{5}{6}$ batch/hr $\implies \frac{6}{5}$ hrs/batch)
- **Mixture Problem Basis**: Total mixture weight equals the sum of its individual components (e.g., a 12g mixture of vinegar and oil has a total mass of 12g). Amount of a substance $=$ concentration $\times$ total amount.
- **Weighted average**: $\frac{w_1 x_1 + w_2 x_2 + \cdots}{w_1 + w_2 + \cdots}$

---

# Geometry & Coordinate Geometry

### Lines & Coordinate Formulas

> [!WARNING] Corrected

- **Standard Equation of Line**: $y = m x + b$, where $m$ is the slope, and $b$ is the $y$-intercept. This is applicable for non-vertical lines only.
- **Slope**: $m = \frac{y_2 - y_1}{x_2 - x_1}$
- **Point-slope form**: $y - y_1 = m(x - x_1)$
- **Distance between two points**: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$
- **Midpoint**: $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$
- **Parallel lines**: equal slopes
- **Perpendicular lines**: slopes are negative reciprocals, $m_1 \cdot m_2 = -1$ (for non-vertical lines; a vertical line is perpendicular to a horizontal one)
- **Intercepts**: $y$-intercept at $x = 0$; $x$-intercept at $y = 0$
- **Reflections of the point $(x, y)$**: across the $x$-axis $\to (x, -y)$; across the $y$-axis $\to (-x, y)$; through the origin $\to (-x, -y)$; across $y = x \to (y, x)$

### Angles

> [!WARNING] Corrected

- **Straight line**: angles on a line sum to $180^\circ$. **Full turn**: angles around a point sum to $360^\circ$.
- **Vertical angles** (opposite each other where two lines cross) are equal.
- **Parallel lines cut by a transversal**: corresponding angles are equal; alternate interior angles are equal; interior angles on the same side are supplementary ($x^\circ + y^\circ = 180^\circ$). Only two distinct angle measures appear: one acute and one obtuse (or all $90^\circ$).

### Polygons

> [!SUCCESS] Verified

- **Convex Polygon**: Interior angles are each less than $180^\circ$
- **Sum of Interior Angles**: For an $n$-sided polygon, $S = (n - 2) \times 180^\circ$
- **Regular Polygon Interior Angle**: $I = \frac{(n - 2) \times 180^\circ}{n}$

### Triangles

> [!WARNING] Corrected

- **Angle sum**: the interior angles of a triangle sum to $180^\circ$
- **Triangle Exterior Angle Theorem**: An exterior angle measure equals the sum of the two remote interior angles ($z = x + y$)
- **Area of a Triangle**: $A = \frac{1}{2} b h$ (the height is perpendicular to the chosen base)
- **Pythagorean Theorem**: $a^2 + b^2 = c^2$ for right triangles ($c$ is the hypotenuse)
- **Common Pythagorean triples**: $3\text{-}4\text{-}5$, $5\text{-}12\text{-}13$, $8\text{-}15\text{-}17$, $7\text{-}24\text{-}25$, and their multiples
- $45^\circ\text{-}45^\circ\text{-}90^\circ$ **Triangle**: side ratio $1 : 1 : \sqrt{2}$
- $30^\circ\text{-}60^\circ\text{-}90^\circ$ **Triangle**: side ratio $1 : \sqrt{3} : 2$ (short leg : long leg : hypotenuse)
- **Equilateral triangle** with side $s$: height $= \frac{\sqrt{3}}{2}s$ and area $= \frac{\sqrt{3}}{4}s^2$
- **Isosceles triangle**: two equal sides, and the angles opposite them are equal
- **Triangle Inequality Theorem**: The length of any side of a triangle must be strictly less than the sum of the lengths of the other two sides, and strictly greater than their positive difference.
- **Side-angle relationship**: the longest side is opposite the largest angle (and the shortest side opposite the smallest).
- **Similar triangles**: equal corresponding angles and proportional sides. If the side ratio is $k$, the area ratio is $k^2$ (and for similar solids the volume ratio is $k^3$).

### Quadrilaterals

> [!WARNING] Corrected

- **Rectangle**: $A = \ell w$, perimeter $= 2(\ell + w)$, diagonal $= \sqrt{\ell^2 + w^2}$
- **Square** with side $s$: $A = s^2$, perimeter $= 4s$, diagonal $= s\sqrt{2}$
- **Parallelogram**: $A = bh$ (height is perpendicular to the base, **not** the slanted side)
- **Area of a Trapezoid**: $A = \frac{1}{2}(b_1 + b_2)h$

### Circles

> [!WARNING] Corrected

- **Circle Equation**: Center $(x', y')$ with radius $r$ is $(x - x')^2 + (y - y')^2 = r^2$
- **Circumference**: $C = 2\pi r$ or $C = \pi d$
- **Area**: $A = \pi r^2$
- **Arc Length**: $\frac{\text{Central Angle}}{360^\circ} \times 2\pi r$
- **Sector Area**: $\frac{\text{Central Angle}}{360^\circ} \times \pi r^2$
- **Inscribed angle**: equals half the central angle that subtends the same arc
- **Angle inscribed in a semicircle** (subtending a diameter) is $90^\circ$
- **Tangent line**: perpendicular to the radius at the point of tangency

### 3D Figures

> [!WARNING] Corrected

- **Rectangular Solid Volume**: $V = \ell w h$
- **Rectangular Solid Surface Area**: $A = 2(\ell w + \ell h + wh)$
- **Space diagonal of a rectangular solid**: $\sqrt{\ell^2 + w^2 + h^2}$
- **Cube** with edge $s$: $V = s^3$, surface area $= 6s^2$, space diagonal $= s\sqrt{3}$
- **Right Circular Cylinder Volume**: $V = \pi r^2 h$
- **Right Circular Cylinder Surface Area**: $A = 2\pi r^2 + 2\pi r h$ (two circular ends plus the lateral surface $2\pi r h$)

### Parabolas

> [!WARNING] Corrected

- **Vertical Parabolas**: $y = ax^2 + bx + c$ (opens up if $a > 0$, opens down if $a < 0$); vertex at $x = -\frac{b}{2a}$
- **Horizontal Parabolas**: $x = ay^2 + by + c$ (opens right if $a > 0$, opens left if $a < 0$)
- **Half-Parabolas** (each equation draws only **half** of a full parabola):
    - $y = \sqrt{x}$ (equivalently $x = y^2$ with $y \ge 0$): the **upper half** of the right-opening parabola $x = y^2$
    - $y = -\sqrt{x}$ (equivalently $x = y^2$ with $y \le 0$): the **lower half** of the right-opening parabola $x = y^2$
    - $\sqrt{y} = x$ (equivalently $y = x^2$ with $x \ge 0$): the **right half** of the upward-opening parabola $y = x^2$
    - $\sqrt{y} = -x$ (equivalently $y = x^2$ with $x \le 0$): the **left half** of the upward-opening parabola $y = x^2$

---

# Data Analysis & Probability

### Basic Statistics

> [!NOTE] New

- **Mean**: $\frac{\text{sum of values}}{\text{number of values}}$, so $\text{sum} = \text{mean} \times n$
- **Median**: middle value of the ordered data (average of the two middle values if $n$ is even)
- **Mode**: most frequent value (a set may have none, one, or several)
- **Range**: $\text{max} - \text{min}$
- **Weighted mean**: $\frac{\sum f_i x_i}{\sum f_i}$ (frequencies or weights $f_i$)
- **Effect of adding a value equal to the mean**: the mean stays the same.
- **Effect of transformations**: adding a constant $c$ to every value shifts mean and median by $c$ and leaves the range and standard deviation unchanged; multiplying every value by $k$ multiplies the mean, median and range by $k$ and the standard deviation by $|k|$.

### Standard Deviation & Quartiles

> [!WARNING] Corrected

- **Standard Deviation Calculation Steps**:
    1. Compute the mean of the data set
    2. Find the difference between the mean and each data value
    3. Square each difference
    4. Find the average of the squared differences
    5. Take the non-negative square root of that average
- Larger spread around the mean $\implies$ larger standard deviation. If all values are equal, the standard deviation is $0$.
- **Quartiles & IQR**:
    - **Median ($Q2$)**: Divides the ordered data into two halves.
    - **$Q1$**: Median of the lower half of the data.
    - **$Q3$**: Median of the upper half of the data.
    - *(If $n$ is odd, the overall median is excluded from both halves.)*
    - **Interquartile Range (IQR)**: $Q3 - Q1$ (measures the spread of the middle 50% of the data).
- **Percentile**: the $k$-th percentile is a value with about $k\%$ of the data at or below it.
- **Box plot**: shows min, $Q1$, median, $Q3$, max.

### Normal Distribution & Standardization

> [!WARNING] Corrected

- **Standardization ($z$-score)**: To transform a normal distribution with mean $m$ and standard deviation $d$ to a standard normal distribution ($\mu = 0, \sigma = 1$), compute: $z = \frac{x - m}{d}$, where $x$ is the raw data value.
- **Empirical Rule**:
    - About $68\%$ (roughly $\frac{2}{3}$) of data lies within $1$ standard deviation of the mean.
    - About $95\%$ lies within $2$ standard deviations of the mean.
    - About $99.7\%$ lies within $3$ standard deviations of the mean.
- The normal curve is symmetric about its mean, so the mean, median and mode coincide.

### Reading Graphs & Data Displays

> [!NOTE] New

- **Histogram**: bar heights show frequency; bars touch. **Bar graph**: separate categories. **Circle graph**: the sectors' percentages sum to $100\%$, so a sector's angle is $\text{percent} \times 360^\circ$.
- **Scatterplot**: a line of best fit with positive slope indicates positive association (and negative slope, negative association). Association does not prove causation.
- **Frequency distribution**: to find the mean or median from a table, use the frequencies as weights or counts.
- **Read carefully**: check the title, units, scale and axis labels, and whether values are given as percents or raw counts before answering.

### Counting & Sets

> [!WARNING] Corrected

- **Multiplication Principle**: For sequential independent choices with $k$ possibilities followed by $m$ possibilities, total outcomes $= k \cdot m$
- **Permutations of all objects**: the number of orderings of $n$ distinct objects is $n!$
- **Permutations (Order matters)**: The number of ways to arrange $k$ objects from $n$ objects is $nP_k = \frac{n!}{(n-k)!}$
- **Combinations (Order does NOT matter)**: The number of ways to choose $k$ objects from $n$ objects is $nC_k = \frac{n!}{(n-k)! \cdot k!}$
- **Symmetry**: $nC_k = nC_{n-k}$; also $nC_0 = nC_n = 1$ and $nC_1 = n$
- **Arrangements with repeats**: $n$ objects with $n_1$ alike of one kind, $n_2$ alike of another, etc.: $\frac{n!}{n_1!\, n_2! \cdots}$
- **Inclusion-Exclusion Principle**: $|A \cup B| = |A| + |B| - |A \cap B|$
    - If $A \cap B = \emptyset$, then $|A \cup B| = |A| + |B|$
    - For two overlapping groups: $\text{Total} = A + B - \text{Both} + \text{Neither}$

### Probability Rules

> [!WARNING] Corrected

- **Probability range**: $0 \le P(E) \le 1$. For equally likely outcomes, $P(E) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$
- **Complement**: $P(\text{not } E) = 1 - P(E)$. For "at least one" problems, compute $1 - P(\text{none})$.
- **General Addition Rule**: $P(E \text{ or } F) = P(E) + P(F) - P(E \text{ and } F)$
- **Mutually Exclusive Events** (Cannot happen at the same time):
    - $P(E \text{ or } F) = P(E) + P(F)$
    - $P(E \text{ and } F) = 0$
- **Independent Events** (One does not affect the other):
    - $P(E \text{ and } F) = P(E) \times P(F)$
- **Conditional Probability**: $P(E \mid F) = \frac{P(E \text{ and } F)}{P(F)}$. $E$ and $F$ are independent exactly when $P(E \mid F) = P(E)$.
- **Expected value**: $E(X) = \sum x_i \cdot P(x_i)$ (each value times its probability)
- **Note**: mutually exclusive events with non-zero probabilities are **not** independent.

---

# Quantitative Comparison & Test-Taking Tips

> [!NOTE] New

- **Quantitative Comparison answers**: (A) Quantity A is greater; (B) Quantity B is greater; (C) the two are equal; (D) the relationship cannot be determined.
- **Choose (D)** only if different allowed values of the variables flip the comparison. If any valid choice gives a different result than another valid choice, the answer is (D).
- **Test special values**: try negatives, zero, $1$, fractions between $0$ and $1$, and large numbers. Squaring or multiplying by a variable can change an inequality's direction.
- **Simplify both quantities** by doing the same operation to each (add or subtract the same term; multiply or divide by a positive number) before comparing.
- **Do not assume figures are drawn to scale** unless the problem says so. Use only the information stated.
- **Estimate when answer choices are far apart**; and use backsolving (plug in the answer choices) for equation-style word problems.
- **Check what is asked**: units, whether a variable must be an integer or positive, and "which of the following **must** be true" versus "**could** be true".

---

# Change Log (v1 to v2)

> [!NOTE] New

- **Corrected (errors)**:
    - Half-parabola labels: $\sqrt{y} = -x$ is the **left half** of $y = x^2$, not "downward"; $\sqrt{x} = -y$ is the **lower half** of $x = y^2$, not "left-opening"; the other two are the right half and upper half.
    - Discriminant with $D < 0$: "no real roots", not "2 imaginary roots".
    - Radical rules now state their domain conditions.
- **Corrected (precision)**: percent change base is the original value; perpendicular slopes apply to non-vertical lines; "almost all ($\sim 95\%$)" replaced by the full $68$-$95$-$99.7$ rule; quartile convention for odd $n$ stated; transversal angle relationships completed; "triangle ratio" and "Parabolas" wording tightened.
- **Added**: primes, factors, GCD/LCM, divisibility; fractions, ratios, order of operations, common values; absolute value; factoring; systems of equations; full function transformations; sequences; rate/work/distance, weighted average, simple interest; coordinate formulas; angle rules; triangle extras (triples, equilateral, similar triangles); quadrilaterals; circle theorems; cube and space diagonal; vertical parabolas; mean/median/mode/range and transformation effects; graph reading; counting extras; complement, general addition, conditional probability, expected value; Quantitative Comparison tips.
