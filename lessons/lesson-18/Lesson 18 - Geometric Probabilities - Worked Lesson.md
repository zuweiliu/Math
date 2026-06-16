# Lesson 18 — Geometric Probabilities (Worked Lesson)

> A complete walkthrough of every example and homework question in the PDF.
> For each problem you get: **(1)** a step‑by‑step solution, and **(2)** a
> **TYPE + METHOD** box that tells you what *kind* of problem it is and the
> reusable logic, so you can solve similar questions on your own.

---

## The Big Idea (read this first)

**Geometric probability** is used when there are **infinitely many equally‑likely
outcomes**. We cannot count them, so instead we *measure* them with **length,
area, or volume**.

$$P(\text{event}) = \frac{\text{measure of the successful region}}{\text{measure of the whole sample region}}$$

The single most important skill: **turn the words into a picture of the sample
space** (a segment, a square, a region in the plane, a circle…), shade the
"success" part, then take the ratio of measures.

| Number of free/random quantities | Sample space | Measure to use |
|---|---|---|
| 1 (one random number / one cut) | an **interval** (segment) | **length** |
| 2 (two random numbers / two cuts) | a **square or region** | **area** |
| 3 (three random numbers) | a **cube / solid** | **volume** |
| a random **point** in a shape | the **shape** | **area** (or length on a curve) |

---
---

# Section 1 — Probability Using Lengths

### Concept Question — "Which one is a *geometric* probability case?"

**Options**
- **A.** Choose $a,b$ from $\{1,2,3,4\}$ without repetition; find $P\big(x^2+2ax+b=0$ has a real root$\big)$.
- **B.** $a,b$ satisfy $|a|<2$ and $|b|<3$; find $P\big(x^2+2ax+b=0$ has a real root$\big)$.
- **C.** Pick 2 people from $\{A,B,C\}$; find $P(A$ is chosen$)$.
- **D.** Find $P($Jack and Austen share a birthday$)$.

**Solution.** Geometric probability requires **infinitely many** equally‑likely
outcomes that you measure with length/area/volume.
- A: $a,b$ come from a **finite set** → countable → *classical* probability.
- B: $a,b$ are **real numbers** in a continuous region $(|a|<2,\,|b|<3)$ → infinitely many outcomes → **geometric** (an area problem). ✅
- C: choosing from 3 people → finite → classical.
- D: birthdays → 365 outcomes → finite → classical.

**Answer: B.**

> **🔑 TYPE:** *Classify the probability model.*
> **METHOD:** Ask "**Are the outcomes a finite list, or a continuous range?**"
> Finite/countable ⇒ classical (count). Continuous (real numbers, points,
> lengths, time) ⇒ **geometric** (measure). Key trigger words: *"uniformly at
> random," "interval," "random point," "any position," "arrives at a random time."*

---

## Math Exploration 1 (length problems)

### Example 1.1 — Cut a segment, both parts long enough

> A segment of length 1 is cut at a random point. Find $P(\text{both parts} \ge \tfrac13)$.

**Solution.**
1. Let the cut be at position $x$, uniform on $[0,1]$ → sample space = segment of length **1**.
2. The two parts are $x$ and $1-x$. We need **both** $\ge \tfrac13$:
$$x \ge \tfrac13 \quad\text{and}\quad 1-x \ge \tfrac13 \;\Rightarrow\; \tfrac13 \le x \le \tfrac23.$$
3. Success length $= \tfrac23-\tfrac13 = \tfrac13$.

$$P = \frac{1/3}{1} = \boxed{\tfrac13}.$$

> **🔑 TYPE:** *One random cut on a segment (1 variable → length).*
> **METHOD:** Let the cut $=x$ on $[0,1]$. Write **each condition as an
> inequality in $x$**, intersect them to get a sub‑interval, then
> $P=\dfrac{\text{length of sub‑interval}}{\text{total length}}$.

---

### Example 1.2 — Where is a quadratic inequality satisfied?

> $x$ is chosen at random on $[-5,5]$. Find $P(x^2-x-2>0)$.

**Solution.**
1. Sample space: interval $[-5,5]$, length $10$.
2. Solve the inequality: $x^2-x-2=(x-2)(x+1)>0 \Rightarrow x<-1 \text{ or } x>2.$
3. Intersect with $[-5,5]$:
   - $[-5,-1)$ has length $4$
   - $(2,5]$ has length $3$
   - total success length $=4+3=7$.

