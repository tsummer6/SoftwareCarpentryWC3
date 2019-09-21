def mundaneMath():
    '''
    When this function is called it will add together all the even numbers
    between 1 and 100, and print that number to the terminal.

    **Parameters**

        None

    **Returns**

        None
    '''
    # This is an empty array to store the even numbers
    a = []
    # A loop to increment from 1 to 100
    for i in range(1, 101):
        # This finds the even numbers from 1 to 100
        # and stores them in the array
        if (i % 2 == 0):
            a.append(i)
    # Adds the even numbers together and stores them in the variable x
    x = sum(a)
    # Prints the output
    print(x)


if __name__ == "__main__":
    mundaneMath()
