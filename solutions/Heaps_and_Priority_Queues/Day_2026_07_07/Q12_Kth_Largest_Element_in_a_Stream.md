# Kth Largest Element in a Stream

## Problem Statement
Design a class to find the Kth largest element in a stream of numbers. The class should have a constructor that takes an integer k as input, and a method add that takes an integer num as input and returns the Kth largest element in the stream so far. If the stream has less than k elements, return the largest element in the stream. For example, if k = 3, the stream is [4, 5, 8, 2], the Kth largest element is 4.

## Approach
We can use a min-heap to store the k largest elements in the stream. When a new number is added to the stream, we check if the heap has less than k elements or if the new number is larger than the smallest element in the heap. If so, we add the new number to the heap and remove the smallest element if the heap has more than k elements.

## Complexity
- Time: O(logk) for the add method
- Space: O(k) for the min-heap

## C++ Solution
```cpp
#include <queue>
using namespace std;

class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k) : k(k) {}

    int add(int num) {
        if (minHeap.size() < k) {
            minHeap.push(num);
        } else if (num > minHeap.top()) {
            minHeap.pop();
            minHeap.push(num);
        }
        return minHeap.size() < k ? minHeap.size() > 0 ? minHeap.top() : -1 : minHeap.top();
    }
};
```

## Test Cases
```
Input: KthLargest kthLargest(3);
kthLargest.add(4); // returns 4
kthLargest.add(5); // returns 5
kthLargest.add(8); // returns 5
kthLargest.add(2); // returns 4
```

## Key Takeaways
- Use a min-heap to store the k largest elements in the stream.
- The add method has a time complexity of O(logk) due to the heap operations.
- The space complexity is O(k) for the min-heap.