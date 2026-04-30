class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
         // create mapping of letter combo -> vector<string> anagrams
        // count letter freq of each string -> encode as string and compare against key
        unordered_map<string, vector<string>> anagrams;
        // avoid copying each string
        for (const string& s : strs) {
            vector<int> count(26);
            for (char c : s) {
                count[c - 'a']++;
            }
            string key = "";
            for (int freq : count) {
                key += to_string(freq) + "#";
            }

            anagrams[key].push_back(s);
        }

        vector<vector<string>> res;
        // structured bindings -> anagrams elements are pair<string, vector<string>> -> unpack as [key, group]
        for (auto& [key, group] : anagrams) {
            res.push_back(group);
        }
        return res;
    }
};
