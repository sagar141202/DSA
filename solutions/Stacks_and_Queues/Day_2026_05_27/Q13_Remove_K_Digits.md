# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number will not contain leading zeros after removal, and the removal of zeros is counted in the total count of k digits removed. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" (note that a leading zero is not allowed). The constraints are 1 <= num.length <= 100000 and 0 <= k <= num.length - 1.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates over the number from left to right, pushing digits onto the stack if they are smaller than or equal to the top of the stack, or if the stack is empty. If the stack is not empty and the top of the stack is greater than the current digit, it pops the stack until it finds a smaller digit or the stack is empty, or until it has removed k digits. The remaining digits in the stack are the result.

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
        // Create a stack to store the digits
        string stack;
        
        // Iterate over the number
        for (char c : num) {
            // While the stack is not empty and the top of the stack is greater than the current digit
            // and we have not removed k digits yet, pop the stack
            while (k > 0 && !stack.empty() && stack.back() > c) {
                stack.pop_back();
                k--;
            }
            // Push the current digit onto the stack
            stack.push_back(c);
        }
        
        // If we have not removed k digits yet, remove the remaining digits from the end of the stack
        if (k > 0) {
            stack.resize(stack.size() - k);
        }
        
        // Remove leading zeros from the stack
        while (!stack.empty() && stack[0] == '0') {
            stack.erase(stack.begin());
        }
        
        // Return the result
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
- Use a stack to keep track of the digits.
- Remove digits from the stack if they are greater than the current digit and we have not removed k digits yet.
- Remove leading zeros from the result.