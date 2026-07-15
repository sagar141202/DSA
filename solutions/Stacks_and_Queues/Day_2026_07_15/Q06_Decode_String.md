# Decode String

## Problem Statement
Given an encoded string, decode it using a stack-based approach. The encoded string contains numbers and letters, where numbers represent the frequency of the following letters. For example, "3[a]" means "aaa" and "3[a2[c]]" means "accaccacc". The string can contain nested encoded strings. The goal is to write a function that takes an encoded string as input and returns the decoded string. The input string is guaranteed to be valid.

## Approach
We will use a stack to store the characters and the counts. When we encounter a '[', we push the current string and count into the stack. When we encounter a ']', we pop the string and count from the stack, and append the current string repeated 'count' times to the popped string.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string decodeString(string s) {
        stack<string> strStack;
        stack<int> numStack;
        string res = "";
        int num = 0;
        
        for (char c : s) {
            if (c == '[') {
                strStack.push(res);
                numStack.push(num);
                res = "";
                num = 0;
            } else if (c == ']') {
                int count = numStack.top();
                numStack.pop();
                string prevStr = strStack.top();
                strStack.pop();
                for (int i = 0; i < count; i++) {
                    prevStr += res;
                }
                res = prevStr;
            } else if (c >= '0' && c <= '9') {
                num = num * 10 + (c - '0');
            } else {
                res += c;
            }
        }
        return res;
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
- Use a stack to store the intermediate results and counts.
- When encountering a '[', push the current string and count into the stack.
- When encountering a ']', pop the string and count from the stack, and append the current string repeated 'count' times to the popped string.