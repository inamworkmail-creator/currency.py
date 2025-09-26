import streamlit as st

st.title("Custom 3-Input Calculator (x, y, z)")

# Step 1: Inputs
x = st.number_input("Enter first number (x):", value=0.0)
y = st.number_input("Enter second number (y):", value=0.0)
z = st.number_input("Enter third number (z):", value=0.0)

st.write(" Example Operations:")
st.markdown("- `x + y + z` (Addition)")
st.markdown("- `(x * y) - z` (Custom Mix)")
st.markdown("- `(x + y) / z` (Division)")
st.markdown("- `x ** y` (Power)")

# Step 2: User Operation
operation = st.text_input(
    "Enter your custom operation using x, y, z:",
    value="x + y + z"
)

# Step 3: Calculate
if st.button("Calculate"):
    try:
        # Safe evaluation
        allowed_names = {"x": x, "y": y, "z": z}
        result = eval(operation, {"__builtins__": {}}, allowed_names)
        st.success(f" Result: {result}")
    except ZeroDivisionError:
        st.error("⚠Error: Division by zero is not allowed!")
    except Exception as e:
        st.error(f"⚠Invalid Expression: {e}")
