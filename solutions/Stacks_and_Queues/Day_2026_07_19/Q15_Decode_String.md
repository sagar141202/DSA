# Decode String

## Problem Statement
Given an encoded string, decode it and return the original string. The encoded string is in the format of `[num[str]]` where `num` is the number of times `str` should be repeated. For example, `3[a]2[bc]` should be decoded to `aaabcbc`. The input string will only contain digits, letters, and square brackets, and it will always be a valid encoded string.

## Approach
We can use a stack to keep track of the current string and the multiplier. When we encounter a digit, we multiply the current multiplier by 10 and add the new digit. When we encounter a letter, we add it to the current string. When we encounter a `[`, we push the current string and multiplier to the stack and reset them. When we encounter a `]`, we pop the last string and multiplier from the stack, repeat the current string that many times, and append it to the last string.

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
        stack<int> numStack;
        stack<string> strStack;
        string res = "";
        int multi = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                multi = multi * 10 + c - '0';
            } else if (c == '[') {
                numStack.push(multi);
                strStack.push(res);
                multi = 0;
                res = "";
            } else if (c == ']') {
                int count = numStack.top();
                numStack.pop();
                string last = strStack.top();
                strStack.pop();
                while (count-- > 0) {
                    last += res;
                }
                res = last;
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
```

## Key Takeaways
- Use a stack to keep track of the current string and the multiplier.
- When encountering a digit, update the multiplier.
- When encountering a letter, add it to the current string.
- When encountering a `[`, push the current string and multiplier to the stack and reset them.
- When encountering a `]`, pop the last string and multiplier from the stack, repeat the current string that many times, and append it to the last string.