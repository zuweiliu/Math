"""
lessonkit — a tiny builder library for Olivia's interactive math lessons.

A *lesson* is authored as a small Python file that creates a `Lesson`, appends
content blocks with the helper methods below, then is rendered to a single HTML
page by `tools/build.py`. All the look-and-feel and the interactive simulation
runtime live in the shared files `common/lesson.css` and `common/lesson.js`, so
every lesson stays consistent and the boilerplate is written exactly once.

Author API (all methods return the Lesson, so calls can be chained):

    L = Lesson("Lesson 19 — Title", "One-line subtitle", logo="📐 Topic")
    L.nav(("#idea","Big Idea"), ("#hw","Homework"))
    L.section("idea", "The Big Idea")
    L.card("<p>...</p>", kind="glow amber")
    L.formula(r"P=\\frac{\\text{good}}{\\text{all}}")
    L.example(title="Example 1", source="AMC 10",
              problem="<p>...</p>",
              canvas=("c1", 360, 360),
              steps=["First...", "Then..."],
              method=("TYPE — ...", "METHOD: ..."))
    L.homework(1, "length", "<p>...</p>", canvas=("hw1", 700, 130), reveal="<p>P=1/2</p>")
    L.cheat([...headers...], [[...row...], ...])
    L.js(gp_montecarlo("c1", "return x+y>1;", target="...", readout="c1r"))
    html = L.render(assets_prefix="")     # "" if output sits next to common/

See tools/README.md for the full guide.
"""

from __future__ import annotations
import html as _html
from textwrap import dedent


# ────────────────────────── free-standing HTML builders ──────────────────────────
def card(body: str, kind: str = "") -> str:
    cls = "card" + (" " + kind if kind else "")
    return f'<div class="{cls}">{body}</div>\n'


def formula(tex: str) -> str:
    return f'<div class="formula">\\[ {tex} \\]</div>\n'


def method(title: str, body: str) -> str:
    return (
        '<div class="method">\n'
        f'  <div class="h">🔑 {title}</div>\n'
        f'  {body}\n'
        '</div>\n'
    )


def steps(items: list[str]) -> str:
    rows = "".join(
        f'    <div class="stepline"><div class="n"></div><div class="b">{s}</div></div>\n'
        for s in items
    )
    return f'<div class="steps">\n{rows}</div>\n'


def reveal(rid: str, body: str, label: str = "Show step‑by‑step ▸") -> str:
    return (
        f'<button class="btn ghost" onclick="rev(\'{rid}\')">{label}</button>\n'
        f'<div class="reveal" id="{rid}">{body}</div>\n'
    )


def sim(canvas: str, w: int, h: int, controls: str = "", readout: str = "",
        caption: str = "") -> str:
    """A centered canvas with optional controls row, readout line and caption."""
    out = ['<div class="simwrap">']
    out.append(f'  <canvas id="{canvas}" class="sim" width="{w}" height="{h}"></canvas>')
    if controls:
        out.append(f'  <div class="controls">{controls}</div>')
    if readout:
        out.append(f'  <div class="readout" id="{readout}"></div>')
    if caption:
        out.append(f'  <div class="cap">{caption}</div>')
    out.append('</div>\n')
    return "\n".join(out)


def choices(items: list[str], correct_index: int) -> str:
    btns = "".join(
        f'<button class="choice"{" data-correct" if i == correct_index else ""}>{t}</button>'
        for i, t in enumerate(items)
    )
    return f'<div class="choices" data-quiz>{btns}</div>\n'


def cheat(headers: list[str], rows: list[list[str]]) -> str:
    head = "".join(f"<th>{h}</th>" for h in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows
    )
    return f'<table class="cheat"><tr>{head}</tr>{body}</table>\n'


# ────────────────────────── JS snippet builders ──────────────────────────
def _opts_js(opts: dict) -> str:
    """Serialize a dict to a JS object literal. Values are emitted verbatim
    (so pass raw JS for functions and quoted strings for text)."""
    return "{" + ",".join(f"{k}:{v}" for k, v in opts.items()) + "}"


def gp_montecarlo(canvas: str, test_body: str, *, readout: str = "", button: str = "",
                  target: str = "", trials: int | None = None,
                  draw_region: str = "", axis_x: str = "", axis_y: str = "") -> str:
    """Return a JS call to GP.monteCarlo.
       test_body : JS body of `function(x,y){ ... }` returning bool."""
    o: dict = {"canvas": _q(canvas), "test": f"function(x,y){{{test_body}}}"}
    if readout:     o["readout"] = _q(readout)
    if button:      o["button"] = _q(button)
    if target:      o["target"] = _q(target)
    if trials:      o["trials"] = str(trials)
    if draw_region: o["drawRegion"] = f"function(ctx,M){{{draw_region}}}"
    if axis_x:      o["axisX"] = _q(axis_x)
    if axis_y:      o["axisY"] = _q(axis_y)
    return f"GP.monteCarlo({_opts_js(o)});"


