# Decode String

## Problem Statement
Given an encoded string, return its decoded string. The encoding rule is: `k[encoded_key]`, where the `encoded_key` inside the square brackets is repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra characters or invalid `k` values. Examples of valid encoded strings include `3[a]2[bc]` and `3[a2[c]]`. The string inside the brackets can also contain numbers and letters.

## Approach
We will use two stacks to keep track of the characters and the counts. When we encounter a '[', we push the current string and count into the stacks. When we encounter a ']', we pop the top count and string from the stacks, repeat the current string that many times, and append it to the top string.

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
        
        // iterate over each character in the string
        for (char c : s) {
            // if the character is a digit, update the count
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } 
            // if the character is a '[', push the current string and count into the stacks
            else if (c == '[') {
                counts.push(k);
                strings.push(res);
                res = "";
                k = 0;
            } 
            // if the character is a ']', pop the top count and string from the stacks, repeat the current string, and append it to the top string
            else if (c == ']') {
                string temp = res;
                res = strings.top();
                strings.pop();
                int count = counts.top();
                counts.pop();
                // repeat the current string 'count' times and append it to the top string
                for (int i = 0; i < count; i++) {
                    res += temp;
                }
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
```

## Key Takeaways
- Use two stacks to keep track of the characters and the counts.
- When encountering a '[', push the current string and count into the stacks.
- When encountering a ']', pop the top count and string from the stacks, repeat the current string, and append it to the top string.