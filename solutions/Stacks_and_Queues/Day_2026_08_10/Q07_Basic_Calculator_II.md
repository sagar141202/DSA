# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval` built-in function. For example, `3+2*2` equals to `7`, and ` 3/2 ` equals to `1`.

## Approach
We will use a stack to store the intermediate results. We iterate through the string, and when we encounter an operator, we calculate the result based on the operator and the top two elements of the stack. We use the `+` and `-` operators to update the stack directly, and the `*` and `/` operators to calculate the result and then update the stack.

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
        char sign = '+';
        int num = 0;
        for (int i = 0; i < s.length(); i++) {
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
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
- Use a stack to store intermediate results
- Handle `+` and `-` operators directly, and `*` and `/` operators by calculating the result and updating the stack
- Iterate through the string and update the stack based on the operators and numbers encountered.