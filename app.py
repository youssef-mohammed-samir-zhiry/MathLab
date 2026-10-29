import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="MathLab",
    page_icon="🧮",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = 0


# =========================================================
# FUNCTIONS
# =========================================================

def add_score(points=10):
    st.session_state.score += points


def show_header(title, description):
    st.title(title)
    st.write(description)
    st.divider()


def plot_function(a, b):
    x = np.linspace(-10, 10, 400)
    y = a * x + b

    fig, ax = plt.subplots()

    ax.plot(x, y)

    ax.axhline(0)
    ax.axvline(0)

    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"f(x) = {a}x + {b}")

    ax.grid(True)

    st.pyplot(fig)


def solve_linear_equation(a, b):
    if a == 0:
        if b == 0:
            return "Infinite solutions"
        return "No solution"

    return -b / a


def matrix_operation(A, B, operation):

    if operation == "Addition":
        return A + B

    elif operation == "Subtraction":
        return A - B

    elif operation == "Multiplication":
        return A @ B

    return None


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🧮 MathLab")

st.sidebar.write("Interactive Mathematics Learning")

page = st.sidebar.radio(
    "Choose a section:",
    [
        "🏠 Home",
        "🔢 Real Numbers",
        "📈 Functions",
        "📐 Inequalities",
        "🏭 Linear Programming",
        "🔢 Matrix Lab",
        "📝 Quiz",
        "📊 My Progress"
    ]
)


# =========================================================
# HOME
# =========================================================

if page == "🏠 Home":

    st.title("🧮 MathLab")

    st.subheader("Learn → Experiment → Solve")

    st.write(
        """
        Welcome to MathLab!

        This application turns mathematics lessons into
        interactive experiments.

        Instead of only reading formulas, you can change values,
        visualize graphs, perform matrix operations,
        solve equations and test your knowledge.
        """
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Your Score",
            st.session_state.score
        )

    with col2:
        st.metric(
            "Questions Answered",
            st.session_state.answered
        )

    with col3:
        if st.session_state.score >= 50:
            level = "Advanced"
        elif st.session_state.score >= 20:
            level = "Intermediate"
        else:
            level = "Beginner"

        st.metric(
            "Level",
            level
        )

    st.divider()

    st.subheader("📚 Available Topics")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            """
            🔢 Real Numbers

            Explore natural, whole, integer,
            rational and irrational numbers.
            """
        )

        st.info(
            """
            📈 Functions

            Create and visualize linear functions.
            """
        )

        st.info(
            """
            📐 Inequalities

            Explore inequalities using graphs.
            """
        )

    with col2:

        st.info(
            """
            🏭 Linear Programming

            Find an optimal solution for a
            simple production problem.
            """
        )

        st.info(
            """
            🔢 Matrix Lab

            Add, subtract and multiply matrices.
            """
        )

        st.info(
            """
            📝 Quiz

            Test your understanding.
            """
        )


# =========================================================
# REAL NUMBERS
# =========================================================

elif page == "🔢 Real Numbers":

    show_header(
        "🔢 Real Numbers",
        "Classify numbers into their appropriate number sets."
    )

    st.write(
        """
        Number sets:

        N → Natural Numbers

        W → Whole Numbers

        Z → Integers

        Q → Rational Numbers

        I → Irrational Numbers

        R → Real Numbers
        """
    )

    st.divider()

    number = st.number_input(
        "Enter a number:",
        value=5.0
    )

    st.subheader("Result")

    if number.is_integer():

        n = int(number)

        if n > 0:
            st.success(
                f"{n} belongs to Natural, Whole, Integer, Rational and Real numbers."
            )

        elif n == 0:
            st.success(
                "0 belongs to Whole, Integer, Rational and Real numbers."
            )

        else:
            st.success(
                f"{n} belongs to Integer, Rational and Real numbers."
            )

    else:

        st.info(
            f"{number} is being treated as a decimal number."
        )

        if str(number).endswith("5"):
            st.write(
                "This example is a rational decimal."
            )

        st.write(
            "In a complete mathematical classifier, "
            "we can distinguish rational and irrational values."
        )


