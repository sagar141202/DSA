# Decode String

## Problem Statement
Given an encoded string, decode it and return the original string. The encoded string is in the format of `3[a]2[bc]`, where the number represents how many times the string inside the brackets should be repeated. The string can contain lowercase letters and numbers, and the brackets can be nested. For example, `3[a2[c]]` should be decoded to `accaccacc`. The input string is guaranteed to be valid.

## Approach
We will use a stack to store the characters and the count of repetitions. When we encounter a '[', we push the current string and count into the stack. When we encounter a ']', we pop the top element from the stack, repeat the current string 'count' times, and append it to the previous string.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<string> strStack;
        stack<int> countStack;
        string curStr = "";
        int k = 0;
        
        for (char c : s) {
            if (c == '[') {
                strStack.push(curStr);
                countStack.push(k);
                curStr = "";
                k = 0;
            } else if (c == ']') {
                string temp = curStr;
                curStr = strStack.top();
                strStack.pop();
                for (int i = 0; i < countStack.top() - 1; i++) {
                    curStr += temp;
                }
                countStack.pop();
            } else if (c >= '0' && c <= '9') {
                k = k * 10 + c - '0';
            } else {
                curStr += c;
            }
        }
        
        return curStr;
    }
};
```

## Test Cases
```
Input: "3[a]2[bc]"
Output: "aaabcbc"
Input: "3[a2[c]]"
Output: "accaccacc"
Input: "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Key Takeaways
- We use two stacks, one for strings and one for counts, to handle nested brackets.
- When we encounter a '[', we push the current string and count into the stacks and reset them.
- When we encounter a ']', we pop the top elements from the stacks, repeat the current string 'count' times, and append it to the previous string.