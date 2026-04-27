# Factorial Trailing Zeroes

## Problem Statement
The problem requires finding the number of trailing zeroes in the factorial of a given number `n`. The factorial of a number `n`, denoted as `n!`, is the product of all positive integers less than or equal to `n`. A trailing zero is a zero at the end of the number. For example, `5! = 120` has one trailing zero. The input `n` is a positive integer, and the output should be the count of trailing zeroes in `n!`. The constraint is `1 <= n <= 10^4`.

## Approach
The algorithm uses the concept of prime factorization to count the trailing zeroes. Since a trailing zero is formed by a pair of 2 and 5, we count the number of 5's in the prime factorization of all numbers up to `n`. This is because there are usually more 2's than 5's in the factorization.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int trailingZeroes(int n) {
        int count = 0;
        while (n > 0) {
            n /= 5;
            count += n;
        }
        return count;
    }
};

int main() {
    Solution solution;
    int n;
    cin >> n;
    cout << solution.trailingZeroes(n) << endl;
    return 0;
}
```

## Test Cases
```
Input: 5
Output: 1
Input: 10
Output: 2
```

## Key Takeaways
- The number of trailing zeroes in `n!` is determined by the number of 5's in the prime factorization of all numbers up to `n`.
- We use a while loop to divide `n` by 5 and add the result to the count, effectively counting the number of 5's in the factorization.
- The time complexity is O(log n) because we divide `n` by 5 in each iteration, reducing the size of `n` logarithmically.