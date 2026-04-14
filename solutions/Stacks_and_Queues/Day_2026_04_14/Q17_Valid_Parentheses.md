# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters, but these characters are ignored for the purpose of this problem. For example, "([)]" is not valid, but "{[]}" is valid.

## Approach
The algorithm uses a stack data structure to keep track of the opening brackets encountered so far. When a closing bracket is encountered, the top of the stack is checked to see if it matches the closing bracket. If it does, the top element is popped from the stack; otherwise, the string is not valid. The stack is empty at the end if the string is valid.

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
            if (c == '(' || c == '{' || c == '[') {
                st.push(c);
            } else if (c == ')' || c == '}' || c == ']') {
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
- Use a stack data structure to solve problems that require checking the order of elements.
- Use an unordered map to store the mapping between closing and opening brackets for easy lookup.
- Check for edge cases such as an empty string or a string with only one bracket.