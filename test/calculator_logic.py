# calculator_logic.py

def safe_eval(expression):
    try:
        # Use eval() safely by defining allowed names.
        allowed_names = {'__builtins__': None}
        return eval(expression, allowed_names)
    except ZeroDivisionError:
        raise ValueError("Division by zero is not allowed.")
    except Exception:
        raise ValueError("Invalid expression")
