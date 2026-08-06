# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number will not contain leading zeros after removal, and the removal should be done in a way that the resulting number is the smallest possible. For example, if num = "1432219" and k = 3, the output should be "1219". The constraints are 1 <= num.length <= 10^5, num consists of only digits, and 0 <= k <= num.length - 1.

## Approach
The algorithm uses a stack to keep track of the digits. It iterates over the string, pushing digits to the stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the top of the stack is greater than the current digit and we can still remove digits, it pops the top of the stack. This process ensures that the resulting number is the smallest possible.

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
            // While the stack is not empty, the top of the stack is greater than the current character, and we can still remove digits
            while (k > 0 && !stack.empty() && stack.back() > c) {
                // Remove the top of the stack
                stack.pop_back();
                // Decrement the number of digits to remove
                k--;
            }
            // Push the current character to the stack
            stack.push_back(c);
        }
        
        // If we still have digits to remove, remove them from the end of the stack
        if (k > 0) {
            stack.erase(stack.size() - k);
        }
        
        // Find the first non-zero digit in the stack
        int start = 0;
        while (start < stack.size() && stack[start] == '0') {
            start++;
        }
        
        // Return the resulting string
        return start == stack.size() ? "0" : stack.substr(start);
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
- Use a stack to keep track of the digits and remove digits from the top of the stack when possible.
- Handle the case where we still have digits to remove after iterating over the entire string.
- Remove leading zeros from the resulting string.