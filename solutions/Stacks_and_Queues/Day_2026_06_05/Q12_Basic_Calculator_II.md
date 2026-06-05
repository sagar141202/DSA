# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers and operators `+`, `-`, `*`, `/`. The integer division should truncate toward zero. Note that division by zero is not allowed, and assume we are not using any extra space other than the space used by the expression itself. For example, if `s = "3+2*2"`, the output should be `7` because `2*2 = 4` and `3 + 4 = 7`.

## Approach
We can use a stack to store the intermediate results. We iterate over the string from left to right, and whenever we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two elements from the stack, apply the operation, and push the result back to the stack.

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
        int num = 0;
        char sign = '+';
        for (int i = 0; i < s.length(); i++) {
            // if the current character is a digit, update the num
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if the current character is not a digit or it's the last character
            if ((!isdigit(s[i])) && s[i] != ' ' || i == s.length() - 1) {
                // apply the previous operator
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
                // update the sign and reset the num
                sign = s[i];
                num = 0;
            }
        }
        // calculate the final result
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
- Use a stack to store the intermediate results.
- Handle the operator '*' and '/' first because they have higher priority than '+' and '-'.
- Be careful when handling the division by zero and the overflow.