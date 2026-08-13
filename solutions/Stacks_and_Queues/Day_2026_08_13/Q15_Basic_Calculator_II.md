# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers, `+`, `-`, `*`, `/` operators and empty spaces. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval()` built-in function. Examples: `s = "3+2*2"` returns 7, `s = " 3/2 "` returns 1, `s = " 3+5 / 2 "` returns 5.

## Approach
The algorithm uses a stack to store numbers and performs operations based on operator precedence. It iterates over the string, parsing numbers and operators. When encountering an operator with lower precedence than the previous one, it pops the stack, performs the operation, and pushes the result back onto the stack.

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
            if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
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
- Use a stack to store intermediate results
- Handle operator precedence by performing operations immediately when encountering lower-precedence operators
- Parse numbers and operators from the input string, using a separate variable to track the current sign and number being parsed.