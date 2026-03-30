# Decode String

## Problem Statement
Given an encoded string, decode it. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly k times. The input string is guaranteed to be valid; there are no extra characters or partial nesting. For example, `3[a]2[bc]` would become `aaabcbc` after decoding.

## Approach
We can use a stack-based approach to solve this problem. The stack will store the characters and the count of repetitions. When we encounter a '[', we push the current string and count into the stack. When we encounter a ']', we pop the top element from the stack, repeat the current string the specified number of times, and append it to the previous string.

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
    
    // iterate over the input string
    for (char c : s) {
        // if the character is a digit, update the count
        if (isdigit(c)) {
            k = k * 10 + c - '0';
        } 
        // if the character is a '[', push the current string and count into the stack
        else if (c == '[') {
            countStack.push(k);
            strStack.push(res);
            res = "";
            k = 0;
        } 
        // if the character is a ']', pop the top element from the stack, repeat the current string, and append it to the previous string
        else if (c == ']') {
            int count = countStack.top();
            countStack.pop();
            string prevStr = strStack.top();
            strStack.pop();
            while (count-- > 0) {
                prevStr += res;
            }
            res = prevStr;
        } 
        // if the character is a letter, append it to the current string
        else {
            res += c;
        }
    }
    
    return res;
}

int main() {
    string input = "3[a]2[bc]";
    string output = decodeString(input);
    cout << output << endl;
    return 0;
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
- Use a stack to store the intermediate results and counts.
- Handle the different characters ('[', ']', digits, and letters) separately.
- Use a while loop to repeat the current string the specified number of times when encountering a ']' character.