# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number will not contain leading zeros, except for the number zero itself. The length of num is at most 10004 digits. You must remove exactly k digits. Return the smallest possible number after removing k digits. For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
We will use a stack-based approach to solve this problem. The idea is to iterate over the digits of the number and push them onto a stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the stack is not empty and the top of the stack is greater than the current digit, we will pop the stack until it is empty or the top of the stack is less than or equal to the current digit, or we have removed k digits.

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
        // Create an empty stack to store the digits
        string stack;
        
        // Iterate over each digit in the number
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current digit, and we have not removed k digits
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Pop the stack
                stack.pop_back();
                // Decrement k
                k--;
            }
            // Push the current digit onto the stack
            stack.push_back(c);
        }
        
        // If we have not removed k digits, remove the remaining digits from the end of the stack
        while (k > 0 && !stack.empty()) {
            stack.pop_back();
            k--;
        }
        
        // Remove leading zeros from the stack
        while (!stack.empty() && stack[0] == '0') {
            stack.erase(stack.begin());
        }
        
        // If the stack is empty, return "0"
        if (stack.empty()) {
            return "0";
        }
        
        // Return the stack as a string
        return stack;
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
- Use a stack to keep track of the digits in the number.
- Remove digits from the stack if they are greater than the current digit and we have not removed k digits.
- Remove leading zeros from the stack before returning the result.