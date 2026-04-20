# Decode String

## Problem Statement
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer. The input string is guaranteed to be a valid encoded string, and the input string will not contain any digits other than the ones used for encoding. For example, the string `"3[a]2[bc]"` would be decoded as `"aaabcbc"`. The string `"3[a2[c]]"` would be decoded as `"accaccacc"`. The string `"10[a]"` would be decoded as `"aaaaaaaaaa"`.

## Approach
We can use a stack-based approach to solve this problem. The stack will store the characters and the counts. When we encounter a '[', we push the current string and the count into the stack. When we encounter a ']', we pop the top element from the stack, repeat the current string the specified number of times, and append it to the previous string.

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
                for (int i = 0; i < countStack.top() - 1; i++) {
                    res += temp;
                }
                countStack.pop();
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
Input: "10[a]"
Output: "aaaaaaaaaa"
```

## Key Takeaways
- Use a stack to store the intermediate results and counts.
- When encountering '[', push the current string and count into the stack.
- When encountering ']', pop the top element from the stack, repeat the current string, and append it to the previous string.
- Handle the digits and characters separately to construct the final decoded string.