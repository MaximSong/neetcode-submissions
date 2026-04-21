class Solution:
    def is_number(self, num_str):
        try:
            float(num_str)
            return True
        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        score_stack = []
        for score in operations:
            if self.is_number(score):
                score_stack.append(int(score))
            elif score == "C":
                score_stack.pop()
            elif score == "D":
                double_prev = int(score_stack[-1]) * 2
                score_stack.append(double_prev)
            else:
                num1 = int(score_stack.pop())
                num2 = int(score_stack[-1])
                score_stack.append(num1)
                score_stack.append(num1 + num2)
        return sum(score_stack)