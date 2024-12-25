# sum_variables.py

def sum_two_variables(a, b):
    """
    This function takes two variables as input and returns their sum.
    
    Parameters:
    a (int or float): The first variable.
    b (int or float): The second variable.
    
    Returns:
    int or float: The sum of a and b.
    """
    return a + b

def main():
    # Example usage
    var1 = 5
    var2 = 7
    result = sum_two_variables(var1, var2)
    print(f"The sum of {var1} and {var2} is: {result}")

if __name__ == "__main__":
    main()