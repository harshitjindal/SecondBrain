# GRE Quantitative Reasoning Quick Reference (v4)

> [!abstract] Overview A formula and concept sheet for GRE Quantitative Reasoning, checked against the ETS **GRE Math Review**. Items marked "beyond the review" are useful extras that the review does not explicitly cover.

---

# Arithmetic & Number Properties

### Integers & Real Numbers

- **Set of Integers**: $\mathbb{Z} = \{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$
- **Commutative Laws**: $r + s = s + r$ and $rs = sr$
- **Associative Laws**: $(r + s) + t = r + (s + t)$ and $(rs)t = r(st)$
- **Distributive Law**: $r(s + t) = rs + rt$
- **Zero and one**: $r + 0 = r$, $r \cdot 0 = 0$, $r \cdot 1 = r$
- **Zero-product property**: if $rs = 0$, then $r = 0$ or $s = 0$ (or both)
- **Division by $0$ is undefined**: $\frac{5}{0}$ and $\frac{0}{0}$ are both undefined (and $0^0$ is undefined)
- **Sign facts**: positive $\times$ positive $=$ positive; negative $\times$ negative $=$ positive; positive $\times$ negative $=$ negative. $0$ is neither positive nor negative.
- **Triangle Inequality**: $|r + s| \le |r| + |s|$
- **Absolute Value Product**: $|rs| = |r||s|$
- **Inequalities under Powers**:
    - If $r > 1$, then $r^2 > r$
    - If $0 < s < 1$, then $s^2 < s$
- **Number line**: $x < y$ means $x$ is to the left of $y$. Every real number is a point on the line and vice versa.
- **Intervals**: $2 < x < 3$ (endpoints excluded), $2 \le x \le 3$ (both included), and the half-open forms $2 \le x < 3$ and $2 < x \le 3$. One-endpoint intervals: $x > 4$, $x \ge 4$, $x < 4$, $x \le 4$.

### Properties of Integers

- **Even/Odd Addition**:
    - $\text{Even} + \text{Even} = \text{Even}$
    - $\text{Odd} + \text{Odd} = \text{Even}$
    - $\text{Even} + \text{Odd} = \text{Odd}$
- **Even/Odd Multiplication**:
    - $\text{Even} \times \text{Even} = \text{Even}$
    - $\text{Odd} \times \text{Odd} = \text{Odd}$
    - $\text{Even} \times \text{Odd} = \text{Even}$
- **Odd numbers** leave remainder $1$ when divided by $2$.
- **Quotient and Remainder**: $c = qd + r$ where $d > 0$ and $0 \le r < d$. The remainder is never negative, even if $c$ is negative.
    - $19 \div 7$: quotient $2$, remainder $5$
    - $-13 \div 5$: quotient $-3$, remainder $2$, since $-13 = (-3)(5) + 2$
    - $80 \div 100$: quotient $0$, remainder $80$
    - Remainder $0$ if and only if $d$ divides $c$

### Primes, Factors & Multiples

- **Factor (divisor) and multiple**: if $c = ab$ for integers, then $a$ and $b$ are factors of $c$ and $c$ is a multiple of $a$ and $b$. Negatives count too ($-2$ is a factor of $60$), but questions usually ask about positive factors.
- **Special cases**: $1$ is a factor of every integer. $0$ is a multiple of every integer. Every nonzero integer has infinitely many multiples.
- **Prime**: an integer $> 1$ whose only positive divisors are $1$ and itself. $2$ is the only even prime. $1$ is **not** prime.
- **Composite**: an integer $> 1$ that is not prime ($4, 6, 8, 9, 10, 12, \dots$)
- **Primes below 30**: $2, 3, 5, 7, 11, 13, 17, 19, 23, 29$
- **Prime factorization**: every integer $> 1$ factors uniquely into primes, e.g. $360 = 2^3 \cdot 3^2 \cdot 5$ and $800 = 2^5 \cdot 5^2$
- **Number of positive divisors**: if $n = p^a q^b r^c \cdots$ then the count is $(a+1)(b+1)(c+1)\cdots$ (beyond the review)
- **GCD and LCM**: GCD uses the *smaller* power of each shared prime, LCM uses the *larger* power of every prime. For positive integers: $\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab$
- **Divisibility rules** (beyond the review):
    - $2$: last digit even
    - $3$: digit sum divisible by $3$
    - $4$: last two digits divisible by $4$
    - $5$: last digit $0$ or $5$
    - $6$: divisible by both $2$ and $3$
    - $8$: last three digits divisible by $8$
    - $9$: digit sum divisible by $9$
    - $10$: last digit $0$
    - $11$: alternating sum of digits divisible by $11$
- **Consecutive integers**: $n, n+1, n+2, \dots$ (consecutive evens or odds: $n, n+2, n+4, \dots$). The mean of consecutive integers is the middle value.

### HCF (GCD) and LCM: How to Calculate

- **Names**: HCF (highest common factor) = GCD (greatest common divisor) = GCF (greatest common factor). The GRE uses "greatest common divisor". LCM = least common multiple.
- **Definitions**: the GCD of $c$ and $d$ is the largest positive integer that divides both. The LCM is the smallest positive integer that is a multiple of both. Example: $\gcd(30, 75) = 15$ and $\operatorname{lcm}(30, 75) = 150$.
- **GCD and LCM**: GCD uses the *smaller* power of each shared prime, LCM uses the *larger* power of every prime. For positive integers: $\gcd(a,b) \cdot \operatorname{lcm}(a,b) = ab$
- **Method 1: List** (fine for small numbers)
    - Divisors of $30$: $1, 2, 3, 5, 6, 10, 15, 30$. Divisors of $75$: $1, 3, 5, 15, 25, 75$. Largest common one: $15$.
    - Multiples of $30$: $30, 60, 90, 120, 150, \dots$. Multiples of $75$: $75, 150, \dots$. Smallest common one: $150$.
- **Method 2: Prime factorization** (most reliable)
    1. Factor each number into primes: $30 = 2 \cdot 3 \cdot 5$ and $75 = 3 \cdot 5^2$
    2. **GCD**: multiply the primes that appear in **all** numbers, each to its **smallest** power: $3 \cdot 5 = 15$
    3. **LCM**: multiply **every** prime that appears in any number, each to its **largest** power: $2 \cdot 3 \cdot 5^2 = 150$
- **Method 3: Euclidean algorithm** (best for large numbers, GCD only): $\gcd(a, b) = \gcd(b, r)$ where $r$ is the remainder of $a \div b$. Repeat until the remainder is $0$; the last nonzero remainder is the GCD.
    - $\gcd(75, 30)$: $75 = 2(30) + 15$, then $30 = 2(15) + 0$, so the GCD is $15$
    - $\gcd(252, 105)$: $252 = 2(105) + 42$; $105 = 2(42) + 21$; $42 = 2(21) + 0$, so the GCD is $21$
- **Product shortcut** (two numbers only): $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = ab$, so $\operatorname{lcm}(a, b) = \frac{ab}{\gcd(a, b)}$. Check: $15 \cdot 150 = 2250 = 30 \cdot 75$. This does **not** hold for three or more numbers.
- **Three or more numbers**: use prime factorization. $12 = 2^2 \cdot 3$, $18 = 2 \cdot 3^2$, $30 = 2 \cdot 3 \cdot 5$ gives $\gcd = 2 \cdot 3 = 6$ and $\operatorname{lcm} = 2^2 \cdot 3^2 \cdot 5 = 180$.
- **Ladder (repeated division) method**, works for any number of integers: divide all the numbers by a prime that divides **all** of them, and repeat until no prime divides all of them. The **GCD** is the product of the divisors used. The **LCM** is that product times the numbers left at the bottom. For $12, 18, 30$: divide by $2$ to get $6, 9, 15$; divide by $3$ to get $2, 3, 5$. GCD $= 2 \cdot 3 = 6$; LCM $= 2 \cdot 3 \cdot 2 \cdot 3 \cdot 5 = 180$.
- **Remainder pattern**: if $n$ leaves remainder $r$ when divided by each of $a$ and $b$, then $n = k \cdot \operatorname{lcm}(a, b) + r$. The smallest such $n > r$ is $\operatorname{lcm}(a, b) + r$ (e.g., remainder $1$ when divided by $4$ and by $6$: $12 + 1 = 13$).
- **Quick facts**:
    - If $\gcd(a, b) = 1$ (the numbers are *coprime*), then $\operatorname{lcm}(a, b) = ab$.
    - If $a$ divides $b$, then $\gcd(a, b) = a$ and $\operatorname{lcm}(a, b) = b$.
    - Every common divisor of $a$ and $b$ divides $\gcd(a, b)$, and every common multiple is a multiple of $\operatorname{lcm}(a, b)$.
- **When to use which**:
    - **GCD**: reduce a fraction (divide top and bottom by the GCD), split things into the largest equal groups or pieces, tile a rectangle with the largest square, reduce a ratio such as $5 : 30 : 20 = 1 : 6 : 4$.
    - **LCM**: find a common denominator, find when repeating events line up again (bells every $12$ and $18$ minutes ring together every $\operatorname{lcm}(12, 18) = 36$ minutes), find the smallest number divisible by several numbers.

### Fractions, Decimals & Ratios

- **Fraction** $\frac{c}{d}$ with $d \ne 0$; every fraction is a rational number, and every integer $n$ equals $\frac{n}{1}$. Signs: $\frac{-c}{d} = \frac{c}{-d} = -\frac{c}{d}$.
- **Reducing**: divide numerator and denominator by a common factor (best, their GCD): $\frac{40}{72} = \frac{5}{9}$
- **Adding / subtracting**: use a common denominator (the LCM of the denominators is the neatest): $\frac{1}{3} + \frac{2}{5}$ uses $15$, giving $\frac{5 + 6}{15} = \frac{11}{15}$. In general $\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$.
- **Multiplying**: multiply numerators and denominators: $\frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}$
- **Dividing**: multiply by the reciprocal: $\frac{a}{b} \div \frac{c}{d} = \frac{a}{b} \cdot \frac{d}{c}$
- **Mixed numbers**: $4\frac{3}{8} = 4 + \frac{3}{8} = \frac{35}{8}$
- **Complex fractions**: $\dfrac{1}{\,2/3\,} = \frac{3}{2}$. Invert the denominator and multiply.
- **Decimals**: place values are powers of $10$: $7{,}532.418 = 7(1000) + 5(100) + 3(10) + 2 + 4\left(\tfrac{1}{10}\right) + 1\left(\tfrac{1}{100}\right) + 8\left(\tfrac{1}{1000}\right)$
- **Decimal to fraction**: $0.612 = \frac{612}{1000}$. **Fraction to decimal**: divide numerator by denominator.
- **Rational numbers** are exactly the terminating or repeating decimals ($\frac{1}{3} = 0.\overline{3}$). **Irrational numbers** (like $\sqrt{2} = 1.41421\ldots$) neither terminate nor repeat.
- **Ratio** $a : b$ means $\frac{a}{b}$ (reduce to lowest terms). Three-part ratios work the same way: $5 : 30 : 20 = 1 : 6 : 4$ (divide by the GCD $5$).
- **Splitting in a ratio**: if a quantity is split in ratio $a : b$, the parts are $\frac{a}{a+b}$ and $\frac{b}{a+b}$ of the total.
- **Proportion**: $\frac{a}{b} = \frac{c}{d} \iff ad = bc$ (cross-multiply)
- **Order of operations (PEMDAS)**: Parentheses, Exponents, Multiplication/Division (left to right), Addition/Subtraction (left to right)
- **Useful approximations**: $\sqrt{2} \approx 1.41$, $\sqrt{3} \approx 1.73$, $\sqrt{5} \approx 2.24$, $\pi \approx 3.14$ (or $\frac{22}{7}$)
- **Perfect squares** $1$ to $20$: $1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400$
- **Perfect cubes** $1$ to $10$: $1, 8, 27, 64, 125, 216, 343, 512, 729, 1000$
- **Common fraction-percent pairs**: $\frac{1}{8} = 12.5\%$, $\frac{1}{6} \approx 16.7\%$, $\frac{1}{5} = 20\%$, $\frac{1}{4} = 25\%$, $\frac{1}{3} \approx 33.3\%$, $\frac{3}{8} = 37.5\%$

