import streamlit as st

st.write("""
    # The Largest
    This app selects the largest among the 3 given numbers :D
""")

st.header("Input any 3 numbers!")

def inputs():
    n1 = st.number_input("Number 1")
    n2 = st.number_input("Number 2")
    n3 = st.number_input("Number 3")
    return n1, n2, n3

def find_largest(n1, n2, n3):
    return max(n1, n2, n3)

n1, n2, n3 = inputs()
largest = find_largest(n1, n2, n3)

st.write(f"# The largest number is: {largest}")