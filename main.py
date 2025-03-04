from parse import parse_latex_to_python

def main():
    print("Welcome to LaTeX to Python Converter! (Type 'exit' to quit)")
    while True:
        try:
            latex_input = input("Enter a LaTeX equation: ")
            if latex_input.lower() == 'exit':
                break
            result = parse_latex_to_python(latex_input)
            if result:
                print("Python Expression:", result)
            else:
                print("Invalid LaTeX input!")
        except EOFError:
            break

if __name__ == '__main__':
    main()
