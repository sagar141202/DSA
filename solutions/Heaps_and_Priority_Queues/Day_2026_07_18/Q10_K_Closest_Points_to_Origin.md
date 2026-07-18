# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2 - x1)^2 + (y2 - y1)^2). If two points have the same distance to the origin, their order in the result does not matter. Return the k closest points.

## Approach
We can use a priority queue to store the points along with their distances from the origin. The priority queue will automatically order the points based on their distances. We then pop the k closest points from the priority queue to get our result.

## Complexity
- Time: O(n log k)
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
        return (a.x * a.x + a.y * a.y) > (b.x * b.x + b.y * b.y);
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Compare> pq;
    
    for (auto point : points) {
        pq.push({point[0], point[1]});
        
        if (pq.size() > k) {
            pq.pop();
        }
    }
    
    vector<vector<int>> result;
    while (!pq.empty()) {
        result.push_back({pq.top().x, pq.top().y});
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
- Using a priority queue can simplify the problem by automatically ordering the points based on their distances from the origin.
- The time complexity is O(n log k) because we are pushing and popping elements from the priority queue n times, and each push and pop operation takes O(log k) time.
- The space complexity is O(k) because we are storing at most k points in the priority queue.