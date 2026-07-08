# Decode String

## Problem Statement
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra characters or invalid input. For example, if the input string is `3[a]2[bc]`, the output should be `aaabcbc`. If the input string is `3[a2[c]]`, the output should be `accaccacc`.

## Approach
The algorithm uses a stack to store the characters and the counts. It iterates over the string, pushing the characters and counts onto the stack when it encounters a `[` and popping them off when it encounters a `]`. The popped characters are then repeated the specified number of times and appended to the result string.

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
                countStack.push(k);
                strStack.push(res);
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
Input: "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
```

## Key Takeaways
- Use a stack to store the characters and counts to handle nested encoded strings.
- Iterate over the string, pushing and popping characters and counts as necessary.
- Repeat the popped characters the specified number of times and append them to the result string.