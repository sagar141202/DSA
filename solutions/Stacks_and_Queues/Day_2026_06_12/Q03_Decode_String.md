# Decode String

## Problem Statement
Given an encoded string, decode it and return the original string. The encoded string is in the format of `[num[str]]` where `num` is the number of times the string `str` should be repeated. The string `str` can also be a combination of other encoded strings. For example, `3[a]2[bc]` should be decoded to `aaabcbc`. The input string is guaranteed to be valid and will only contain digits, letters, and square brackets.

## Approach
We can use a stack-based approach to solve this problem by iterating over the string and pushing/popping elements from the stack when we encounter opening/closing brackets. We will maintain two stacks, one for the strings and one for the counts. When we encounter a '[', we push the current string and count to the stacks and reset them. When we encounter a ']', we pop the top string and count from the stacks, repeat the current string that many times, and append it to the top string.

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
                for (int i = 0; i < countStack.top() - 1; i++) {
                    res += temp;
                }
                strStack.pop();
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
- We use two stacks to keep track of the strings and counts.
- When we encounter a '[', we push the current string and count to the stacks and reset them.
- When we encounter a ']', we pop the top string and count from the stacks, repeat the current string that many times, and append it to the top string.