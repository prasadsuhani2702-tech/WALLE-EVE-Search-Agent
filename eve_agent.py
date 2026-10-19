import streamlit as st
import random
import time

st.set_page_config(page_title="WALLE-EVE Search Agent", page_icon="🤖")

st.title("🤖 WALLE-EVE Search Agent")
st.write("A visual grid-based search simulation")

SIZE = 10

# Generate a hidden EVE position
if "eve" not in st.session_state:
    st.session_state.eve = (
        random.randint(0, SIZE - 1),
        random.randint(0, SIZE - 1)
    )

if "walle" not in st.session_state:
    st.session_state.walle = (0, 0)

if "visited" not in st.session_state:
    st.session_state.visited = set()

if "found" not in st.session_state:
    st.session_state.found = False

# Display information
st.subheader("Search Grid")
st.write("🤖 = WALL-E | ❓ = Unsearched cell | 🟩 = Visited cell")
st.write("EVE is hidden somewhere in the grid!")

# Search button
if st.button("🔍 Search for EVE"):
    eve_x, eve_y = st.session_state.eve
    found = False

    for x in range(SIZE):
        for y in range(SIZE):
            st.session_state.walle = (x, y)
            st.session_state.visited.add((x, y))

            if (x, y) == (eve_x, eve_y):
                st.session_state.found = True
                found = True
                break

        if found:
            break

    st.rerun()

# Reset button
if st.button("🔄 Reset Simulation"):
    st.session_state.eve = (
        random.randint(0, SIZE - 1),
        random.randint(0, SIZE - 1)
    )
    st.session_state.walle = (0, 0)
    st.session_state.visited = set()
    st.session_state.found = False
    st.rerun()

# Draw the visual grid
for x in range(SIZE):
    cols = st.columns(SIZE)

    for y in range(SIZE):
        position = (x, y)

        if position == st.session_state.eve:
            if st.session_state.found:
                symbol = "💚"
            else:
                symbol = "❓"

        elif position == st.session_state.walle:
            symbol = "🤖"

        elif position in st.session_state.visited:
            symbol = "🟩"

        else:
            symbol = "⬜"

        cols[y].markdown(
            f"<div style='text-align:center;"
            f"font-size:22px;border:1px solid #aaa;"
            f"padding:8px;'>{symbol}</div>",
            unsafe_allow_html=True
        )

# Result
if st.session_state.found:
    st.success("🎉 WALL-E found EVE!")
    st.write(f"EVE's position: {st.session_state.eve}")
else:
    st.info("Click 'Search for EVE' to start the search.")
