# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`th largest element in the stream at any given time. The stream can be thought of as a sequence of integers that are generated one by one. You can assume that the integers are non-negative and that `k` is less than or equal to the number of elements in the stream. For example, if the stream is `[4, 5, 8, 2]` and `k = 3`, the `k`th largest element is `4`.

## Approach
Use a min-heap to store the `k` largest elements seen so far. When a new element is added to the stream, check if the heap has less than `k` elements. If it does, add the new element to the heap. If the heap already has `k` elements, check if the new element is larger than the smallest element in the heap. If it is, remove the smallest element and add the new element.

## Complexity
- Time: O(log k) for adding an element to the stream, O(1) for finding the kth largest element
- Space: O(k) for storing the min-heap

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
Input: KthLargest kthLargest(3, [4, 5, 8, 2]);
       kthLargest.add(3);
       kthLargest.add(5);
       kthLargest.add(10);
       kthLargest.add(9);
       kthLargest.add(4);
Output: 4, 5, 5, 8, 8
```

## Key Takeaways
- Use a min-heap to efficiently store the k largest elements in the stream.
- The add operation has a time complexity of O(log k) due to the heap operations.
- The space complexity is O(k) for storing the min-heap.