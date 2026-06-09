# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given integer n. The factorial of a number n, denoted by n!, is the product of all positive integers less than or equal to n. A trailing zero is a zero that appears at the end of the number. For example, the factorial of 5 (5! = 120) has one trailing zero. The input will be an integer n, and the output should be the number of trailing zeroes in n!. The constraints are 1 ≤ n ≤ 10^4.

## Approach
The algorithm is based on the fact that a trailing zero is created by a pair of 2 and 5 in the prime factorization of the numbers in the factorial. Since there are usually more factors of 2 than 5, we just need to count the number of factors of 5.

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
        // count the number of factors of 5
        while (n >= 5) {
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
```

## Key Takeaways
- To find the number of trailing zeroes in n!, count the number of factors of 5 in all the numbers from 1 to n.
- Use a while loop to divide the input number by powers of 5 and add the result to the count.
- The time complexity is O(log n) because we are dividing the input number by 5 in each iteration.