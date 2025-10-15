#pip install streamlit altair pandas numpy -> streamlit run dice.py
import time
import random
import re
from collections import Counter, deque
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np
import pandas as pd
import streamlit as st
import altair as alt

DICE_RE = re.compile(r"^\s*(?P<count>\d*)d(?P<sides>\d+)\s*(?P<mod>[+-]\s*\d+)?\s*$", re.IGNORECASE)
DIE_UNICODE = {1:"⚀",2:"⚁",3:"⚂",4:"⚃",5:"⚄",6:"⚅"}

@dataclass
class DiceExpr:
    count: int
    sides: int
    modifier: int

def parse_expr(expr: str) -> DiceExpr:
    m = DICE_RE.match(expr)
    if not m:
        raise ValueError("Invalid expression. Try: d6, 2d6+3, 4d8-1")
    count = int(m.group("count") or "1")
    sides = int(m.group("sides"))
    mod   = int((m.group("mod") or "0").replace(" ", ""))
    if count <= 0 or sides <= 1:
        raise ValueError("Count must be ≥ 1 and sides ≥ 2.")
    return DiceExpr(count, sides, mod)

def roll_once(dx: DiceExpr) -> Tuple[List[int], int]:
    rolls = [random.randint(1, dx.sides) for _ in range(dx.count)]
    total = sum(rolls) + dx.modifier
    return rolls, total

def simulate_totals(dx: DiceExpr, n: int) -> List[int]:
    return [roll_once(dx)[1] for _ in range(n)]

st.set_page_config(page_title="Dice Rolling Simulator", page_icon="🎲", layout="centered")

