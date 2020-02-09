import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Arrays;
 
class Solution {
    public String rearrangeString(String s, int k) {
        if (k == 0){
            return s;
        }
        int[] array = new int[128];
        for (int i = 0; i < s.length(); i++) {
            int index = (int)s.charAt(i);
            array[index] += 1;
        }
        char[] result = new char[s.length()];
        int size = s.length() % k == 0 ? k : s.length() % k;
        int[] longArray = new int[size];
        for (int i = 0; i < longArray.length; i++) {
            longArray[i] = -1;
        }
        int index = k-1;
        int traverse = k-1;
        int longIndex = 0;
        for (int i = 0; i < array.length; i++) {
            int groupNum = (s.length() + k - 1) / k;
            if (array[i] > groupNum){
                return "";
            }
            if (array[i] == groupNum){
                if (longIndex > longArray.length - 1){
                    return "";
                }
                longArray[longIndex++] = i;
                continue;
            }
            for (int j = 1; j <= array[i]; j++) {
                result[index] = (char)i;
                index += k;
                if (index > result.length - 1){
                    traverse--;
                    index = traverse;
                }
            }
        }
        int resultIndex = 0;
        int resultTraverse = 0;
        for (int i = 0; i < longArray.length; i++) {
            if (longArray[i] == -1){
                continue;
            }
            for (int j = 0; j < result.length; j++) {
                result[resultIndex] = (char) longArray[i];
                resultIndex += k;
                if (resultIndex > result.length - 1){
                    break;
                }
            }
            resultTraverse ++;
            resultIndex = resultTraverse;
        }
        return new String(result);
    } 
}