# Basic Calculator II

## Problem Statement
Given a string s which represents an expression, evaluate this expression and return its value. The expression contains only integers and the operators '+' , '-' , '*' , and '/' . The integer division should truncate toward zero. You may assume that the given expression is always valid. The expression does not contain any spaces, and the only numbers in the expression are non-negative integers. For example, "3+2*2" = 7 and " 3/2 " = 1 and " 3+5 / 2 " = 5.

## Approach
We will use a stack to store the intermediate results and operators. We iterate through the expression, and when we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two elements from the stack, apply the operation, and push the result back to the stack. We handle the '*' and '/' operators separately by applying them immediately when encountered.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
#include <stack>
#include <string>

class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        char sign = '+';
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            // if the current character is a digit, update the num
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if the current character is not a digit or it's the last character
            if ((!(isdigit(s[i])) && !isspace(s[i])) || i == s.length() - 1) {
                if (sign == '+') {
                    st.push(num);
                } else if (sign == '-') {
                    st.push(-num);
                } else if (sign == '*') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev * num);
                } else if (sign == '/') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev / num);
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
- We use a stack to store the intermediate results and operators.
- We handle the '*' and '/' operators separately by applying them immediately when encountered.
- The time complexity is O(n) where n is the length of the input string, and the space complexity is also O(n) due to the use of the stack.