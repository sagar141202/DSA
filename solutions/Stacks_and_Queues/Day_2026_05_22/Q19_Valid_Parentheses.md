# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The input string may contain other characters that are not brackets.

## Approach
The algorithm uses a stack to keep track of the opening brackets and checks if the corresponding closing bracket is valid. When a closing bracket is encountered, the top of the stack is checked to see if it matches the closing bracket. If it does, the top element is popped from the stack; otherwise, the string is not valid.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        unordered_map<char, char> mp = {{')', '('}, {']', '['}, {'}', '{'}};
        
        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c);
            } else if (c == ')' || c == ']' || c == '}') {
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
                st.pop();
            }
        }
        
        return st.empty();
    }
};
```

## Test Cases
```
Input: "([])"
Output: true
Input: "([)]"
Output: false
Input: "{[]}"
Output: true
```

## Key Takeaways
- Use a stack to keep track of the opening brackets.
- Use an unordered map to store the corresponding closing brackets for each opening bracket.
- Check if the stack is empty after processing the entire string to ensure all brackets were matched correctly.