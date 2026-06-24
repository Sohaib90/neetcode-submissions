class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mapSum;
        vector<int> res;
        for (int i = 0; i < nums.size(); i++){
            if (mapSum.find(target - nums[i]) != mapSum.end()){
                res.push_back(mapSum[target-nums[i]]); 
                res.push_back(i);
                return res;
            }
            else {
                mapSum.insert(pair<int, int>(nums[i], i));
            }
        }
    }
};
