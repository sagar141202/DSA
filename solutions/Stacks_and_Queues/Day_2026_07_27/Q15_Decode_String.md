# Decode String

## Problem Statement
Given an encoded string, decode it and return the decoded string. The encoding rule is: `k[encoded_string]`, where the encoded string inside the square brackets is repeated exactly `k` times. The input string is guaranteed to be valid. For example, if the input string is "3[a]2[bc]", the output should be "aaabcbc". The input string only contains digits, letters, and square brackets.

## Approach
We will use a stack to store the characters and the counts. When we encounter a '[', we push the current string and count into the stack. When we encounter a ']', we pop the top element from the stack, repeat the current string the specified number of times, and append it to the previous string.

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
                string tmp = res;
                res = strStack.top();
                strStack.pop();
                for (int i = 0; i < countStack.top() - 1; i++) {
                    res += tmp;
                }
                countStack.pop();
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
```

## Key Takeaways
- Use a stack to store the intermediate results and counts.
- When encountering a '[', push the current string and count into the stack.
- When encountering a ']', pop the top element from the stack, repeat the current string the specified number of times, and append it to the previous string.