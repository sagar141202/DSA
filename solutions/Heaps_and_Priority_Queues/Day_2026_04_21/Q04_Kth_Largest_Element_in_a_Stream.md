# Kth Largest Element in a Stream

## Problem Statement
Given an integer k and a stream of integers, design a data structure to find the kth largest element in the stream. The stream can be thought of as an unbounded array of integers, and the data structure should be able to efficiently handle the addition of new integers to the stream and query the kth largest element at any point in time. The integers in the stream are not necessarily distinct.

## Approach
We can use a min-heap data structure to solve this problem. The min-heap will store the k largest elements seen so far in the stream. When a new integer is added to the stream, we check if the heap has less than k elements. If it does, we add the new integer to the heap. If the heap already has k elements, we compare the new integer with the smallest element in the heap (the root of the min-heap). If the new integer is larger, we remove the smallest element from the heap and add the new integer.

## Complexity
- Time: O(log k) for adding a new integer to the stream and O(1) for querying the kth largest element
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
Input: k = 3, nums = [4, 5, 8, 2], val = 3
Output: 4
Input: k = 1, nums = [0], val = -1
Output: -1
```

## Key Takeaways
- Use a min-heap to store the k largest elements seen so far in the stream.
- When adding a new integer to the stream, compare it with the smallest element in the heap and update the heap accordingly.
- The kth largest element can be queried in O(1) time by returning the root of the min-heap.