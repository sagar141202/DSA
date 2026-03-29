# Basic Calculator II

## Problem Statement
Implement a basic calculator to evaluate a simple expression string. The expression string contains only non-negative integers, '+', '-', '*', '/' operators and empty spaces. The integer division should truncate toward zero. For example, " 3/2 " = 1, " 4/3 " = 1. Note: Do not use the built-in eval function. Also, assume that the input has been simplified so that there are no two consecutive operators and there are no leading or trailing spaces.

## Approach
We can use a stack to store the intermediate results. We iterate through the string, and when we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two elements from the stack, apply the operation, and push the result back to the stack. We handle the '*' and '/' operators immediately when encountered.

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
        int num = 0;
        char sign = '+';
        for (int i = 0; i < s.size(); i++) {
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.size() - 1) {
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
        int sum = 0;
        while (!st.empty()) {
            sum += st.top();
            st.pop();
        }
        return sum;
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
- Use a stack to store intermediate results.
- Handle '*' and '/' operators immediately when encountered.
- Use a variable to keep track of the current operator.