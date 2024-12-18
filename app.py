import streamlit as st

def main():
    st.title("Simple Calculator")
   
    st.write("This is a basic calculator app. Select the operation and input numbers.")
   
    # Input fields
    num1 = st.number_input("Enter the first number", value=0.0)
    num2 = st.number_input("Enter the second number", value=0.0)
   
    # Select operation
    operation = st.selectbox("Select an operation", ["Addition", "Subtraction", "Multiplication", "Division"])
   
    # Perform calculation
    if operation == "Addition":
        result = num1 + num2
        st.write(f"The result of addition is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"The result of subtraction is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"The result of multiplication is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result of division is: {result}")
        else:
            st.write("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    main()
