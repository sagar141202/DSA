# K Closest Points to Origin

## Problem Statement
Given an array of points where points[i] = [xi, yi] represents a point on a 2D plane, find the k closest points to the origin (0, 0). The distance of a point from the origin is calculated using the Euclidean distance formula: √(x^2 + y^2). Return the k closest points. You can return the answer in any order. The input array will have at least one point, and the number of points will not exceed 10^4. The value of k will be in the range [1, 10^4].

## Approach
We can use a priority queue to store the points along with their Euclidean distances from the origin. The priority queue will be ordered based on the distance. We then pop the k smallest elements from the queue to get the k closest points.

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
        int distA = a.x * a.x + a.y * a.y;
        int distB = b.x * b.x + b.y * b.y;
        return distA > distB;
    }
};

vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
    priority_queue<Point, vector<Point>, compare> pq;
    
    for (auto point : points) {
        Point p;
        p.x = point[0];
        p.y = point[1];
        pq.push(p);
        
        if (pq.size() > k) {
            pq.pop();
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
```

## Key Takeaways
- Use a priority queue to efficiently find the k smallest elements.
- The Euclidean distance formula is used to calculate the distance of each point from the origin.
- The priority queue is ordered based on the distance, allowing for efficient retrieval of the k closest points.