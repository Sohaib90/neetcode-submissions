class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()){
            return false;
        }

        map<char, int> checkCount;
        for (char& alphabet: s){
            if (checkCount.count(alphabet)){
                checkCount[alphabet]++;
            }
            else checkCount.insert(pair<char, int>(alphabet, 1));
        }

        for (char& alphabet: t){
            if (checkCount.count(alphabet)){
                checkCount[alphabet]--;
            }
            else {
                return false;
            }
        }

        for (auto const& [key, val] : checkCount){
            if (val != 0){
                return false;
            }

        }
        return true;
    }
};

