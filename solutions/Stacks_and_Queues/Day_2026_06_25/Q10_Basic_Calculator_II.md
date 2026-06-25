# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the result. The expression is composed of integers and operators `+`, `-`, `*`, `/`. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval` built-in function. Examples: `3+2*2` should return `7`, ` 3/2 ` should return `1`, ` 3+5 / 2 ` should return `5`.

## Approach
We can use a stack to store the intermediate results. We iterate over the string, and when we encounter a number, we push it to the stack. When we encounter an operator, we pop the top two elements from the stack, apply the operation, and push the result back to the stack.

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
            // if current char is digit, update num
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if current char is not digit or we are at the end
            if ((!isdigit(s[i])) && s[i] != ' ' || i == s.length() - 1) {
                // apply previous sign
                if (sign == '+') {
                    st.push(num);
                } else if (sign == '-') {
                    st.push(-num);
                } else if (sign == '*') {
                    st.push(st.top() * num);
                    st.pop();
                } else if (sign == '/') {
                    st.push(int(st.top() / num)); // truncate toward zero
                    st.pop();
                }
                // update sign and reset num
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
- We use a stack to store intermediate results.
- We iterate over the string and apply operators when we encounter them.
- We handle integer division by using `int(st.top() / num)` to truncate toward zero.