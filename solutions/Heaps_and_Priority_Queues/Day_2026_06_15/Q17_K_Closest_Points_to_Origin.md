# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). If two points have the same distance to the origin, their order in the result does not matter. The input array will have at least one point, and k will be between 1 and the number of points.

## Approach
We can use a priority queue to store the points along with their distances from the origin. The priority queue will automatically order the points based on their distances. We then pop the k closest points from the priority queue and add them to our result.

## Complexity
- Time: O(N log k)
- Space: O(k)

## C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Point {
    int x, y;
};

struct Compare {
    bool operator()(const Point& a, const Point& b) {
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    // Create a priority queue to store the points
    priority_queue<Point, vector<Point>, Compare> pq;
    
    // Add all points to the priority queue
    for (auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        pq.push(p);
    }
    
    // Create a result vector to store the k closest points
    vector<vector<int>> result;
    
    // Pop the k closest points from the priority queue and add them to the result
    for (int i = 0; i < k; i++) {
        Point p = pq.top();
        pq.pop();
        result.push_back({p.x, p.y});
    }
    
    return result;
}
```

## Test Cases
```
Input: points = [[1, 3], [-2, 2]], k = 1
Output: [[-2, 2]]
Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
```

## Key Takeaways
- We can use a priority queue to efficiently find the k closest points to the origin.
- The time complexity is O(N log k) because we are pushing N points into the priority queue, and each push operation takes O(log k) time.
- The space complexity is O(k) because we are storing the k closest points in the result vector.