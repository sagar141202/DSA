# Pow(x,n)

## Problem Statement
Implement a function `pow(x, n)` that calculates the value of `x` raised to the power of `n`, where `x` is a floating-point number and `n` is an integer. The function should handle cases where `n` is negative, zero, or positive. If `x` is zero and `n` is negative, the function should return an error or a special value indicating that the result is undefined.

## Approach
The solution uses the concept of exponentiation by squaring to achieve efficient computation. This involves recursively dividing the problem into smaller sub-problems and solving them only when necessary. The base cases are when `n` is zero or `x` is one.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
#include <iostream>
using namespace std;

double myPow(double x, int n) {
    // handle edge case
    if (x == 0 && n < 0) {
        throw runtime_error("Cannot divide by zero");
    }

    // base case
    if (n == 0) {
        return 1;
    }

    // recursive case with negative n
    if (n < 0) {
        return 1 / myPow(x, -n);
    }

    // recursive case with even n
    if (n % 2 == 0) {
        double halfPow = myPow(x, n / 2);
        return halfPow * halfPow;
    }

    // recursive case with odd n
    double halfPow = myPow(x, n / 2);
    return x * halfPow * halfPow;
}

int main() {
    double x = 2.0;
    int n = 3;
    try {
        double result = myPow(x, n);
        cout << "Result: " << result << endl;
    } catch (const exception& e) {
        cerr << "Error: " << e.what() << endl;
    }
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
- Use exponentiation by squaring for efficient computation of `x` raised to the power of `n`.
- Handle edge cases such as `x` being zero and `n` being negative.
- Use recursive approach to divide the problem into smaller sub-problems and solve them only when necessary.