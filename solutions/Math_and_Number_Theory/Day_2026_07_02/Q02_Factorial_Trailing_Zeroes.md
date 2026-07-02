# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number. The factorial of a number n, denoted by n!, is the product of all positive integers less than or equal to n. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is 120, which has 1 trailing zero. The input is a single integer n, and the output is the number of trailing zeroes in n!. The constraint is 1 ≤ n ≤ 10^4.

## Approach
The algorithm is based on the fact that trailing zeroes are created by the product of 2 and 5. Since there are more factors of 2 than 5 in a factorial, we only need to count the factors of 5. We use a loop to count the factors of 5 in n!.

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
        // count the factors of 5
        while (n >= 5) {
            count += n / 5;
            n /= 5;
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
- The number of trailing zeroes in n! is determined by the number of factors of 5 in n!.
- We can use a loop to count the factors of 5 in n! by dividing n by powers of 5.
- The time complexity of the solution is O(log n) because we are dividing n by 5 in each iteration.