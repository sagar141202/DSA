# Decode String

## Problem Statement
Given an encoded string, decode it. The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is repeated exactly k times. The decoding process should repeat this rule until there are no more square brackets in the string. The string contains only lowercase letters, digits, and square brackets. The string is guaranteed to be a valid encoded string. For example, "3[a]2[bc]" would be decoded as "aaabcbc" and "3[a2[c]]" would be decoded as "accaccacc".

## Approach
We will use a stack to store the characters and the counts. When we encounter an opening bracket, we push the current string and count into the stack. When we encounter a closing bracket, we pop the last string and count from the stack, repeat the current string count times, and append it to the last string.

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
        stack<string> strStack;
        stack<int> countStack;
        string currStr = "";
        int k = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } else if (c == '[') {
                strStack.push(currStr);
                countStack.push(k);
                currStr = "";
                k = 0;
            } else if (c == ']') {
                string prevStr = strStack.top();
                strStack.pop();
                int count = countStack.top();
                countStack.pop();
                for (int i = 0; i < count; i++) {
                    prevStr += currStr;
                }
                currStr = prevStr;
            } else {
                currStr += c;
            }
        }
        
        return currStr;
    }
};

int main() {
    Solution solution;
    string input = "3[a]2[bc]";
    string output = solution.decodeString(input);
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
- When encountering a closing bracket, pop the last string and count from the stack and repeat the current string count times.
- Use a separate string to store the current string being processed.