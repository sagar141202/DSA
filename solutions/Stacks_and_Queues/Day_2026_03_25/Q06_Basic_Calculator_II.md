# Basic Calculator II

## Problem Statement
Given a string s which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers and operators (+, -, *, /) with no parentheses. The operators have the following precedence: multiplication and division have higher precedence than addition and subtraction. For example, "3+2*2" = 7 and " 3/2 " = 1. Assume that the input expression is always valid and does not contain any spaces.

## Approach
We can use a stack to store the intermediate results. We iterate over the string and whenever we encounter a number, we push it to the stack. When we encounter an operator, we pop the last two numbers from the stack, apply the operation, and push the result back to the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
#include <stack>
#include <string>

int calculate(string s) {
    stack<int> st;
    char operation = '+';
    int currentNumber = 0;
    for (int i = 0; i < s.length(); i++) {
        if (isdigit(s[i])) {
            currentNumber = currentNumber * 10 + s[i] - '0';
        }
        if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
            if (operation == '+') {
                st.push(currentNumber);
            } else if (operation == '-') {
                st.push(-currentNumber);
            } else if (operation == '*') {
                int num = st.top();
                st.pop();
                st.push(num * currentNumber);
            } else if (operation == '/') {
                int num = st.top();
                st.pop();
                st.push(num / currentNumber);
            }
            operation = s[i];
            currentNumber = 0;
        }
    }
    int result = 0;
    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    return result;
}

int main() {
    string s = "3+2*2";
    cout << calculate(s) << endl;
    return 0;
}
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
- Using a stack to store intermediate results helps in evaluating the expression with the correct order of operations.
- We need to handle the case when the input string contains spaces and when it does not.
- The time complexity is O(n) where n is the length of the input string, and the space complexity is also O(n) due to the use of the stack.