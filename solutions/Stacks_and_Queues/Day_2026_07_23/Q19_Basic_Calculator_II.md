# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression is composed of non-negative integers and operators `+`, `-`, `*`, and `/`. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval` built-in function. For example, if `s = "3+2*2"`, the output should be `7` because `2*2 = 4` and `3 + 4 = 7`. If `s = " 3/2 "`, the output should be `1`. If `s = " 3+5 / 2 "`, the output should be `5`.

## Approach
We can use a stack-based approach to solve this problem. We iterate over the string, and whenever we encounter a number, we push it to the stack. Whenever we encounter an operator, we pop the top two elements from the stack, perform the operation, and push the result back to the stack. We handle the `*` and `/` operators separately because they have higher precedence than `+` and `-`.

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
        int currNum = 0;
        char operation = '+';
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                currNum = currNum * 10 + s[i] - '0';
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
                if (operation == '+') {
                    st.push(currNum);
                } else if (operation == '-') {
                    st.push(-currNum);
                } else if (operation == '*') {
                    int num = st.top();
                    st.pop();
                    st.push(num * currNum);
                } else if (operation == '/') {
                    int num = st.top();
                    st.pop();
                    st.push(num / currNum);
                }
                operation = s[i];
                currNum = 0;
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
- We use a stack to store the intermediate results.
- We handle the `*` and `/` operators separately because they have higher precedence than `+` and `-`.
- We use a variable `operation` to keep track of the current operator.