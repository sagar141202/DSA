# Decode String

## Problem Statement
Given an encoded string, decode it and return the decoded string. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra spaces, and there will be no special or invalid characters. For example, if the input string is "3[a]2[bc]", the output should be "aaabcbc". If the input string is "3[a2[c]]", the output should be "accaccacc".

## Approach
We will use a stack to keep track of the characters and the counts. When we encounter a '[', we push the current string and count into the stack. When we encounter a ']', we pop the top element from the stack, repeat the current string that many times, and append it to the previous string.

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
        stack<int> numStack;
        string res = "";
        int multi = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                multi = multi * 10 + c - '0';
            } else if (c == '[') {
                numStack.push(multi);
                strStack.push(res);
                res = "";
                multi = 0;
            } else if (c == ']') {
                int count = numStack.top();
                numStack.pop();
                string prevStr = strStack.top();
                strStack.pop();
                for (int i = 0; i < count; i++) {
                    prevStr += res;
                }
                res = prevStr;
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
- Use a stack to keep track of the characters and counts when decoding the string.
- Repeat the current string the specified number of times when encountering a ']' character.
- Handle the edge cases where the input string is empty or contains invalid characters.