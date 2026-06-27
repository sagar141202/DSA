# Beautiful Arrangement

## Problem Statement
Suppose you have N integers from 1 to N, we need to find the number of possible arrangements of these integers such that for every i, the ith integer is either divisible by i or i is divisible by the ith integer. We will be given an integer N and we need to return the number of possible arrangements.

## Approach
The problem can be solved using recursion and backtracking. We can start by placing the first integer, then recursively try to place the remaining integers. If at any point we find that it's not possible to place an integer, we backtrack and try a different placement.

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
        vector<bool> visited(N + 1, false);
        int count = 0;
        backtrack(1, N, visited, count);
        return count;
    }
    
    void backtrack(int index, int N, vector<bool>& visited, int& count) {
        if (index == N + 1) {
            count++;
            return;
        }
        
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (i % index == 0 || index % i == 0)) {
                visited[i] = true;
                backtrack(index + 1, N, visited, count);
                visited[i] = false;
            }
        }
    }
};

int main() {
    Solution solution;
    int N = 3;
    cout << solution.countArrangement(N) << endl;
    return 0;
}
```

## Test Cases
```
Input: N = 3
Output: 3
Explanation: The possible arrangements are:
[1, 2, 3]
[2, 1, 3]
[3, 1, 2]
```

## Key Takeaways
- Use recursion and backtracking to solve the problem.
- Keep track of the visited integers to avoid duplicates.
- Use a helper function to perform the backtracking.