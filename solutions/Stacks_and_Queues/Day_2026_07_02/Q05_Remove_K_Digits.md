# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The length of num is at most 10004 digits and k is such that 0 ≤ k ≤ num.length. You must remove at least one digit if k is greater than 0. The resulting number should not have leading zeros.

## Approach
The problem can be solved using a stack data structure, where we iterate over the digits of the number and push them onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the top of the stack is greater than the current digit, we pop the top of the stack until it is less than or equal to the current digit or the stack is empty, or we have removed k digits.

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
        // Initialize an empty stack to store the result
        string stack;
        
        // Iterate over each character in the input string
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current character, and we have removals left
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Remove the top of the stack
                stack.pop_back();
                // Decrement the number of removals left
                k--;
            }
            // Push the current character onto the stack
            stack.push_back(c);
        }
        
        // If we still have removals left, remove the last k characters from the stack
        if (k > 0) {
            stack.resize(stack.size() - k);
        }
        
        // Find the first non-zero character in the stack (to remove leading zeros)
        int start = 0;
        while (start < stack.size() && stack[start] == '0') {
            start++;
        }
        
        // Return the result (or "0" if the stack is empty)
        return start == stack.size() ? "0" : string(stack.begin() + start, stack.end());
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
- We use a stack to efficiently remove digits from the number.
- We iterate over the digits of the number from left to right to ensure the resulting number is the smallest possible.
- We handle the case where the resulting number has leading zeros by finding the first non-zero character in the stack.