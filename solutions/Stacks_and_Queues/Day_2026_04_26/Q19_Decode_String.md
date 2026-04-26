# Decode String

## Problem Statement
Given an encoded string, decode it by following the given rules: the string consists of digits and '[' and ']' characters, where each digit represents the number of times the substring enclosed in the following '[' and ']' should be repeated. For example, "3[a]2[bc]" would become "aaabcbc" after decoding. The input string is guaranteed to be valid and will not contain any whitespace or special characters other than '[' and ']'. The input string will also not contain any nested '[' and ']' characters.

## Approach
We can use a stack-based approach to solve this problem by iterating through the string and pushing characters onto the stack when we encounter them. When we encounter a '[', we push the current string and the multiplier onto the stack. When we encounter a ']', we pop the string and multiplier from the stack and append the current string repeated by the multiplier to the previous string.

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
                int count = numStack.top();
                numStack.pop();
                for (int i = 1; i < count; i++) {
                    res += temp;
                }
                res = strStack.top() + res;
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
- Use a stack to keep track of the current string and multiplier when encountering '[' and ']' characters.
- When encountering a '[', push the current string and multiplier onto the stack and reset the current string and multiplier.
- When encountering a ']', pop the string and multiplier from the stack and append the current string repeated by the multiplier to the previous string.