# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is not sorted, and the output should not contain duplicate permutations. For example, if the input is `[1, 1, 2]`, the output should be `[[1, 1, 2], [1, 2, 1], [2, 1, 1]]`. The numbers in the input collection are in the range `[1, 100]`, and the length of the input collection is in the range `[1, 100]`.

## Approach
The solution uses recursion and backtracking to generate all permutations. It sorts the input array to handle duplicates and skips the same elements to avoid duplicate permutations. The base case for recursion is when the index reaches the end of the array.

## Complexity
- Time: O(N! / (K1! * K2! * ... * Km!)) where N is the length of the input array, and K1, K2, ..., Km are the frequencies of each distinct element
- Space: O(N) for the recursion stack

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

void backtrack(vector<int>& nums, int start, vector<vector<int>>& result) {
    if (start == nums.size()) {
        result.push_back(nums);
        return;
    }
    for (int i = start; i < nums.size(); i++) {
        // Skip duplicates
        if (i > start && nums[i] == nums[start]) continue;
        swap(nums[start], nums[i]);
        backtrack(nums, start + 1, result);
        swap(nums[start], nums[i]);
    }
}

vector<vector<int>> permuteUnique(vector<int>& nums) {
    vector<vector<int>> result;
    sort(nums.begin(), nums.end());
    backtrack(nums, 0, result);
    return result;
}

int main() {
    vector<int> nums = {1, 1, 2};
    vector<vector<int>> result = permuteUnique(nums);
    for (auto& vec : result) {
        for (auto& num : vec) {
            cout << num << " ";
        }
        cout << endl;
    }
    return 0;
}
```

## Test Cases
```
Input: [1, 1, 2]
Output: 
1 1 2 
1 2 1 
2 1 1 
```

## Key Takeaways
- Sorting the input array helps to handle duplicates by grouping the same elements together.
- Skipping the same elements in the recursion loop avoids generating duplicate permutations.
- The recursion and backtracking approach allows generating all permutations of the input array.