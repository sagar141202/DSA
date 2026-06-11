# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The input string may contain other characters that are not brackets, but these characters will not affect the validity of the string.

## Approach
The algorithm uses a stack to keep track of the opening brackets encountered so far. When a closing bracket is encountered, it checks if the top of the stack contains the corresponding opening bracket. If it does, the opening bracket is popped from the stack; otherwise, the string is invalid. The string is valid if the stack is empty after processing all characters.

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
        unordered_map<char, char> mp = {{')', '('}, {'}', '{'}, {']', '['}};
        
        for (char c : s) {
            if (mp.find(c) != mp.end()) {
                if (st.empty() || st.top() != mp[c]) return false;
                st.pop();
            } else if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            }
        }
        
        return st.empty();
    }
};
```

## Test Cases
```
Input: "()"
Output: true
Input: "()[]{}"
Output: true
Input: "(]"
Output: false
Input: "([)]"
Output: false
Input: "{[]}"
Output: true
```

## Key Takeaways
- Use a stack to keep track of the opening brackets.
- Use an unordered map to store the corresponding opening bracket for each closing bracket.
- Check if the stack is empty after processing all characters to determine the validity of the string.