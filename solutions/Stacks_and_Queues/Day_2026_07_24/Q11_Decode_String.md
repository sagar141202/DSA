# Decode String

## Problem Statement
Given an encoded string, decode it and return the decoded string. The encoding rule is: `k[encoded_string]`, where the encoded string inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. The input string is guaranteed to be valid, and there will not be any digits after the closing bracket. For example, the input `"3[a]2[bc]"` would return `"aaabcbc"`, and the input `"3[a2[c]]"` would return `"accaccacc"`.

## Approach
We will use a stack-based approach to solve this problem. We iterate through the string, pushing characters onto the stack when we encounter them. When we encounter a `[`, we push the current string and the count onto the stack. When we encounter a `]`, we pop the top two elements off the stack, repeat the current string that many times, and append it to the previous string.

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
        stack<int> counts;
        stack<string> strings;
        string res = "";
        int k = 0;
        
        // iterate through the string
        for (char c : s) {
            // if the character is a digit, update the count
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } 
            // if the character is a '[', push the current string and count onto the stack
            else if (c == '[') {
                counts.push(k);
                strings.push(res);
                res = "";
                k = 0;
            } 
            // if the character is a ']', pop the top two elements off the stack and repeat the current string
            else if (c == ']') {
                int count = counts.top();
                counts.pop();
                string prev = strings.top();
                strings.pop();
                // repeat the current string count times and append it to the previous string
                for (int i = 0; i < count; i++) {
                    prev += res;
                }
                res = prev;
            } 
            // if the character is a letter, append it to the current string
            else {
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
- Use a stack to store the intermediate results and counts.
- Iterate through the string, pushing characters onto the stack when we encounter them.
- When we encounter a `[`, push the current string and the count onto the stack.
- When we encounter a `]`, pop the top two elements off the stack, repeat the current string that many times, and append it to the previous string.