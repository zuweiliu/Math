# Factorization (AMC 10 AIME Camp) - Regular Worked Lesson

This regular lesson follows the camp PDF scope and uses the same example/homework types.

---

## Concept 1 - Factoring by Grouping

### Example 1
Given
\[
a^2+2b^2+2c^2-2ab-2bc-6c+9=0,
\]
find \(abc\).

\[
a^2+2b^2+2c^2-2ab-2bc-6c+9=(a-b)^2+(b-c)^2+(c-3)^2.
\]
Since this sum is 0, each square is 0:
\[
a=b,\quad b=c,\quad c=3.
\]
So \(a=b=c=3\), and
\[
\boxed{abc=27}.
\]

### Example 2
If
\[
x^2+y^2=10x-6y-34,
\]
find \(x+y\).

Move terms:
\[
x^2-10x+y^2+6y+34=0.
\]
Complete squares:
\[
(x-5)^2-25+(y+3)^2-9+34=0
\]
\[
(x-5)^2+(y+3)^2=0.
\]
Hence \(x=5\), \(y=-3\), so
\[
\boxed{x+y=2}.
\]

---

## Concept 2 - Splitting and Adding Terms

### Example 3
Factor
\[
a^2-4a+3.
\]
Find numbers with product \(3\) and sum \(-4\): \(-1,-3\).
\[
a^2-4a+3=(a-1)(a-3).
\]

### Example 4
Factor
\[
x^4+4.
\]

How to figure out the added term:

We want a difference of squares,
\[
x^4+4=\text{(square)}-\text{(square)}.
\]
Try
\[
(x^2+m)^2-(nx)^2=x^4+(2m-n^2)x^2+m^2.
\]
To match \(x^4+4\):

- Constant term requires \(m^2=4\Rightarrow m=2\).
- No \(x^2\)-term requires \(2m-n^2=0\Rightarrow 4-n^2=0\Rightarrow n=2\).

So the target is
\[
(x^2+2)^2-(2x)^2,
\]
which means we must add and subtract \(4x^2\).

Now compute:
\[
x^4+4=x^4+4x^2+4-4x^2=(x^2+2)^2-(2x)^2.
\]
Difference of squares:
\[
\boxed{x^4+4=(x^2-2x+2)(x^2+2x+2)}.
\]

---

## Concept 3 - Simon's Favorite Factoring Trick (SFFT)

### Example 5
Given positive integers \(x,y\):
\[
xy-2x-3y=6,
\]
find the sum of all possible values of \(x\).

Add 6:
\[
xy-2x-3y+6=12
\]
\[
(x-3)(y-2)=12.
\]
For positive integers, \(x-3\in\{1,2,3,4,6,12\}\):
\[
x\in\{4,5,6,7,9,15\}.
\]
Sum:
\[
4+5+6+7+9+15=\boxed{46}.
\]

### Example 6
Given positive integers \(x,y\):
\[
6xy-10x-21y=49,
\]
find all solution pairs.

Add 35:
\[
6xy-10x-21y+35=84
\]
\[
(2x-7)(3y-5)=84.
\]
Valid integer-positive pairs are:
\[
(2x-7,3y-5)=(3,28),(21,4).
\]
So
\[
\boxed{(x,y)=(5,11),(14,3)}.
\]

---

## Concept 4 - Extreme Values by Completing Squares

### Example 7
Find the least value of
\[
2x^2-4xy+4y^2+8y+11.
\]

\[
2x^2-4xy+4y^2+8y+11=2(x-y)^2+2y^2+8y+11
\]
\[
=2(x-y)^2+2(y+2)^2+3\ge 3.
\]
Least value:
\[
\boxed{3}.
\]

### Example 8
Find the least value of
\[
(x+1)(x+2)(x+3)(x+4)+2019.
\]

Pair factors:
\[
(x^2+5x+4)(x^2+5x+6)+2019.
\]
Let \(t=x^2+5x\):
\[
(t+4)(t+6)+2019=t^2+10t+24+2019=(t+5)^2+2018\ge 2018.
\]
Least value:
\[
\boxed{2018}.
\]

---

## Homework Answers (PDF Scope)

### How to start each homework

1. Group powers first: \(3^{n+2}+3^n\), \(-2^{n+3}-2^{n+1}\).
2. Use sum-product factoring on the quadratic.
3. Convert “10% increase” into an equation, then clear denominators.
4. Pair alternating terms with \((2k-1)^2-(2k)^2\).
5. Replace \(x^2+x\) immediately, then derive \(x^3\) from \(x^2+x+1=0\).
6. Rewrite as \(x^{70}+(y-1)^2=1\) and split cases.
7. Apply SFFT by adding 20: \(xy-4x-5y+20\).
8. Substitute \(t=x^2\), solve in \(t\), then map back to integer \(x\).
9. Solve the algebra system first, then check triangle validity.

1. \(3^{n+2}-2^{n+3}+3^n-2^{n+1}=10(3^n-2^{n+1})\), so a factor is \(\boxed{10}\).
2. \(x^2-9x+8=(x-1)(x-8)\), so \(\boxed{x-1}\) is a factor.
3. Fraction condition yields only reduced pair \((x,y)=(5,11)\), so count \(\boxed{1}\).
4. \(\dfrac{1^2-2^2+\cdots+99^2-100^2}{1+2+\cdots+100}=\boxed{-1}\).
5. If \(x^2+x+1=0\), then \(x^3=1\), so
   \(x^3+2x^2+2x+2018=1+2(x^2+x)+2018=\boxed{2017}\).
6. \(x^{70}+y^2=2y\Rightarrow x^{70}+(y-1)^2=1\), total pairs \(\boxed{4}\).
7. \(xy-4x-5y=14\Rightarrow (x-5)(y-4)=34\), possible \(x\): \(6,7,22,39\), sum \(\boxed{74}\).
8. \(x^4-51x^2+50<0\Rightarrow 1<x^2<50\), integer \(x\) count \(\boxed{12}\).
9. From \(9a^2-b^2=-13\), \(3a+b=13\), we get \((a,b)=(2,7)\). Valid isosceles triangle gives third side \(\boxed{7}\).
