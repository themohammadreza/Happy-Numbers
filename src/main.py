class HappyNumber:
    """A class to determine if a number is a happy number.
    
    A happy number is defined by the following process:
    1. Starting with any positive integer, replace the number by the sum of the squares of its digits.
    2. Repeat the process until:
       - The number equals 1 (making it a happy number), or
       - It enters a cycle (making it an unhappy number)
    """

    def __init__(self):
        """Initialize the HappyNumber class."""
        self._tried_numbers = []

    def is_happy(self, number: int) -> bool:
        """Check if a given number is a happy number.

        Args:
            number (int): The number to check.

        Returns:
            bool: True if the number is happy, False otherwise.

        Examples:
            >>> hn = HappyNumber()
            >>> hn.is_happy(7)
            True
            >>> hn.is_happy(44)
            True
            >>> hn.is_happy(45)
            False
        """
        # Reset tried numbers for new calculation
        self._tried_numbers = []
        return self._calculate(number)

    def _calculate(self, number: int) -> bool:
        """Recursive helper method to calculate if a number is happy.

        Args:
            number (int): The current number in the calculation sequence.

        Returns:
            bool: True if the number leads to 1, False if it enters a cycle.
        """
        if number == 1:
            return True
        if number in self._tried_numbers:
            return False

        self._tried_numbers.append(number)
        next_number = sum(int(digit) ** 2 for digit in str(number))

        return self._calculate(next_number)


if __name__ == "__main__":
    happy_checker = HappyNumber()
    
    # Test cases
    assert happy_checker.is_happy(7) == True
    assert happy_checker.is_happy(44) == True
    assert happy_checker.is_happy(45) == False
    
    print("All test cases passed!")