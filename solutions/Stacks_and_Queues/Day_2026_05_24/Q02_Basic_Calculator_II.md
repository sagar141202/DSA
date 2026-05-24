# Basic Calculator II

## Problem Statement
Given a string `s` which represents a mathematical expression, evaluate the expression and return the result. The string `s` contains only numbers, `+`, `-`, `*`, `/`, and spaces. The expression is evaluated from left to right, and the `*` and `/` operations have higher precedence than the `+` and `-` operations. For example, `3+2*2` should be evaluated as `3+(2*2)`. Assume that the input expression is valid and does not contain any parentheses or invalid characters.

## Approach
We use a stack-based approach to solve this problem, where we iterate over the string and process the operators based on their precedence. We use two stacks, one for numbers and one for operators, to keep track of the intermediate results. When we encounter a `*` or `/` operator, we pop the top number from the stack, perform the operation, and push the result back onto the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> numbers;
        char op = '+';
        int currNum = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                currNum = currNum * 10 + s[i] - '0';
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
                if (op == '+') {
                    numbers.push(currNum);
                } else if (op == '-') {
                    numbers.push(-currNum);
                } else if (op == '*') {
                    int top = numbers.top();
                    numbers.pop();
                    numbers.push(top * currNum);
                } else if (op == '/') {
                    int top = numbers.top();
                    numbers.pop();
                    numbers.push(top / currNum);
                }
                op = s[i];
                currNum = 0;
            }
        }
        
        int result = 0;
        while (!numbers.empty()) {
            result += numbers.top();
            numbers.pop();
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: "3+2*2"
Output: 7
Input: " 3/2 "
Output: 1
Input: " 3+5 / 2 "
Output: 5
```

## Key Takeaways
- Use a stack-based approach to handle the precedence of operators.
- Iterate over the string and process the operators based on their precedence.
- Use two stacks, one for numbers and one for operators, to keep track of the intermediate results.