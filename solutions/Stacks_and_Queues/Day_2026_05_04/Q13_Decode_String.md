# Decode String

## Problem Statement
Given an encoded string, decode it by repeating the substring specified by the number in front of it. The encoded string will be in the format "3[a]2[bc]" where "3[a]" means "aaa" and "2[bc]" means "bcbc". The string will only contain digits, letters, and brackets. The digits will be in the range 1-9, and the letters will be lowercase. The encoded string will not be empty and will not contain any whitespace.

## Approach
We will use a stack-based approach to solve this problem, where we iterate through the string and push/pop characters from the stack as needed. When we encounter a digit, we will multiply the current number by 10 and add the new digit. When we encounter a '[', we will push the current string and number onto the stack. When we encounter a ']', we will pop the string and number from the stack, repeat the current string that many times, and append it to the previous string.

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
        stack<int> numStack;
        string res = "";
        int num = 0;
        
        for (char c : s) {
            if (isdigit(c)) {
                num = num * 10 + c - '0';
            } else if (c == '[') {
                strStack.push(res);
                numStack.push(num);
                res = "";
                num = 0;
            } else if (c == ']') {
                string temp = res;
                res = strStack.top();
                strStack.pop();
                for (int i = 0; i < numStack.top() - 1; i++) {
                    res += temp;
                }
                strStack.pop();
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
- Use a stack to keep track of the current string and number when encountering '[' and ']'.
- Multiply the current number by 10 and add the new digit when encountering a digit.
- Repeat the current string the specified number of times when encountering ']' and append it to the previous string.