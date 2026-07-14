# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `kth` largest element in the stream. The stream can be a continuous flow of integers, and at any point, you should be able to return the `kth` largest element seen so far. The integers in the stream can be positive, negative, or zero, and there can be duplicates. The value of `k` is a positive integer.

## Approach
We can use a min-heap data structure to keep track of the `k` largest elements seen so far. The min-heap will store the `k` largest elements, and whenever a new element is added to the stream, we check if it's larger than the smallest element in the heap. If it is, we remove the smallest element and add the new one.

## Complexity
- Time: O(log k) for adding an element to the stream and finding the kth largest element
- Space: O(k) for storing the k largest elements in the min-heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    priority_queue<int, vector<int>, greater<int>> minHeap;
    int k;

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
Input: KthLargest kthLargest(3, [4, 5, 8, 2]);
Output: 
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

## Key Takeaways
- Use a min-heap to store the k largest elements seen so far.
- When adding a new element to the stream, check if it's larger than the smallest element in the heap.
- If the new element is larger, remove the smallest element and add the new one to maintain a size of k in the heap.