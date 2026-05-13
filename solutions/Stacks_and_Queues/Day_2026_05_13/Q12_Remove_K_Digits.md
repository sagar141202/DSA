# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number will not contain leading zeros, and the length of the number will be between 1 and 100,000 digits. If the number becomes zero after removing k digits, return "0". For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
The algorithm uses a stack data structure to iterate through the digits of the number, removing the largest digits first to minimize the resulting number. It iterates through each digit in the number, comparing it to the top of the stack and removing the top of the stack if it's larger than the current digit and k is greater than 0.

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
        // Initialize an empty stack to store the digits
        stack<char> stk;
        
        // Iterate through each digit in the number
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current digit, and k is greater than 0
            while (!stk.empty() && stk.top() > c && k > 0) {
                // Remove the top of the stack and decrement k
                stk.pop();
                k--;
            }
            // Push the current digit onto the stack
            stk.push(c);
        }
        
        // If k is still greater than 0, remove the top k digits from the stack
        while (k > 0 && !stk.empty()) {
            stk.pop();
            k--;
        }
        
        // Initialize an empty string to store the result
        string res;
        
        // While the stack is not empty
        while (!stk.empty()) {
            // Append the top of the stack to the result and pop the stack
            res = stk.top() + res;
            stk.pop();
        }
        
        // If the result is empty, return "0"
        if (res.empty()) return "0";
        
        // Find the index of the first non-zero digit in the result
        int i = 0;
        while (i < res.size() && res[i] == '0') i++;
        
        // Return the result starting from the first non-zero digit
        return res.substr(i);
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
- Use a stack to efficiently remove the largest digits from the number.
- Iterate through each digit in the number, comparing it to the top of the stack and removing the top of the stack if it's larger than the current digit and k is greater than 0.
- After iterating through all digits, if k is still greater than 0, remove the top k digits from the stack.