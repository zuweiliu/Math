# Lesson generator (lessonkit)

A small tool to generate interactive HTML math lessons in the same dark "space"
style as the Physics lessons. The look-and-feel and all the interactive
simulation code live in **shared files**, so each new lesson is just a short
Python spec — no copy-pasted boilerplate.

## Layout

Each lesson lives in its **own folder** under `lessons/`, holding the spec, any
source material (PDF, notes), and the generated HTML.

```
Math2/
├── common/
│   ├── lesson.css      ← shared theme (colors, cards, buttons, sims…)
│   └── lesson.js       ← shared runtime: starfield, MathJax, quiz grading,
│                         and the GP.* simulation library
├── tools/
│   ├── lessonkit.py    ← Python builder API (Lesson + helpers)
│   ├── build.py        ← the generator CLI
│   └── README.md       ← this file
└── lessons/
    ├── demo/
    │   ├── demo_lesson.py        ← example spec (build it to see everything)
    │   └── Lesson 00 - Demo.html ← generated output
    └── lesson-18/
        ├── Lesson 18 - Geometric Probabilities.html      ← hand-authored
        ├── Lesson 18 - Geometric Probabilities - Worked Lesson.md
        └── AMC10 Geometric Probabilities.pdf             ← source material
```

Generated HTML is written **into the spec's own folder**; the links to
`common/lesson.css` / `common/lesson.js` are resolved with a relative prefix
(e.g. `../../common/`) computed automatically.

## Build

```bash
python3 tools/build.py lessons/demo/demo_lesson.py   # build one lesson
python3 tools/build.py --all                          # build every lessons/**/*.py
python3 tools/build.py lessons/demo/demo_lesson.py --out "My.html"
```

The HTML is written into the spec's folder; the relative `common/` links resolve
automatically. Open the `.html` directly in a browser — no server needed
(MathJax loads from a CDN, so keep internet on).

## Write a new lesson

Make a folder `lessons/lesson-19/` and add a spec `lesson19.py` inside it. Build
a `Lesson`, then expose it as a module-level variable named `lesson` (and
optionally set `OUTPUT`):

```python
from lessonkit import Lesson, choices, gp_montecarlo, gp_numberline

OUTPUT = "Lesson 19 - My Topic.html"

lesson = Lesson("Lesson 19 — My Topic", "One-line subtitle.", logo="📐 Topic")
lesson.nav(("#idea", "Big Idea"), ("#hw", "Homework"))

lesson.section("idea", "The Big Idea")
lesson.card("<p style='color:var(--text)'>...</p>", kind="glow amber")
lesson.formula(r"P=\frac{\text{good}}{\text{all}}")

lesson.example(
    title="Example 1",
    source="AMC 10",                       # optional pill
    problem=r"\(x,y\in[0,1]\). Find \(P(x+y>1)\).",
    canvas=("c1", 360, 360),               # (id, width, height)
    controls='<button class="btn amber" id="c1-run">▶ Run</button>',
    readout="c1-read",
    caption="Green = success region.",
    steps_list=["Step one…", "Step two…"], # numbered reveal
    method=("TYPE — …", "<b>METHOD:</b> …"),
)
lesson.js(gp_montecarlo("c1", "return x+y>1;",
                        readout="c1-read", button="c1-run", target="1/2"))

lesson.section("hw", "Homework")
lesson.homework(1, "length",
    r"Point on \([0,3]\); find \(P(<1)\).",
    canvas=("hw1", 700, 120), readout="hw1-read",
    reveal_body=r"\(P=\) <span class='answer'>1/3</span>.")
lesson.js(gp_numberline("hw1", readout="hw1-read", min=0, max=3,
                        success_body="return t<1;", regions=[(0,1)], prob="1/3"))
```

Then `python3 tools/build.py lessons/lesson-19/lesson19.py`.

## Builder reference (`lessonkit`)

`Lesson` methods (all chainable):

| Method | Purpose |
|---|---|
| `nav(*(href,label))` | top-bar anchor links |
| `section(id, title)` | a `§` heading with an anchor |
| `card(body, kind="")` | a panel; `kind` ∈ `glow amber green purple prob` |
| `formula(tex)` | centered display equation |
| `example(...)` | problem card + canvas + step reveal + method box |
| `homework(num, tag, problem, …)` | a homework item with optional sim + reveal |
| `cheat(headers, rows)` | a styled summary table |
| `divider()` | a horizontal rule |
| `add(html)` | append any raw HTML |
| `js(code)` | append JS that runs after load (inside `GP.ready`) |

Free helpers you can compose yourself: `card`, `formula`, `method`, `steps`,
`reveal`, `sim`, `choices`, `cheat`.

## Interactive simulations (`GP.*` in lesson.js)

Add a `<canvas>` (via `canvas=(...)` or `sim(...)`) then wire behavior with one
of these from `lesson.js(...)`:

**`gp_montecarlo(canvas, test_body, …)`** — area probability. `test_body` is the
JS body of `function(x,y){…}` returning `true` on success, with `x,y ∈ [0,1]`.
Options: `readout`, `button` (run button id; omit to auto-run), `target` (goal
string), `trials`, `draw_region` (JS body of `function(ctx,M){…}` to shade the
favorable region; `M.X(v)`, `M.Y(v)`, `M.sz` map unit coords to pixels),
`axis_x`, `axis_y`.

**`gp_numberline(canvas, …)`** — 1-D length probability with a draggable point.
Options: `readout`, `min`, `max`, `start`, `success_body` (`function(t){…}`),
`regions` (list of `(lo,hi)` green intervals), `prob` (exact answer string).

For anything bespoke (custom geometry, multi-point dragging, animations) just
write plain canvas JS in `lesson.js("""…""")` and use the shared helpers
`hidpi(canvas)`, `mj()`, `rev(id)`, and the color var `C2`.

## Notes

- LaTeX uses `\(…\)` inline and `\[…\]` display (MathJax 3). In Python specs use
  raw strings `r"\(…\)"` so backslashes survive.
- The auto-graded quiz markup is produced by `choices([...], correct_index)`.
- Editing `common/lesson.css` or `common/lesson.js` updates **all** lessons at
  once (rebuild not required for CSS/JS-only tweaks — just refresh the browser).
