# 🔒 Password Strength Meter

A modern, user-friendly password strength checker and generator built with Python and Streamlit. This application helps users create and evaluate secure passwords with real-time feedback and detailed analysis.

## 🌟 Features

- **Password Strength Checker**
  - Real-time strength evaluation
  - Custom scoring weights
  - Detailed feedback and suggestions
  - Visual strength indicators
  - Common password detection

- **Password Generator**
  - Customizable length (8-32 characters)
  - Ensures all security criteria are met
  - Includes special characters, numbers, and mixed case
  - Copy-friendly interface
  - Strength verification of generated passwords

- **User Interface**
  - Modern, clean design
  - Color-coded feedback
  - Progress indicators
  - Helpful tips and guidelines
  - Responsive layout

## 📋 Requirements

- Python 3.7+
- Streamlit
- Regular Expressions (re)
- Random
- String

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-strength-meter.git
cd password-strength-meter
```

2. Install required packages:
```bash
pip install streamlit
```

3. Run the application:
```bash
streamlit run main.py
```

## 💪 Password Strength Criteria

The application evaluates passwords based on multiple criteria:

| Criterion | Weight | Description |
|-----------|--------|-------------|
| Length | 2 points | Minimum 8 characters |
| Character Mix | 2 points | Both uppercase and lowercase |
| Numbers | 1 point | At least one digit |
| Special Characters | 1 point | At least one special character |
| Extra Length | 1 point | Bonus for 12+ characters |

Total possible score: 7 points

### Strength Levels:
- 🔴 Weak (0-3 points)
- 🟡 Moderate (4-6 points)
- 🟢 Strong (7 points)

## 🛡️ Security Features

- Common password detection
- Case-insensitive comparison
- Comprehensive password database
- Real-time strength analysis
- Secure password generation

## 📱 Interface Components

1. **Check Password Tab**
   - Password input field
   - Strength indicator
   - Detailed feedback
   - Improvement suggestions
   - Password requirements

2. **Generate Password Tab**
   - Length selector
   - Generation button
   - Strength verification
   - Copy functionality
   - Password features list

3. **Sidebar**
   - About section
   - Requirements checklist
   - Usage tips
   - Security guidelines

## 🔍 Code Structure