### Percents

- **Percent**: $x\%$ means $\frac{x}{100}$. Convert by moving the decimal two places: $12\% = 0.12$, $0.3\% = 0.003$.
- **Watch the symbol**: $0.01 = 1\%$ but $0.01\% = 0.0001$.
- **Three basic questions** (part $=$ percent $\times$ whole):
    - Percent from part and whole: $\frac{\text{part}}{\text{whole}} \times 100\%$ (e.g. $\frac{13}{20} = 65\%$)
    - Part from percent and whole: $30\%$ of $350 = 0.3 \times 350 = 105$
    - Whole from percent and part: $15$ is $60\%$ of $z$, so $0.6z = 15$ and $z = 25$
- **Percents above 100%**: $15$ is $300\%$ of $5$; $250\%$ of $16$ is $2.5 \times 16 = 40$. The "whole" is called the base.
- **Percent Change**: $\frac{\text{Amount of Change}}{\text{Original Amount}} \times 100\%$ *(The base is always the **original** value. For an increase the original is the smaller number; for a decrease it is the larger.)*
- **Growth factors**: an increase of $p\%$ multiplies by $1 + \frac{p}{100}$; a decrease of $p\%$ multiplies by $1 - \frac{p}{100}$. A $12\%$ rise on $\$1{,}300$: $1{,}300 \times 1.12 = 1{,}456$. To undo it, **divide** by $1.12$.
- **Successive percent changes multiply**: $+8\%$ then $-6\%$ gives $1.08 \times 0.94$, not $+2\%$. A $20\%$ increase followed by a $20\%$ decrease leaves $1.2 \times 0.8 = 0.96$, or $96\%$ of the original. Each change uses the result of the previous one as its base.
- **Percent vs. percentage points**: going from $40\%$ to $50\%$ is $+10$ percentage points but a $25\%$ increase.
- **Different totals trap**: percents from different totals cannot be compared as counts. If a category rises from $20\%$ of $22{,}998$ to $22.1\%$ of $13{,}278$, the actual count **fell** even though the percent rose. Only compare percents directly when they share the same total.

### Exponents & Radicals

- **Negative bases**: $(-3)^2 = 9$ and $(-3)^3 = -27$ (even power gives positive, odd power gives negative), but $-3^2 = -9$ because the exponent applies only to $3$.
- **Square Root of Square**: $(\sqrt{a})^2 = a$ for $a \ge 0$, and $\sqrt{a^2} = |a|$
- **Product of Radicals**: $\sqrt{ab} = \sqrt{a}\sqrt{b}$ **for $a, b \ge 0$**
- **Quotient of Radicals**: $\sqrt{\frac{a}{b}} = \frac{\sqrt{a}}{\sqrt{b}}$ **for $a \ge 0,\ b > 0$**
- **Simplifying**: $\sqrt{24} = \sqrt{4}\sqrt{6} = 2\sqrt{6}$
- **Fractional exponents**: $x^{1/n} = \sqrt[n]{x}$ and $x^{m/n} = \left(\sqrt[n]{x}\right)^m$
- **$\sqrt{x}$ means the non-negative root**: $\sqrt{100} = 10$, never $-10$. Every positive number has two square roots ($\pm$), but the symbol gives only the positive one. Square roots of negatives are not real.
- **Odd vs. even roots**: odd-order roots exist for every real number ($\sqrt[3]{-8} = -2$). Even-order roots have two values for a positive number and none for a negative number.
- **Warning**: $\sqrt{a + b} \ne \sqrt{a} + \sqrt{b}$ in general.

### Absolute Value

- **Definition**: $|x| = x$ if $x \ge 0$, and $|x| = -x$ if $x < 0$. Always $|x| \ge 0$. It is the distance from $x$ to $0$.
- $|x| = a$ (with $a > 0$) $\iff x = a$ or $x = -a$
- $|x| < a \iff -a < x < a$
- $|x| > a \iff x < -a$ or $x > a$
- $|x - c|$ is the distance between $x$ and $c$ on the number line.

---

# Algebra, Functions & Word Problems

### Definitions & Terminology

