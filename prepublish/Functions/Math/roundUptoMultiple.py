def roundUpToMultiple(number:float, multiple:int) -> int:
    """
    RETURNS VALUE ROUNDED TO A NEAREST MULTIPLE 
    
    (REDUCES SIG FIGS BY FACTOR OF PROVIDED MULTIPLE
    WHEN MULTIPLE IS A FACTOR OF 10)
    ------------------------------------------------
    Example: 
        12501 --multiple of 100--> 12600
    """

    rounded = number + (multiple - 1)
    return int(rounded - (rounded % multiple))



def rtmult() -> int:
    """ROUNDS NUMBER TO A SPECIFIED MULTIPLE"""
    
    number = float(input("Value: "))
    multiple = int(input("Multiple: "))

    rounded = roundUpToMultiple(number,multiple)
    return rounded

if __name__ == "__main__":
    print(main())