# Factorial Trailing Zeroes

## Problem Statement
The problem statement is to find the number of trailing zeroes in the factorial of a given number. The factorial of a number n, denoted by n!, is the product of all positive integers less than or equal to n. A trailing zero is a zero at the end of the number. For example, the factorial of 5 is 120, which has one trailing zero. The input is a single integer n, and the output is the number of trailing zeroes in n!. The constraint is that n is a non-negative integer.

## Approach
The algorithm to solve this problem is based on the concept that a trailing zero is formed by a pair of 2 and 5 in the prime factorization of the factorial. Since there are more factors of 2 than 5, we only need to count the number of factors of 5. We can use a loop to count the number of factors of 5 in the factorial of the given number.

## Complexity
- Time: O(log n)
- Space: O(1)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

// function to calculate the number of trailing zeroes in n!
int findTrailingZeroes(int n) {
    int count = 0;
    int i = 5;
    while (n / i >= 1) {
        count += n / i;
        i *= 5;
    }
    return count;
}

int main() {
    int n;
    cin >> n;
    cout << findTrailingZeroes(n) << endl;
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
- The number of trailing zeroes in n! is determined by the number of factors of 5 in the prime factorization of n!.
- We can use a loop to count the number of factors of 5 in the factorial of the given number.
- The time complexity of the solution is O(log n) because we are using a while loop that runs until n / i is less than 1, where i is multiplied by 5 in each iteration.