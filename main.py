import re
import random
import string
import streamlit as st
from common import COMMON_PASSWORDS

# Set page config must be the first Streamlit command
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒", layout="wide")

# Custom CSS for better styling
st.markdown("""
    <style>
    .stProgress .st-bo {
        background-color: #4CAF50;
    }
    .stButton>button {
        width: 100%;
        margin-top: 10px;
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .password-strength {
        font-size: 1.2em;
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 5px;
        margin: 10px 0;
    }
    .strong {
        background-color: #dff0d8;
        color: #3c763d;
    }
    .moderate {
        background-color: #fcf8e3;
        color: #8a6d3b;
    }
    .weak {
        background-color: #f2dede;
        color: #a94442;
    }
    </style>
""", unsafe_allow_html=True)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check for common passwords first (case-insensitive)
    if password.lower() in [p.lower() for p in COMMON_PASSWORDS]:
        return 0, ["❌ This is a common password. Please choose a more unique password."]
    
    # Length Check (weight: 2 points)
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check (weight: 2 points)
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 2
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check (weight: 1 point)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check (weight: 1 point)
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Additional Complexity (weight: 1 point)
    if len(password) >= 12:
        score += 1
    elif len(password) >= 10:
        score += 0.5
    
    # Strength Rating
    if score == 7:
        feedback.append("✅ Strong Password!")
    elif score >= 4:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")
    
    return score, feedback

def generate_strong_password(length=12):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*"
    
    # Ensure at least one of each required character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest randomly to make it the desired length
    all_chars = lowercase + uppercase + digits + special_chars
    remaining_length = length - len(password)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password
    random.shuffle(password)
    
    return ''.join(password)

def get_strength_class(score):
    if score == 7:
        return "strong"
    elif score >= 4:
        return "moderate"
    return "weak"

def main():
    # Sidebar with information
    with st.sidebar:
        st.title("About")
        st.write("""
        This Password Strength Meter helps you:
        - Check your password strength
        - Generate secure passwords
        - Get detailed feedback
        - Avoid common passwords
        """)
        st.markdown("---")
        st.write("Password Requirements:")
        st.write("✅ At least 8 characters")
        st.write("✅ Mix of uppercase & lowercase")
        st.write("✅ Include numbers")
        st.write("✅ Special characters")
    
    # Main content
    st.title("🔒 Password Strength Meter")
    st.write("Check your password strength or generate a secure password.")
    
    # Create tabs for different functions
    tab1, tab2 = st.tabs(["Check Password", "Generate Password"])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.header("Check Password Strength")
            password = st.text_input("Enter your password:", type="password")
            if st.button("Check Strength"):
                if password:
                    score, feedback = check_password_strength(password)
                    strength_class = get_strength_class(score)
                    st.markdown(f'<div class="password-strength {strength_class}">Password Strength: {score}/7</div>', unsafe_allow_html=True)
                    st.progress(score/7)
                    
                    for message in feedback:
                        if "❌" in message:
                            st.error(message)
                        elif "⚠️" in message:
                            st.warning(message)
                        else:
                            st.success(message)
                else:
                    st.error("Please enter a password")
        
        with col2:
            st.header("Password Tips")
            st.write("""
            - Use a mix of characters
            - Avoid personal information
            - Don't reuse passwords
            - Use longer passwords
            - Avoid common patterns
            """)
    
    with tab2:
        col1, col2 = st.columns([2, 1])
        with col1:
            st.header("Generate Strong Password")
            length = st.slider("Password Length", min_value=8, max_value=32, value=12)
            if st.button("Generate Password"):
                generated_password = generate_strong_password(length)
                st.text_area("Generated Password", generated_password, height=100)
                st.success("✅ Password generated successfully!")
                st.write("This password meets all security criteria:")
                score, feedback = check_password_strength(generated_password)
                strength_class = get_strength_class(score)
                st.markdown(f'<div class="password-strength {strength_class}">Password Strength: {score}/7</div>', unsafe_allow_html=True)
                st.progress(score/7)
                for message in feedback:
                    st.success(message)
        
        with col2:
            st.header("Password Features")
            st.write("""
            Generated passwords include:
            - Uppercase letters
            - Lowercase letters
            - Numbers
            - Special characters
            - Random length
            - No common patterns
            """)

if __name__ == "__main__":
    main()