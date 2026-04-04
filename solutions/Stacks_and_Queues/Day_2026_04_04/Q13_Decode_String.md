# Decode String

## Problem Statement
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_key]`, where the `encoded_key` inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, if the input string is `3[a]2[bc]`, the output should be `aaabcbc`. If the input string is `3[a2[c]]`, the output should be `accaccacc`.

## Approach
We will use a stack-based approach to solve this problem. The stack will store the intermediate results and the counts. When we encounter a '[', we push the current result and count into the stack. When we encounter a ']', we pop the last result and count from the stack, and append the current result repeated 'count' times to the last result.

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
                strStack.push(res);
                numStack.push(num);
                res = "";
                num = 0;
            } else if (c == ']') {
                string temp = res;
                res = strStack.top();
                strStack.pop();
                int count = numStack.top();
                numStack.pop();
                for (int i = 0; i < count; i++) {
                    res += temp;
                }
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
Input: "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Key Takeaways
- Use a stack to store the intermediate results and counts.
- When encountering a '[', push the current result and count into the stack and reset them.
- When encountering a ']', pop the last result and count from the stack, and append the current result repeated 'count' times to the last result.
- Handle the digits and characters separately to correctly construct the decoded string.