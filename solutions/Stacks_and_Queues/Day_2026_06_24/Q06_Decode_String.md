# Decode String

## Problem Statement
Given an encoded string, return its decoded version. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly `k` times. The `k` is guaranteed to be a positive integer. For example, `3[a]` is decoded as `aaa`, and `3[a2[b]]` is decoded as `ababab`. You are given a string `s`, which contains at most 20 pairs of brackets and at most 100 characters. The string `s` will be a valid encoded string.

## Approach
We will use a stack-based approach to solve this problem, where we iterate over the string and use two stacks, one for the characters and one for the counts. When we encounter a '[', we push the current string and count into the stacks. When we encounter a ']', we pop the top element from the stacks, repeat the current string that many times, and append it to the previous string.

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
                string temp = strings.top();
                strings.pop();
                int count = counts.top();
                counts.pop();
                for (int i = 0; i < count; i++) {
                    temp += res;
                }
                res = temp;
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
- Use a stack-based approach to handle nested brackets.
- Keep track of the current string and count using two separate stacks.
- When encountering a '[', push the current string and count into the stacks and reset them.
- When encountering a ']', pop the top element from the stacks, repeat the current string that many times, and append it to the previous string.