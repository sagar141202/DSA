# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number will not contain any leading zeros after removal. Note that the input number may have leading zeros. For example, if the input is "10200" and k = 1, the output will be "0200" after removing the first '1', but since we cannot have leading zeros in the result, the actual output will be "200". If k = 2, then the output will be "00" after removing '1' and '2'. However, the output should be "0" as the number cannot have leading zeros.

## Approach
The approach involves using a stack to keep track of the digits. We iterate over the number from left to right, pushing digits to the stack if the stack is empty or the current digit is larger than or equal to the top of the stack. If the stack is not empty and the current digit is smaller than the top of the stack, we pop the top of the stack until it is empty or the current digit is larger than or equal to the top of the stack, or we have removed k digits. This process ensures that the resulting number is the smallest possible.

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
        // Create an empty stack
        string stack;
        
        // Iterate over each character in the number
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current character, and we can still remove digits
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Remove the top of the stack
                stack.pop_back();
                // Decrement the count of digits to remove
                k--;
            }
            // Push the current character to the stack
            stack.push_back(c);
        }
        
        // If we still have digits to remove, remove them from the end of the stack
        if (k > 0) {
            stack.resize(stack.size() - k);
        }
        
        // Find the first non-zero character in the stack
        int start = 0;
        while (start < stack.size() && stack[start] == '0') {
            start++;
        }
        
        // Return the result
        return start == stack.size() ? "0" : stack.substr(start);
    }
};
```

## Test Cases
```
Input: num = "1432219", k = 3
Output: "1219"
Input: num = "10200", k = 1
Output: "200"
Input: num = "10", k = 2
Output: "0"
```

## Key Takeaways
- Use a stack to keep track of the digits and remove the larger digits first to get the smallest possible number.
- Handle the case where the number of digits to remove is more than the number of digits in the stack.
- Handle the case where the resulting number has leading zeros.