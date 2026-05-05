# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return the result. The expression contains non-negative integers and operators `+`, `-`, `*`, `/`. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval` built-in function. Examples: 
- Input: `s = "3+2*2"`
- Output: `7`
- Input: `s = " 3/2 `"
- Output: `1`
- Input: `s = " 3+5 / 2 `"
- Output: `5`

## Approach
We will iterate through the string, using a stack to store the intermediate results. When we encounter an operator, we will apply it to the top two elements of the stack. We will also keep track of the current number being processed.

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
            // check if current character is a digit
            if (isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            // if current character is not a digit or we have reached the end of the string
            if ((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
                if (sign == '+') {
                    st.push(num);
                } else if (sign == '-') {
                    st.push(-num);
                } else if (sign == '*') {
                    int pre = st.top();
                    st.pop();
                    st.push(pre * num);
                } else if (sign == '/') {
                    int pre = st.top();
                    st.pop();
                    st.push(pre / num);
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
- Keep track of the current number and operator
- Apply operators to the top two elements of the stack when encountering a new operator or the end of the string