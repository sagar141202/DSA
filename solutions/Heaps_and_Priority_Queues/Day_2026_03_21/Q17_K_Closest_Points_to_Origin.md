# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin. The distance between two points (x1, y1) and (x2, y2) is calculated using the Euclidean distance formula: √((x2 - x1)^2 + (y2 - y1)^2). The answer can be returned in any order. 

## Approach
We will utilize a priority queue to store points based on their Euclidean distance from the origin. The priority queue will automatically order points based on their distance, with the closest points at the top. We then extract the k closest points from the queue.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        // Create a priority queue to store points based on their distance from the origin
        priority_queue<pair<int, vector<int>>, vector<pair<int, vector<int>>>, greater<pair<int, vector<int>>>> pq;
        
        // Iterate over each point
        for (auto point : points) {
            // Calculate the Euclidean distance of the point from the origin
            int distance = point[0] * point[0] + point[1] * point[1];
            
            // Push the point into the priority queue
            pq.push({distance, point});
            
            // If the size of the queue exceeds k, pop the point with the largest distance
            if (pq.size() > k) {
                pq.pop();
            }
        }
        
        // Extract the k closest points from the queue
        vector<vector<int>> result;
        while (!pq.empty()) {
            result.push_back(pq.top().second);
            pq.pop();
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
- Utilize a priority queue to efficiently order points based on their distance from the origin.
- The priority queue automatically handles the ordering, simplifying the extraction of the k closest points.
- The time complexity is O(n log k) due to the insertion and removal of points from the priority queue.