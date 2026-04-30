# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are 1 <= k <= num.length <= 10000, and num does not contain any leading zero. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" (or "2" if the output is allowed to have leading zeros, but in this case, it's not).

## Approach
The algorithm uses a stack to keep track of the digits. It iterates over the string, pushing digits onto the stack if the stack is empty or the top of the stack is less than or equal to the current digit. If the stack is not empty and the top of the stack is greater than the current digit, it pops the stack until it's empty or the top of the stack is less than or equal to the current digit, or until it has removed k digits.

## Complexity
- Time: O(n)
- Space: O(n)

## C++ Solution
```cpp
#include <string>
using namespace std;

string removeKdigits(string num, int k) {
    string res;
    for (char c : num) {
        while (k > 0 && !res.empty() && res.back() > c) {
            k--;
            res.pop_back();
        }
        res.push_back(c);
    }
    // remove remaining k digits from the end
    while (k > 0) {
        res.pop_back();
        k--;
    }
    // remove leading zeros
    while (!res.empty() && res[0] == '0') {
        res.erase(res.begin());
    }
    return res.empty() ? "0" : res;
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
- Use a stack to keep track of the digits and remove k digits to get the smallest possible number.
- Remove leading zeros from the result.
- Handle edge cases, such as when the input number is "0" or when k is equal to the length of the input number.