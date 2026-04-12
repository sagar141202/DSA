# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the result. The string `s` contains numbers from `0-9`, `+`, `-`, `*`, `/` operators, and spaces. The expression is evaluated assuming that the `+` and `-` operators have lower precedence than the `*` and `/` operators. For example, `3+2*2` should be evaluated as `3+(2*2)`.

## Approach
We can use a stack-based approach to solve this problem. We iterate through the string and push numbers onto the stack. When we encounter an operator, we pop the top two numbers from the stack, apply the operation, and push the result back onto the stack.

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
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
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
- Use a stack to store intermediate results
- Handle the `+` and `-` operators separately from the `*` and `/` operators due to precedence
- Be careful with the handling of spaces in the input string