- **Rational vs. Irrational Numbers**: Rational numbers ($c/d$) can be represented as terminating or repeating decimals, whereas irrational numbers cannot.
- **Like Terms**: Terms with identical variables and corresponding exponents (e.g., $5z^2$ and $-z^2$). Combine by adding coefficients: $3xy + 2x - xy - 3x = 2xy - x$.
- **Coefficient and constant term**: in $5z^2$ the coefficient is $5$; a term with no variable is a constant (degree $0$).
- **Degree of a Term & Polynomial**:
    - **Term Degree**: Sum of the exponents of all variables in that term (e.g., degree of $5xy^2$ is $1 + 2 = 3$)
    - **Polynomial Degree**: The maximum degree among its terms (e.g., degree of $4x^2 + 7x^5y - 62$ is $6$)
    - Degree $2$ is *quadratic*, degree $3$ is *cubic*.

### Key Algebraic Identities

- **Distributive Property**: $c(a + b) = ca + cb$ and $c(a - b) = ca - cb$
- **Square of a Sum**: $(a + b)^2 = a^2 + 2ab + b^2$
- **Square of a Difference**: $(a - b)^2 = a^2 - 2ab + b^2$
- **Difference of Squares**: $a^2 - b^2 = (a + b)(a - b)$
- **Cube of a Sum**: $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$
- **Cube of a Difference**: $(a - b)^3 = a^3 - 3a^2b + 3ab^2 - b^3$
- **Multiplying expressions**: multiply each term by each term, then combine like terms: $(x + 2)(3x - 7) = 3x^2 - 7x + 6x - 14 = 3x^2 - x - 14$

### Factoring & Simplifying Fractions

- **Common factor**: $ab + ac = a(b + c)$, e.g. $15y^2 - 9y = 3y(5y - 3)$
- **Trinomial**: $x^2 + (p + q)x + pq = (x + p)(x + q)$. Find two numbers whose sum equals the $x$-coefficient and whose product equals the constant.
- **Simplifying a fraction**: factor top and bottom, then cancel **common factors** (not common terms). $\frac{7x^2 + 14x}{2x + 4} = \frac{7x(x + 2)}{2(x + 2)} = \frac{7x}{2}$, valid only for $x \ne -2$ (the original is undefined there).
- **Never divide by a variable that could be $0$**; factor and use the zero-product property instead.

### Common Mistakes to Avoid

- $(x^a)(y^b) \ne (xy)^{a+b}$. For the same base: $(x^a)(x^b) = x^{a+b}$ and $(x^a)^b = x^{ab}$.
- $(x + y)^2 \ne x^2 + y^2$; the correct expansion has the extra middle term $2xy$.
- $(-x)^2 = x^2 \ne -x^2$
- $\sqrt{x^2 + y^2} \ne x + y$
- $\frac{a}{x + y} \ne \frac{a}{x} + \frac{a}{y}$, **but** $\frac{x + y}{a} = \frac{x}{a} + \frac{y}{a}$

### Solving Linear Equations

- **Equivalent equations**: adding or subtracting the same number on both sides, or multiplying or dividing both sides by the same **nonzero** number, keeps the solution set. Check by substituting the answer back.
- **One variable**: combine like terms and isolate $x$. It can happen that there is **no solution** ($2x + 3 = 2(7 + x)$ reduces to $3 = 14$) or **every $x$ works** ($3x - 6 = -3(2 - x)$ is an identity).
- **Two variables**: $ax + by = c$ has infinitely many solutions $(x, y)$.

### Linear Inequalities

- **Sign Reversal**: When multiplying or dividing both sides of an inequality by a negative number, you **MUST** reverse the direction of the inequality sign. ($-3x + 5 \le 17 \implies x \ge -4$.)
- **Positive roots**: taking the positive square root (or any positive root) of both sides of an inequality between non-negative numbers keeps the direction.

### Rules of Exponents

- **Exponential Equality**: For positive $x \ne 1$, if $x^a = x^b$, then $a = b$ (e.g. $2^{3c+1} = 2^{10} \implies c = 3$)
- **Negative Exponents**: $x^{-a} = \frac{1}{x^a}$
- **Product Rule**: $x^a \cdot x^b = x^{a+b}$
- **Quotient Rule**: $\frac{x^a}{x^b} = x^{a-b} = \frac{1}{x^{b-a}}$
- **Zero Exponent**: $x^0 = 1$ (where $x \ne 0$)
- **Power of a Product**: $(xy)^a = x^a y^a$
- **Power of a Quotient**: $\left(\frac{x}{y}\right)^a = \frac{x^a}{y^a}$
- **Power of a Power**: $(x^a)^b = x^{ab}$

### Quadratic Equations & Discriminant

- **Standard form**: $ax^2 + bx + c = 0$ with $a \ne 0$; there are $0$, $1$ or $2$ real solutions.
- **Quadratic Formula**: $x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$
- **Discriminant ($D = b^2 - 4ac$)**:
    - $D > 0$: 2 distinct real roots
    - $D = 0$: 1 real root (a repeated root)
    - $D < 0$: **no real roots** (the parabola does not cross the $x$-axis)
- **Factoring**: $2x^2 - x - 6 = (2x + 3)(x - 2) = 0 \implies x = -\frac{3}{2}$ or $x = 2$. Try factoring first; use the formula if it does not factor quickly.
- **Sum and product of roots** (Vieta, beyond the review): $x_1 + x_2 = -\frac{b}{a}$ and $x_1 x_2 = \frac{c}{a}$
- Solving Quadratic Equations:
	- Use Quadratic Formula
	- Use Factoring: 
		- Get equation in the form of $a \cdot x^2+b \cdot y+c=0$
		- Find 2 numbers such that their product is $a \cdot c$ and sum is $b$.
		- Break down the $b \cdot y$ term according to the 2 numbers found above.

### Systems of Equations

- **Substitution**: solve one equation for a variable and substitute into the other.
- **Elimination**: multiply an equation so a variable's coefficients match, then add or subtract to cancel it.
- **Number of solutions** of two linear equations: one (lines intersect), none (parallel lines), or infinitely many (same line).
- **Shortcut**: GRE questions often ask for an expression such as $x + y$ or $x - y$. Try adding or subtracting the equations directly before solving for each variable.

### Functions

- **Function**: each input $x$ gives exactly one output $f(x)$, but different inputs can give the same output ($g(x) = x^2 - 2x + 3$ has $g(0) = g(2) = 3$).
- **Domain**: all permissible inputs, unless stated. Exclude values that make a denominator $0$ or put a negative under a square root: $f(x) = \frac{2x}{x - 6}$ excludes $x = 6$; $g(x) = \sqrt{x + 2}$ needs $x \ge -2$.
- **Even function example**: $h(x) = |x|$ satisfies $h(x) = h(-x)$.
- **Intersection of two graphs**: set $f(x) = g(x)$ and solve for $x$, then find $y$.

### Function Transformations

For any function $h(x)$ and positive number $c$:

- **Vertical shift**: $h(x) + c$ moves the graph **up** $c$; $h(x) - c$ moves it **down** $c$
- **Horizontal shift**: $h(x + c)$ moves the graph **left** $c$; $h(x - c)$ moves it **right** $c$ (opposite to the sign)
- **Vertical stretch**: $c \cdot h(x)$ stretches the graph vertically by a factor of $c$ if $c > 1$
- **Vertical shrink**: $c \cdot h(x)$ shrinks the graph vertically by a factor of $c$ if $0 < c < 1$
- **Reflection across the $x$-axis**: $y = -h(x)$
- **Reflection across the $y$-axis**: $y = h(-x)$
- **Reflection across the line $y = x$**: interchange $x$ and $y$ (gives the inverse relation)
- **Tip**: if unsure of a shift direction, test a few points.

### Sequences (beyond the review)

- **Arithmetic** (common difference $d$): $a_n = a_1 + (n - 1)d$; sum of the first $n$ terms $S_n = \frac{n(a_1 + a_n)}{2}$
- **Geometric** (common ratio $r$): $a_n = a_1 r^{\,n-1}$; sum of the first $n$ terms $S_n = \frac{a_1(1 - r^n)}{1 - r}$ for $r \ne 1$

### Translating Words & Word Problems