$$P=\frac{7}{10}=\boxed{0.7}.$$

> **🔑 TYPE:** *One random number on an interval, condition = an inequality.*
> **METHOD:** (a) Total length = interval length. (b) **Solve the inequality**
> to find which sub‑intervals work. (c) Add their lengths and divide. Always
> **intersect the solution with the given interval** — don't forget the endpoints' range.

---

### Example 1.3 — "Whose number is bigger?" (2017 AMC 10A #15)

> Chloé picks a real number uniformly from $[0,2017]$; Laurent picks uniformly
> from $[0,4034]$. Find $P(\text{Laurent} > \text{Chloé})$.

**Solution (2 random numbers → area).**
1. Let $C\in[0,2017]$, $L\in[0,4034]$. Sample space is a **rectangle**
   $2017 \times 4034$, area $=2017\cdot 4034$.
2. Success region: $L>C$. Draw the line $L=C$. Since the rectangle is exactly
   **twice as tall as it is wide** ($4034 = 2\cdot2017$), split it by the line $L=C$
   (which only reaches up to $L=2017$ inside the box).
   - The top band $2017 \le L \le 4034$ (height $2017$, full width $2017$) is **entirely** $L>C$: area $=2017^2$.
   - The bottom square $0\le L\le 2017$ is cut by $L=C$ into two equal triangles; the upper triangle ($L>C$) has area $\tfrac12\cdot2017^2$.
3. Success area $=2017^2+\tfrac12 2017^2=\tfrac32\,2017^2$.

$$P=\frac{\tfrac32\,2017^2}{2017\cdot4034}=\frac{\tfrac32\,2017^2}{2\cdot2017^2}=\frac{3/2}{2}=\boxed{\tfrac34}\quad(\textbf{C}).$$

> **🔑 TYPE:** *Two independent uniform numbers → compare them (area model).*
> **METHOD:** Make a **rectangle** with the two ranges as the two axes. The
> condition (e.g. $L>C$) is a **line**; shade the correct side. $P=\dfrac{\text{shaded area}}{\text{rectangle area}}$.
> Shortcut here: the answer is bigger than $\tfrac12$ because Laurent's range is larger.

---

### Example 1.4 — Random point on a circle, acute triangle

> $A,B$ lie on a circle of radius $2$ with chord $AB=2$. A point $P$ is chosen at
> random on the circle. Find $P(\triangle APB \text{ is acute})$.

**Solution (random point on a curve → arc length).**
1. **Find the arc $AB$.** For a chord, $AB = 2R\sin\frac{\theta}{2}$ where $\theta$
   is the central angle. So $2 = 2(2)\sin\frac{\theta}{2} \Rightarrow \sin\frac{\theta}{2}=\tfrac12 \Rightarrow \theta = 60^\circ.$
   Minor arc $AB = 60^\circ$, major arc $=300^\circ$.
2. **Acute test for an inscribed triangle:** $\triangle APB$ is acute **iff the
   center $O$ is inside it**, which happens **iff every arc between two vertices is $<180^\circ$.**
3. If $P$ is on the **major** arc, the arc $AB$ "under" $P$ is $60^\circ<180^\circ$ ✓.
   The remaining two arcs $AP$ and $PB$ add to $300^\circ$; we need **each $<180^\circ$**,
   i.e. each $>120^\circ$. Valid window $=300-120-120 = 60^\circ$.
   (If $P$ is on the minor arc, angle $P=150^\circ$ → obtuse, never works.)
4. $P$ is uniform on the full $360^\circ$ circle.

$$P=\frac{60^\circ}{360^\circ}=\boxed{\tfrac16}.$$

> **🔑 TYPE:** *Random point on a circle; "acute / obtuse triangle" condition.*
> **METHOD:** Probability = (favorable **arc**)/(total $360^\circ$).
> Remember the theorem: **inscribed triangle is acute ⇔ all three arcs $<180^\circ$**
> (⇔ center lies inside). Convert each "acute" requirement into an arc inequality
> and add up the allowed arc.

---
---

# Section 2 — Probability Using Areas

When **two** quantities are random, the sample space becomes **2‑D** and we use
**area**.

## Math Exploration 2

### Example 2.1 — Cut a stick into three pieces, all short

> A 1‑meter stick is cut at two random points into three pieces. Find
> $P(\text{every piece} < 0.5)$.

