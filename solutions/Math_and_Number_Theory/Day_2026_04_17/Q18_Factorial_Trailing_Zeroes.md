# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given integer n. The factorial of a number n, denoted by n!, is the product of all positive integers less than or equal to n. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is 120, which has one trailing zero. The input integer n will be in the range 0 to 10^5.

## Approach
The approach to solve this problem is to use the concept of prime factorization, specifically the number of factors of 5 in the factorial of a number, as a trailing zero is formed by a factor of 2 and a factor of 5. We will count the number of factors of 5 in n! to find the number of trailing zeroes.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        // count the number of factors of 5 in n!
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
};
```

## Test Cases
```
Input: 5
Output: 1
Input: 10
Output: 2
Input: 25
Output: 6
```

## Key Takeaways
- The number of trailing zeroes in n! is determined by the number of factors of 5 in n!, as there are usually more factors of 2 than 5.
- We use a while loop to count the number of factors of 5 in n!, dividing n by 5 in each iteration and adding the result to the count.
- This solution has a time complexity of O(log n) due to the while loop, and a space complexity of O(1) as it uses a constant amount of space.