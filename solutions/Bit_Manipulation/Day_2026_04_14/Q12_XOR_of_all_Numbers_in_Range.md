# XOR of all Numbers in Range

## Problem Statement
Given a range of integers from 0 to n, find the XOR of all numbers in this range. The range is inclusive, meaning it includes both 0 and n. For example, if n = 3, the XOR of all numbers in the range would be 0 ^ 1 ^ 2 ^ 3 = 4 (since 0 ^ 1 = 1, 1 ^ 2 = 3, and 3 ^ 3 = 0, but we made a mistake, the correct sequence is 0 ^ 1 = 1, 1 ^ 2 = 3, 3 ^ 3 = 2, so the correct answer is indeed 2, not 4, for n = 3, but for n = 4 the correct sequence is 0 ^ 1 = 1, 1 ^ 2 = 3, 3 ^ 3 = 2, 2 ^ 4 = 6, but we made another mistake, the correct answer for n = 4 is indeed 4, not 6, for n = 5 the correct sequence is 0 ^ 1 = 1, 1 ^ 2 = 3, 3 ^ 3 = 2, 2 ^ 4 = 6, 6 ^ 5 = 3, so the correct answer is indeed 1 for n = 5, and so on), but we can observe a pattern: for n = 0, the answer is 0, for n = 1, the answer is 1, for n = 2, the answer is 3, for n = 3, the answer is 0, and this pattern repeats every 4 numbers.

## Approach
The XOR operation has a pattern when applied to a range of numbers from 0 to n. By using this pattern, we can find the XOR of all numbers in the range in constant time. The pattern is based on the fact that the XOR of all numbers from 0 to n repeats every 4 numbers.

## Complexity
- Time: O(1)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

int findXOR(int n) {
    // If n is a multiple of 4, the XOR is 0 (since 0 ^ 1 ^ 2 ^ 3 = 0)
    if (n % 4 == 0) {
        return n;
    }
    // If n is 1 more than a multiple of 4, the XOR is 1 (since 0 ^ 1 = 1)
    else if (n % 4 == 1) {
        return 1;
    }
    // If n is 2 more than a multiple of 4, the XOR is 3 (since 0 ^ 1 ^ 2 = 3)
    else if (n % 4 == 2) {
        return n + 1;
    }
    // If n is 3 more than a multiple of 4, the XOR is 0 (since 0 ^ 1 ^ 2 ^ 3 = 0)
    else {
        return 0;
    }
}

int main() {
    int n;
    cin >> n;
    cout << findXOR(n) << endl;
    return 0;
}
```

## Test Cases
```
Input: 0
Output: 0
Input: 1
Output: 1
Input: 2
Output: 3
Input: 3
Output: 0
Input: 4
Output: 4
```

## Key Takeaways
- The XOR of all numbers in a range from 0 to n repeats every 4 numbers.
- We can use this pattern to find the XOR of all numbers in the range in constant time.
- The solution does not require iterating over all numbers in the range, making it efficient for large inputs.