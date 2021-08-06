#121. Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        min_value = prices[0]
        mx = 0
        for i in range(1,len(prices)):
            min_value = min(prices[i],min_value)
            mx = max(mx,prices[i]-min_value)#current value minus before min value
        return mx
//#122. Best Time to Buy and Sell Stock II
//you must sell after buy, you can buy and sell at the same day
//Input: prices = [7,1,5,3,4,6] Output: 7  (buy at 3 sell at 4 then buy 4 sell at 6, same profit with buy 3 sell 6)
public int maxProfit(int[] prices) {
	int max = 0;
	for(int i=1; i<prices.length;++i){
		if(prices[i]>prices[i-1]){
			max += prices[i]-prices[i-1];
			//i++;
		}
	}
	return max;
}