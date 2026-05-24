# Decode String

## Problem Statement
Given an encoded string, decode it. The encoding rule is: `k[encoded_string]`, where the encoded_string inside the square brackets is repeated exactly k times. Note that k is guaranteed to be a positive integer. The string is guaranteed to be syntactically correct and not empty. For example, `3[a]2[bc]` would become `aaabcbc` after decoding.

## Approach
We will use a stack-based approach to solve this problem, where we iterate over the string and push the characters and counts onto the stack. When we encounter a ']', we pop the top element from the stack, repeat the string the specified number of times, and append it to the previous string.

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
        int k = 0;
        string res = "";
        for (char c : s) {
            if (isdigit(c)) {
                k = k * 10 + c - '0';
            } else if (c == '[') {
                counts.push(k);
                strings.push(res);
                k = 0;
                res = "";
            } else if (c == ']') {
                string tmp = strings.top();
                strings.pop();
                int count = counts.top();
                counts.pop();
                for (int i = 0; i < count; i++) {
                    tmp += res;
                }
                res = tmp;
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
- Use a stack to keep track of the counts and strings.
- When encountering a '[', push the current count and string onto the stack and reset the count and string.
- When encountering a ']', pop the top count and string from the stack, repeat the current string the specified number of times, and append it to the previous string.