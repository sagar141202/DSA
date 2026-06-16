# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to construct a new array such that for every i, the value at index i is either a multiple of i or a factor of i. The task is to find the count of all such possible arrays. The constraints are 1 ≤ N ≤ 15.

## Approach
The problem can be solved using recursion and backtracking. We can start by placing numbers from 1 to N in the array one by one and check if the current number is a multiple or factor of its index. If it is, we can recursively place the remaining numbers.

## Complexity
- Time: O(2^N)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countArrangement(int N) {
        vector<bool> visited(N + 1, false);
        int count = 0;
        backtrack(count, visited, 1, N);
        return count;
    }

    void backtrack(int& count, vector<bool>& visited, int index, int N) {
        if (index > N) {
            count++;
            return;
        }
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (i % index == 0 || index % i == 0)) {
                visited[i] = true;
                backtrack(count, visited, index + 1, N);
                visited[i] = false;
            }
        }
    }
};

int main() {
    Solution solution;
    cout << solution.countArrangement(2) << endl;  // Output: 2
    cout << solution.countArrangement(3) << endl;  // Output: 3
    return 0;
}
```

## Test Cases
```
Input: N = 2
Output: 2
Input: N = 3
Output: 3
```

## Key Takeaways
- The problem requires constructing an array where each element is either a multiple or factor of its index.
- Recursion and backtracking can be used to solve this problem by trying all possible combinations of numbers.
- The time complexity is exponential due to the recursive nature of the solution, while the space complexity is linear for storing the visited numbers.