# =========================================================
# FUNCTIONS
# =========================================================

elif page == "📈 Functions":

    show_header(
        "📈 Function Playground",
        "Experiment with a linear function f(x) = ax + b."
    )

    st.write(
        """
        Change the values of a and b and observe
        how the graph changes.
        """
    )

    col1, col2 = st.columns(2)

    with col1:

        a = st.slider(
            "a",
            min_value=-10,
            max_value=10,
            value=1
        )

    with col2:

        b = st.slider(
            "b",
            min_value=-10,
            max_value=10,
            value=0
        )

    st.subheader(
        f"f(x) = {a}x + {b}"
    )

    plot_function(a, b)

    st.divider()

    st.subheader("🧮 Calculate f(x)")

    x_value = st.number_input(
        "Enter x:",
        value=0.0
    )

    y_value = a * x_value + b

    st.success(
        f"f({x_value}) = {y_value}"
    )


# =========================================================
# INEQUALITIES
# =========================================================

elif page == "📐 Inequalities":

    show_header(
        "📐 Inequality Visualizer",
        "Visualize a simple linear inequality."
    )

    st.write(
        """
        Example:

        ax + b ≥ 0
        """
    )

    a = st.slider(
        "Choose a",
        -10,
        10,
        2
    )

    b = st.slider(
        "Choose b",
        -10,
        10,
        -4
    )

    operator = st.selectbox(
        "Choose inequality:",
        [
            "≥",
            "≤",
            ">",
            "<"
        ]
    )

    x = np.linspace(-10, 10, 500)
    y = a * x + b

    fig, ax = plt.subplots()

    ax.plot(x, y)

    ax.axhline(0)
    ax.axvline(0)

    ax.set_xlabel("x")
    ax.set_ylabel("y")

    ax.grid(True)

    ax.set_title(
        f"{a}x + {b} {operator} 0"
    )

    st.pyplot(fig)

    st.info(
        """
        The graph above represents the expression.
        The next version of MathLab can shade the
        exact solution region automatically.
        """
    )


# =========================================================
# LINEAR PROGRAMMING
# =========================================================

elif page == "🏭 Linear Programming":

    show_header(
        "🏭 Linear Programming Simulator",
        "Find the production combination that gives the highest profit."
    )

    st.write(
        """
        A factory produces two products:

        Product A

        Product B

        We want to maximize the total profit.
        """
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        profit_a = st.number_input(
            "Profit of Product A",
            min_value=0,
            value=50
        )

        machine_a = st.number_input(
            "Machine hours for A",
            min_value=1,
            value=2
        )

    with col2:

        profit_b = st.number_input(
            "Profit of Product B",
            min_value=0,
            value=40
        )

        machine_b = st.number_input(
            "Machine hours for B",
            min_value=1,
            value=1
        )

    available_hours = st.number_input(
        "Available machine hours",
        min_value=1,
        value=100
    )

    st.divider()

    best_profit = 0
    best_a = 0
    best_b = 0

    for A in range(available_hours + 1):

        for B in range(available_hours + 1):

            used_hours = (
                machine_a * A +
                machine_b * B
            )

            if used_hours <= available_hours:

                profit = (
                    profit_a * A +
                    profit_b * B
                )

                if profit > best_profit:

                    best_profit = profit
                    best_a = A
                    best_b = B

    st.subheader("🎯 Optimal Solution")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Product A",
            best_a
        )

    with col2:
        st.metric(
            "Product B",
            best_b
        )

    with col3:
        st.metric(
            "Maximum Profit",
            best_profit
        )

    st.success(
        f"""
        Produce {best_a} units of Product A
        and {best_b} units of Product B.

        Maximum profit = {best_profit}
        """
    )


# =========================================================
# MATRIX LAB
# =========================================================

