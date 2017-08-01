struct Number {
    int n;
    int index;
    bool operator<(const Number &number) const {
        return (n < number.n) || !(number.n < n) && (index < number.index);
    }
};

/*
template<typename T>
T min(T a, T b) 
{
    if (a < b) {
        return a;
    } else {
        return b;
    }
}

template<typename T>
T max(T a, T b) 
{
    if (a > b) {
        return a;
    } else {
        return b;
    }
}
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i, j;
        int len = nums.size();
        vector<Number>numbers;
        for (i = 0; i < len;  ++i) {
            Number nn;
            nn.n = nums[i];
            nn.index = i;
            numbers.push_back(nn);
        }
        sort(numbers.begin(), numbers.end());
        vector<int> answer(2, 0);
        i = 0; j = len-1;
        while (i < j) {
            if (numbers[i].n + numbers[j].n < target) {
                i++;
            } else if (numbers[i].n + numbers[j].n > target) {
                j--;
            } else {
                break;
            }
        }
        answer[0] = min(numbers[i].index, numbers[j].index) + 1;
        answer[1] = max(numbers[i].index, numbers[j].index) + 1;
        return answer;
    }
};
