# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream at any point in time. The data structure should support the following operations:
- `KthLargest(int k, int[] nums)`: Initializes the data structure with an integer `k` and a stream of integers `nums`.
- `add(int val)`: Adds a new integer `val` to the stream and returns the `k`th largest element in the stream.
The constraint is that `1 <= k <= 10^4` and `1 <= nums.length <= 10^5`.

## Approach
We can use a min-heap data structure to solve this problem efficiently. The min-heap will store the `k` largest elements seen so far. When a new element is added to the stream, we check if the heap has less than `k` elements. If it does, we add the new element to the heap. If the heap already has `k` elements and the new element is larger than the smallest element in the heap, we remove the smallest element from the heap and add the new element.

## Complexity
- Time: O(log k) for the `add` operation
- Space: O(k) for storing the min-heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k, vector<int>& nums) : k(k) {
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
Input: k = 3, nums = [4, 5, 8, 2]
Output: [4, 5, 5, 8]
```

## Key Takeaways
- Use a min-heap data structure to efficiently find the `k`th largest element in a stream of integers.
- The min-heap should store the `k` largest elements seen so far.
- When a new element is added to the stream, check if the heap has less than `k` elements or if the new element is larger than the smallest element in the heap.