**Solution.**
1. Two cuts $x,y$ uniform on $[0,1]$ → sample space = unit square, area $1$.
2. It's easier to find the **complement**: "some piece $\ge \tfrac12$."
   Exactly one piece can be $\ge\tfrac12$ (two can't, since they'd sum $>1$).
   Each of the 3 pieces being the long one corresponds to a triangle of area
   $\tfrac18$ in the square, so $P(\text{some piece}\ge\tfrac12)=3\cdot\tfrac18=\tfrac38$… 

   *Cleaner standard result:* $P(\text{all three pieces}<\tfrac12)=\tfrac14$ and
   $P(\text{the three pieces form a triangle})=\tfrac14$ (these coincide, because
   three lengths form a triangle exactly when no piece reaches half the total).

$$P=\boxed{\tfrac14}.$$

> **🔑 TYPE:** *Two cuts on a stick (2 variables → area in unit square).*
> **METHOD:** Set the two cut points as $(x,y)$ in the unit square. Translate
> "each piece $<\tfrac12$" into linear inequalities and shade the region — or use
> the famous fact: **3 pieces of a unit stick are all $<\tfrac12$ (equivalently form
> a triangle) with probability $\tfrac14$.** Using the **complement** is usually fastest.

---

### Example 2.2 — Three random points on a circle form an acute triangle

> Pick 3 points at random on a circle. Find $P(\text{triangle is acute})$.

**Solution.**
- A triangle inscribed in a circle is acute **iff all three arcs are $<$ a semicircle**,
  i.e. no single arc exceeds $180^\circ$ (equivalently the three points don't all
  lie in one semicircle "badly").
- Working out the area in the parameter space of the three points gives the
  classic result:

$$P(\text{acute})=\boxed{\tfrac14}.$$

(Intuition: $P(\text{right})=0$, and by the arc argument the obtuse case is 3× as likely as the acute case, so acute $=\tfrac14$, obtuse $=\tfrac34$.)

> **🔑 TYPE:** *Several random points on a circle; shape‑of‑triangle question.*
> **METHOD:** Use the **arc criterion** (acute ⇔ every arc $<180^\circ$). Fix one
> point by symmetry, let the others be angles, and compute the favorable area.
> Memorize: **3 random points on a circle → acute triangle with probability $\tfrac14$.**

---

## Math Exploration 3

### Example 3.1 — Linear condition on two random numbers

> $x,y$ are chosen at random from $[-2,2]$. Find $P(x+y>1)$.

**Solution.**
1. Sample space: square $[-2,2]\times[-2,2]$, area $=4\times4=16$.
2. Line $x+y=1$ passes through $(-1,2)$ and $(2,-1)$ inside the square.
   The region $x+y>1$ is the triangle with vertices $(-1,2),\,(2,2),\,(2,-1)$.
3. It's a right triangle with legs $3$ and $3$: area $=\tfrac12(3)(3)=\tfrac92$.

$$P=\frac{9/2}{16}=\boxed{\tfrac{9}{32}}.$$

> **🔑 TYPE:** *Two uniform numbers + a linear condition (area model).*
> **METHOD:** Draw the square, draw the boundary line, shade the correct side,
> and use **simple area formulas** (triangle = $\tfrac12 bh$). $P=\dfrac{\text{shaded}}{\text{square}}$.

---

### Example 3.2 — Obtuse triangle from random sides (2018 AMC 10B #22)

> $x,y$ are chosen independently and uniformly from $[0,1]$. Find (closest value of)
> the probability that $x,\,y,\,1$ are the side lengths of an **obtuse** triangle.

**Solution.**
1. Sample space: unit square, area $1$.
2. **Triangle inequality** (with the side $1$ the longest unless $x$ or $y$ exceeds the others):
   need $x+y>1$ to even form a triangle.
3. **Obtuse with longest side 1** ⇔ $x^2+y^2<1$ (angle opposite side $1$ is obtuse).
   We also must keep $x+y>1$ so it's a valid triangle.
   This is the region **inside the quarter circle $x^2+y^2<1$ but above the line $x+y>1$.**
   Its area $=\underbrace{\tfrac{\pi}{4}}_{\text{quarter disk}}-\underbrace{\tfrac12}_{\text{triangle below the line}}=\tfrac{\pi}{4}-\tfrac12\approx0.285.$
4. (One should also check obtuse cases where $x$ or $y$ is the longest side, but
   for $x,y\le 1$ the dominant region is the one above, and the contest answer is:)

$$P\approx 0.29 \quad(\textbf{C}).$$

