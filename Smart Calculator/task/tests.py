from hstest.stage_test import *
from hstest.test_case import TestCase


class CalcTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=["17 9", self.test_1, self.test_2, self.test_3, self.test_4, self.test_5,
                                self.test_6, self.test_7, self.test_8, self.test_9])]

    # sum of single digits #####################################################
    # two positive
    def test_1(self, output):
        output = str(output).lower().strip()
        if "26" != output:
            return CheckResult.wrong("Your program cannot sum two positive single digits.")
        return "-2 5"

    # positive and negative
    def test_2(self, output):
        output = str(output).lower().strip()
        if "3" != output:
            return CheckResult.wrong("Your program cannot sum positive and negative numbers.")
        return ""

    # input empty string
    def test_3(self, output):
        output = str(output)
        if len(output) != 0:
            return CheckResult.wrong("Incorrect response to an empty string. " +
                                     "The program should not print anything.")
        return "7"

    # input one number
    def test_4(self, output):
        output = str(output).lower().strip()
        if "7" != output:
            return CheckResult.wrong("The program printed not the same number that was entered.")
        return "100 200"

    # sum of three-digit numbers ###############################################
    # two positive numbers
    def test_5(self, output):
        output = str(output).lower().strip()
        if "300" != output:
            return CheckResult.wrong("Your program cannot sum two positive three-digit numbers.")
        return "500"

    # input one number
    def test_6(self, output):
        output = str(output).lower().strip()
        if "500" != output:
            return CheckResult.wrong("The program printed not the same number that was entered.")
        return "300 -400"

    # positive and negative
    def test_7(self, output):
        output = str(output).lower().strip()
        if "-100" != output:
            return CheckResult.wrong("Your program cannot sum positive and negative numbers.")
        return "-500"

    # input one negative number
    def test_8(self, output):
        output = str(output).lower().strip()
        if "-500" != output:
            return CheckResult.wrong("The program printed not the same number that was entered.")
        return "1 -1"

    # the sum of the numbers is zero
    def test_9(self, output):
        output = str(output).lower().strip()
        if "0" != output:
            return CheckResult.wrong("The problem when sum is equal to 0 has occurred")
        return "/exit"

    def check(self, reply: str, attach) -> CheckResult:
        reply = str(reply).lower().strip()
        if "bye" not in reply:
            return CheckResult.wrong("Your program didn't print \"bye\" after entering \"/exit\".")
        return CheckResult.correct()


if __name__ == '__main__':
    CalcTest("calculator.calculator").run_tests()
