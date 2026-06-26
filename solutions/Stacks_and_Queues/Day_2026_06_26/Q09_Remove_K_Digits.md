# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number, and return the smallest possible integer. You can assume that the input num is a non-empty string, and k is a non-negative integer. Note that removing a digit from the number may change its original order, and you cannot remove more digits than the number of digits in num. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000". If num = "10" and k = 2, the output should be "0".

## Approach
The algorithm uses a stack to keep track of the digits in the number. It iterates through the number, and for each digit, it checks if the stack is not empty and the top of the stack is greater than the current digit. If this condition is met, it pops the stack until it is empty or the top of the stack is less than or equal to the current digit, or k becomes 0. Then, it pushes the current digit into the stack. Finally, it removes any remaining k digits from the end of the stack.

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
                // Pop the stack
                stk.pop();
                // Decrement k
                k--;
            }
            // Push the current digit into the stack
            stk.push(c);
        }
        
        // If k is still greater than 0, remove the remaining k digits from the end of the stack
        while (k > 0 && !stk.empty()) {
            stk.pop();
            k--;
        }
        
        // Initialize an empty string to store the result
        string res = "";
        
        // While the stack is not empty
        while (!stk.empty()) {
            // Pop the stack and append the digit to the result
            res = stk.top() + res;
            stk.pop();
        }
        
        // Remove leading zeros from the result
        while (res.size() > 1 && res[0] == '0') {
            res.erase(0, 1);
        }
        
        // Return the result
        return res.empty() ? "0" : res;
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
- Remove digits from the stack when a smaller digit is encountered and k is greater than 0.
- Remove any remaining k digits from the end of the stack after iterating through the number.