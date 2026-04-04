# Basic Calculator II

## Problem Statement
Given a string s which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers and operators (+, -, \*, /) and empty space. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the eval built-in function. Examples: "3+2\*2" = 7, " 3/2 " = 1, " 3+5 / 2 " = 5.

## Approach
We will use a stack to store the intermediate results. We iterate over the string, when we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two elements from the stack, apply the operation, and push the result back to the stack. We handle the operators with higher precedence first.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <stack>
#include <string>
using namespace std;

class Solution {
public:
    int calculate(string s) {
        stack<int> st;
        int curr = 0;
        char op = '+';
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                curr = curr * 10 + (s[i] - '0');
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
                if (op == '+') {
                    st.push(curr);
                } else if (op == '-') {
                    st.push(-curr);
                } else if (op == '*') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev * curr);
                } else if (op == '/') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev / curr);
                }
                op = s[i];
                curr = 0;
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
- Use a stack to store intermediate results when evaluating an expression with multiple operators.
- Handle operators with higher precedence first to ensure correct order of operations.
- Be careful with integer division to ensure truncation toward zero.