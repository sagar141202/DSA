# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are 1 <= k <= num.length <= 10000, and num does not contain any leading zero. For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
The approach is to iterate over the string and use a stack to keep track of the digits. If the stack is not empty and the top of the stack is greater than the current digit, we pop the stack until it's empty or the top of the stack is less than or equal to the current digit, or we have removed k digits. This ensures that the resulting number is the smallest possible.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string removeKdigits(string num, int k) {
        // Create a stack to store the digits
        string stack;
        
        // Iterate over the string
        for (char c : num) {
            // Remove the top of the stack if it's greater than the current digit and we can still remove digits
            while (k > 0 && !stack.empty() && stack.back() > c) {
                stack.pop_back();
                k--;
            }
            // Push the current digit to the stack
            stack.push_back(c);
        }
        
        // Remove the remaining digits if we still have removals left
        if (k > 0) {
            stack.resize(stack.size() - k);
        }
        
        // Remove leading zeros
        int start = 0;
        while (start < stack.size() && stack[start] == '0') {
            start++;
        }
        
        // Return the result
        return start == stack.size() ? "0" : stack.substr(start);
    }
};
```

## Test Cases
```
Input: num = "1432219", k = 3
Output: "1219"
Input: num = "10200", k = 1
Output: "2000"
Input: num = "10", k = 2
Output: "0"
```

## Key Takeaways
- Use a stack to keep track of the digits and remove the top of the stack if it's greater than the current digit.
- Remove the remaining digits if we still have removals left after iterating over the string.
- Remove leading zeros from the result.