- **Translate carefully**: "square of $x$ multiplied by $3$, then $10$ added" is $3x^2 + 10$. "Increase $s$ by $14\%$" is $1.14s$. "$y$ gallons shared after giving one gallon to someone, split among $4$" is $\frac{y - 1}{4}$.
- **Average (mean)**: $\text{average} = \frac{\text{sum}}{\text{count}}$. To hit a target mean, find the needed total first: three scores $82, 74, 90$ and a goal of $85$ over $4$ exams needs $4 \times 85 - 246 = 94$.
- **Weighted average**: $\frac{w_1 x_1 + w_2 x_2 + \cdots}{w_1 + w_2 + \cdots}$
- **Distance**: $d = r \cdot t$. **Keep units consistent**: if the speed is in miles per hour, convert minutes to hours ($40\ \text{min} = \frac{40}{60}\ \text{hr}$).
- **Average speed** $= \frac{\text{total distance}}{\text{total time}}$. This is **not** the average of the two speeds unless the times are equal.
- **Combined Work Rates**: Work rates ($\text{batches}/\text{hr}$) can be added directly. Sum the rates and take the reciprocal to find combined time per batch (e.g., Machine A: 3 hrs/batch, Machine B: 2 hrs/batch $\implies \frac{1}{3} + \frac{1}{2} = \frac{5}{6}$ batch/hr $\implies \frac{6}{5}$ hrs/batch, i.e. $1$ hr $12$ min)
- **Mixture Problem Basis**: Total mixture weight equals the sum of its individual components. Amount of a substance $=$ concentration $\times$ total amount. Example: a $12$ g mixture that is $40\%$ vinegar; to make it $25\%$ vinegar add $x$ g oil: $\frac{0.40(12)}{12 + x} = 0.25 \implies x = 7.2$.
- **Counting-and-cost systems**: apples at $\$0.15$, pears at $\$0.20$, $21$ fruits costing $\$3.80$: use $a + p = 21$ and $0.15a + 0.20p = 3.80$.
- **Profit** $=$ revenue $-$ cost. "Profit greater than $\$8{,}200$" on $500$ radios costing $\$30$ each at price $y$: $500(y - 30) > 8200$.

### Interest & Compounding Formulas

- **Simple Interest**: value after $t$ years is $V = P\left(1 + \frac{rt}{100}\right)$ (interest $I = P \cdot \frac{r}{100} \cdot t$)
- **Annual Compound Interest**: $V = P\left(1 + \frac{r}{100}\right)^t$
- **Periodic Compounding**: $V = P\left(1 + \frac{r}{n \cdot 100}\right)^{nt}$ ($n$ compounding periods per year; for quarterly compounding $n = 4$: divide the rate by $4$ and multiply the number of years by $4$)
- **Solving for $P$ or $r$**: divide by the growth factor to find $P$; for $r$, take a root of both sides ($\sqrt[4]{x} = \sqrt{\sqrt{x}}$, and positive roots preserve inequalities).

---

# Geometry & Coordinate Geometry

### Coordinate Plane Basics

- **Axes and quadrants**: the $x$-axis is horizontal and the $y$-axis vertical, crossing at the origin $(0, 0)$. Quadrants run counterclockwise from the top right: I $(+,+)$, II $(-,+)$, III $(-,-)$, IV $(+,-)$.
- **Points**: $(x, y)$ is $x$ units right of the $y$-axis (left if negative) and $y$ units above the $x$-axis (below if negative). If $x = 0$ the point is on the $y$-axis; if $y = 0$ it is on the $x$-axis.
- **Reflections of the point $(x, y)$**: across the $x$-axis $\to (x, -y)$; across the $y$-axis $\to (-x, y)$; through the origin $\to (-x, -y)$; across $y = x \to (y, x)$

### Lines & Coordinate Formulas

- **Slope-intercept form**: $y = m x + b$, where $m$ is the slope and $b$ is the $y$-intercept. Applies to non-vertical lines only.
- **Slope**: $m = \frac{y_2 - y_1}{x_2 - x_1}$ ("rise over run"), for $x_1 \ne x_2$
- **Horizontal line**: $y = b$, slope $0$. **Vertical line**: $x = a$, slope **undefined**.
- **Point-slope form**: $y - y_1 = m(x - x_1)$
- **Equation from two points**: find $m$, then substitute one point to get $b$. Points $(-2, -3)$ and $(4, 1.5)$: $m = \frac{4.5}{6} = 0.75$, then $-3 = 0.75(-2) + b$ gives $b = -1.5$.
- **Intercepts**: $y$-intercept at $x = 0$; $x$-intercept at $y = 0$ (set $y = 0$ and solve for $x$)
- **Distance between two points**: $d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$ (the Pythagorean theorem)
- **Midpoint**: $\left(\frac{x_1 + x_2}{2}, \frac{y_1 + y_2}{2}\right)$
- **Parallel lines**: equal slopes
- **Perpendicular lines**: slopes are negative reciprocals, $m_1 \cdot m_2 = -1$ (for non-vertical lines; a vertical line is perpendicular to a horizontal one)
- **Solving a system graphically**: the solution is the point where the two lines meet.
- **Inverse relation**: swap $x$ and $y$ to reflect across $y = x$; the line $y = 2x + 5$ becomes $y = \frac{1}{2}x - \frac{5}{2}$.

### Graphing Inequalities

- **One inequality**: $y \le mx + b$ is the line and everything **below** it; $y \ge mx + b$ is the line and everything **above** it. Strict inequalities ($<$, $>$) exclude the boundary line.
- **System of inequalities**: the solution set is the region where all the shaded regions **overlap**.
- **Rewrite first**: solve each inequality for $y$ (remember to flip the sign when dividing by a negative).

### Graphs of Functions

- **Absolute value**: $y = |x|$ is V-shaped with its corner at the origin, made of the pieces $y = x$ ($x \ge 0$) and $y = -x$ ($x < 0$).
- **Parabola** $y = ax^2 + bx + c$: opens up if $a > 0$ (vertex is the lowest point) and down if $a < 0$ (vertex is the highest point). Vertex at $x = -\frac{b}{2a}$. It is symmetric about the vertical line through the vertex, so the two $x$-intercepts are equally far from that line. The $y$-intercept is $c$.
- **Example**: $y = x^2 - 2x - 3$ has $x$-intercepts $-1$ and $3$, vertex $(1, -4)$, axis of symmetry $x = 1$, and $y$-intercept $-3$.
- **Horizontal parabolas**: $x = ay^2 + by + c$ (opens right if $a > 0$, left if $a < 0$)
- **Half-Parabolas** (each equation draws only **half** of a full parabola):
    - $y = \sqrt{x}$ (equivalently $x = y^2$ with $y \ge 0$): the **upper half** of the right-opening parabola $x = y^2$
    - $y = -\sqrt{x}$ (equivalently $x = y^2$ with $y \le 0$): the **lower half** of the right-opening parabola $x = y^2$
    - $\sqrt{y} = x$ (equivalently $y = x^2$ with $x \ge 0$): the **right half** of the upward-opening parabola $y = x^2$
    - $\sqrt{y} = -x$ (equivalently $y = x^2$ with $x \le 0$): the **left half** of the upward-opening parabola $y = x^2$
- **Circles on the plane**: $(x - a)^2 + (y - b)^2 = r^2$ has center $(a, b)$ and radius $r$; $x^2 + y^2 = 100$ is a circle of radius $10$ at the origin.

### Lines & Angles

- **Segments**: a segment has two endpoints; congruent segments have equal length; the **midpoint** splits a segment into two congruent parts.
- **Straight line**: angles on a line sum to $180^\circ$. **Full turn**: angles around a point sum to $360^\circ$.
- **Vertical (opposite) angles** where two lines cross are equal, and the four angles sum to $360^\circ$.
- **Types**: acute $< 90^\circ$, right $= 90^\circ$ (perpendicular lines), obtuse between $90^\circ$ and $180^\circ$.
- **Parallel lines cut by a transversal**: eight angles with only two measures, $x^\circ$ (four angles) and $y^\circ$ (four angles), where $x + y = 180$. Corresponding and alternate interior angles are equal; interior angles on the same side are supplementary. If $x = y$, all are $90^\circ$.

### Polygons

- **Convex Polygon**: Interior angles are each less than $180^\circ$. The review treats "polygon" as convex.
- **Sum of Interior Angles**: For an $n$-sided polygon, $S = (n - 2) \times 180^\circ$ (it splits into $n - 2$ triangles). Quadrilateral: $360^\circ$; hexagon: $720^\circ$; octagon: $1080^\circ$.
- **Regular polygon** (all sides and angles equal): each interior angle is $I = \frac{(n - 2) \times 180^\circ}{n}$; a regular octagon has $135^\circ$ angles.
- **Perimeter** is the sum of the side lengths; **area** is the region enclosed.

