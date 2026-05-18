# Decode String

## Problem Statement
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_key]`, where the encoded key is a sequence of encoded strings, and `k` is the number of times the encoded key should be repeated. For example, `3[a]2[bc]` would become `aaabcbc`. The input string is guaranteed to be a valid encoded string, and the number of nested encodings will not exceed 100. The length of the input string will not exceed 300.

## Approach
We can use a stack-based approach to solve this problem by iterating through the input string and pushing the characters onto the stack when we encounter a '[', and popping the characters off the stack when we encounter a ']'. We also need to keep track of the repeat count and the current string being built.

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
        stack<int> counts;
        stack<string> results;
        string res = "";
        int k = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } else if (c == '[') {
                counts.push(k);
                results.push(res);
                res = "";
                k = 0;
            } else if (c == ']') {
                string temp = res;
                for (int i = 0; i < counts.top() - 1; i++) {
                    res += temp;
                }
                res = results.top() + res;
                results.pop();
                counts.pop();
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
- Use a stack to keep track of the repeat counts and the current strings being built.
- When encountering a '[', push the current string and repeat count onto the stack and reset the current string and repeat count.
- When encountering a ']', pop the repeat count and previous string off the stack, and append the current string repeated the specified number of times to the previous string.