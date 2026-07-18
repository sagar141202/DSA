# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers and operators `+`, `-`, `*`, `/`. Operators have the same precedence and are evaluated from left to right. Assume that the given expression is always valid and does not contain any white spaces.

## Approach
We can use a stack to store the intermediate results. We iterate over the string, and when we encounter a number, we push it to the stack. When we encounter an operator, we pop the last two numbers from the stack, apply the operation, and push the result back to the stack.

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
        // if the character is not a digit or it's the last character
        if (!isdigit(s[i]) && s[i] != ' ' || i == s.length() - 1) {
            if (sign == '+') {
                st.push(num);
            } else if (sign == '-') {
                st.push(-num);
            } else if (sign == '*') {
                st.push(st.top() * num);
                st.pop();
            } else if (sign == '/') {
                st.push(int(st.top() / num));
                st.pop();
            }
            sign = s[i];
            num = 0;
        }
    }
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
- Use a stack to store the intermediate results
- Handle the operators `+`, `-`, `*`, `/` separately
- Be careful with the edge cases, such as the last character in the string or the empty stack.