# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, find the k closest points to the origin (0, 0). The distance between two points on the X-Y plane is calculated using the Euclidean distance formula: √(x2 - x1)^2 + (y2 - y1)^2. Here, we can simplify the distance calculation to x^2 + y^2 since we are only comparing distances and do not need the actual distance values. The answer should be the k points with the smallest distance to the origin. If there are multiple answers, any of them is acceptable. Constraints: 1 <= k <= points.length <= 10^4, -10^4 < xi, yi < 10^4.

## Approach
We can use a priority queue to store points based on their distance from the origin. The priority queue will automatically keep track of the k closest points. Alternatively, we can use a sorting approach to sort all points by their distance and then return the first k points.

## Complexity
- Time: O(n log k) for the priority queue approach or O(n log n) for the sorting approach
- Space: O(k) for the priority queue approach or O(1) for the sorting approach (if sorting in-place)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Create a min-heap to store points
        priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, greater<pair<int, vector<int>>>> min_heap;
        
        // Calculate the distance for each point and push it into the min-heap
        for (auto point : points) {
            int distance = point[0] * point[0] + point[1] * point[1];
            min_heap.push({distance, point});
            
            // If the size of the min-heap exceeds k, pop the point with the largest distance
            if (min_heap.size() > k) {
                min_heap.pop();
            }
        }
        
        // Extract the k closest points from the min-heap
        vector<vector<int>> result;
        while (!min_heap.empty()) {
            result.push_back(min_heap.top().second);
            min_heap.pop();
        }
        
        return result;
    }
};
```

## Test Cases
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
```

## Key Takeaways
- The priority queue is a suitable data structure for this problem because it allows us to efficiently keep track of the k closest points.
- We can simplify the distance calculation by using the squared distance (x^2 + y^2) instead of the actual Euclidean distance (√(x^2 + y^2)), since we are only comparing distances.