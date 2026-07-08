# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number. The factorial of a number n (denoted as n!) is the product of all positive integers less than or equal to n. A trailing zero is a zero at the end of the number. For example, the factorial of 5 (5! = 120) has one trailing zero. The input will be a single integer, and the output should be the count of trailing zeroes in its factorial. The constraint is that the input number can range from 1 to 10^4.

## Approach
The algorithm involves counting the number of factors of 5 in the factorial, as each trailing zero is a result of 2 * 5, and there are usually more factors of 2 than 5. We will iterate through the numbers from 1 to the input number, counting the factors of 5.

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
- We use a while loop to count the factors of 5, starting from 5 and multiplying by 5 in each iteration to account for numbers like 25, 125, etc.
- The time complexity is O(log n) due to the while loop, which runs until n / i is less than 1.