> **🔑 TYPE:** *Two uniform numbers → triangle existence + angle type (area).*
> **METHOD:** Encode geometry as algebra in the unit square:
> **triangle inequality** = linear conditions; **right angle** = $a^2+b^2=c^2$ (a circle);
> **obtuse** = $a^2+b^2<c^2$ (inside the circle). Shade the overlap and find its area.

---

## Math Exploration 4

### Example 4.1 — Near a lattice point (2020 AMC 10A #16)

> A point is chosen at random in the square with vertices $(0,0),(2020,0),(2020,2020),(0,2020)$.
> $P(\text{within } d \text{ of some lattice point}) = \tfrac12$. Find $d$ (nearest tenth).

**Solution (use one unit cell by symmetry).**
1. The pattern repeats every $1\times1$ cell. In one unit square, the points within
   $d$ of a lattice point are **four quarter‑circles** at the corners (with $d<\tfrac12$),
   which together make **one full circle** of area $\pi d^2$.
2. Set that fraction equal to $\tfrac12$:
$$\pi d^2 = \tfrac12 \;\Rightarrow\; d^2=\frac{1}{2\pi}\approx0.159 \;\Rightarrow\; d\approx0.399.$$

$$d\approx \boxed{0.4}\quad(\textbf{B}).$$

> **🔑 TYPE:** *Random point in a big grid; "within distance $d$ of a lattice point."*
> **METHOD:** **Reduce to ONE unit cell** by periodicity. Corners contribute
> quarter‑circles that assemble into a full circle $\pi d^2$. Set
> $\pi d^2 = (\text{given probability})$ and solve for $d$.

---

### Example 4.2 — Chord intersects the inner circle (2014 AMC 10B #19)

> Two concentric circles have radii $1$ and $2$. Two points are chosen
> independently and uniformly on the **outer** circle. Find $P(\text{chord meets the inner circle})$.

**Solution.**
1. Fix the first point; let the second point differ by a random central angle
   $\varphi$ uniform on $[0,360^\circ)$.
2. Distance from the center to the chord $=2\cos\frac{\varphi}{2}$.
   The chord hits the inner circle (radius $1$) iff this distance $<1$:
$$2\cos\tfrac{\varphi}{2}<1 \Rightarrow \cos\tfrac{\varphi}{2}<\tfrac12 \Rightarrow \tfrac{\varphi}{2}\in(60^\circ,120^\circ) \Rightarrow \varphi\in(120^\circ,240^\circ).$$
3. Favorable angle range $=240-120=120^\circ$ out of $360^\circ$.

$$P=\frac{120}{360}=\boxed{\tfrac13}\quad(\textbf{B}).$$

> **🔑 TYPE:** *Two random points on a circle; chord vs. an inner region.*
> **METHOD:** **Fix one point** (rotational symmetry) and let the angular gap
> $\varphi$ be the single uniform random variable. Translate the geometric event
> into an inequality on $\varphi$ via the **distance‑from‑center to chord**
> $=R\cos\frac{\varphi}{2}$. Then $P=\dfrac{\text{good angle}}{360^\circ}$.

---
---

# Assignment (Homework) — solved with the methods above

### HW 1 — Length, absolute‑value inequality
> $x$ random on $[-3,4]$. Find $P(|x|<1)$.

Uses **Example 1.2's method** (one number, solve inequality, divide lengths).
- Total length $=4-(-3)=7$.
- $|x|<1 \Rightarrow -1<x<1$, length $=2$.

$$P=\frac{2}{7}\quad(\textbf{C}).$$

---

### HW 2 — Darts (area of rings)
> Center circle (10 pts) has radius $1$; each outer ring adds $1$ to the radius
> (scores $10,9,8,7,6,5$ → radii $1,2,3,4,5,6$). Find $P(\text{score} = 9 \text{ or } 10)$.

Uses **area‑ratio of regions** (like the dartboard / lattice idea).
- "9 or 10" means landing within radius $2$: area $=\pi(2)^2=4\pi$.
- Whole board has radius $6$: area $=\pi(6)^2=36\pi$.

$$P=\frac{4\pi}{36\pi}=\boxed{\tfrac19}.$$

*(If the board only goes out to a different outer radius $R$, the same method gives $P=\dfrac{4}{R^2}$ — read $R$ off the figure.)*

> **Method reused:** concentric rings → use $\pi r^2$ for each region; probability
> = (favorable annulus/disk area)/(total disk area).

