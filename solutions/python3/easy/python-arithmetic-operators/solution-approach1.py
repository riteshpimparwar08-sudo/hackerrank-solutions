# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true
# Problem     Arithmetic Operators
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-10-31, 01:36 p.m.
# Technique   basic-arithmetic-operations
# Time        O(1)
# Space       O(1)
# Insight     The implementation performs standard arithmetic operations on two integer inputs and prints the results sequentially as required by the problem statement.
# Interview   Before: "How would you perform basic arithmetic on two inputs?" After: "I read two integers from standard input and apply addition, subtraction, and multiplication operators, resulting in O(1) time and space complexity for any integer size."
# Pitfalls    (1) Failing to convert input strings to integers using int() before performing arithmetic operations.  (2) Printing the results in an incorrect order, violating the requirement to output sum, difference, and product sequentially.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
