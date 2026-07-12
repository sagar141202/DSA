# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not. The string may contain other characters, but the brackets must be properly nested. For example, "([)]" is not valid, but "{[]}" is valid.

## Approach
We can solve this problem using a stack data structure. The algorithm will iterate over the string and push opening brackets into the stack. When it encounters a closing bracket, it will check if the top of the stack contains the corresponding opening bracket. If it does, it will pop the opening bracket from the stack; otherwise, it will return false.

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
Input: "([)]"
Output: false
Input: "({[]})"
Output: true
Input: "(]"
Output: false
```

## Key Takeaways
- Use a stack to keep track of opening brackets
- Use an unordered map to store the corresponding opening bracket for each closing bracket
- Iterate over the string and push opening brackets into the stack, and pop them when encountering the corresponding closing bracket