# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n`, denoted as `n!`, is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is 120, which has one trailing zero. The constraints are `1 <= n <= 10^4`.

## Approach
The algorithm is based on the fact that trailing zeroes in a factorial are caused by the multiplication of 2 and 5. Since there are usually more factors of 2 than 5, we just need to count the number of factors of 5. We can do this by dividing `n` by powers of 5 and summing up the results.

## Complexity
- Time: O(log(n))
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        // Initialize count of trailing zeroes
        int count = 0;
        
        // Divide n by powers of 5 and sum up the results
        int i = 5;
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
Input: n = 5
Output: 1
Input: n = 10
Output: 2
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of factors of 5 in `n!`.
- We can count the number of factors of 5 by dividing `n` by powers of 5 and summing up the results.
- The time complexity of the solution is O(log(n)) due to the while loop that runs until `n` is no longer divisible by the current power of 5.