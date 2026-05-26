# Kth Largest Element in a Stream

## Problem Statement
Given an unsorted array of integers `nums` and an integer `k`, find the `k`th largest element in the array. The array can be very large and does not fit into memory, so we need to process it as a stream. We can only use a limited amount of extra memory. The input array is a stream of integers, and we need to find the `k`th largest element at each step.

## Approach
We can use a min-heap to keep track of the `k` largest elements seen so far. We iterate over the stream of integers, and for each integer, we check if the heap has less than `k` elements. If it does, we push the integer into the heap. If the heap already has `k` elements, we check if the current integer is larger than the smallest element in the heap. If it is, we replace the smallest element with the current integer.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <queue>
#include <vector>

class KthLargest {
public:
    // Initialize the data structure with the given k
    KthLargest(int k, std::vector<int>& nums) : k_(k) {
        // Create a min-heap
        for (int num : nums) {
            add(num);
        }
    }

    // Add a new integer to the data structure
    void add(int val) {
        // If the heap has less than k elements, push the integer into the heap
        if (heap_.size() < k_) {
            heap_.push(val);
        } 
        // If the heap already has k elements and the current integer is larger than the smallest element in the heap
        else if (val > heap_.top()) {
            // Replace the smallest element with the current integer
            heap_.pop();
            heap_.push(val);
        }
    }

    // Return the kth largest element
    int getKthLargest() {
        // The kth largest element is the smallest element in the heap
        return heap_.top();
    }

private:
    int k_;
    std::priority_queue<int, std::vector<int>, std::greater<int>> heap_;
};
```

## Test Cases
```
Input: nums = [4, 5, 8, 2], k = 3
Output: 4
```

## Key Takeaways
- We use a min-heap to keep track of the k largest elements seen so far.
- We iterate over the stream of integers and update the heap accordingly.
- The time complexity is O(n log k) and the space complexity is O(k).