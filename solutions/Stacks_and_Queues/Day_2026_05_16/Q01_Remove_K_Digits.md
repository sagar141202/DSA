# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The length of num is at most 10004 digits and k is at most the length of num. Return the resulting number after removing k digits. Note that the number may have leading zeros, but the result should not have leading zeros unless the result is zero.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates through the number from left to right, pushing digits onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the stack is not empty and the top of the stack is greater than the current digit, it pops the stack until it is empty or the top of the stack is less than or equal to the current digit, or it has popped k digits. This ensures that the resulting number is the smallest possible.

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
        stack<char> s;
        
        // Iterate through the number
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current digit, and we have not removed k digits
            while (k > 0 && !s.empty() && s.top() > c) {
                // Pop the stack
                s.pop();
                // Decrement k
                k--;
            }
            // Push the current digit onto the stack
            s.push(c);
        }
        
        // If we have not removed k digits, remove the remaining digits from the end of the stack
        while (k > 0 && !s.empty()) {
            s.pop();
            k--;
        }
        
        // Initialize an empty string to store the result
        string result;
        
        // While the stack is not empty
        while (!s.empty()) {
            // Pop the stack and append the digit to the result
            result = s.top() + result;
            s.pop();
        }
        
        // Remove leading zeros from the result
        int start = 0;
        while (start < result.size() && result[start] == '0') {
            start++;
        }
        
        // Return the result
        return start == result.size() ? "0" : result.substr(start);
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
- Use a stack to keep track of the digits and remove the largest digits first to get the smallest possible number.
- Remove leading zeros from the result unless the result is zero.
- Handle edge cases where the input number is empty or k is greater than the length of the number.