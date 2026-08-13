# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are 1 <= k <= num.length <= 10000, and num does not contain any leading zero. For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
The algorithm uses a stack to store the digits of the number. It iterates over the number from left to right and pops the top of the stack if it is greater than the current digit and k is greater than 0. This ensures that the resulting number is the smallest possible.

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
        // Initialize an empty stack
        string stack;
        
        // Iterate over the number
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current digit, and k is greater than 0
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Pop the top of the stack
                stack.pop_back();
                // Decrement k
                k--;
            }
            // Push the current digit to the stack
            stack.push_back(c);
        }
        
        // If k is still greater than 0, remove the remaining top digits from the stack
        while (k > 0 && !stack.empty()) {
            stack.pop_back();
            k--;
        }
        
        // Remove leading zeros from the stack
        while (!stack.empty() && stack[0] == '0') {
            stack.erase(stack.begin());
        }
        
        // Return the resulting number
        return stack.empty() ? "0" : stack;
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
- Use a stack to store the digits of the number and iterate over the number from left to right.
- Pop the top of the stack if it is greater than the current digit and k is greater than 0.
- Remove leading zeros from the resulting number.