# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number. The factorial of a number n, denoted as n!, is the product of all positive integers less than or equal to n. A trailing zero is a zero at the end of the number. For example, the factorial of 5 (5! = 120) has 1 trailing zero. The input will be a single integer, and the output will be the count of trailing zeroes in its factorial. The constraint is that the input number will be in the range from 1 to 10^4.

## Approach
The approach to solve this problem is based on the fact that trailing zeroes in a factorial are caused by the multiplication of 2 and 5. Since there are usually more factors of 2 than 5 in a factorial, we just need to count the factors of 5. We will use a loop to divide the input number by powers of 5 and sum up the quotients.

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
        long long i = 5;
        while (n / i >= 1) {
            count += n / i;
            i *= 5;
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
- The number of trailing zeroes in n! is determined by the number of factors of 5 in all the numbers from 1 to n.
- We can calculate this by dividing n by powers of 5 and summing up the quotients.
- This approach has a time complexity of O(log n) because we are dividing n by powers of 5 in each iteration.