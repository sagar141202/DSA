# Valid Parentheses

## Problem Statement
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. The brackets must close in the correct order, i.e., "()" and "()[]{}" are all valid, but "(]" and "([)]" are not. The string may contain other characters that are not brackets.

## Approach
We will use a stack to store the opening brackets and pop them when we encounter a matching closing bracket. If we encounter a closing bracket that does not match the top of the stack, or if there are brackets left in the stack at the end, the string is not valid. This approach allows us to efficiently check for valid parentheses in a single pass through the string.

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

int main() {
    Solution solution;
    cout << boolalpha << solution.isValid("()") << endl;  // true
    cout << boolalpha << solution.isValid("()[]{}") << endl;  // true
    cout << boolalpha << solution.isValid("(]") << endl;  // false
    cout << boolalpha << solution.isValid("([)]") << endl;  // false
    cout << boolalpha << solution.isValid("{[]}") << endl;  // true
    return 0;
}
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
- Use a stack to store the opening brackets and pop them when a matching closing bracket is encountered.
- Use an unordered map to store the mapping between closing and opening brackets for efficient lookups.
- Check if the stack is empty at the end to ensure all brackets were properly closed.