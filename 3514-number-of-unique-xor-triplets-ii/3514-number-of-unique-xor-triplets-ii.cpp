class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        unordered_set<int> pair_xor;

        int n = nums.size();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                pair_xor.insert(nums[i] ^ nums[j]);
            }
        }

        unordered_set<int> ans;

        for (int x : pair_xor) {
            for (int num : nums) {
                ans.insert(x ^ num);
            }
        }

        return ans.size();
    }
};