# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers and the operators `+`, `-`, `*`, `/`. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval` built-in function. Examples: 
- Input: `s = "3+2*2"` 
- Output: `7`
- Input: `s = " 3/2 ` 
- Output: `1`
- Input: `s = " 3+5 / 2 ` 
- Output: `5`

## Approach
We will use a stack to store the intermediate results. We iterate over the string and whenever we encounter an operator, we update the stack accordingly. For `+` and `-` operators, we simply push the current number onto the stack. For `*` and `/` operators, we pop the last number from the stack, perform the operation, and then push the result back onto the stack.

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
        int currNum = 0;
        char operation = '+';
        for (int i = 0; i < s.length(); i++) {
            // if the current character is a digit, update the current number
            if (isdigit(s[i])) {
                currNum = currNum * 10 + (s[i] - '0');
            }
            // if the current character is an operator or we have reached the end of the string
            if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
                if (operation == '+') {
                    st.push(currNum);
                } else if (operation == '-') {
                    st.push(-currNum);
                } else if (operation == '*') {
                    int top = st.top();
                    st.pop();
                    st.push(top * currNum);
                } else if (operation == '/') {
                    int top = st.top();
                    st.pop();
                    st.push(top / currNum);
                }
                operation = s[i];
                currNum = 0;
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
- Use a stack to store the intermediate results.
- Update the stack based on the operators encountered in the string.
- Handle the `*` and `/` operators separately by popping the last number from the stack, performing the operation, and pushing the result back onto the stack.