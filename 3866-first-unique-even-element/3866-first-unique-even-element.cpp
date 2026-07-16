class Solution {
public:
    int firstUniqueEven(vector<int>& nums) {
         
         
           vector<int>ans,a;
        
          unordered_map<int ,int>mp;
          for(int x : nums){
            mp[x]++;
          }
          for(auto it : mp){
            if(it.second==1){
                ans.push_back(it.first);
            }
          }
          for(int x : ans){
            if(x%2==0){
                a.push_back(x);
            }
          }
          int s=INT_MAX;
          for(int i=0; i<a.size(); i++){
            for(int j=0; j<nums.size(); j++){
                if(a[i]==nums[j])
                s=min(s,j);
            }
             
          }
          return  s==INT_MAX ? -1 : nums[s];
    }
};