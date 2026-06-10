# Pow(x,n)

## Problem Statement
Implement the pow(x, n) function, where x is a floating point number and n is an integer. The function should return the value of x raised to the power of n. The input range is -100.0 < x < 100.0 and -2^31 <= n <= 2^31 - 1. For example, pow(2.0, 3) = 8, pow(2.1, 3) = 9.261, and pow(2.0, -3) = 0.125.

## Approach
The solution uses the concept of exponentiation by squaring to reduce the time complexity. This approach takes advantage of the fact that x^(2n) = (x^2)^n and x^(2n+1) = x * (x^2)^n. The algorithm recursively calculates the power by squaring the base and reducing the exponent by half.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

double myPow(double x, int n) {
    // handle edge case where n is negative
    if (n < 0) {
        x = 1 / x;
        n = -n;
    }
    // base case where n is 0
    if (n == 0) {
        return 1;
    }
    // recursive case
    if (n % 2 == 0) {
        return myPow(x * x, n / 2);
    } else {
        return x * myPow(x * x, n / 2);
    }
}

int main() {
    cout << myPow(2.0, 3) << endl;  // output: 8
    cout << myPow(2.1, 3) << endl;  // output: 9.261
    cout << myPow(2.0, -3) << endl; // output: 0.125
    return 0;
}
```

## Test Cases
```
Input: x = 2.0, n = 3
Output: 8.0
Input: x = 2.1, n = 3
Output: 9.261
Input: x = 2.0, n = -3
Output: 0.125
```

## Key Takeaways
- The key to solving this problem efficiently is to use the concept of exponentiation by squaring.
- Handling the edge case where n is negative is crucial to ensure the function works correctly for all possible inputs.
- The recursive approach allows for a clean and efficient implementation of the exponentiation by squaring algorithm.