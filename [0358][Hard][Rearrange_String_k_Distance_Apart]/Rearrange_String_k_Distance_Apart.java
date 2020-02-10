import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;
// solution 3, analysis and design. somehow similar to problem 621 solution 3.
// code can still be optimized.
// leetcode time     cost : 7 ms
// leetcode memory   cost : 46.8 MB 
// Time  Complexity: O(M*N),M is all the char type number,N is all the char number
// Space Complexity: O(1)
class Solution {
    public String rearrangeString(String s, int k) {
        if (k == 0){
            return s;
        }
        //the max char number of ASCII is 128 characters.
        int[] charDict = new int[128];
        for (int i = 0; i < s.length(); i++) {
            int index = (int)s.charAt(i);
            charDict[index] += 1;
        }
        char[] result = new char[s.length()];
        int size = s.length() % k == 0 ? k : s.length() % k;
        int[] lastGroupStr = new int[size];
        //use the negative counter as the counter in the dict value, 
        for (int i = 0; i < lastGroupStr.length; i++) {
            lastGroupStr[i] = -1;
        }
        int index = k-1;
        int traverse = k-1;
        int lastGroupStrIndex = 0;
        for (int i = 0; i < charDict.length; i++) {
            //in the possible solution, the max counter char must be arranged in different group,every group except the last has at least k char, 
            //the char number in last group maybe k or less than k( s.length() % k ).
            int groupNum = (s.length() - 1) / k + 1;
            //if any individual char number is more than max char number(group number) in the possible solution, then there will be no solution.
            if (charDict[i] > groupNum){
                return "";
            }
            //if any individual char number is equal to group number in the possible solution, it is one of the max number char,it will exists in the last group.
            if (charDict[i] == groupNum){
                //if real char number in the last group is more than the number of the last group length in possible solution, there will be no solution.
                if (lastGroupStrIndex > lastGroupStr.length - 1){
                    return "";
                }
                lastGroupStr[lastGroupStrIndex++] = i;
                continue;
            }
            //for every individual char, use up all this char to add it in the different location of the result.
            for (int j = 1; j <= charDict[i]; j++) {
                //change back the dict key from int to char
                result[index] = (char)i;
                //result index jump k to observe vacant location for (k-1) other chars.
                index += k;
                //keep the char insert location index in the range of s.length.
                if (index > s.length() - 1){
                    //index, traverse start with k-1, traverse is the sub index of every k long sub str.
                    traverse--;
                    index = traverse;
                }
            }
        }
        int resultIndex = 0;
        int resultSubIndex = 0;
        for (int i = 0; i < lastGroupStr.length; i++) {
            // -1 means no char inserted at this position, 
            if (lastGroupStr[i] == -1){
                continue;
            }
            //otherwise it is char converted ASCII int value. put the last group str into the result, start with 0, 
            for (int j = 0; j < result.length; j++) {
                result[resultIndex] = (char) lastGroupStr[i];
                resultIndex += k;
                if (resultIndex > result.length - 1){
                    break;
                }
            }
            resultSubIndex ++;
            resultIndex = resultSubIndex;
        }
        return new String(result);
    } 
}