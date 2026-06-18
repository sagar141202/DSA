# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the calculated result. The expression string contains only non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero. You may assume that the given expression is always valid and does not contain any division by zero.

## Approach
We will iterate through the string and use a stack to store the intermediate results. When we encounter an operator, we will pop the last two elements from the stack, apply the operation, and push the result back into the stack. We will handle the `+` and `-` operators separately from the `*` and `/` operators.

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
            // if the current character is a digit, update the num
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if the current character is not a digit or it's the last character
            if (!isdigit(s[i]) && s[i] != ' ' || i == s.length() - 1) {
                // apply the previous sign to the num
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
- Handle the `+` and `-` operators separately from the `*` and `/` operators.
- Use the `isdigit` function to check if a character is a digit.