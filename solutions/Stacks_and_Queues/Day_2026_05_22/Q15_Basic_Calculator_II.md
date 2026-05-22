# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the result. The expression contains non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero. The expression does not contain any parentheses, and the operators are evaluated from left to right. For example, `3/2` equals `1`, and `6/(-3)` equals `-2`. If the expression is empty, return `0`.

## Approach
We will use a stack to store the intermediate results and operators. We will iterate through the string, and for each digit, we will form a number. If we encounter an operator, we will push the current number and the operator to the stack. We will then pop the top two numbers and the operator from the stack, perform the operation, and push the result back to the stack.

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
        stack<int> st;
        int curr_num = 0;
        char curr_op = '+';
        
        for (int i = 0; i < s.length(); i++) {
            // if the current character is a digit, form the number
            if (isdigit(s[i])) {
                curr_num = curr_num * 10 + (s[i] - '0');
            }
            
            // if the current character is an operator or it's the last character
            if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
                // perform the operation based on the current operator
                if (curr_op == '+') {
                    st.push(curr_num);
                } else if (curr_op == '-') {
                    st.push(-curr_num);
                } else if (curr_op == '*') {
                    int top = st.top();
                    st.pop();
                    st.push(top * curr_num);
                } else if (curr_op == '/') {
                    int top = st.top();
                    st.pop();
                    st.push(top / curr_num);
                }
                
                // update the current operator and reset the current number
                curr_op = s[i];
                curr_num = 0;
            }
        }
        
        // calculate the final result by summing up all the numbers in the stack
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
```

## Key Takeaways
- Use a stack to store intermediate results and operators.
- Iterate through the string and perform operations based on the current operator.
- Handle the cases where the expression is empty or contains only one number.