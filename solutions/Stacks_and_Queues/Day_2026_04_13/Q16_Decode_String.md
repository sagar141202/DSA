# Decode String

## Problem Statement
Given an encoded string, decode it using the following rules: the string consists of digits and '[' and ']' characters, where digits represent the number of times to repeat the substring inside the brackets, and the substring can also contain encoded strings. The task is to write a function that takes an encoded string as input and returns the decoded string. For example, given the encoded string "3[a]2[2[c]]", the decoded string would be "aaaccc". The function should handle all possible valid encoded strings and return an empty string if the input string is invalid.

## Approach
We can use a stack to store the characters and counts, then pop and repeat the characters when we encounter a ']' character. The algorithm iterates over the string, pushing characters and counts onto the stack, and popping them when it encounters a ']' character. We use two stacks, one for characters and one for counts.

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
                int count = numStack.top();
                numStack.pop();
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
Input: "3[a]2[2[c]]"
Output: "aaaccc"
Input: "3[a2[c]]"
Output: "accaccacc"
```

## Key Takeaways
- Use two stacks to store characters and counts separately.
- Iterate over the string, pushing and popping from the stacks as necessary.
- Handle the case where the input string is invalid by returning an empty string.