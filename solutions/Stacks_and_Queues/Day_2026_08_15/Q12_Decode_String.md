# Decode String

## Problem Statement
Given an encoded string, decode it using a stack-based approach. The encoded string contains numbers and letters, where numbers represent the count of consecutive occurrences of the substring that follows. The substring can be a single character or a previously decoded string. For example, "3[a]2[bc]" represents "aaabcbc". The input string is guaranteed to be valid and only contains lowercase letters, digits, and brackets. The length of the input string will not exceed 100.

## Approach
We use a stack to store the intermediate results and multipliers. When we encounter a digit, we update the multiplier. When we encounter a '[', we push the current result and multiplier into the stack. When we encounter a ']', we pop the result and multiplier from the stack, repeat the current result the specified number of times, and append it to the previous result.

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
        stack<int> numStack;
        stack<string> strStack;
        string res = "";
        int multi = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                multi = multi * 10 + c - '0';
            } else if (c == '[') {
                numStack.push(multi);
                strStack.push(res);
                multi = 0;
                res = "";
            } else if (c == ']') {
                int count = numStack.top();
                numStack.pop();
                string prevStr = strStack.top();
                strStack.pop();
                while (count > 0) {
                    prevStr += res;
                    count--;
                }
                res = prevStr;
            } else {
                res += c;
            }
        }
        return res;
    }
};

int main() {
    Solution solution;
    string input = "3[a]2[bc]";
    cout << solution.decodeString(input) << endl;
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
- Use a stack to store intermediate results and multipliers.
- Update the multiplier when encountering a digit.
- Push the current result and multiplier into the stack when encountering a '['.
- Pop the result and multiplier from the stack, repeat the current result, and append it to the previous result when encountering a ']'.