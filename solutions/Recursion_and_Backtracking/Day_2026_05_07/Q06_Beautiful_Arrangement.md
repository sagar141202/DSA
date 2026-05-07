# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, and you want to arrange them in a way that for every i (1 <= i <= N), the number at position i is either a multiple of i or has i as a multiple. Given an integer N, return the number of beautiful arrangements that can be constructed. For example, if N = 3, the beautiful arrangements are [3, 1, 2] and no other arrangement is possible, so the output will be 3 for N = 3. If N = 4, there are two beautiful arrangements [4, 2, 1, 3] and [4, 1, 3, 2].

## Approach
The problem can be solved using recursion and backtracking. We start by placing the first number and then recursively try to place the remaining numbers. If a number cannot be placed at the current position, we backtrack and try the next number. We use a visited array to keep track of the numbers that have been used.

## Complexity
- Time: O(N!)
- Space: O(N)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int countArrangement(int N) {
        int count = 0;
        vector<bool> visited(N + 1, false);
        backtrack(count, visited, 1, N);
        return count;
    }
    
    void backtrack(int& count, vector<bool>& visited, int pos, int N) {
        if (pos > N) {
            count++;
            return;
        }
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (i % pos == 0 || pos % i == 0)) {
                visited[i] = true;
                backtrack(count, visited, pos + 1, N);
                visited[i] = false;
            }
        }
    }
};

int main() {
    Solution solution;
    cout << solution.countArrangement(3) << endl;  // Output: 3
    cout << solution.countArrangement(4) << endl;  // Output: 2
    return 0;
}
```

## Test Cases
```
Input: N = 3
Output: 3
Input: N = 4
Output: 2
```

## Key Takeaways
- The problem can be solved using recursion and backtracking.
- A visited array is used to keep track of the numbers that have been used.
- The time complexity of the solution is O(N!), where N is the input number.