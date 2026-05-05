# Decode String

## Problem Statement
Given an encoded string, decode it and return the original string. The encoding rule is: `k[encoded_string]`, where `k` is the number of times the `encoded_string` should be repeated. For example, `3[a]` should be decoded as `aaa`, and `3[a2[c]]` should be decoded as `accaccacc`. The input string is guaranteed to be valid.

## Approach
We can use a stack-based approach to solve this problem. The idea is to iterate over the input string, and whenever we encounter a digit, we push it onto the stack. When we encounter a `[`, we push the current string and the count onto the stack. When we encounter a `]`, we pop the top two elements from the stack, repeat the current string that many times, and append it to the previous string.

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
                string tmp = res;
                for (int i = 0; i < counts.top() - 1; i++) {
                    res += tmp;
                }
                res = strings.top() + res;
                strings.pop();
                counts.pop();
            } else {
                res += c;
            }
        }
        
        return res;
    }
};

int main() {
    Solution solution;
    string input = "3[a2[c]]";
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
- Use a stack to keep track of the counts and strings.
- When encountering a `[`, push the current string and count onto the stack.
- When encountering a `]`, pop the top two elements from the stack, repeat the current string that many times, and append it to the previous string.
- The time complexity is O(n), where n is the length of the input string.