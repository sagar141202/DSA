# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10000, and num consists of only digits. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" which is "200" after removing leading zeros.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates over the string, pushing digits onto the stack if the stack is empty or the top of the stack is smaller than the current digit. If the top of the stack is larger than the current digit, it pops the stack until it is empty or the top of the stack is smaller than the current digit, or k becomes 0. This process ensures that the resulting number is the smallest possible.

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
        
        // Iterate over the string
        for (char c : num) {
            // While the stack is not empty, the top of the stack is larger than the current digit, and k is greater than 0
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Pop the stack
                stack.pop_back();
                // Decrement k
                k--;
            }
            // Push the current digit onto the stack
            stack.push_back(c);
        }
        
        // If k is still greater than 0, remove the last k digits from the stack
        if (k > 0) {
            stack.erase(stack.size() - k);
        }
        
        // Initialize the result
        string result;
        
        // Initialize a flag to track leading zeros
        bool leadingZero = true;
        
        // Iterate over the stack
        for (char c : stack) {
            // If the current digit is not zero or leadingZero is false
            if (c != '0' || !leadingZero) {
                // Append the current digit to the result
                result.push_back(c);
                // Set leadingZero to false
                leadingZero = false;
            }
        }
        
        // If the result is empty, return "0"
        if (result.empty()) {
            return "0";
        }
        
        // Return the result
        return result;
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
- Use a stack to keep track of the digits.
- Iterate over the string and push digits onto the stack if the stack is empty or the top of the stack is smaller than the current digit.
- Pop the stack if the top of the stack is larger than the current digit and k is greater than 0.