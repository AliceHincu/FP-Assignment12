class Recursive:
    def generate_parentheses(self, n):
        """
        --- Description
        Generate  all sequences of n parentheses that close correctly. (Method: recursive)

        --- Parameters
        :param n: the number of parentheses (type: <int>)

        --- Return
        :return: the solutions
        """
        string = ""
        self.backtracking(n, 0, 0, string)

    def backtracking(self, n, closing, opening, string):
        """
        --- Description
        Steps:
            - if the value of opening brackets and closing brackets is equal to n/2 then return the string
            - if the count of opening bracket is greater than count of closing bracket then we add a closing bracket
            - if the count of opening bracket is less than n then we add an opening bracket
        :param n: the number of parentheses (type: <int>)
        :param closing: the number of closed parentheses (type: <int>)
        :param opening: the number of open parentheses (type: <int>)
        :param string: the created string with the parentheses (type: <str>)
        :return: the solutions
        """
        if closing == n/2 and opening == n/2:
            print(string)

        if opening > closing:
            self.backtracking(n, closing+1, opening, string + ")")

        if opening <= n/2:
            self.backtracking(n, closing, opening+1, string + "(")

