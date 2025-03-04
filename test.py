from parse import parse_latex_to_python

test_cases = [
    # Basic Arithmetic
    (r"3 + 5", "(3 + 5)"),
    (r"10 - 2", "(10 - 2)"),
    (r"4 \times 7", "(4 * 7)"),
    (r"8 \div 2", "(8 / 2)"),
    (r"2^3", "(2 ** 3)"),

    # Fractions
    (r"\frac{3}{4}", "(3 / 4)"),
    (r"\frac{10}{2}", "(10 / 2)"),
    (r"\frac{7}{\frac{3}{2}}", "(7 / (3 / 2))"),
    (r"\frac{\frac{1}{2}}{3}", "((1 / 2) / 3)"),
    (r"\frac{a}{b}", "(a / b)"),

    # Square Roots
    (r"\sqrt{4}", "(4 ** 0.5)"),
    (r"\sqrt{16}", "(16 ** 0.5)"),
    (r"\sqrt{\frac{9}{4}}", "((9 / 4) ** 0.5)"),
    (r"\sqrt{x}", "(x ** 0.5)"),

    # Trigonometric Functions
    (r"\sin{0}", "math.sin(0)"),
    (r"\cos{0}", "math.cos(0)"),
    (r"\tan{1}", "math.tan(1)"),
    (r"\sin{\frac{\pi}{2}}", "math.sin((math.pi / 2))"),
    (r"\cos{\frac{\pi}{3}}", "math.cos((math.pi / 3))"),

    # Logarithms and Exponentials
    (r"\log{10}", "math.log(10)"),
    (r"\log{\frac{1}{2}}", "math.log((1 / 2))"),
    (r"\exp{2}", "math.exp(2)"),
    (r"\exp{\frac{3}{2}}", "math.exp((3 / 2))"),

    # Nested Expressions
    (r"\frac{\sin{1}}{\cos{1}}", "(math.sin(1) / math.cos(1))"),
    (r"\frac{\sqrt{9}}{3}", "((9 ** 0.5) / 3)"),
    (r"\sqrt{\frac{1}{\frac{2}{3}}}", "((1 / (2 / 3)) ** 0.5)"),
    (r"\frac{\frac{\frac{2}{3}}{4}}{5}", "(((2 / 3) / 4) / 5)"),

    # Parentheses Handling
    (r"(3 + 4) \times 2", "((3 + 4) * 2)"),
    (r"\sin{(x + y)}", "math.sin((x + y))"),
    (r"\frac{(1 + 2)}{(3 + 4)}", "((1 + 2) / (3 + 4))"),
    (r"\sqrt{(x + y)^2}", "(((x + y) ** 2) ** 0.5)"),

    # Symbolic Expressions
    (r"a + b", "(a + b)"),
    (r"x - y", "(x - y)"),
    (r"2a + 3b", "((2 * a) + (3 * b))"),
    (r"\frac{x}{y}", "(x / y)"),
    (r"\sin{x} + \cos{y}", "(math.sin(x) + math.cos(y))"),

    # Complex Combinations
    (r"\frac{\sin{x} + \cos{x}}{\log{x}}", "((math.sin(x) + math.cos(x)) / math.log(x))"),
    (r"\sqrt{\sin{\frac{x}{y}}}", "(math.sin((x / y)) ** 0.5)"),
    (r"\frac{\sqrt{x + y}}{\log{z}}", "(((x + y) ** 0.5) / math.log(z))"),

    # Handling of \left and \right
    (r"\sin{\left(\frac{1}{2}\right)}", "math.sin((1 / 2))"),
    (r"\cos{\left(x^3\right)}", "math.cos((x ** 3))"),
    (r"\tan{\left(\sqrt{x}\right)}", "math.tan((x ** 0.5))"),

    # Parentheses and Nested Functions
    (r"\sin{(x + \cos{x})}", "math.sin((x + math.cos(x)))"),
    (r"\log{\left(\exp{x}\right)}", "math.log((math.exp(x)))"),
    (r"\sqrt{\left(\frac{1 + x}{2}\right)}", "((1 + x) / 2) ** 0.5"),
    (r"\exp{\left(\sin{x} + \cos{x}\right)}", "math.exp((math.sin(x) + math.cos(x)))"),

    # Edge Cases
    (r"\frac{0}{1}", "(0 / 1)"),
    (r"\frac{1}{0}", "(1 / 0)"),
    (r"\sqrt{0}", "(0 ** 0.5)"),
    (r"\sin{\pi}", "math.sin(math.pi)"),
    (r"\cos{0} + \sin{0}", "(math.cos(0) + math.sin(0))")
]

def run_tests():
    passed = []
    failed = []
    
    print("Running Test Cases...\n")
    for latex, expected in test_cases:
        try:
            result = parse_latex_to_python(latex)
            if result == expected:
                passed.append((latex, result))
            else:
                failed.append((latex, result, expected))
        except Exception as e:
            failed.append((latex, str(e), expected))
    
    print("\nPassed Tests:")
    for latex, result in passed:
        print(f"✔ {latex} => {result}")
    
    print("\nFailed Tests:")
    for latex, result, expected in failed:
        print(f"✘ {latex} => {result} (Expected: {expected})")
    
    print(f"\nSummary: {len(passed)} Passed, {len(failed)} Failed")
    
if __name__ == "__main__":
    run_tests()
