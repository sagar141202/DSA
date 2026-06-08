# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10^5, and num consists of only digits. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000", or "2" and "0200" are also acceptable.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates through the string, pushing digits onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the top of the stack is greater than the current digit, it pops the stack until it's empty or the top is less than or equal to the current digit, or k becomes 0. This process ensures the resulting number is the smallest possible.

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
        
        // Iterate through each digit in the number
        for (char c : num) {
            // While the stack is not empty, k is greater than 0, and the top of the stack is greater than the current digit
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Pop the top of the stack
                stack.pop_back();
                // Decrement k
                k--;
            }
            // Push the current digit onto the stack
            stack.push_back(c);
        }
        
        // If k is still greater than 0, remove the last k digits from the stack
        if (k > 0) {
            stack.erase(stack.end() - k, stack.end());
        }
        
        // Initialize the result string
        string result;
        
        // Initialize a flag to track if we've encountered a non-zero digit
        bool nonZeroEncountered = false;
        
        // Iterate through each digit in the stack
        for (char c : stack) {
            // If the digit is not zero or we've encountered a non-zero digit
            if (c != '0' || nonZeroEncountered) {
                // Append the digit to the result string
                result.push_back(c);
                // Set the flag to true
                nonZeroEncountered = true;
            }
        }
        
        // If the result string is empty, return "0"
        if (result.empty()) {
            return "0";
        }
        
        // Return the result string
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
- Use a stack to keep track of the digits and remove k digits to get the smallest possible number.
- Iterate through the string and push digits onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit.
- Remove the last k digits from the stack if k is still greater than 0 after iterating through the string.