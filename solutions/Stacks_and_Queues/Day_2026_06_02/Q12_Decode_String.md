# Decode String

## Problem Statement
Given an encoded string, return its decoded version. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra characters or invalid inputs. For example, the input string "3[a]2[bc]" should return "aaabcbc", and "3[a2[c]]" should return "accaccacc".

## Approach
We will use a stack-based approach to solve this problem, parsing the string from left to right and using two stacks to keep track of the characters and the counts. When we encounter a '[', we push the current string and count onto the stacks. When we encounter a ']', we pop the top string and count from the stacks, and append the current string repeated 'count' times to the top string.

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
- Use two stacks to keep track of the counts and the strings.
- When encountering a '[', push the current string and count onto the stacks.
- When encountering a ']', pop the top string and count from the stacks, and append the current string repeated 'count' times to the top string.
- The time complexity is O(N), where N is the length of the input string.