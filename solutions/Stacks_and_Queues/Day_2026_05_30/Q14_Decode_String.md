# Decode String

## Problem Statement
Given an encoded string, decode it and return the decoded string. The encoded string is in the format of `3[a]2[bc]`, where `3[a]` means the string "a" is repeated three times, and `2[bc]` means the string "bc" is repeated twice. The string can contain numbers, letters, and brackets. The numbers can be single-digit or multi-digit. The string is guaranteed to be valid.

## Approach
We will use a stack to keep track of the characters and the counts. When we encounter a digit, we will multiply the current count by 10 and add the new digit. When we encounter a '[', we will push the current string and count into the stack. When we encounter a ']', we will pop the string and count from the stack, and append the current string repeated by the count to the popped string.

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
        stack<int> countStack;
        string res = "";
        int k = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } else if (c == '[') {
                strStack.push(res);
                countStack.push(k);
                res = "";
                k = 0;
            } else if (c == ']') {
                string temp = res;
                res = strStack.top();
                strStack.pop();
                int count = countStack.top();
                countStack.pop();
                for (int i = 0; i < count; i++) {
                    res += temp;
                }
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
- Use a stack to keep track of the characters and the counts.
- When encountering a '[', push the current string and count into the stack.
- When encountering a ']', pop the string and count from the stack, and append the current string repeated by the count to the popped string.