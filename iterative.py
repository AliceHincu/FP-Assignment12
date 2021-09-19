
class Iterative:
    def generate_parentheses(self, n):
        """
        --- Description
        Generate  all sequences of n parentheses that close correctly. (Method: recursive)

        --- Parameters
        :param n: the number of parentheses (type: <int>)
        """
        array = []
        for i in range(n):
            array.append("-")
        self.backtracking(array, n)

    @staticmethod
    def condition(array, n):
        closing = array.count(")")
        opening = array.count("(")
        return closing <= opening <= n / 2

    def backtracking(self, array, n):
        """
        We have in a stack the array that saves the parentheses(0 for opening, 1 for closing) and the index where we are
        We first have in the stack --------, 0
        """
        stack = [(array, 0)]
        while len(stack) > 0:  # while we have possibilities
            array, index = stack.pop()  # pop the possibility and the index where we stopped
            for i in ["(", ")"]:  # two possibilities for index value
                array[index] = i
                if self.condition(array, n):
                    # if it is valid either save it on the stack or have it as a solution
                    if index == n - 1:  # this is a solution
                        string = ""
                        print(string.join(array))
                    else:  # this is another possibility
                        stack.append((array[:], index + 1))

