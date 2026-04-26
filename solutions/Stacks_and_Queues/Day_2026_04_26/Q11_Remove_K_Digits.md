# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number may have leading zeros. You must remove exactly k digits. Return the smallest possible number after removing k digits. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" or "0200" which is "2000" after removing leading zeros. If num = "10" and k = 2, the output should be "0".

## Approach
The approach is to use a stack to keep track of the digits. We iterate over the string and push each digit to the stack. If the stack is not empty and the top of the stack is greater than the current digit, we pop the stack until it's empty or the top of the stack is not greater than the current digit. We repeat this process until we have removed k digits. Finally, we join the stack into a string and remove any leading zeros.

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
        
        // Iterate over each character in the string
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current character, and k is greater than 0
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Pop the stack
                stack.pop_back();
                // Decrement k
                k--;
            }
            // Push the current character to the stack
            stack.push_back(c);
        }
        
        // If k is still greater than 0, remove the last k characters from the stack
        if (k > 0) {
            stack.erase(stack.size() - k);
        }
        
        // Find the first non-zero character in the stack
        int start = 0;
        while (start < stack.size() && stack[start] == '0') {
            start++;
        }
        
        // Return the stack as a string, starting from the first non-zero character
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
- Use a stack to keep track of the digits.
- Remove digits from the stack that are greater than the current digit.
- Handle the case where k is still greater than 0 after iterating over the string.
- Remove leading zeros from the final result.