def gp_numberline(canvas: str, *, readout: str = "", min: float = 0, max: float = 1,
                  start: float | None = None, success_body: str = "",
                  regions: list[tuple[float, float]] | None = None,
                  prob: str = "") -> str:
    """Return a JS call to GP.numberLine.
       success_body : JS body of `function(t){ ... }` returning bool."""
    o: dict = {"canvas": _q(canvas), "min": str(min), "max": str(max)}
    if readout:        o["readout"] = _q(readout)
    if start is not None: o["start"] = str(start)
    if success_body:   o["success"] = f"function(t){{{success_body}}}"
    if regions:        o["regions"] = "[" + ",".join(f"[{a},{b}]" for a, b in regions) + "]"
    if prob:           o["prob"] = _q(prob)
    return f"GP.numberLine({_opts_js(o)});"


def _q(s: str) -> str:
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'") + "'"


# ────────────────────────── the Lesson document ──────────────────────────
class Lesson:
    def __init__(self, title: str, subtitle: str = "", *, logo: str = "📐 Lesson",
                 tag: str = ""):
        self.title = title
        self.subtitle = subtitle
        self.logo = logo
        self.tag = tag
        self._nav: list[tuple[str, str]] = []
        self._blocks: list[str] = []
        self._js: list[str] = []

    # -- structure --
    def nav(self, *links: tuple[str, str]) -> "Lesson":
        self._nav.extend(links)
        return self

    def add(self, html_block: str) -> "Lesson":
        self._blocks.append(html_block)
        return self

    def js(self, code: str) -> "Lesson":
        self._js.append(code)
        return self

    def section(self, sid: str, title: str) -> "Lesson":
        return self.add(f'<h2 class="sec" id="{sid}">{title}</h2>\n')

    def divider(self) -> "Lesson":
        return self.add('<hr class="div">\n')

    # -- convenience wrappers around the free builders --
    def card(self, body: str, kind: str = "") -> "Lesson":
        return self.add(card(body, kind))

    def formula(self, tex: str) -> "Lesson":
        return self.add(formula(tex))

    def cheat(self, headers: list[str], rows: list[list[str]]) -> "Lesson":
        return self.add(cheat(headers, rows))

    def example(self, *, title: str, problem: str, source: str = "",
                canvas: tuple | None = None, controls: str = "", readout: str = "",
                caption: str = "", steps_list: list[str] | None = None,
                method: tuple | None = None, reveal_id: str = "") -> "Lesson":
        pill = f' <span class="pill">{source}</span>' if source else ""
        self.add(f'<h3 class="ex">{title}{pill}</h3>\n')
        body = [card(f'<p style="color:var(--text);margin:0;">{problem}</p>', "amber")]
        inner = []
        if canvas:
            cid, w, h = canvas
            inner.append(sim(cid, w, h, controls, readout, caption))
        if steps_list:
            rid = reveal_id or (canvas[0] + "-sol" if canvas else "sol")
            inner.append(reveal(rid, steps(steps_list)))
        if method:
            inner.append(globals()["method"](method[0], method[1]))
        body.append(card("".join(inner)))
        return self.add("".join(body))

    def homework(self, num: int, tag: str, problem: str, *, canvas: tuple | None = None,
                 controls: str = "", readout: str = "", reveal_body: str = "") -> "Lesson":
        out = ['<div class="hw">']
        out.append(f'  <span class="hwnum">HW {num}</span><span class="pill">{tag}</span>')
        out.append(f'  <p style="color:var(--text);">{problem}</p>')
        if canvas:
            cid, w, h = canvas
            out.append(sim(cid, w, h, controls, readout))
        if reveal_body:
            out.append(reveal(f"h{num}", f'<div class="card prob">{reveal_body}</div>', "Reveal ▸"))
        out.append('</div>\n')
        return self.add("\n".join(out))

    # -- output --
    def render(self, assets_prefix: str = "") -> str:
        nav = "\n".join(f'    <a href="{h}">{t}</a>' for h, t in self._nav)
        tag = f'<div class="tag">{self.tag}</div>\n  ' if self.tag else ""
        body = "\n".join(self._blocks)
        js = "\n\n".join(self._js)
        css = f"{assets_prefix}common/lesson.css"
        runtime = f"{assets_prefix}common/lesson.js"
        return dedent(f"""\
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{_html.escape(self.title)}</title>
        <link rel="stylesheet" href="{css}">
        <script src="{runtime}"></script>
        <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js" async></script>
        </head>
        <body>
        <canvas id="stars"></canvas>

        <div id="topbar">
          <div class="logo">{self.logo}</div>
          <nav>
        {nav}
          </nav>
        </div>

        <div class="wrap">

        <div class="hero">
          {tag}<h1>{self.title}</h1>
          <p>{self.subtitle}</p>
        </div>

        {body}

        <div class="foot">Generated with lessonkit · Olivia's Math Lessons</div>
        </div>

        <script>
        GP.ready(function(){{
        {js}
        mj();
        }});
        </script>
        </body>
        </html>
        """)
