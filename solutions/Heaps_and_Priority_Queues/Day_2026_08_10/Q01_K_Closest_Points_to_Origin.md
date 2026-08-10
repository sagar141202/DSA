# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance between two points (x1, y1) and (x2, y2) is calculated as sqrt((x2-x1)^2 + (y2-y1)^2). If two points have the same distance to the origin, their order does not matter. Return the k closest points. You may return the answer in any order. The number of points, n, will be in the range [1, 10^4], and k will be in the range [1, n]. 

## Approach
We can use a priority queue to store the points based on their distance from the origin. The priority queue will automatically order the points based on their distance, with the closest point at the top. We can then pop the top k points from the queue to get the k closest points.

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

struct compare {
    bool operator()(const Point& a, const Point& b) {
        // calculate distance from origin for each point
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        
        // if distances are equal, return false (equal elements are considered equal)
        // if distance of a is greater than distance of b, return true (a will be placed after b in the priority queue)
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, compare> pq;
    
    // push all points into the priority queue
    for (auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        pq.push(p);
        
        // if size of priority queue exceeds k, pop the top element (farthest point)
        if (pq.size() > k) {
            pq.pop();
        }
    }
    
    // create result vector
    vector<vector<int>> result;
    while (!pq.empty()) {
        Point p = pq.top();
        pq.pop();
        result.push_back({p.x, p.y});
    }
    
    return result;
}
```

## Test Cases
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
```

## Key Takeaways
- The priority queue automatically orders elements based on a comparison function, making it ideal for this problem.
- The comparison function calculates the distance of each point from the origin and orders them accordingly.
- The time complexity is O(n log k) because we are pushing and popping elements from the priority queue n times, and each push and pop operation takes O(log k) time.