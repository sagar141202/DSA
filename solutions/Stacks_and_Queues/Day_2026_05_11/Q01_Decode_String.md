# Decode String

## Problem Statement
Given an encoded string, decode it. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits do not appear in the result. For example, the string `"3[a]2[bc]"` would be decoded as `"aaabcbc"`, and the string `"3[a2[c]]"` would be decoded as `"accaccacc"`.

## Approach
We will use a stack-based approach to solve this problem, where we iterate over the string and use the stack to keep track of the characters and counts. When we encounter a '[', we push the current string and count onto the stack and reset them. When we encounter a ']', we pop the top string and count from the stack, repeat the current string that many times, and append it to the top string.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string decodeString(string s) {
    stack<string> strStack;
    stack<int> countStack;
    string res = "";
    int k = 0;
    
    // iterate over the string
    for (char c : s) {
        // if the character is a digit, update the count
        if (isdigit(c)) {
            k = k * 10 + c - '0';
        } 
        // if the character is a '[', push the current string and count onto the stack
        else if (c == '[') {
            countStack.push(k);
            strStack.push(res);
            res = "";
            k = 0;
        } 
        // if the character is a ']', pop the top string and count from the stack, repeat the current string that many times, and append it to the top string
        else if (c == ']') {
            int count = countStack.top();
            countStack.pop();
            string prevStr = strStack.top();
            strStack.pop();
            for (int i = 0; i < count; i++) {
                prevStr += res;
            }
            res = prevStr;
        } 
        // if the character is a letter, add it to the current string
        else {
            res += c;
        }
    }
    
    return res;
}
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
- Use a stack to keep track of the characters and counts.
- Iterate over the string and update the stack accordingly.
- When encountering a ']', repeat the current string the specified number of times and append it to the top string.