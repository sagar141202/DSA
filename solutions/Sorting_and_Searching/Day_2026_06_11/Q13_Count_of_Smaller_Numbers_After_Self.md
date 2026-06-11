# Count of Smaller Numbers After Self

## Problem Statement
You are given an integer array `nums`, and you need to find the count of smaller numbers after self for each element in the array. The count of smaller numbers after self for an element at index `i` is the number of elements in the array to the right of `i` (i.e., `nums[i+1:]`) that are smaller than `nums[i]`. The function should return an array of counts, where the count at index `i` is the count of smaller numbers after self for the element at index `i` in the input array. For example, given the input `[5, 2, 6, 1]`, the output should be `[2, 1, 1, 0]`.

## Approach
The approach is to use a Binary Indexed Tree (BIT) to keep track of the count of smaller numbers. We first create a sorted array of unique elements from the input array, and then for each element in the input array, we find its rank in the sorted array and update the BIT accordingly.

## Complexity
- Time: O(n log n)
- Space: O(n)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class BIT {
public:
    vector<int> tree;
    int n;
    BIT(int n) : n(n), tree(n + 1, 0) {}

    void update(int i, int val) {
        while (i <= n) {
            tree[i] += val;
            i += i & -i;
        }
    }

    int query(int i) {
        int sum = 0;
        while (i > 0) {
            sum += tree[i];
            i -= i & -i;
        }
        return sum;
    }
};

vector<int> countSmaller(vector<int>& nums) {
    vector<int> sortedNums = nums;
    sort(sortedNums.begin(), sortedNums.end());
    map<int, int> ranks;
    int rank = 1;
    for (int num : sortedNums) {
        if (ranks.find(num) == ranks.end()) {
            ranks[num] = rank++;
        }
    }

    int n = nums.size();
    vector<int> result(n);
    BIT bit(n);
    for (int i = n - 1; i >= 0; i--) {
        result[i] = bit.query(ranks[nums[i]] - 1);
        bit.update(ranks[nums[i]], 1);
    }
    return result;
}

int main() {
    vector<int> nums = {5, 2, 6, 1};
    vector<int> result = countSmaller(nums);
    for (int num : result) {
        cout << num << " ";
    }
    return 0;
}
```

## Test Cases
```
Input: [5, 2, 6, 1]
Output: [2, 1, 1, 0]
```

## Key Takeaways
- We use a Binary Indexed Tree to efficiently update and query the count of smaller numbers.
- We create a sorted array of unique elements to find the rank of each element in the input array.
- We iterate over the input array from right to left to ensure that we only consider elements to the right of each element when counting smaller numbers.