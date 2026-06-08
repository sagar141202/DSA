# Decode String

## Problem Statement
Given an encoded string, decode it using the following rules: the string consists of digits and '[' and ']', where digits represent the number of times the substring inside the brackets should be repeated. For example, "3[a]" means "aaa" and "3[a2[c]]" means "accaccacc". The input string is guaranteed to be valid.

## Approach
We can use a stack to keep track of the characters and the count of repetitions. When we encounter a '[', we push the current string and count onto the stack. When we encounter a ']', we pop the top element from the stack, repeat the current string the specified number of times, and append it to the previous string.

## Complexity
- Time: O(n)
- Space: O(n)

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

int main() {
    string s = "3[a2[c]]";
    cout << decodeString(s) << endl;
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
- Use a stack to keep track of the characters and the count of repetitions.
- When encountering a '[', push the current string and count onto the stack.
- When encountering a ']', pop the top element from the stack, repeat the current string the specified number of times, and append it to the previous string.