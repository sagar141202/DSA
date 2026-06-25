# Kth Largest Element in a Stream

## Problem Statement
Given an unsorted array of integers `nums` and an integer `k`, find the `k`th largest element in the array. The array is a stream of integers, and we need to find the `k`th largest element at each step. The constraints are: `1 <= k <= nums.size()` and `nums` contains distinct integers.

## Approach
We can use a min-heap to store the `k` largest elements seen so far. At each step, we push the new element into the heap and pop the smallest element if the heap size exceeds `k`. The top element of the heap will be the `k`th largest element.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        if (minHeap.size() < k) {
            minHeap.push(val);
        } else if (val > minHeap.top()) {
            minHeap.pop();
            minHeap.push(val);
        }
        return minHeap.top();
    }
};
```

## Test Cases
```
Input: nums = [4, 5, 8, 2], k = 3
Output: [4, 5, 4, 2]
```

## Key Takeaways
- Use a min-heap to store the `k` largest elements seen so far.
- At each step, push the new element into the heap and pop the smallest element if the heap size exceeds `k`.
- The top element of the heap will be the `k`th largest element.