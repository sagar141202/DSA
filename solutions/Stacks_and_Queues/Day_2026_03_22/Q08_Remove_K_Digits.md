# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10000, and num does not contain any leading zeros. For example, if num = "1432219" and k = 3, the output should be "1219".

## Approach
We will use a stack to keep track of the digits in the resulting number. We iterate over each digit in the input number and pop the stack if the top of the stack is greater than the current digit and we can still remove digits. This ensures that the resulting number is the smallest possible.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

string removeKdigits(string num, int k) {
    stack<char> st;
    for (char c : num) {
        // if the stack is not empty, the top of the stack is greater than the current digit, and we can still remove digits
        while (k > 0 && !st.empty() && st.top() > c) {
            st.pop();
            k--;
        }
        st.push(c);
    }
    // if we still have digits to remove, remove them from the end of the stack
    while (k > 0) {
        st.pop();
        k--;
    }
    // build the resulting string
    string result;
    while (!st.empty()) {
        result = st.top() + result;
        st.pop();
    }
    // remove leading zeros
    while (result.size() > 1 && result[0] == '0') {
        result.erase(0, 1);
    }
    return result.empty() ? "0" : result;
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
- Use a stack to keep track of the digits in the resulting number.
- Iterate over each digit in the input number and pop the stack if the top of the stack is greater than the current digit and we can still remove digits.
- Remove leading zeros from the resulting string.