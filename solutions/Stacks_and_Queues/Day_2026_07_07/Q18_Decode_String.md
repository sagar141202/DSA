# Decode String

## Problem Statement
Given an encoded string, return its decoded version. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra characters or partially regular encodings. For example, the string "3[a]2[bc]" would be decoded as "aaabcbc", and the string "3[a2[c]]" would be decoded as "accaccacc".

## Approach
We will use a stack-based approach to solve this problem, where we iterate over the string and push opening brackets and numbers onto the stack. When we encounter a closing bracket, we pop the top elements from the stack, repeat the string, and append it to the result. The algorithm will iterate over the string only once, making it efficient.

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
        stack<int> nums;
        stack<string> strs;
        string res = "";
        int multi = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                multi = multi * 10 + c - '0';
            } else if (c == '[') {
                nums.push(multi);
                strs.push(res);
                res = "";
                multi = 0;
            } else if (c == ']') {
                string tmp = res;
                for (int i = 0; i < nums.top() - 1; i++) {
                    res += tmp;
                }
                res = strs.top() + res;
                strs.pop();
                nums.pop();
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
- Use a stack to keep track of the opening brackets and numbers.
- When encountering a closing bracket, pop the top elements from the stack and repeat the string accordingly.
- The algorithm has a linear time complexity due to the single pass over the input string.