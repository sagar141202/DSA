# Basic Calculator II

## Problem Statement
Given a string `s` which represents an expression, evaluate this expression and return its value. The expression is composed of digits `0-9`, `+`, `-`, `*`, `/` and `space`. For example, `strings` = `" 3+5 / 2 "` should return `5` and `strings` = `" 3+5 / 2-3*4"` should return `-4`. Assume that the input string only contains valid characters and does not contain any white spaces.

## Approach
We use a stack to store the intermediate results. We iterate over the string and whenever we encounter a digit, we update the current number. When we encounter an operator, we pop the last number from the stack, apply the operation and push the result back to the stack.

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
        // if current character is a digit, update the current number
        if (isdigit(s[i])) num = num * 10 + s[i] - '0';
        // if current character is not a digit or it's the last character
        if (!isdigit(s[i]) && !isspace(s[i]) || i == s.length() - 1) {
            // apply the previous operator
            if (sign == '+') st.push(num);
            else if (sign == '-') st.push(-num);
            else if (sign == '*') st.push(st.top() * num);
            else if (sign == '/') st.push(st.top() / num);
            // update the operator and reset the current number
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

int main() {
    string s = "3+5/2";
    cout << calculate(s) << endl;
    return 0;
}
```

## Test Cases
```
Input: "3+5/2"
Output: 5
Input: " 3/2 "
Output: 1
Input: " 3+5 / 2 "
Output: 5
```

## Key Takeaways
- Use a stack to store the intermediate results
- Update the current number whenever a digit is encountered
- Apply the previous operator whenever a non-digit character is encountered