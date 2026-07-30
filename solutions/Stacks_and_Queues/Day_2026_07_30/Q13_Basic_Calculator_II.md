# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval` built-in function. For example, `3+2*2` should return `7`, and ` 3/2 ` should return `1`.

## Approach
We will use a stack-based approach to solve this problem. The idea is to iterate over the expression and whenever we encounter an operator with lower precedence than the previous operator, we will evaluate the previous operation and push the result back to the stack. We will handle the `+` and `-` operators separately.

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
            // if current character is a digit, update num
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if current character is not a digit or it's the last character
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
                // evaluate the previous operation
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
                // update sign and reset num
                sign = s[i];
                num = 0;
            }
        }
        // sum up all elements in the stack
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
- Handle `+` and `-` operators separately to avoid confusion with the sign of the number.
- Be careful with integer division, it should truncate toward zero.