# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression contains non-negative integers and the following operators: `+`, `-`, `*`, `/`. The integer division should truncate toward zero. You may assume that the given expression is always valid. Do not use the `eval` built-in function. The expression is guaranteed to be valid and only contains non-negative integers and the four basic operators. The length of `s` is in the range `[1, 215]`. `s` consists of digits, `+`, `-`, `*`, `/`, and spaces. `s` does not contain any leading or trailing spaces.

## Approach
We will use a stack-based approach to solve this problem. We iterate over the string and push numbers to the stack. When we encounter an operator, we pop the last two numbers from the stack, perform the operation, and push the result back to the stack. We handle the `+` and `-` operators separately from the `*` and `/` operators.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

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

int main() {
    string s = "3+2*2";
    cout << calculate(s) << endl;
    return 0;
}
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
- Handle the `*` and `/` operators immediately when encountered.
- Handle the `+` and `-` operators at the end by summing up all the elements in the stack.