"""
Demo lesson — shows every lessonkit feature in one short file.
Build it with:   python3 tools/build.py lessons/demo_lesson.py
Output:          "Lesson 00 - Demo.html"  (next to common/)
"""
from lessonkit import Lesson, card, formula, method, steps, reveal, sim, choices, gp_montecarlo, gp_numberline

OUTPUT = "Lesson 00 - Demo.html"

lesson = Lesson(
    title="Lesson 00 — Generator Demo",
    subtitle="A tiny lesson proving the build pipeline: cards, formulas, a Monte-Carlo "
             "area sim, a draggable number-line sim, a quiz, homework and a cheat sheet.",
    logo="📐 Demo",
    tag="lessonkit · sample",
)

lesson.nav(
    ("#idea", "Big Idea"),
    ("#ex", "Example"),
    ("#hw", "Homework"),
    ("#cheat", "Cheat Sheet"),
)

# ── Big Idea ──
lesson.section("idea", "The Big Idea")
lesson.card(
    '<p style="color:var(--text);font-size:1.05rem;">Geometric probability '
    'replaces <b style="color:#fff">counting</b> with <b style="color:#fff">measuring</b>.</p>',
    kind="glow amber",
)
lesson.formula(r"P(\text{event})=\frac{\text{measure of success region}}{\text{measure of whole region}}")

# A concept-check quiz (auto-graded by lesson.js)
lesson.card(
    '<p style="color:var(--text);font-weight:600;">Two random numbers ⇒ which measure?</p>'
    + choices(["length", "area", "volume"], correct_index=1)
)

# ── Example with a Monte-Carlo area sim ──
lesson.example(
    title="Example — P(x + y > 1)",
    source="unit square",
    problem=r"\(x,y\) are chosen uniformly from \([0,1]\). Find \(P(x+y>1)\).",
    canvas=("cex", 360, 360),
    controls='<button class="btn amber" id="cex-run">▶ Run 3000 points</button>',
    readout="cex-read",
    caption="Green = success region above the line \\(x+y=1\\). Empirical \\(P\\) → 1/2.",
    steps_list=[
        "Two random numbers ⇒ the sample space is the <b>unit square</b>, area 1.",
        r"The line \(x+y=1\) splits it into two equal triangles.",
        r"The upper triangle is the success set, area \(\tfrac12\). "
        r"\(P=\) <span class='answer'>1/2</span>.",
    ],
    method=("TYPE — two uniform numbers + a linear condition",
            "<b>METHOD:</b> draw the square, draw the boundary line, shade the correct "
            "side, divide its area by the square's area."),
)
# the simulation behaviour for the canvas above
lesson.js(gp_montecarlo(
    "cex", "return x+y>1;",
    readout="cex-read", button="cex-run", target="1/2 = 0.5",
    draw_region="ctx.beginPath();ctx.moveTo(M.X(0),M.Y(1));ctx.lineTo(M.X(1),M.Y(1));"
                "ctx.lineTo(M.X(1),M.Y(0));ctx.closePath();ctx.fill();",
    axis_x="x", axis_y="y",
))

# ── Homework ──
lesson.section("hw", "Homework")
lesson.homework(
    1, "length on a segment",
    r"A point is chosen at random on \([0,3]\). Find \(P(\text{point} < 1)\).",
    canvas=("hw1", 700, 120), readout="hw1-read",
    reveal_body=r"Success interval \([0,1]\) has length 1 out of 3. \(P=\) "
                r"<span class='answer'>1/3</span>.",
)
lesson.js(gp_numberline(
    "hw1", readout="hw1-read", min=0, max=3, start=1,
    success_body="return t<1;", regions=[(0, 1)], prob="1/3",
))

lesson.homework(
    2, "area · circle in square",
    r"A point lands uniformly in a \(2\times2\) square. Find \(P(\text{within 1 of the center})\).",
    canvas=("hw2", 340, 340), readout="hw2-read",
    controls='<button class="btn amber" id="hw2-run">▶ Run 3000 points</button>',
    reveal_body=r"Favorable = unit disk area \(\pi\); square area 4. \(P=\) "
                r"<span class='answer'>π/4 ≈ 0.785</span>.",
)
lesson.js(gp_montecarlo(
    "hw2", "var dx=x-0.5,dy=y-0.5;return dx*dx+dy*dy<0.25;",   # circle radius .5 in unit square
    readout="hw2-read", button="hw2-run", target="π/4 ≈ 0.785",
    draw_region="ctx.beginPath();ctx.arc(M.X(0.5),M.Y(0.5),M.sz*0.5,0,6.283);ctx.fill();",
))

# ── Cheat sheet ──
lesson.divider()
lesson.section("cheat", "Cheat Sheet")
lesson.cheat(
    ["Random quantities", "Sample space", "Measure"],
    [
        ["1 number", "an interval", "<b style='color:var(--accent2)'>length</b>"],
        ["2 numbers", "a square/region", "<b style='color:var(--accent2)'>area</b>"],
        ["3 numbers", "a cube/solid", "<b style='color:var(--accent2)'>volume</b>"],
    ],
)
