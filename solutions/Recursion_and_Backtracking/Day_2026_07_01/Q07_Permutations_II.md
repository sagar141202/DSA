# Permutations II

## Problem Statement
Given a collection of numbers that might contain duplicates, return all possible unique permutations. The input collection is given as an array of integers, and the output should be a list of lists, where each sublist is a unique permutation of the input array. For example, given the input [1, 1, 2], the output should be [[1, 1, 2], [1, 2, 1], [2, 1, 1]]. The length of the input array will not exceed 10, and the array will only contain integers.

## Approach
The approach to solve this problem is to use a recursive backtracking algorithm, sorting the input array first to handle duplicates, and then swapping each element in the array with the remaining elements to generate all permutations. The algorithm will skip duplicates to ensure uniqueness of the permutations.

## Complexity
- Time: O(N! / (k1! * k2! * ... * km!)) where N is the length of the input array, and k1, k2, ..., km are the frequencies of each distinct element in the array.
- Space: O(N) for the recursion stack.

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
    for (auto& perm : result) {
        for (auto& num : perm) {
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
- Use backtracking to generate all permutations of the input array.
- Sort the input array to handle duplicates and ensure uniqueness of the permutations.
- Skip duplicates by checking if the current element is the same as the previous one, to avoid duplicate permutations.