### Triangles

- **Angle sum**: the interior angles of a triangle sum to $180^\circ$
- **Triangle Exterior Angle Theorem**: An exterior angle measure equals the sum of the two remote interior angles ($z = x + y$)
- **Types**: *equilateral* (three equal sides, all angles $60^\circ$); *isosceles* (at least two equal sides, and the angles opposite them are equal, with the converse also true); *right* (one $90^\circ$ angle; the side opposite is the hypotenuse, the others are legs).
- **Area of a Triangle**: $A = \frac{1}{2} b h$ (the height is perpendicular to the chosen base; it can fall outside the triangle on an extended base)
- **Pythagorean Theorem**: $a^2 + b^2 = c^2$ for right triangles ($c$ is the hypotenuse)
- **Common Pythagorean triples** (beyond the review): $3\text{-}4\text{-}5$, $5\text{-}12\text{-}13$, $8\text{-}15\text{-}17$, $7\text{-}24\text{-}25$, and their multiples
- $45^\circ\text{-}45^\circ\text{-}90^\circ$ **Triangle**: side ratio $1 : 1 : \sqrt{2}$
- $30^\circ\text{-}60^\circ\text{-}90^\circ$ **Triangle**: side ratio $1 : \sqrt{3} : 2$ (short leg : long leg : hypotenuse; it is half of an equilateral triangle)
- **Equilateral triangle** with side $s$ (beyond the review): height $= \frac{\sqrt{3}}{2}s$ and area $= \frac{\sqrt{3}}{4}s^2$
- **Triangle Inequality Theorem**: The length of any side of a triangle must be strictly less than the sum of the lengths of the other two sides, and strictly greater than their positive difference. (Sides $4, 7, 12$ are impossible since $12 > 4 + 7$.)
- **Side-angle relationship** (beyond the review): the longest side is opposite the largest angle.
- **Congruent triangles** (same shape and size): SSS (three sides equal), SAS (two sides and the included angle), ASA (two angles and the included side), and AAS.
- **Similar triangles** (same shape): equal corresponding angles, and corresponding sides in the same ratio (the scale factor): $\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}$. All $30^\circ\text{-}60^\circ\text{-}90^\circ$ triangles are similar. If the scale factor is $k$, the area ratio is $k^2$ (and volume ratio $k^3$ for similar solids).

### Quadrilaterals

- **Angle sum**: the interior angles of any quadrilateral sum to $360^\circ$.
- **Rectangle**: four right angles; opposite sides parallel and congruent; the diagonals are congruent. $A = \ell w$, perimeter $= 2(\ell + w)$, diagonal $= \sqrt{\ell^2 + w^2}$.
- **Square**: a rectangle with four equal sides. $A = s^2$, perimeter $= 4s$, diagonal $= s\sqrt{2}$.
- **Parallelogram**: both pairs of opposite sides parallel; opposite sides congruent and opposite angles congruent. Every rectangle is a parallelogram. $A = bh$ (the height is perpendicular to the base, **not** the slanted side).
- **Trapezoid**: at least one pair of parallel sides (the bases). $A = \frac{1}{2}(b_1 + b_2)h$.

### Circles

- **Terms**: radius $r$, diameter $d = 2r$, chord (segment joining two points on the circle; a diameter is a chord through the center), concentric circles (same center).
- **Circle Equation**: Center $(x', y')$ with radius $r$ is $(x - x')^2 + (y - y')^2 = r^2$
- **Circumference**: $C = 2\pi r$ or $C = \pi d$ (since $\frac{C}{d} = \pi$)
- **Area**: $A = \pi r^2$
- **Arc**: an arc's measure equals its central angle; the full circle is $360^\circ$. **Arc Length** $= \frac{\text{Central Angle}}{360^\circ} \times 2\pi r$.
- **Sector Area**: $\frac{\text{Central Angle}}{360^\circ} \times \pi r^2$
- **Tangent line**: touches the circle at exactly one point and is perpendicular to the radius at the point of tangency (and the converse).
- **Inscribed triangles**: if one side is a diameter, the triangle is a right triangle (right angle opposite the diameter), and conversely.
- **Inscribed angle** (beyond the review): equals half the central angle that subtends the same arc.
- **Inscribed/circumscribed**: a polygon is inscribed if all its vertices lie on the circle; circumscribed if all its sides are tangent to the circle.

### 3D Figures

*(The review develops only rectangular solids and right circular cylinders. Sphere and cone formulas are not needed.)*

- **Rectangular solid**: $6$ faces, $12$ edges, $8$ vertices. A **cube** has all edges equal.
- **Rectangular Solid Volume**: $V = \ell w h$
- **Rectangular Solid Surface Area**: $A = 2(\ell w + \ell h + wh)$
- **Space diagonal of a rectangular solid** (beyond the review): $\sqrt{\ell^2 + w^2 + h^2}$
- **Cube** with edge $s$ (beyond the review): $V = s^3$, surface area $= 6s^2$, space diagonal $= s\sqrt{3}$
- **Right Circular Cylinder Volume**: $V = \pi r^2 h$ (base area times height)
- **Right Circular Cylinder Surface Area**: $A = 2\pi r^2 + 2\pi r h$ (two circular bases plus the lateral surface $2\pi r h$)

---

# Data Analysis & Probability

### Presenting Data

- **Variables**: *numerical* (e.g. height) or *categorical* (e.g. candidate voted for).
- **Frequency** is a count; **relative frequency** is the count divided by the total (a percent, fraction or decimal). Relative frequencies sum to $100\%$ (or $1$). Large lists are often **grouped** into classes (e.g. $61$ to $70$).
- **Bar graph**: separate bars with heights proportional to frequency; a **segmented (stacked) bar graph** splits each bar into parts. Read parts by subtraction (total $-$ part).
- **Histogram**: bars for numerical intervals on a **number line**, with no gaps unless an interval is empty. Bar area is proportional to the amount of data, and total area equals $100\%$ or $1$. Use it to see the shape, center and spread.
- **Circle graph (pie chart)**: each sector's area and central angle are proportional to its share, so the angle $=$ percent $\times 360^\circ$ ($7\%$ is $25.2^\circ$). Categories with the same total can be compared by their percents directly.
- **Scatterplot**: shows two numerical variables. A trend (best-fit) line can predict values, and its **slope** is a rate (e.g. hours per index unit). Positive slope means positive association.
- **Line graph (time series)**: points joined left to right. The **steepest** segment is the biggest change per period.
- **Reading tables and graphs**: check titles, units, scales, whether values are percents or counts, and whether different percents share the same base (see Percents).

### Basic Statistics

- **Mean**: $\frac{\text{sum of values}}{\text{number of values}}$, so $\text{sum} = \text{mean} \times n$
- **Weighted mean**: $\frac{\sum f_i x_i}{\sum f_i}$ (frequencies or weights $f_i$). The mean of a list with repeated values is the weighted mean of its distinct values.
- **Median**: middle value of the ordered data (average of the two middle values if $n$ is even)
- **Mode**: most frequent value (a list may have none, one, or several)
- **Frequency distribution**: to find the mean or median from a table, use the frequencies as weights or counts.
- **Mean vs. median**: an unusually high or low value pulls the mean but barely moves the median. Combining two groups: the combined mean is a weighted mean, but the combined median generally **cannot** be determined from the group medians alone.
- **Range**: $\text{max} - \text{min}$
- **Effect of adding a value equal to the mean**: the mean stays the same.
- **Effect of transformations**: adding a constant $c$ to every value shifts mean and median by $c$ and leaves the range, IQR and standard deviation unchanged; multiplying every value by $k$ multiplies the mean, median, range and IQR by $k$ and the standard deviation by $|k|$.

### Standard Deviation & Quartiles

- **Standard Deviation Calculation Steps**:
    1. Compute the mean of the data set
    2. Find the difference between the mean and each data value
    3. Square each difference
    4. Find the average of the squared differences
    5. Take the non-negative square root of that average
