// solution 1 greedy algorithm.
// leetcode time     cost : 116 ms
// leetcode memory   cost : 27.7 MB 
// Time  Complexity: O(N)
// Space Complexity: O(1)
//#include <stdlib.h>
#include<bits\stdc++.h> 
struct VectorHash {
    size_t operator()(const std::pair<int, int>& v) const {
        std::hash<int> hasher;
        size_t seed = 0;

        seed ^= hasher(v.first) + hasher(v.second) + 0x9e3779b9 + (seed<<6) + (seed>>2);

        return seed;
    }
};
using namespace std; 
class Solution {
public:
    int robotSim(vector<int>& commands, vector<vector<int>>& obstacles) {
        int dx[4] = {0, 1, 0, -1};
        int dy[4] = {1, 0, -1, 0};
        int x = 0, y = 0, di = 0;
        //unordered_set<pair<int, int>,VectorHash> obstacleSet;     // error pair<int, int> doesn't  have hash function.
        unordered_set<pair<int, int>,VectorHash> obstacleSet;
        for (vector<int> obstacle: obstacles)
            obstacleSet.insert(make_pair(obstacle[0], obstacle[1]));

        int ans = 0;
        for (int cmd: commands) {
            if (cmd == -2)
                di = (di + 3) % 4;
            else if (cmd == -1)
                di = (di + 1) % 4;
            else {
                for (int k = 0; k < cmd; ++k) {
                    int nx = x + dx[di];
                    int ny = y + dy[di];
                    if (obstacleSet.find(make_pair(nx, ny)) == obstacleSet.end()) {
                        x = nx;
                        y = ny;
                        ans = max(ans, x*x + y*y);
                    }
                }
            }
        }
        return ans;
    }
};
int main(){
    vector<int> commands = {4,-1,4,-2,4};
    vector<vector<int>> obstacles = {{2,4}};
    Solution *Solution_obj = new Solution();
    int result = Solution_obj->robotSim(commands, obstacles);
	cout << "In cpp code,result value is " << result << '\n';
    return 0;
}