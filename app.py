import sys
import utils
"""this works for oparations between two values only"""
def is_valid_expression(exp: str) -> bool:
    """Validate a simple arithmetic expression in the form 'a op b'."""
    
    parts = exp.strip().split()

    # Expression must have exactly 3 parts: number, operator, number
    if len(parts) != 3:
        print("Expression must have exactly 3 parts: e.g., '2 + 3'")
        return False

    a_str, operator, b_str = parts

    # Validate operands
    try:
        float(a_str)
        float(b_str)
    except ValueError:
        print("Both operands must be valid numbers (int or float).")
        return False

    # Validate operator
    valid_ops = {"+", "-", "*", "/", "x", "X"}
    if operator not in valid_ops:
        print(f" Invalid operator '{operator}'. Must be one of {', '.join(valid_ops)}.")
        return False

    # If all checks pass
    return True

print("""
        \033[33m==========================================================================
        Welcome to the calculator:
      
            \033[38;5;208m-> \033[33mh\033[38;5;208m to view history (last 5 opartions)
            -> \033[33mc\033[38;5;208m to clear history
            -> \033[33mr\033[38;5;208m to set round off digit i.e 2 means answers will look like 7.33
            -> enter expresstion like i.e \033[33m(1 + 1)\033[38;5;208m to get an answer
            have a space in-between 
            -> \033[33mq\033[38;5;208m to quit program
        \033[33m==========================================================================
      
      \033[0m""")



if __name__ == "__main__":
    rounding_digit = 0
    calc = utils.Calculator(rounding_digit)
    history = utils.History("History.txt")
    
    while True:
        user_input = input("\033[36m> \033[0m")
        parts = user_input.split(" ")
        if (user_input.strip().lower() == "h"):
            print("--------History---------\n")
            h = history.restore()
            for exp in h[:-6:-1]:
                print("-\t",exp,end="")
            print()
        #clears History of the calculator in a text file 
        elif (user_input.strip().lower() == "c"):
            history.clear()
        #sets new round off digit
        elif (user_input.strip().lower() == "q"):
            sys.exit(0)
        elif (user_input.strip().lower() == "r"):
        
            try:
                rounding_digit = int(input("Enter rounding Digits: "))
                calc.set_round_digits(rounding_digit)
            except:
                print("ValueError : Expecting Integer")
            
        #calculates expression
        elif (is_valid_expression(user_input)):
            
            match parts[1].lower():
                case "+":
                    ans = calc.addtion(float(parts[0]),float(parts[2]))
                case "-":
                    ans = calc.subtraction(float(parts[0]),float(parts[2]))
                case "*" | "x" :
                    ans = calc.multiplication(float(parts[0]),float(parts[2]))
                case "/":
                    ans = calc.division(float(parts[0]),float(parts[2]))

                
            history.save(f"{user_input.strip()} = {ans}")
            print("=",ans,end="\n\n")
