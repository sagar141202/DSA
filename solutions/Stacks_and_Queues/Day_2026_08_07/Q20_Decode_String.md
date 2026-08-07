# Decode String

## Problem Statement
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_key]`, where the encoded key is a sequence of alphabets and `k` is an integer from 1 to 100 which represents how many times the encoded key should be repeated. For example, `3[a]` should be decoded as `aaa`, and `3[a2[c]]` should be decoded as `accaccacc`. The input string is guaranteed to be valid.

## Approach
We can use a stack to store the characters and the count of repetitions. When we encounter a `[`, we push the current string and count into the stack. When we encounter a `]`, we pop the top element from the stack, repeat the current string the specified number of times, and append it to the previous string.

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
Input: "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Key Takeaways
- Use a stack to store the intermediate results and counts.
- When encountering a `[`, push the current string and count into the stack.
- When encountering a `]`, pop the top element from the stack, repeat the current string, and append it to the previous string.