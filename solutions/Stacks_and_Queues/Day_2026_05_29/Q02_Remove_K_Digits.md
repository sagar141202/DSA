# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number of digits to remove is given by k. For example, if num = "1432219" and k = 3, the output should be "1219". The constraints are 1 <= num.length <= 10^5 and 0 <= k <= num.length.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates through the number from left to right, pushing digits onto the stack if they are smaller than the top of the stack or if the stack is empty. If the stack is not empty and the top of the stack is larger than the current digit, it pops the top of the stack until it finds a smaller digit or the stack is empty, or until it has removed k digits.

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
        
        // Iterate through the number
        for (char c : num) {
            // While the stack is not empty, the top of the stack is larger than the current digit, and we have not removed k digits
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Remove the top of the stack
                stack.pop_back();
                // Decrement k
                k--;
            }
            // Push the current digit onto the stack
            stack.push_back(c);
        }
        
        // If we still have not removed k digits, remove the last k digits from the stack
        if (k > 0) {
            stack.resize(stack.size() - k);
        }
        
        // Remove leading zeros
        while (!stack.empty() && stack[0] == '0') {
            stack.erase(stack.begin());
        }
        
        // If the stack is empty, return "0"
        if (stack.empty()) {
            return "0";
        }
        
        // Return the resulting number as a string
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
- Use a stack to keep track of the digits and remove larger digits when a smaller digit is encountered.
- Be careful with edge cases such as leading zeros and removing more digits than necessary.
- The algorithm has a time complexity of O(n) and a space complexity of O(n), where n is the number of digits in the input number.