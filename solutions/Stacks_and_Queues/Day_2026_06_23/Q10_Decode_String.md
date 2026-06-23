# Decode String

## Problem Statement
Given an encoded string, decode it and return the decoded string. The encoding rule is: `k[encoded_string]`, where the encoded string inside the square brackets is repeated exactly `k` times. The encoded string can contain lowercase letters, digits, and the '[' and ']' characters. For example, if the input string is "3[a]2[bc]", the output should be "aaabcbc". If the input string is "3[a2[c]]", the output should be "accaccacc". The input string is guaranteed to be a valid encoded string.

## Approach
We will use a stack-based approach to solve this problem, where we iterate through the input string and push the characters onto the stack. When we encounter a '[', we push the current number and the current string onto the stack. When we encounter a ']', we pop the top two elements from the stack, repeat the current string that many times, and append it to the previous string.

## Complexity
- Time: O(N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string decodeString(string s) {
    stack<int> numStack;
    stack<string> strStack;
    string res = "";
    int num = 0;
    
    for (char c : s) {
        // if the character is a digit, update the current number
        if (isdigit(c)) {
            num = num * 10 + c - '0';
        } 
        // if the character is a '[', push the current number and string onto the stack
        else if (c == '[') {
            numStack.push(num);
            strStack.push(res);
            res = "";
            num = 0;
        } 
        // if the character is a ']', pop the top two elements from the stack, repeat the current string, and append it to the previous string
        else if (c == ']') {
            int n = numStack.top();
            numStack.pop();
            string prev = strStack.top();
            strStack.pop();
            for (int i = 0; i < n; i++) {
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
```

## Test Cases
```
Input: "3[a]2[bc]"
Output: "aaabcbc"
Input: "3[a2[c]]"
Output: "accaccacc"
```

## Key Takeaways
- Use a stack to keep track of the current number and string when encountering '[' and ']'.
- Repeat the current string the specified number of times when encountering ']'.
- Append the repeated string to the previous string to form the final decoded string.