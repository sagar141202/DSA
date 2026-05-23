# Pow(x,n)

## Problem Statement
Implement the pow(x, n) function, which calculates the value of x raised to the power of n. The function should handle both positive and negative values of x and n. The input values of x and n are integers, and the output should also be an integer. For example, pow(2.0, 3) should return 8.0, and pow(2.1, 3) should return 9.261. The function should also handle the case where n is 0, in which case the function should return 1.0.

## Approach
We can solve this problem using a recursive approach with a time complexity of O(log n) by dividing the problem into two sub-problems of size n/2. We will handle the cases where n is even and odd separately.

## Complexity
- Time: O(log n)
- Space: O(log n)

## C++ Solution
```cpp
class Solution {
public:
    double myPow(double x, int n) {
        // Handle the case where n is negative
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        
        // Initialize the result
        double res = 1;
        
        // Calculate the power using a loop
        while (n > 0) {
            // If n is odd, multiply the result by x
            if (n % 2 == 1) {
                res *= x;
            }
            
            // Divide n by 2 and square x
            n /= 2;
            x *= x;
        }
        
        return res;
    }
};
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
- We can solve the problem using a recursive approach with a time complexity of O(log n) by dividing the problem into two sub-problems of size n/2.
- We need to handle the cases where n is even and odd separately to calculate the power correctly.
- We can also use a loop to calculate the power instead of using recursion.