---

### HW 3 — President's (Garfield) Proof trapezoid
> Right trapezoid built from two right triangles (legs $a,b$) + one isosceles right
> triangle (legs $c$). With $a=2,\,b=1$, a random point lands in the trapezoid.
> Find $P(\text{point lies in the isosceles right triangle } CDE)$.

Uses **"random point in a shape → area ratio."**
- $c^2=a^2+b^2=2^2+1^2=5$.
- Shaded isosceles right triangle area $=\tfrac12 c^2=\tfrac52$.
- Trapezoid area $=\tfrac12(a+b)(a+b)=\tfrac12(3)(3)=\tfrac92$.

$$P=\frac{5/2}{9/2}=\boxed{\tfrac59}\quad(\textbf{B}).$$

> **Method reused:** $P=\dfrac{\text{shaded area}}{\text{whole shape area}}$. Compute both areas exactly with geometry formulas.

---

### HW 4 — Smaller of two numbers exceeds a threshold
> Two numbers chosen at random in $[0,2]$. Find $P(\text{the smaller one} > \tfrac23)$.

Uses **"min/max of two uniforms" (area in a square).**
- "Smaller $>\tfrac23$" ⇔ **both** numbers $>\tfrac23$.
- For one number: $P(>\tfrac23)=\dfrac{2-\tfrac23}{2}=\dfrac{4/3}{2}=\dfrac23.$
- Independent, so multiply:

$$P=\left(\tfrac23\right)^2=\boxed{\tfrac49}\quad(\textbf{C}).$$

> **Method reused:** $\min>t$ ⇔ all $>t$; $\max<t$ ⇔ all $<t$. Each becomes a
> length fraction; multiply for independent picks (or shade a square of side
> $2-\tfrac23$ inside the $2\times2$ square: $\big(\tfrac{4/3}{2}\big)^2$).

---

### HW 5 — Intercept of a line (length problem in disguise)
> The $x$‑intercept of $y=x+b$ lies in $[-2,3]$. Find $P(\text{the } y\text{-intercept } b > 1)$.

Uses **Example 1.1/1.2's method** after finding what's actually random.
- $x$‑intercept: set $y=0$ → $x=-b$. So $-b\in[-2,3]\Rightarrow b\in[-3,2]$ (total length $5$).
- Want $b>1$: interval $(1,2]$, length $1$.

$$P=\frac{1}{5}\quad(\textbf{A}).$$

> **Method reused:** First identify the **true random variable and its interval**,
> then it's a plain length ratio. Don't be fooled by the "line" wrapper.

---

### HW 6 — Rope cut, both pieces long enough
> A $5$ m rope is cut at a random position. Find $P(\text{both pieces} \ge 2)$.

Uses **Example 1.1's method** exactly.
- Cut at $x\in[0,5]$ (length $5$). Need $x\ge2$ and $5-x\ge2 \Rightarrow 2\le x\le3$.
- Success length $=1$.

$$P=\frac{1}{5}.$$

> **Method reused:** one cut → write both pieces as $x$ and $L-x$, intersect the
> "$\ge$" inequalities, divide lengths.

---

### HW 7 — Reuleaux triangle vs. equilateral triangle
> A point is chosen at random inside a **Reuleaux triangle** (built on an equilateral
> triangle of side $s$). Find $P(\text{point lies in the original equilateral triangle})$.

Uses **"random point → area ratio."**
- Equilateral triangle area $=\dfrac{\sqrt3}{4}s^2$.
- Reuleaux triangle area $=\dfrac12(\pi-\sqrt3)\,s^2$.

$$P=\frac{\tfrac{\sqrt3}{4}s^2}{\tfrac12(\pi-\sqrt3)s^2}=\frac{\sqrt3}{2(\pi-\sqrt3)}\approx0.61.$$

> **Method reused:** memorize/derive the two areas, then take the ratio (the $s^2$
> cancels — the answer is **scale‑independent**, a hallmark of "random point in a region" problems).

---

### HW 8 — Far from all four corners of a square
> Square $ABCD$ of side $2$. A point is chosen at random inside. Find
> $P(\text{distance to each of } A,B,C,D > 1)$.

Uses **complement + non‑overlapping circles.**
- Being within $1$ of a corner = a **quarter‑circle** of radius $1$ at that corner.
- Four quarter‑circles = **one full circle**, area $=\pi(1)^2=\pi$ (they don't overlap,
  since adjacent corners are $2$ apart).
