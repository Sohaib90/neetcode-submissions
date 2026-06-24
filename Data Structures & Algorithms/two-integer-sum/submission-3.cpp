class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> mapSum;
        for (int i = 0; i < nums.size(); i++){
            if (mapSum.find(target - nums[i]) != mapSum.end()){
                return {mapSum[target-nums[i]], i};
            }
            else {
                mapSum.insert({nums[i], i});
            }
        }
    }
};
