# Decode String

## Problem Statement
Given an encoded string, return its decoded version. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer. You may assume that the input string is always valid; there are no extra spaces, and there will be no special or invalid characters. For example, if the input string is "3[a]2[bc]", the output should be "aaabcbc". The string can contain digits (1-9), letters (a-z), and square brackets.

## Approach
We will use a stack-based approach to solve this problem. The stack will store the characters and the count of the repeated string. When we encounter an opening bracket, we push the current string and count into the stack. When we encounter a closing bracket, we pop the string and count from the stack, repeat the current string the specified number of times, and append it to the previous string.

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

    for (char c : s) {
        if (isdigit(c)) {
            k = k * 10 + c - '0';
        } else if (c == '[') {
            strStack.push(res);
            countStack.push(k);
            res = "";
            k = 0;
        } else if (c == ']') {
            string temp = res;
            res = strStack.top();
            strStack.pop();
            for (int i = 0; i < countStack.top() - 1; i++) {
                res += temp;
            }
            countStack.pop();
        } else {
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
- Use a stack to store the intermediate results and counts.
- When encountering an opening bracket, push the current string and count into the stack.
- When encountering a closing bracket, pop the string and count from the stack, repeat the current string, and append it to the previous string.
- Handle digits and letters separately to correctly parse the input string.