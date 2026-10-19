import streamlit as st
import random
import math
import time

st.set_page_config(page_title="WALL-E & EVE", page_icon="🤖")

st.title("🤖 WALL-E & EVE Search Agent")
st.write("Watch WALL-E search a 10 × 10 grid for EVE!")

if "eve" not in st.session_state:
    st.session_state.eve = (
        random.randint(0, 9),
        random.randint(0, 9)
    )

if "wall_e" not in st.session_state:
    st.session_state.wall_e = (0, 0)

if "step" not in st.session_state:
    st.session_state.step = 0

if "finished" not in st.session_state:
    st.session_state.finished = False


def draw_grid(reveal=False):
    eve_x, eve_y = st.session_state.eve
    wall_x, wall_y = st.session_state.wall_e

    grid = []

    for y in range(10):
        row = []

        for x in range(10):
            if (x, y) == (wall_x, wall_y):
                cell = "🤖"
            elif (x, y) == (eve_x, eve_y) and (
                reveal or st.session_state.finished
            ):
                cell = "👽"
            else:
                cell = "⬜"

            row.append(cell)

        grid.append(row)

    st.table(grid)


def move_wall_e():
    wall_x, wall_y = st.session_state.wall_e
    eve_x, eve_y = st.session_state.eve

    # Move one step toward EVE
    if wall_x < eve_x:
        wall_x += 1
    elif wall_x > eve_x:
        wall_x -= 1
    elif wall_y < eve_y:
        wall_y += 1
    elif wall_y > eve_y:
        wall_y -= 1

    st.session_state.wall_e = (wall_x, wall_y)
    st.session_state.step += 1

    if (wall_x, wall_y) == (eve_x, eve_y):
        st.session_state.finished = True


col1, col2 = st.columns(2)

with col1:
    if st.button("▶️ Move WALL-E"):
        if not st.session_state.finished:
            move_wall_e()

with col2:
    if st.button("🔄 Restart Search"):
        st.session_state.eve = (
            random.randint(0, 9),
            random.randint(0, 9)
        )
        st.session_state.wall_e = (0, 0)
        st.session_state.step = 0
        st.session_state.finished = False

st.subheader("Search Grid")
draw_grid()

st.write(f"**Steps taken:** {st.session_state.step}")
st.write(f"**WALL-E's position:** {st.session_state.wall_e}")

if st.session_state.finished:
    st.success("🎉 WALL-E found EVE!")
    st.write(f"**EVE's position:** {st.session_state.eve}")
else:
    st.info("EVE is hidden. Click 'Move WALL-E' to continue searching.")
