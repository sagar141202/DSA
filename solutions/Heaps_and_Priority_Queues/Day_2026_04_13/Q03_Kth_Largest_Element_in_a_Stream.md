# Kth Largest Element in a Stream

## Problem Statement
Given an unbounded stream of integers, find the kth largest element from the stream at any given time. The stream can be thought of as a sequence of integers that are generated on the fly, and we need to maintain a data structure that can efficiently report the kth largest element seen so far. The constraints are that we can only process the stream one integer at a time, and we need to be able to report the kth largest element in O(log n) time. For example, if the stream is [4, 5, 8, 2], and k = 2, then after processing the first two integers, the 2nd largest element is 4. After processing the first three integers, the 2nd largest element is 5, and so on.

## Approach
We will use a min-heap data structure to solve this problem, where the heap stores the k largest elements seen so far. We will maintain the heap such that the smallest element in the heap is always at the root, and the heap size is at most k. When a new integer is processed, we will check if the heap is not full, and if it is not, we will add the new integer to the heap. If the heap is full and the new integer is larger than the smallest element in the heap, we will remove the smallest element and add the new integer to the heap.

## Complexity
- Time: O(log k) for adding a new integer to the heap, where k is the number of largest elements to track
- Space: O(k) for storing the k largest elements in the heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
public:
    priority_queue<int, vector<int>, greater<int>> min_heap;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }

    int add(int val) {
        if (min_heap.size() < k) {
            min_heap.push(val);
        } else if (val > min_heap.top()) {
            min_heap.pop();
            min_heap.push(val);
        }
        return min_heap.top();
    }
};
```

## Test Cases
```
Input: KthLargest kthLargest(3, [4, 5, 8, 2]);
Output: kthLargest.add(3); // returns 4
        kthLargest.add(5); // returns 5
        kthLargest.add(10); // returns 5
        kthLargest.add(9); // returns 8
        kthLargest.add(4); // returns 8
```

## Key Takeaways
- Using a min-heap to track the k largest elements seen so far allows for efficient reporting of the kth largest element in O(log k) time.
- The min-heap size is at most k, which ensures that the space complexity is O(k).
- The add method checks if the heap is not full before adding a new integer, and if the heap is full, it checks if the new integer is larger than the smallest element in the heap before removing and adding.