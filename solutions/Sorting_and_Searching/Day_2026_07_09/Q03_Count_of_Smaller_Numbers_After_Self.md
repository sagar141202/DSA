# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. This means that for each element at index `i`, you need to find the number of elements at indices `j` where `j > i` and `nums[j] < nums[i]`. The function should return an array of these counts. The input array will have a length between 1 and 20000, and the elements will be between 0 and 10^4. For example, if the input array is `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`, because for the first element `5`, there are two elements after it that are smaller (`2` and `1`).

## Approach
We can use a Binary Indexed Tree (BIT) to solve this problem efficiently. The BIT will store the cumulative count of elements seen so far. We iterate through the array from right to left, and for each element, we query the BIT to find the count of smaller elements.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class BinaryIndexedTree {
public:
    vector<int> tree;
    int size;

    BinaryIndexedTree(int size) {
        this->size = size;
        tree.resize(size + 1, 0);
    }

    void update(int index, int value) {
        while (index <= size) {
            tree[index] += value;
            index += index & -index;
        }
    }

    int query(int index) {
        int sum = 0;
        while (index > 0) {
            sum += tree[index];
            index -= index & -index;
        }
        return sum;
    }
};

vector<int> countSmaller(vector<int>& nums) {
    vector<int> ranks(nums.begin(), nums.end());
    sort(ranks.begin(), ranks.end());
    unordered_map<int, int> rankMap;
    for (int i = 0; i < ranks.size(); i++) {
        rankMap[ranks[i]] = i + 1;
    }

    BinaryIndexedTree bit(ranks.size());
    vector<int> result(nums.size(), 0);
    for (int i = nums.size() - 1; i >= 0; i--) {
        result[i] = bit.query(rankMap[nums[i]] - 1);
        bit.update(rankMap[nums[i]], 1);
    }
    return result;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
Input: [1, 2, 3, 4]
Output: [0, 0, 0, 0]
```

## Key Takeaways
- The Binary Indexed Tree is a powerful data structure for range sum queries and updates.
- The time complexity of the solution is O(n log n) due to the sorting and BIT operations.
- The space complexity of the solution is O(n) for storing the BIT and the rank map.