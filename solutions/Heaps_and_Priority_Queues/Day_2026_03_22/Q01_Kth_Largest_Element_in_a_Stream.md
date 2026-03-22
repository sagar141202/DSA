# Kth Largest Element in a Stream

## Problem Statement
Given an integer `k` and a stream of integers, design a data structure to find the `k`-th largest element in the stream. The stream can contain duplicate integers, and you need to find the `k`-th largest element after each new integer is added to the stream. The integers in the stream can be positive or negative, and `k` is a positive integer.

## Approach
We can use a min-heap to store the `k` largest elements seen so far. When a new integer is added to the stream, we check if the heap has less than `k` elements or if the new integer is larger than the smallest element in the heap. If so, we add the new integer to the heap and remove the smallest element if the heap has more than `k` elements.

## Complexity
- Time: O(log k) for adding a new integer to the stream
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
Input: KthLargest kthLargest(3, [4, 5, 8, 2]); 
       kthLargest.add(3);   
       kthLargest.add(5);   
       kthLargest.add(10); 
       kthLargest.add(9);   
       kthLargest.add(4);
Output: 4, 5, 5, 8, 8
```

## Key Takeaways
- We use a min-heap to store the `k` largest elements seen so far.
- The time complexity for adding a new integer to the stream is O(log k) due to the heap operations.
- The space complexity is O(k) for storing the min-heap.