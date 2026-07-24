# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number. The factorial of a number n, denoted by n!, is the product of all positive integers less than or equal to n. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is 120, which has one trailing zero. The problem statement is to write a function that takes an integer n as input and returns the number of trailing zeroes in n!. The input range is 1 <= n <= 10^4.

## Approach
The approach is to use the concept of prime factorization to find the number of trailing zeroes. Since a trailing zero is formed by a pair of 2 and 5, we need to count the number of 5's in the prime factorization of n!. This is because there are usually more 2's than 5's in the factorization.

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
        // count the number of 5's in the prime factorization of n!
        while (i <= n) {
            count += n / i;
            i *= 5;
        }
        return count;
    }
};

// example usage
int main() {
    Solution solution;
    cout << solution.trailingZeroes(5) << endl;  // output: 1
    cout << solution.trailingZeroes(10) << endl;  // output: 2
    return 0;
}
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
- The number of trailing zeroes in n! is determined by the number of 5's in the prime factorization of n!.
- We can use a loop to count the number of 5's by dividing n by powers of 5.
- The time complexity of the solution is O(log n) because the loop runs until i exceeds n, and i grows exponentially.