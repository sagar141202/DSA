# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the calculated result. The string may contain only non-negative integers, `+`, `-`, `*`, `/`, and spaces. However, the division is integer division (e.g., `5 / 2 = 2`, `10 / 3 = 3`). Assume the expression is valid and doesn't contain any parentheses. For example, `3+2*2`, ` 3/2 `, ` 100/10/2 `.

## Approach
The algorithm uses a stack to store intermediate results and operators. It iterates over the string, applying operators with higher precedence immediately and those with lower precedence after the current number is processed. The key insight is to differentiate between the operators based on their precedence.

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
        int res = 0;
        
        for (int i = 0; i < s.length(); i++) {
            // if current char is digit, update num
            if (isdigit(s[i]))
                num = num * 10 + s[i] - '0';
            
            // if current char is not digit and not space
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
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
        
        // calculate the final res
        while (!st.empty()) {
            res += st.top();
            st.pop();
        }
        
        return res;
    }
};
```

## Test Cases
```
Input: "3+2*2"
Output: 7
Input: " 3/2 "
Output: 1
Input: " 100/10/2 "
Output: 5
```

## Key Takeaways
- Use a stack to store intermediate results for efficient calculation.
- Differentiate between operators based on precedence to apply them correctly.
- Apply the operator with higher precedence immediately when encountered.