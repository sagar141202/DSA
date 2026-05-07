# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
We can use a stack data structure to solve this problem by pushing opening brackets onto the stack and popping them off when we encounter a matching closing bracket. If we encounter a closing bracket that doesn't match the top of the stack, or if there are brackets left on the stack at the end, the string is not valid. This approach ensures that the brackets are properly nested and closed in the correct order.

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
                if (st.empty() || st.top() != mp[c]) {
                    return false;
                }
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
- Use a stack to keep track of opening brackets.
- Use an unordered map to store the corresponding closing brackets for each opening bracket.
- Iterate through the string, pushing opening brackets onto the stack and popping them off when a matching closing bracket is encountered.
- If a closing bracket is encountered that doesn't match the top of the stack, or if there are brackets left on the stack at the end, the string is not valid.