CUSTOM_CSS = """
<style>
/* Card look for dice boxes */
.dice-card {
    display: inline-flex; align-items:center; justify-content:center;
    width: 96px; height: 96px; margin: 6px; border-radius: 18px;
    background: radial-gradient(100% 100% at 50% 0%, #ffffff 0%, #f1f3f6 100%);
    border: 1px solid rgba(0,0,0,0.08); box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    font-size: 40px; font-weight: 700; user-select: none;
}
.dice-sub { font-size: 14px; color: #6b7280; margin-top: -6px; }
.total-chip {
    display:inline-block; padding:8px 14px; border-radius: 999px; margin: 10px 6px 0 0;
    background: linear-gradient(135deg,#6366f1, #22d3ee); color:white; font-weight:700;
}
.mod-chip {
    display:inline-block; padding:6px 10px; border-radius: 8px; margin-left:8px;
    background:#f3f4f6; color:#111827; border:1px solid #e5e7eb; font-weight:600;
}
.help { color:#6b7280; }
</style>
"""
st.markdown("""
<style>
@keyframes wobble {
  0%,100% { transform: translate(0,0) rotate(0deg); }
  25% { transform: translate(-2px,1px) rotate(-6deg); }
  50% { transform: translate(2px,-1px) rotate(6deg); }
  75% { transform: translate(-1px,0px) rotate(-4deg); }
}
.wobble .dice-card { animation: wobble 0.12s linear infinite; }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Controls")
expr_input = st.sidebar.text_input("Dice expression", value="2d6+3", help="Examples: d6, 3d8, 4d10-2")
frames = st.sidebar.slider("Animation frames", 5, 40, 18, help="How long the dice shake")
frame_delay = st.sidebar.slider("Frame delay (seconds)", 0.01, 0.15, 0.06, step=0.01)
auto_sim_n = st.sidebar.number_input("Quick stats: simulate N totals", min_value=100, max_value=200000, value=5000, step=1000)
clear_hist = st.sidebar.button("Clear roll history")

st.sidebar.markdown("---")
st.sidebar.caption("Tip: Use `stats` box below for a separate simulation.")

if "history" not in st.session_state:
    st.session_state.history = deque(maxlen=200)
if clear_hist:
    st.session_state.history.clear()

st.title("Dice Rolling Simulator — Streamlit Edition")
st.caption("Roll expressions like **d6**, **2d6+3**, **4d8-1**. Watch the dice *shake*, then see totals, history, and distributions.")

error_box = st.empty()
try:
    dx = parse_expr(expr_input.strip())
    error_box.empty()
except Exception as e:
    error_box.error(str(e))
    st.stop()


colA, colB = st.columns([1, 1])
with colA:
    st.subheader("Roll the dice")
    roll_btn = st.button("Roll Now", use_container_width=True)
with colB:
    st.subheader("Quick Stats")
    run_stats_btn = st.button("Run Simulation", use_container_width=True)

dice_area = st.container()
result_area = st.container()
hist_area = st.container()

def render_dice_faces(values: List[int], sides: int):
    """Render dice as pretty cards; for d6 use unicode pips."""
    rows = []
    for v in values:
        face = DIE_UNICODE.get(v, str(v)) if sides == 6 else str(v)
        rows.append(f'<div class="dice-card">{face}</div>')
    st.markdown("".join(rows), unsafe_allow_html=True)
    st.markdown(f'<div class="dice-sub">d{sides} × {len(values)}</div>', unsafe_allow_html=True)

def animate_shake(count: int, sides: int, frames: int, delay: float):
    """Shake animation by flashing random faces with guaranteed on-screen updates."""
    placeholder = dice_area.empty()
    for _ in range(frames):
        rnd = [random.randint(1, sides) for _ in range(count)]
        with placeholder.container():
            render_dice_faces(rnd, sides)
        time.sleep(delay)

if roll_btn:
    placeholder = dice_area.empty()
    for _ in range(frames):
        rnd = [random.randint(1, dx.sides) for _ in range(dx.count)]
        with placeholder.container():
            st.markdown('<div class="wobble">', unsafe_allow_html=True)
            render_dice_faces(rnd, dx.sides)
            st.markdown('</div>', unsafe_allow_html=True)
        time.sleep(frame_delay)

    rolls, total = roll_once(dx)
    with placeholder.container():
        render_dice_faces(rolls, dx.sides)

    with result_area:
        parts = " + ".join(map(str, rolls))
        mod_txt = f"{'+' if dx.modifier>=0 else '-'} {abs(dx.modifier)}" if dx.modifier else ""
        st.markdown(
            f'<span class="total-chip">Total: {total}</span>'
            f'{f"<span class=mod-chip>Modifier: {dx.modifier:+d}</span>" if dx.modifier else ""}',
            unsafe_allow_html=True
        )
        st.write(f"Breakdown: **{parts}** {mod_txt}")

    if dx.count == 1 and ((dx.sides == 20 and rolls[0] == 20) or rolls[0] == dx.sides):
        st.balloons()
    elif total >= dx.count * dx.sides + dx.modifier - max(2, dx.count):
        st.snow()

    st.session_state.history.append(
        {"expr": expr_input.strip(), "rolls": rolls, "modifier": dx.modifier, "total": total, "time": time.time()}
    )

if len(st.session_state.history):
    st.subheader("Recent Rolls")
    df_hist = pd.DataFrame([
        {"Expression": h["expr"], "Rolls": ", ".join(map(str, h["rolls"])), "Modifier": h["modifier"], "Total": h["total"]}
        for h in list(st.session_state.history)[::-1]
    ])
    st.dataframe(df_hist, use_container_width=True, hide_index=True)


def plot_distribution(totals: List[int], title: str):
    df = pd.DataFrame({"Total": totals})
    freq = df.value_counts("Total").rename("Count").reset_index()
    chart = (
        alt.Chart(freq)
        .mark_bar()
        .encode(x=alt.X("Total:Q", bin=False), y="Count:Q")
        .properties(height=240, title=title)
    )
    st.altair_chart(chart, use_container_width=True)
    st.caption(f"Mean: **{np.mean(totals):.3f}**, Min: **{np.min(totals)}**, Max: **{np.max(totals)}**")

if run_stats_btn:
    with hist_area:
        with st.spinner(f"Simulating {auto_sim_n:,} totals for {expr_input.strip()}..."):
            totals = simulate_totals(dx, int(auto_sim_n))
        plot_distribution(totals, title=f"Distribution of {auto_sim_n:,} totals for {expr_input.strip()}")


with st.expander("Advanced: Run a custom stats simulation"):
    cols = st.columns(3)
    with cols[0]:
        stats_expr = st.text_input("Expression", value=expr_input.strip(), key="stats_expr")
    with cols[1]:
        stats_n = st.number_input("Simulations (N)", min_value=100, max_value=500000, value=20000, step=1000, key="stats_n")
    with cols[2]:
        go_stats = st.button("Simulate", key="go_stats")
    if go_stats:
        try:
            dx2 = parse_expr(stats_expr)
        except Exception as e:
            st.error(str(e))
        else:
            with st.spinner(f"Simulating {stats_n:,} totals for {stats_expr}..."):
                totals2 = simulate_totals(dx2, int(stats_n))
            plot_distribution(totals2, title=f"Distribution of {stats_n:,} totals for {stats_expr}")

st.markdown("---")
st.markdown(
    '<span class="help">Formats: <code>d6</code>, <code>2d6+3</code>, <code>4d8-1</code>. '
    'Animation shows randomized “shake” frames before the final roll.</span>',
    unsafe_allow_html=True
)