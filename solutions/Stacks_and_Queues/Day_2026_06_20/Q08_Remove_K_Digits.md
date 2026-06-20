# Remove K Digits

## Problem Statement
Given a non-empty string num representing a non-negative integer, and a positive integer k, remove k digits from num to form the smallest possible integer. The string num will not contain leading zeros except for the number zero itself. The length of num will be between 1 and 10^5. k will be between 1 and the length of num.

## Approach
The algorithm uses a stack-based approach to remove k digits from the input string. It iterates over the string, pushing characters onto the stack if they are smaller than the top of the stack or if the stack is empty. If the stack is not empty and the top of the stack is greater than the current character, it pops the stack until it finds a smaller character or the stack is empty, or until it has removed k digits.

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
        stack<char> st;
        
        // Iterate over the input string
        for (char c : num) {
            // While the stack is not empty, the top of the stack is greater than the current character, and k is greater than 0
            while (!st.empty() && st.top() > c && k > 0) {
                // Pop the stack
                st.pop();
                // Decrement k
                k--;
            }
            // Push the current character onto the stack
            st.push(c);
        }
        
        // If k is still greater than 0, pop the stack k times
        while (k > 0 && !st.empty()) {
            st.pop();
            k--;
        }
        
        // Initialize an empty string to store the result
        string result;
        
        // While the stack is not empty
        while (!st.empty()) {
            // Pop the stack and append the character to the result string
            result = st.top() + result;
            st.pop();
        }
        
        // If the result string is empty, return "0"
        if (result.empty()) return "0";
        
        // Find the first non-zero character in the result string
        int i = 0;
        while (i < result.size() && result[i] == '0') i++;
        
        // Return the result string starting from the first non-zero character
        return result.substr(i);
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
- Use a stack-based approach to remove k digits from the input string.
- Iterate over the input string and push characters onto the stack if they are smaller than the top of the stack or if the stack is empty.
- Pop the stack until it finds a smaller character or the stack is empty, or until it has removed k digits.