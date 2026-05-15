# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, `+`, `-`, `*`, `/` operators, and spaces. Note that the division operator in this problem only performs integer division. It is guaranteed that the given expression is valid and there are no two consecutive operators or two consecutive numbers in the expression.

## Approach
We will use a stack to store the intermediate results. We iterate over the string, and when we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two elements from the stack, apply the operation, and push the result back to the stack.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int calculate(string s) {
    stack<int> st;
    char sign = '+';
    int num = 0;
    for (int i = 0; i < s.length(); i++) {
        // if the character is a digit, update the num
        if (isdigit(s[i])) {
            num = num * 10 + s[i] - '0';
        }
        // if the character is not a digit or a space, or it's the last character
        if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
            // apply the previous sign to the num
            if (sign == '+') {
                st.push(num);
            } else if (sign == '-') {
                st.push(-num);
            } else if (sign == '*') {
                st.top() *= num;
            } else if (sign == '/') {
                st.top() /= num;
            }
            // update the sign and reset the num
            sign = s[i];
            num = 0;
        }
    }
    // the result is the sum of all elements in the stack
    int result = 0;
    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    return result;
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
- Use a stack to store the intermediate results.
- Handle the division operator carefully to perform integer division.
- Be careful with the sign of the numbers and the order of operations.