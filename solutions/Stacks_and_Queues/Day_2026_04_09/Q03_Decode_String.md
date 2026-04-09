# Decode String

## Problem Statement
Given an encoded string, return its decoded version. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. The input string is guaranteed to be a valid encoded string. For example, `3[a]2[bc]` would become `aaabcbc`, and `3[a2[c]]` would become `accaccacc`.

## Approach
We will use a stack-based approach to solve this problem. The stack will store the characters and the counts. When we encounter a `[`, we push the current string and count into the stack. When we encounter a `]`, we pop the top element from the stack, repeat the current string that many times, and append it to the previous string.

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
            if (c == '[') {
                numStack.push(num);
                strStack.push(res);
                res = "";
                num = 0;
            } else if (c == ']') {
                string temp = strStack.top();
                strStack.pop();
                int count = numStack.top();
                numStack.pop();
                for (int i = 0; i < count; i++) {
                    temp += res;
                }
                res = temp;
            } else if (c >= '0' && c <= '9') {
                num = num * 10 + c - '0';
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
- Use a stack to store the intermediate results.
- Handle the `[` and `]` characters separately to repeat the strings.
- Use a separate stack to store the counts of repetitions.