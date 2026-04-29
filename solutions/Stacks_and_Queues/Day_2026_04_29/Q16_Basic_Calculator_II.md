# Basic Calculator II

## Problem Statement
Implement a basic calculator to evaluate a simple expression string. The expression string contains only non-negative integers, '+', '-', '*', '/' operators and empty spaces. The integer division should truncate toward zero. For example, " 3/2 " = 1, " 4/1/2 " = 2. You may assume that the given expression is always valid.

## Approach
The algorithm uses a stack to store the intermediate results. It iterates through the string, pushing numbers onto the stack and popping them when encountering an operator. The operator is then applied to the top two elements of the stack. The '+' and '-' operators are handled separately from '*' and '/' to ensure correct order of operations.

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
        for(int i = 0; i < s.length(); i++) {
            if(isdigit(s[i])) {
                num = num * 10 + s[i] - '0';
            }
            if((!isdigit(s[i]) && !isspace(s[i])) || i == s.length() - 1) {
                if(sign == '+') {
                    st.push(num);
                } else if(sign == '-') {
                    st.push(-num);
                } else if(sign == '*') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev * num);
                } else if(sign == '/') {
                    int prev = st.top();
                    st.pop();
                    st.push(prev / num);
                }
                sign = s[i];
                num = 0;
            }
        }
        int sum = 0;
        while(!st.empty()) {
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
- Use a stack to store intermediate results and handle operator precedence.
- Iterate through the string, pushing numbers onto the stack and popping them when encountering an operator.
- Apply the operator to the top two elements of the stack and push the result back onto the stack.
- Handle '+' and '-' operators separately from '*' and '/' to ensure correct order of operations.