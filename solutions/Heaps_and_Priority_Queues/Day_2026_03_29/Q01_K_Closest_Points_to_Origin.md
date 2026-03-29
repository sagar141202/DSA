# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). Return the k closest points. You may return the answer in any order. The number of points is at least 1 and k is at least 1. 1 <= k <= number of points <= 10^4. -10^4 < xi, yi < 10^4.

## Approach
Use a priority queue to store points based on their distance from the origin. The priority queue will automatically keep track of the k closest points. We can use a lambda function as the comparator for the priority queue to calculate the distance of each point from the origin.

## Complexity
- Time: O(n log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // Create a priority queue to store points
    priority_queue<pair<int, vector<int>>> pq;
    
    // Iterate over each point
    for (auto point : points) {
        // Calculate the distance from the origin
        int distance = point[0] * point[0] + point[1] * point[1];
        
        // Push the point into the priority queue
        pq.push({distance, point});
        
        // If the size of the priority queue exceeds k, pop the point with the largest distance
        if (pq.size() > k) {
            pq.pop();
        }
    }
    
    // Create a result vector to store the k closest points
    vector<vector<int>> result;
    
    // Pop all points from the priority queue and push them into the result vector
    while (!pq.empty()) {
        result.push_back(pq.top().second);
        pq.pop();
    }
    
    return result;
}
```

## Test Cases
```
Input: points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
```

## Key Takeaways
- Use a priority queue to efficiently keep track of the k closest points.
- Calculate the distance from the origin using the formula sqrt((x2 - x1)^2 + (y2 - y1)^2), but since we are comparing distances, we can skip the sqrt operation.
- Use a lambda function as the comparator for the priority queue to calculate the distance of each point from the origin.