elif page == "🔢 Matrix Lab":

    show_header(
        "🔢 Matrix Laboratory",
        "Perform operations on two 2×2 matrices."
    )

    st.subheader("Matrix A")

    col1, col2 = st.columns(2)

    with col1:

        a11 = st.number_input(
            "A11",
            value=1,
            key="a11"
        )

        a21 = st.number_input(
            "A21",
            value=3,
            key="a21"
        )

    with col2:

        a12 = st.number_input(
            "A12",
            value=2,
            key="a12"
        )

        a22 = st.number_input(
            "A22",
            value=4,
            key="a22"
        )

    A = np.array([
        [a11, a12],
        [a21, a22]
    ])

    st.write("A =")

    st.dataframe(A)

    st.divider()

    st.subheader("Matrix B")

    col1, col2 = st.columns(2)

    with col1:

        b11 = st.number_input(
            "B11",
            value=5,
            key="b11"
        )

        b21 = st.number_input(
            "B21",
            value=7,
            key="b21"
        )

    with col2:

        b12 = st.number_input(
            "B12",
            value=6,
            key="b12"
        )

        b22 = st.number_input(
            "B22",
            value=8,
            key="b22"
        )

    B = np.array([
        [b11, b12],
        [b21, b22]
    ])

    st.write("B =")

    st.dataframe(B)

    st.divider()

    operation = st.selectbox(
        "Choose an operation:",
        [
            "Addition",
            "Subtraction",
            "Multiplication"
        ]
    )

    if st.button("Calculate"):

        result = matrix_operation(
            A,
            B,
            operation
        )

        st.subheader("Result")

        st.dataframe(result)

        if operation == "Multiplication":

            st.write("Step example:")

            st.write(
                f"""
                First element:

                ({a11} × {b11}) + ({a12} × {b21})

                = {a11*b11} + {a12*b21}

                = {a11*b11 + a12*b21}
                """
            )


# =========================================================
# QUIZ
# =========================================================

elif page == "📝 Quiz":

    show_header(
        "📝 Math Challenge",
        "Answer the questions and increase your score."
    )

    st.subheader("Question 1")

    answer1 = st.radio(
        "What is the solution of 2x + 5 = 15?",
        [
            "x = 10",
            "x = 5",
            "x = 2",
            "x = 7"
        ],
        key="q1"
    )

    st.subheader("Question 2")

    answer2 = st.radio(
        "What is the determinant of [[1, 2], [3, 4]]?",
        [
            "2",
            "-2",
            "10",
            "4"
        ],
        key="q2"
    )

    st.subheader("Question 3")

    answer3 = st.radio(
        "Which one is an irrational number?",
        [
            "4",
            "0.5",
            "√2",
            "-3"
        ],
        key="q3"
    )

    st.divider()

    if st.button("Submit Quiz"):

        score = 0

        if answer1 == "x = 5":
            score += 10

        if answer2 == "-2":
            score += 10

        if answer3 == "√2":
            score += 10

        st.session_state.score += score
        st.session_state.answered += 3

        st.success(
            f"You earned {score} points!"
        )

        st.write(
            f"Your total score is {st.session_state.score}"
        )


# =========================================================
# PROGRESS
# =========================================================

elif page == "📊 My Progress":

    show_header(
        "📊 My Progress",
        "Track your learning progress."
    )

    score = st.session_state.score

    st.metric(
        "Total Score",
        score
    )

    st.metric(
        "Questions Answered",
        st.session_state.answered
    )

    progress = min(score / 100, 1.0)

    st.progress(
        progress
    )

    if score < 20:

        st.info(
            "🌱 Beginner — keep practicing!"
        )

    elif score < 50:

        st.info(
            "📚 Intermediate — you're making progress!"
        )

    else:

        st.success(
            "🚀 Great progress!"
        )

    st.divider()

    st.subheader("Learning Path")

    topics = {
        "Real Numbers": score >= 10,
        "Functions": score >= 20,
        "Inequalities": score >= 30,
        "Linear Programming": score >= 40,
        "Matrices": score >= 50
    }

    for topic, completed in topics.items():

        if completed:

            st.success(
                f"✓ {topic}"
            )

        else:

            st.write(
                f"○ {topic}"
            )