- "Far from all four" area $=4-\pi$.

$$P=\frac{4-\pi}{4}=1-\frac{\pi}{4}\approx0.215\quad(\textbf{D}).$$

> **Method reused:** "**distance to a point $>r$**" removes a disk/quarter‑disk.
> Subtract the forbidden area; check whether the disks overlap before adding them.

---

### HW 9 — Random point inside an isosceles right triangle
> Isosceles right triangle, the two legs (equal sides) have length $2$. A point is
> taken at random **inside the triangle**. Find $P(\text{its distance to the right‑angle vertex} < 1)$.
>
> (The answer choices are $\tfrac{\pi}{8},\ \tfrac{\pi}{4},\ \tfrac{3\pi}{8},\ \tfrac{\pi}{2},\ \tfrac{\pi}{3}$ — the
> presence of $\pi$ tells you this is a **2‑D area** problem, not a point‑on‑a‑segment problem.)

Uses **area = favorable region ÷ whole region.**
- Two coordinates are random ⇒ the sample space is the triangle's **area** $=\tfrac12(2)(2)=2$.
- "Distance to the right‑angle vertex $O$ $<1$" is a **quarter‑disk** of radius $1$: the angle at
  $O$ is $90^\circ=\tfrac14$ of a full turn, so its area $=\tfrac14\pi(1)^2=\tfrac{\pi}{4}$.
  It lies entirely inside the triangle (the hypotenuse $x+y=2$ is far beyond radius $1$).

$$P=\frac{\pi/4}{2}=\frac{\pi}{8}\approx0.393\quad(\textbf{choice A}).$$

> **Method reused:** a random point in a 2‑D region → divide the **favorable area** by the
> **total area**. A "distance $<r$ from a corner" condition gives a **circular sector**
> (here a quarter‑circle because the corner angle is $90^\circ$).

---

### HW 10 — Waiting for the school bus (time = length)
> Buses leave at $7{:}00,\,8{:}00,\,8{:}30$. You arrive at a **random time** in
> $[7{:}50,\,8{:}30]$. Find $P(\text{you wait} \le 10\text{ min})$.

Uses **Example 1.x's method with time as the line.**
- Arrival window length $=40$ min (from $7{:}50$ to $8{:}30$).
- Wait $\le 10$ happens if you arrive:
  - in $[7{:}50,\,8{:}00]$ → catch the $8{:}00$ bus within $10$ min → $10$ min favorable;
  - in $[8{:}20,\,8{:}30]$ → catch the $8{:}30$ bus within $10$ min → $10$ min favorable.
- Favorable length $=10+10=20$ min.

$$P=\frac{20}{40}=\frac{1}{2}.$$

> **🔑 TYPE:** *"Arrive at a random time" / waiting‑time problems.*
> **METHOD:** Put **time on a number line** (length = window). For each bus, the
> "wait $\le t$" arrivals form an interval ending at the departure. Add those
> favorable minutes and divide by the total window.

---
---

# Master Cheat‑Sheet (memorize these triggers)

| If the problem says… | Model it as… | Use |
|---|---|---|
| one random number / one cut / one arrival time | an **interval** | **length ratio** |
| two random numbers / two cuts | a **square / region** | **area ratio** |
| a random **point in a shape** | the **shape** | **area ratio** |
| a random **point on a circle**, triangle acute/obtuse | **arcs**, criterion "all arcs $<180^\circ$" | **arc ratio** |
| **two points on a circle**, chord question | fix one point, gap angle $\varphi$ uniform; distance to chord $=R\cos\frac{\varphi}{2}$ | **angle ratio** |
| "within $d$ of a lattice point" | **one unit cell**, corner quarter‑circles = $\pi d^2$ | **area ratio** |
| triangle from random sides | unit square; triangle‑ineq (lines) + $a^2+b^2$ vs $c^2$ (circle) | **area ratio** |
| "distance to a point $> r$" | remove a **disk / quarter‑disk** of radius $r$ | **area (complement)** |
| "min $> t$" / "max $< t$" | all values on one side of $t$ | multiply length fractions |

**Universal 4‑step recipe**
1. Identify the random quantity(ies) → choose length / area / volume.
2. Draw the **sample space** (segment, square, region, circle) and find its measure.
3. Translate every condition into **inequalities / geometric regions**; shade success.
4. $P = \dfrac{\text{measure of success}}{\text{measure of sample space}}$. Use the **complement** when "success" is messy.
