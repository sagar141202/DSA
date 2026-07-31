# Decode String

## Problem Statement
Given an encoded string, return its decoded version. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. The string is guaranteed to be syntactically correct and not empty. For example, if the input string is `3[a]2[bc]`, the output should be `aaabcbc`. If the input string is `3[a2[c]]`, the output should be `accaccacc`.

## Approach
We can use a stack to store the characters and the counts. When we encounter a '[', we push the current string and count into the stack. When we encounter a ']', we pop the top element from the stack, repeat the current string that many times, and append it to the previous string.

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
        stack<string> strings;
        string res = "";
        int k = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } else if (c == '[') {
                counts.push(k);
                strings.push(res);
                res = "";
                k = 0;
            } else if (c == ']') {
                int count = counts.top();
                counts.pop();
                string prev = strings.top();
                strings.pop();
                while (count-- > 0) {
                    prev += res;
                }
                res = prev;
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
- Use a stack to store the intermediate results.
- When encountering a '[', push the current string and count into the stack.
- When encountering a ']', pop the top element from the stack, repeat the current string that many times, and append it to the previous string.