- **Example**: $0, 7, 8, 10, 10$ has mean $7$, squared differences $49, 0, 1, 9, 9$, average $13.6$, so SD $\approx 3.7$.
- **Population vs. sample SD**: the GRE's standard deviation divides by $n$. The *sample* standard deviation divides by $n - 1$ and is a different (qualified) term.
- More spread from the mean means a larger SD. If all values are equal, the SD is $0$.
- **Quartiles & IQR**:
    - **Median ($Q2$)**: Divides the ordered data into two halves.
    - **$Q1$**: Median of the lower half of the data.
    - **$Q3$**: Median of the upper half of the data.
    - *(If $n$ is odd, the overall median is excluded from both halves. The review's answer key uses this: for $19, 21, 22, 22, 28, 31, 33, 44, 50$, $Q1 = 21.5$, $Q3 = 38.5$, IQR $= 17$.)*
    - **Interquartile Range (IQR)**: $Q3 - Q1$ (measures the spread of the middle 50% of the data).
- **Percentiles**: $Q1 = P_{25}$, $Q2 = P_{50}$ (the median), $Q3 = P_{75}$.
- **Box plot**: shows the five numbers min, $Q1$, median, $Q3$, max. Useful for comparing lists by median, range and IQR.

### Standardization & Normal Distribution

- **Standardization ($z$-score)**: $z = \frac{x - m}{d}$ for a value $x$ with mean $m$ and standard deviation $d$. It says how many SDs above (positive) or below (negative) the mean the value is. The mean standardizes to $0$.
- **Going backward**: a value $r$ standard deviations above the mean is $m + rd$. (Mean $32.5$, SD $7.1$: a score of $48$ is $\frac{48 - 32.5}{7.1} \approx 2.2$ SDs above.)
- **In any data set, most values lie within $3$ standard deviations of the mean.**
- **Normal (bell-shaped) data**: mean, median and mode are (nearly) equal, and the data are symmetric about the mean.
- **Empirical Rule**:
    - About $68\%$ (roughly two-thirds) of data lies within $1$ standard deviation of the mean.
    - About $95\%$ ("almost all") lies within $2$ standard deviations of the mean.
    - About $99.7\%$ lies within $3$ standard deviations of the mean.
- **Normal distribution as a curve**: total area under the curve is $1$; $P(W > \text{mean}) = \frac{1}{2}$; $\mu = 0, \sigma = 1$ is the **standard** normal. A larger SD makes the curve lower and wider; changing the mean shifts it left or right.
- **Quick estimates**: with mean $5$ and SD $2$, $P(3 < W < 7) \approx \frac{2}{3}$, and $P(W < -1)$ ($3$ SDs below) is far below $5\%$.

### Counting & Sets

- **Sets vs. lists**: in a **set** order and repeats do not matter ($\{1, 2, 3, 2\} = \{3, 1, 2\}$, which has $3$ elements). In a **list** both matter ($1, 2, 3, 2$ and $1, 2, 2, 3$ are different).
- **Set terms**: union $A \cup B$ (in either or both), intersection $A \cap B$ (in both), subset, the empty set $\emptyset$, and **disjoint** (mutually exclusive) sets with $A \cap B = \emptyset$. $|S|$ is the number of elements.
- **Inclusion-Exclusion Principle**: $|A \cup B| = |A| + |B| - |A \cap B|$
    - If $A \cap B = \emptyset$, then $|A \cup B| = |A| + |B|$
    - For two overlapping groups: $\text{Total} = A + B - \text{Both} + \text{Neither}$. Example: $250$ travelers, $93$ to Africa, $155$ to Asia, $70$ both gives $93 + 155 - 70 = 178$ to at least one and $250 - 178 = 72$ to neither.
    - Venn diagrams (two or three sets) help organize these counts.
- **Multiplication Principle**: For sequential independent choices with $k$ possibilities followed by $m$ possibilities, total outcomes $= k \cdot m$. Without repeats the choices shrink: a password with one digit and three **different** letters has $10 \cdot 26 \cdot 25 \cdot 24 = 156{,}000$ options; with repeats allowed, $10 \cdot 26^3 = 175{,}760$. Eight coin tosses give $2^8 = 256$ outcomes.
- **Factorial**: $n! = n(n-1)(n-2)\cdots 2 \cdot 1$, with $0! = 1$ and $n! = n \cdot (n-1)!$
- **Permutations of all objects**: the number of orderings of $n$ distinct objects is $n!$
- **Permutations (Order matters)**: The number of ways to arrange $k$ objects from $n$ objects is $nP_k = \frac{n!}{(n-k)!}$
- **Combinations (Order does NOT matter)**: The number of ways to choose $k$ objects from $n$ objects is $nC_k = \frac{n!}{(n-k)! \cdot k!}$ (the number of $k$-element subsets). Example: $9C3 = 84$.
- **Symmetry**: $nC_k = nC_{n-k}$; also $nC_0 = nC_n = 1$ and $nC_1 = n$
- **Arrangements with repeats** (beyond the review): $n$ objects with $n_1$ alike of one kind, $n_2$ alike of another, etc.: $\frac{n!}{n_1!\, n_2! \cdots}$

### Probability Rules

- **Basics**: the sample space is all possible outcomes; an event is a set of outcomes. $0 \le P(E) \le 1$. The probabilities of all outcomes sum to $1$. If $E$ is certain, $P(E) = 1$; if impossible, $0$.
- **Equally likely outcomes**: $P(E) = \frac{\text{favorable outcomes}}{\text{total outcomes}}$. Outcomes need not be equally likely (a weighted die): let the base probability be $p$ and use the sum $= 1$ to solve for it.
- **Complement**: $P(\text{not } E) = 1 - P(E)$. For "at least one" problems, compute $1 - P(\text{none})$.
- **General Addition Rule**: $P(E \text{ or } F) = P(E) + P(F) - P(E \text{ and } F)$
- **Mutually Exclusive Events** (Cannot happen at the same time):
    - $P(E \text{ or } F) = P(E) + P(F)$
    - $P(E \text{ and } F) = 0$
- **Independent Events** (One does not affect the other):
    - $P(E \text{ and } F) = P(E) \times P(F)$
    - Example: two rolls of a die, $P(3 \text{ then } 3) = \frac{1}{6} \cdot \frac{1}{6} = \frac{1}{36}$
- **Dependent events** (e.g. drawing **without replacement**): $P(A \text{ then } B) = P(A) \cdot P(B \text{ given } A)$. Box of $5$ orange, $4$ red, $1$ blue: $P(\text{red then orange}) = \frac{4}{10} \cdot \frac{5}{9} = \frac{2}{9}$.
- **Conditional Probability** (beyond the review's notation): $P(E \mid F) = \frac{P(E \text{ and } F)}{P(F)}$. $E$ and $F$ are independent exactly when $P(E \mid F) = P(E)$.
- **Not independent example**: rolling a $3$ and rolling an odd number are dependent, since $P(\text{both}) = \frac{1}{6} \ne \frac{1}{6} \cdot \frac{1}{2}$.
- **Note**: mutually exclusive events with non-zero probabilities are **not** independent.

### Random Variables & Distributions

- **Random variable** $X$: a numerical outcome of a random experiment (for example, a randomly chosen value from a data set). $P(X = 3)$ is the relative frequency of the value $3$.
- **Probability distribution**: a table of values and probabilities; it equals the relative frequency distribution of the data and its probabilities sum to $1$.
- **Mean (expected value)**: $E(X) = \sum x_i \cdot P(x_i)$ (each value times its probability). Median, SD and the other statistics apply to the distribution as well.
- **Discrete** random variables have separate values; **uniform** means all outcomes are equally likely (a flat histogram).
- **Continuous** random variables use a density curve: probabilities are **areas** under the curve over intervals, the total area is $1$, and $P(X = c) = 0$ for any single value $c$.

---

# Common GRE Traps

> [!INFO] Read this first

- These are mistakes the GRE is designed to catch. Traps that are **already covered above are not repeated here**: the Quantitative Comparison special-values test and choice (D) logic, figures not drawn to scale, the algebra "Common Mistakes" list, percent traps (original base, successive changes, percentage points, different totals), average speed, work rates, "must" versus "could", and the unit-conversion note.
- **How to use this section**: before you finalize an answer, run through four quick checks: *sign* (can the variable be negative or zero?), *size* (is the answer plausible?), *units* (is it in the units asked?), *question* (did I answer the last line?).

### Number & Sign Traps

- **"Number" does not mean positive integer.** Unless told otherwise a variable can be negative, zero, or a fraction. Watch the exact words: *integer*, *positive* ($> 0$), *nonnegative* ($\ge 0$, includes $0$), *distinct*, *consecutive*.
- **Special numbers**: $0$ is even and is neither positive nor negative. $1$ is neither prime nor composite. $2$ is the only even prime. $0^n = 0$ and $1^n = 1$ for every positive $n$.
- **Squares have two roots.** $x^2 = 9$ gives $x = 3$ or $x = -3$; $x^2 = 16$ does **not** imply $x = 4$. Likewise $x^2 > 4$ means $x > 2$ **or** $x < -2$, not just $x > 2$.
- **Squaring does not preserve order for negatives.** $-3 < 2$ but $(-3)^2 > 2^2$. "If $x > y$ then $x^2 > y^2$" is false in general; it is safe only when both sides are non-negative.
- **Power direction depends on the size of $x$**:
    - $x > 1$: $x^2 > x$ and $\sqrt{x} < x$
    - $0 < x < 1$: $x^2 < x$, $\sqrt{x} > x$, and $\frac{1}{x} > 1$
    - $x < 0$: $x^2 > x$ (a square is never negative)
- **Never multiply or divide an inequality by an expression whose sign you do not know.** Example: $\frac{1}{x} > 2$ does **not** simply give $x < \frac{1}{2}$. For $x > 0$ it gives $0 < x < \frac{1}{2}$; for $x < 0$ the left side is negative, so no negative $x$ works.
- **Reciprocals reverse order only when both numbers have the same sign.** For $0 < a < b$: $\frac{1}{a} > \frac{1}{b}$. For $a < 0 < b$: $\frac{1}{a} < \frac{1}{b}$.
- **Adding the same number to top and bottom changes a fraction**: $\frac{1}{2} \to \frac{2}{3}$. Do not "cancel" across a sum.
- **Subtracting a sum**: $a - (b + c) = a - b - c$ (not $a - b + c$). Subtracting a negative adds: $5 - (-3) = 8$.
- **Wording order**: "$5$ less than $x$" is $x - 5$; "$x$ less than $5$" is $5 - x$. "$x$ is $3$ times $y$" is $x = 3y$ (not $y = 3x$).
- **Counting inclusively (fencepost)**: the integers from $12$ to $30$ **inclusive** number $30 - 12 + 1 = 19$, not $18$.
- **Division by a fraction**: $6 \div \frac{1}{2} = 12$ (not $3$). "Half of $6$" is $3$.
- **Percent of a fraction**: $\frac{1}{2}\% = 0.5\% = 0.005$, not $0.5$.

### Algebra Traps (Extra)

- **Dividing by a variable loses a solution.** $x^2 = 5x$ has **two** solutions, $x = 0$ and $x = 5$. Factor instead: $x(x - 5) = 0$.
- **Squaring both sides can create extraneous solutions.** $\sqrt{2x + 3} = x$ becomes $2x + 3 = x^2$, giving $x = 3$ or $x = -1$; but $x = -1$ fails the original (a square root cannot equal a negative). Always plug back in, and also exclude any value that makes a denominator $0$.
- **Function notation**: $f(x + 1) \ne f(x) + 1$ and $f(2x) \ne 2f(x)$. With $f(x) = x^2$: $f(x + 1) = x^2 + 2x + 1$ but $f(x) + 1 = x^2 + 1$; $f(2x) = 4x^2$ but $2f(x) = 2x^2$. Evaluate the inside first, then apply $f$.
- **Absolute-value inequalities**: $|x - 3| < 2$ means $1 < x < 5$ ("and"); $|x - 3| > 2$ means $x < 1$ **or** $x > 5$. $|x - 3| = 2$ gives two answers, $x = 1$ and $x = 5$.
- **Compare powers with a common exponent or base.** Is $2^{100}$ or $3^{60}$ larger? Write $2^{100} = (2^5)^{20} = 32^{20}$ and $3^{60} = (3^3)^{20} = 27^{20}$, so $2^{100}$ is larger.
- **"Solving" both quantities in a comparison**: if you multiply or divide both sides by a variable, check its sign first.

### Word-Problem Traps

- **"More than" versus "of"**: "$x$ is $25\%$ **more than** $y$" means $x = 1.25y$; "$x$ is $25\%$ **of** $y$" means $x = 0.25y$; "$x$ is $25\%$ **less than** $y$" means $x = 0.75y$.
- **Undoing a percent change is not the opposite percent**: after a $25\%$ increase ($100 \to 125$), returning to $100$ is a $20\%$ **decrease**, not $25\%$.
- **Ratios: part-to-part versus part-to-whole.** If boys : girls $= 3 : 5$, boys are $\frac{3}{8}$ of the class, not $\frac{3}{5}$. "The ratio of $a$ to $b$" is $a : b$ (order matters).
- **Average of averages**: do **not** average two group means unless the groups are the same size. Group A: $10$ people, mean $80$; group B: $30$ people, mean $90$. Combined mean $= \frac{800 + 2700}{40} = 87.5$, not $85$.
- **Overlapping groups**: do not double count. *Exactly one* of two groups $= A + B - 2(\text{Both})$. *At least one* $= A + B - \text{Both}$. *Neither* $= \text{Total} - (\text{at least one})$.
- **Read what is asked for**: solve for $x$, then answer the question (maybe $3x + 1$, a total rather than an average, a difference rather than a value, or an answer "in terms of $y$").

### Geometry Traps

- **Radius versus diameter.** If the problem gives the diameter, halve it before using $\pi r^2$ or $2\pi r$.
- **Scaling**: doubling a radius or a side multiplies **length** by $2$, **area** by $4$, and **volume** by $8$ (a circle's circumference only doubles). If a figure's perimeter doubles, its area quadruples.
- **Units**: perimeter and circumference are lengths (cm); area is cm$^2$; volume is cm$^3$.
- **Do not assume** right angles, parallel lines, equal sides, midpoints or equal angles from a drawing. Use only marked or stated facts.
- **The Pythagorean theorem is for right triangles only**, and the hypotenuse is the side **opposite** the $90^\circ$ angle (always the longest side).
- **Special triangles: put the $\sqrt{\ }$ on the right side.**
    - $45^\circ\text{-}45^\circ\text{-}90^\circ$: hypotenuse $=$ leg $\times \sqrt{2}$, so leg $=$ hypotenuse $\div \sqrt{2}$. A square with diagonal $d$ has side $\frac{d}{\sqrt{2}}$.
    - $30^\circ\text{-}60^\circ\text{-}90^\circ$: short leg $= x$ (opposite $30^\circ$), long leg $= x\sqrt{3}$ (opposite $60^\circ$), hypotenuse $= 2x$. The $\sqrt{3}$ belongs to the **long leg**, not the hypotenuse.
- **Height is not a slanted side.** For triangles, parallelograms and trapezoids use the **perpendicular** height. In an obtuse triangle the height can fall **outside** the triangle.
- **Shaded regions**: usually area of the whole minus area of the unshaded part(s). For a sector use $\frac{\text{central angle}}{360^\circ}$ times the circle's area (not its circumference); for an arc use that fraction times the **circumference**. Do not mix the two.
- **Polygon angle sum** uses $(n - 2) \times 180^\circ$, not $n \times 180^\circ$.
- **Coordinate geometry**:
    - Keep the point order consistent in slope: $\frac{y_2 - y_1}{x_2 - x_1}$ (do not subtract $y$'s in one order and $x$'s in the other).
    - A perpendicular slope **flips and changes sign**: $\frac{2}{3} \to -\frac{3}{2}$.
    - A point's coordinates in a quadrant must match its signs; points on an axis are in no quadrant.

### Counting & Probability Traps

- **Does order matter?** Roles or rankings (president, vice-president, treasurer; a lineup; a password) use permutations: $9 \cdot 8 \cdot 7 = 504$. A committee or hand uses combinations: $\binom{9}{3} = 84 = \frac{504}{3!}$.
- **Overcounting**: build counts from cases that do **not overlap**, or divide by the number of equivalent orderings. For "at least one", use the complement.
- **Repeated items**: arrangements of BOOK $= \frac{4!}{2!} = 12$, not $4! = 24$.
- **"And" versus "or"**: independent "A **and** B" **multiplies**; "A **or** B" **adds** (and subtracts the overlap). Adding for "and", or multiplying for "or", is a classic wrong answer.
- **The gambler's fallacy**: past independent outcomes do not change the next one. After five heads, the next flip is still $\frac{1}{2}$ heads. But "at least one head in $3$ flips" is $1 - \left(\frac{1}{2}\right)^3 = \frac{7}{8}$.
- **Outcomes are not always equally likely.** Two dice: the sum $7$ has probability $\frac{6}{36}$, the sum $12$ only $\frac{1}{36}$. Two coins: one head and one tail has probability $\frac{1}{2}$ (HT and TH), not $\frac{1}{3}$. Count the ordered outcomes.
- **Expected value** weights each outcome by its probability. It is **not** the simple average of the possible values.
- **Independent versus mutually exclusive**: they are different ideas (see Probability above); two events with non-zero probabilities cannot be both.

### Statistics & Data Interpretation Traps

- **Percentile is not a percent.** The $90$th percentile means about $90\%$ of the data are at or below that value; it does not mean a score of $90\%$.
- **Compare across distributions with $z$-scores.** A score of $80$ (mean $70$, SD $5$, so $z = 2$) is better than $75$ (mean $60$, SD $10$, so $z = 1.5$), even though the raw scores look close.
- **Normal-curve slices**: about $34\%$ lie between the mean and $1$ SD above it (half of $68\%$), and about $13.5\%$ between $1$ and $2$ SD above it. $P(X = c) = 0$ for a continuous variable.
- **Range is not standard deviation.** Two sets can share the same range but have different SDs, because the range depends only on the two extreme values. Set $0, 10, 10, 10, 10, 10, 20$ has a smaller SD than $0, 5, 10, 15, 20$, even though both have range $20$.
- **Read graphs carefully**:
    - Check the **units** (thousands? millions? percent?) and the **scale**. A vertical axis that does not start at $0$ exaggerates differences.
    - **Stacked bars**: a middle segment's size is the **difference** of its edges, not the value at the top.
    - **Largest change** may mean largest absolute change or largest percent change; use what the question says.
    - **Wrong row or year**: re-read the title, legend and the exact category the question names.
    - **Displayed percents** can add to $99\%$ or $101\%$ because of rounding.
    - **Histograms**: bar heights equal frequencies only when the classes have equal width; also check which class an endpoint belongs to.
    - **Trend lines** are for predicting inside the data range. Extrapolating far beyond it is unreliable, and association never proves causation.
- **Be careful with "approximately"**: pick the closest choice; when the choices are far apart, estimate rather than compute.

### Quantitative Comparison Traps (Extra)

- **One test value is not a proof.** Choice (C) needs the two quantities to be equal for **every** allowed value; (A) or (B) needs the **same** quantity to win every time. Test at least two or three values, including a negative, $0$, a fraction, and a large number.
- **Choose (D) only after you have shown two different outcomes**, not because the problem looks hard.
- **A symbol that appears in both quantities stands for the same value in both.** Information given above or between the two quantities applies to both.
- **Comparing fractions**: use a common denominator, or cross-multiply **only when both denominators are positive**.
- **Close quantities**: do not round carelessly. $3.14$ and $\frac{22}{7}$ differ in the third decimal place, so keep $\pi$ exact when the quantities are close.

### Answer-Format & Test-Strategy Traps

- **"Select one or more" questions**: you generally earn credit only by selecting **every** correct choice and **no** incorrect one. If the question says "select two", select exactly two.
- **Numeric entry**: follow the format and rounding instructions in the question; round only at the end. The on-screen calculator has a Transfer Display button for copying a result into the answer box.
- **Wrong-answer choices are built from typical mistakes**: the unfinished intermediate value, the sign-flipped value, the reciprocal, and the value from using $r$ instead of $d$. If your answer is a "too easy" match, re-check the last line of the question.
- **Sanity-check every answer**: sign, rough size, units, and whether it should be an integer.
- **Calculator**: use it for arithmetic, not for setting up the problem. Do **not** round intermediate results, use parentheses for negatives and fractions, and check the result against a quick estimate.
- **Do not leave questions blank**: there is no penalty for wrong answers.
- **Pacing**: spend roughly $1.5$ to $2$ minutes per question on average. Mark a question that is taking too long, move on, and return if time allows (you can go back within a section).


---

# Quantitative Comparison & Test-Taking Tips

> [!TIP] Tips

- **Quantitative Comparison answers**: (A) Quantity A is greater; (B) Quantity B is greater; (C) the two are equal; (D) the relationship cannot be determined.
- **Choose (D)** only if different allowed values of the variables flip the comparison. If any valid choice gives a different result than another valid choice, the answer is (D).
- **Test special values**: try negatives, zero, $1$, fractions between $0$ and $1$, and large numbers. Squaring or multiplying by a variable can change an inequality's direction.
- **Simplify both quantities** by doing the same operation to each (add or subtract the same term; multiply or divide by a positive number) before comparing.
- **Do not assume figures are drawn to scale** unless the problem says so. Use only the information stated.
- **Estimate when answer choices are far apart**; and use backsolving (plug in the answer choices) for equation-style word problems.
- **Check what is asked**: units, whether a variable must be an integer or positive, and "which of the following **must** be true" versus "**could** be true".
- **Units**: the review does not list unit conversions. Know time ($60$ s $= 1$ min, $60$ min $= 1$ hr, $24$ hr $= 1$ day, $7$ days $= 1$ week, $12$ months $= 1$ year). Anything else will normally be given. To convert area or volume units, square or cube the length factor ($1\ \text{ft}^2 = 144\ \text{in}^2$).

---

# Change Log (v1 to v2)

> [!INFO] Info

- **Corrected (errors)**:
    - Half-parabola labels: $\sqrt{y} = -x$ is the **left half** of $y = x^2$, not "downward"; $\sqrt{x} = -y$ is the **lower half** of $x = y^2$, not "left-opening"; the other two are the right half and upper half.
    - Discriminant with $D < 0$: "no real roots", not "2 imaginary roots".
    - Radical rules now state their domain conditions.
- **Corrected (precision)**: percent change base is the original value; perpendicular slopes apply to non-vertical lines; "almost all ($\sim 95\%$)" replaced by the full $68$-$95$-$99.7$ rule; quartile convention for odd $n$ stated; transversal angle relationships completed; "triangle ratio" and "Parabolas" wording tightened.
- **Added**: primes, factors, GCD/LCM, divisibility; fractions, ratios, order of operations, common values; absolute value; factoring; systems of equations; full function transformations; sequences; rate/work/distance, weighted average, simple interest; coordinate formulas; angle rules; triangle extras (triples, equilateral, similar triangles); quadrilaterals; circle theorems; cube and space diagonal; vertical parabolas; mean/median/mode/range and transformation effects; graph reading; counting extras; complement, general addition, conditional probability, expected value; Quantitative Comparison tips.

# Change Log (v2 to v3)

> [!INFO] Info

- **Added: HCF/GCD and LCM** with four tools (listing, prime factorization, Euclidean algorithm, $\gcd \cdot \operatorname{lcm} = ab$), worked examples, and when to use each.
- **Added from the Math Review**: zero rules and division by zero; intervals; remainders with negatives; factors/multiples facts and composites; mixed numbers, complex fractions, decimals and rational vs. irrational; three-part ratios; percents above 100%, finding the whole, successive changes and the different-totals trap; negative bases and odd roots; common algebra mistakes; cancelling factors with domain; linear equations with no solution or all solutions; positive roots of inequalities; domain details; coordinate-plane basics (quadrants, horizontal/vertical lines, line from two points, intercepts, inverse relation); graphing inequalities; parabola symmetry and intersections; $|x|$ graph; congruent and similar triangles; quadrilateral and circle terms; frequency, histogram, circle graph, scatterplot and line-graph reading; mean vs. median and combining groups; population vs. sample SD; percentiles; standardization usage; sets vs. lists and counting with/without repeats; weighted outcomes; dependent events; random variables, expected value, uniform and continuous distributions.
- **Labeled "beyond the review"**: divisibility rules, number of divisors, Vieta's formulas, sequences, Pythagorean triples, equilateral formulas, side-angle relation, inscribed-angle theorem, cube/space diagonal, arrangements with repeats, conditional probability notation.
- **Verified against the review**: half-parabola labels, discriminant wording, percent base, perpendicular slopes, odd-$n$ quartile rule (answer key IQR $= 17$), and that only rectangular solids and cylinders are covered.

# Change Log (v3 to v4)

- Added common GRE traps.
