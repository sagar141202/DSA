# Decode String

## Problem Statement
Given an encoded string, return its decoded version. The encoding rule is: `k[encoded_string]`, where the encoded string inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra characters or partially decoded strings. For example, the string "3[a]2[bc]" would be decoded as "aaabcbc", and "3[a2[c]]" would be decoded as "accaccacc".

## Approach
We can use a stack to keep track of the characters and the counts. When we encounter a '[', we push the current string and count onto the stack. When we encounter a ']', we pop the count and previous string from the stack, repeat the current string that many times, and append it to the previous string.

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
        stack<int> numStack;
        string res = "";
        int num = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                num = num * 10 + c - '0';
            } else if (c == '[') {
                strStack.push(res);
                numStack.push(num);
                res = "";
                num = 0;
            } else if (c == ']') {
                string temp = res;
                res = strStack.top();
                strStack.pop();
                for (int i = 0; i < numStack.top() - 1; i++) {
                    res += temp;
                }
                numStack.pop();
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
- Use a stack to keep track of the characters and counts.
- When encountering a '[', push the current string and count onto the stack.
- When encountering a ']', pop the count and previous string from the stack, repeat the current string that many times, and append it to the previous string.