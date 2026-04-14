# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The number will not contain leading zeros. You must remove exactly k digits. If the number is already smaller than the number of digits to remove, the function should return "0". For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000". If num = "10" and k = 2, the output should be "0".

## Approach
The approach is to use a stack to keep track of the digits. We iterate through the number and push each digit to the stack. If the stack is not empty and the top of the stack is greater than the current digit, we pop the stack until it's empty or the top of the stack is less than or equal to the current digit, or we have removed k digits. This ensures that the resulting number is the smallest possible.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    // Create an empty stack to store the digits
    stack<char> st;
    
    // Iterate through each digit in the number
    for (char c : num) {
        // While the stack is not empty, the top of the stack is greater than the current digit, and we have not removed k digits
        while (k > 0 && !st.empty() && st.top() > c) {
            // Remove the top of the stack
            st.pop();
            // Decrement k
            k--;
        }
        // Push the current digit to the stack
        st.push(c);
    }
    
    // If we still have digits to remove, remove them from the end of the stack
    while (k > 0 && !st.empty()) {
        st.pop();
        k--;
    }
    
    // Create a string to store the result
    string res = "";
    
    // While the stack is not empty
    while (!st.empty()) {
        // Append the top of the stack to the result
        res = st.top() + res;
        // Pop the stack
        st.pop();
    }
    
    // If the result is empty, return "0"
    if (res == "") return "0";
    
    // Find the index of the first non-zero digit
    int i = 0;
    while (i < res.size() && res[i] == '0') i++;
    
    // Return the result starting from the first non-zero digit
    return res.substr(i);
}

int main() {
    string num = "1432219";
    int k = 3;
    cout << removeKdigits(num, k) << endl;
    return 0;
}
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
- Be careful when handling edge cases, such as when the number is already smaller than the number of digits to remove.
- Use a string to store the result and find the index of the first non-zero digit to handle leading zeros.