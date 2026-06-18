# Factorization (AMC 10 AIME Camp) — Preview Worked Lesson

> **Preview before the teacher's lesson.** This follows the same scope as the
> camp PDF *"Preview: Basic Ways of Factorization"* (Lesson 1-8), but every
> example here is **different** from the PDF so the in-class problems stay fresh.
> After the teacher's lesson we will build the full lesson on the official
> PDF problems.

---

## Preview — Basic Ways of Factorization (review)

Factoring rewrites a polynomial as a **product of simpler polynomials**. Keep
these automatic before the advanced tricks:

- **GCF first:** pull out the greatest common factor.
- **Difference of squares:** $a^2-b^2=(a+b)(a-b)$
- **Perfect square trinomial:** $a^2\pm 2ab+b^2=(a\pm b)^2$
- **Sum of cubes:** $a^3+b^3=(a+b)(a^2-ab+b^2)$
- **Difference of cubes:** $a^3-b^3=(a-b)(a^2+ab+b^2)$
- **Cube of a binomial:** $a^3\pm 3a^2b+3ab^2\pm b^3=(a\pm b)^3$
- **Cross method:** $ax^2+bx+c\to(mx+p)(nx+q)$

**Warm-up.** $50x^2-72=2(25x^2-36)=2(5x-6)(5x+6)$. GCF first, squares after.

---

## Section 1 — Advanced Ways of Factorization

### Concept 1 — Factoring by Grouping

Used when a polynomial has **four or more terms** and no overall GCF. Group so
each part shares a factor. Common shapes: **2-2 grouping** and **3-1 grouping**.

**Example 1 (2-2).** Factor $x^3+3x^2+2x+6$.
$$x^3+3x^2+2x+6=x^2(x+3)+2(x+3)=(x+3)(x^2+2).$$

> **TYPE:** 2-2 grouping. **METHOD:** Split into two pairs that each factor, then
> pull out the shared binomial.

**Example 2 (3-1).** Factor $x^2+6x+9-y^2$.
$$=(x+3)^2-y^2=(x+3-y)(x+3+y).$$

> **TYPE:** 3-1 grouping. **METHOD:** Find three terms forming a perfect square,
> then use $A^2-B^2$ with the leftover.

---

### Concept 2 — Splitting & Adding Terms (Completing Squares)

- **Splitting:** rewrite one term as a sum (e.g. $3a^2=a^2+2a^2$).
- **Adding:** add and subtract the same quantity to expose a perfect square.
- Finish with a difference of squares $A^2-B^2=(A-B)(A+B)$.

**Example 3 (add/subtract).** Factor $x^4+4$.
$$x^4+4=x^4+4x^2+4-4x^2=(x^2+2)^2-(2x)^2=(x^2-2x+2)(x^2+2x+2).$$

> **TYPE:** Add the missing $2AB$ term. **METHOD:** Build $A^2-B^2$ by adding the
> middle term and subtracting it back as a square.

**Example 4 (split the middle term).** Factor $a^2-6a+8$.
$$a^2-2a-4a+8=a(a-2)-4(a-2)=(a-2)(a-4).$$

> **TYPE:** Split $bx$ into two terms with product $ac$, sum $b$; then group.

---

### Concept 3 — Simon's Favorite Factoring Trick (SFFT)

For $xy+ax+by$, add the constant $ab$ so it factors:
$$xy+ax+by+ab=(x+b)(y+a).$$

**Example 5.** Positive integers $x,y$ with $xy+2x+y=20$. Find all $(x,y)$.
$$xy+2x+y = x(y+2)+(y+2)-2 \;\Rightarrow\; (x+1)(y+2)=22.$$
Positive divisor pairs with $x+1\ge2,\ y+2\ge3$: $(2,11)\Rightarrow(x,y)=(1,9)$;
$(11,2)$ gives $y=0$ (rejected).
$$\boxed{(x,y)=(1,9)}$$

> **TYPE:** SFFT integer equation. **METHOD:** Complete $(x+b)(y+a)$, then match
> positive-divisor pairs of the right-hand number.

---

### Concept 4 — Extreme Values by Completing Squares

Since $A^2\ge 0$, writing an expression as **(squares) + constant** reveals its
minimum immediately.

**Example 6.** Least value of $x^2+6x+11$.
$$=(x+3)^2+2\ge 2,\quad\text{min }2\text{ at }x=-3.$$

**Example 7.** Least value of $x^2+2y^2-2xy+4y+7$.
$$=(x-y)^2+(y^2+4y+7)=(x-y)^2+(y+2)^2+3\ge 3,$$
minimum $3$ at $y=-2,\ x=-2$.

> **TYPE:** Sum-of-squares minimum. **METHOD:** Complete the square one variable
> at a time until only $\ge0$ squares plus a constant remain.

---

## Practice-by-Type Answer Key (short)

1. $2x^3-x^2+6x-3=(2x-1)(x^2+3)$
2. $a^2-2a+1-9b^2=(a-1-3b)(a-1+3b)$
3. $x^4+x^2+1=(x^2-x+1)(x^2+x+1)$
4. $3x^2+10x+8=(3x+4)(x+2)$
5. $xy+3x+2y=29\Rightarrow(x+2)(y+3)=35\Rightarrow(x,y)=(3,4)$
6. $2x^2+8x+15=2(x+2)^2+7$, min $7$
7. $x^4-7x^2+1=(x^2-\sqrt5\,x-1)(x^2+\sqrt5\,x-1)$

---

## Final Checklist (preview)

- GCF first?
- Four+ terms → try **grouping** (2-2 or 3-1)?
- "Almost a square" → **add/subtract** to build $A^2-B^2$?
- Two integer unknowns, $xy+\dots$ → **SFFT**?
- Asked for min/max → **complete the square**?

That sequence covers the four concepts you'll see in the teacher's lesson.
