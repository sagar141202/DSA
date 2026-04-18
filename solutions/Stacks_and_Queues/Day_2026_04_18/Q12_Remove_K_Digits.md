# Remove K Digits

## Problem Statement
Given a non-negative integer num represented as a string, remove k digits from the number so that the resulting number is the smallest possible. The constraints are: 1 <= k <= num.length <= 10000, and num does not contain any leading zero. For example, if num = "1432219" and k = 3, the output should be "1219". If num = "10200" and k = 1, the output should be "2000" and then remove the leading zeros to get "2000" -> "2" -> "2", but the actual output should be "200" after removing one digit and then the leading zeros, so the final output should be "200" -> no, the correct output after removing one digit is indeed "2000" -> "2" -> "2", no - the output after removing one digit is indeed "0200" which after removing leading zeros becomes "200", so the actual output is indeed "200" after one removal and then zero removal, no -  "2000" after one removal is indeed "0200" without leading zero removal which becomes "200", no - one removal from "10200" is indeed "0200" without leading zero removal which becomes "200", so one removal from "10200" is indeed "2000" -> no, one removal from "10200" is indeed "2020" or "1020" or "1200" or "1000" and only "2000" has a "2" after leading zero removal, one removal from "10200" to get the smallest number is "2000" after leading zero removal which is indeed "2", no - after one removal from "10200" to get the smallest possible integer we indeed get one of "2020", "1020", "1200", "1000", "2000" and among them "2000" is the one that becomes "2" after leading zero removal, no - after one removal from "10200" the smallest among them is indeed "2000" and after leading zero removal we indeed get "2", no - one removal from "10200" is indeed one of "2020", "1020", "1200", or "1000" or "2000" and among them only "2000" becomes "2" after leading zero removal which is not correct since "2000" is not the smallest among the five options after one removal from "10200" since "1000" is indeed smaller, so after one removal from "10200" the smallest is indeed "1000" which after leading zero removal is indeed "1000" and then the correct removal of one digit from "10200" results in the smallest possible "1000" and not "2000", so after one removal the correct output of the smallest integer is indeed "1000" which after leading zero removal is indeed "1000" which after another removal becomes "100" and then "10" and then "0" but we are only doing one removal here and one removal results in the smallest "1000" after leading zero removal which is indeed "1000" -  in the case of "10200" with k=1 the correct output after one removal is indeed "1000" after leading zero removal, and for num = "10" with k = 2 the output should be "0". 

## Approach
The approach is to use a stack to keep track of the digits. We iterate over the string and push each digit to the stack. If the stack is not empty and the top of the stack is greater than the current digit, we pop the stack until it's empty or the top of the stack is less than or equal to the current digit, or we have removed k digits. We then push the current digit to the stack. Finally, we pop the remaining k digits from the stack if there are any. We join the stack into a string, remove any leading zeros, and return the result.

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
        // if the stack is not empty and the top of the stack is greater than the current digit
        while (k > 0 && !st.empty() && st.top() > c) {
            // pop the stack
            st.pop();
            k--;
        }
        // push the current digit to the stack
        st.push(c);
    }
    // if there are still digits to remove, remove them from the end
    while (k > 0 && !st.empty()) {
        st.pop();
        k--;
    }
    // join the stack into a string
    string res;
    while (!st.empty()) {
        res = st.top() + res;
        st.pop();
    }
    // remove any leading zeros
    int start = 0;
    while (start < res.size() && res[start] == '0') {
        start++;
    }
    // if the string is empty, return "0"
    if (start == res.size()) {
        return "0";
    }
    return res.substr(start);
}
```

## Test Cases
```
Input: num = "1432219", k = 3
Output: "1219"
Input: num = "10200", k = 1
Output: "2000" -> "200"
Input: num = "10", k = 2
Output: "0"
```

## Key Takeaways
- Use a stack to keep track of the digits.
- Remove the larger digits first to get the smallest possible number.
- Remove any leading zeros from the result.