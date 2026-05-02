# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, find the k points that are closest to the origin. The distance of a point from the origin is calculated using the Euclidean distance formula: √(x^2 + y^2). If there are multiple points with the same distance, the points are considered to be in any order. The constraints are 1 <= k <= points.length <= 10^4 and -10^4 <= xi, yi <= 10^4.

## Approach
This problem can be solved using a priority queue where the priority is the Euclidean distance of the point from the origin. We can store the k closest points in the priority queue. The algorithm will iterate through all points, calculate their distances, and push them into the priority queue.

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

struct Comparator {
    bool operator()(const Point& p1, const Point& p2) {
        int dist1 = p1.x * p1.x + p1.y * p1.y;
        int dist2 = p2.x * p2.x + p2.y * p2.y;
        return dist1 > dist2;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, Comparator> pq;
    for (auto& point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        if (pq.size() < k) {
            pq.push(p);
        } else {
            int dist = p.x * p.x + p.y * p.y;
            int maxDist = pq.top().x * pq.top().x + pq.top().y * pq.top().y;
            if (dist < maxDist) {
                pq.pop();
                pq.push(p);
            }
        }
    }
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
- Use a priority queue to store the k closest points.
- Calculate the Euclidean distance for each point and use it as the priority in the priority queue.
- If the priority queue is not full, push all points into it. If it's full, only push points with a smaller distance than the point with the maximum distance in the queue.