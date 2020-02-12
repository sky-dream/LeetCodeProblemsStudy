// solution 3, analysis and design.
// leetcode time     cost : 15 ms
// leetcode memory   cost : 47.4 MB 
// Time  Complexity: O(M)
// Space Complexity: O(1)
import java.util.Arrays;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;
class CharCounter{
    char index;
    int counter;
    CharCounter(char index,int counter){
        this.index = index;
        this.counter = counter;
    }
}

class Solution {

    public String rearrangeString(String s, int k) {
        int[] map = new int[26];
        if (k <= 1){
            return s;
        }
        ArrayList<CharCounter> charcounter_list = new ArrayList<CharCounter>();
        StringBuilder result = new StringBuilder();
        Comparator<CharCounter> comparator = new Comparator<CharCounter>(){
            public int compare(CharCounter s1, CharCounter s2) {
                //sort by counter
                return s1.counter-s2.counter;
            }
        };
        for (char c: s.toCharArray()){
            map[c - 'a']++;
        }
        for(int i =0; i < map.length;i++){
            char c = (char)(i+'a');
            CharCounter charCounter = new CharCounter(c,map[i]);
            charcounter_list.add(charCounter); 
        }
        int charDictMaxIndex = charcounter_list.size()-1;

        Collections.sort(charcounter_list,comparator);

        int char_max_count = charcounter_list.get(charDictMaxIndex).counter; 
        int possible_groupNum = s.length() / k + 1;        
        //if max individual char number is more than max char number(group number) in the possible solution, then there will be no solution.
        if (char_max_count > possible_groupNum){
            return "";
        }
        
        while (charcounter_list.get(charDictMaxIndex).counter > 0) {
            int i = 0;
            int validCharInSubLoop =0;
            //when k interval is reached, reset i, start from the last position map[25] to get the char again.
            while (i < k) {                
                //for every cal in the loop, sort the array map, always keep the max number char in the last position map[25],
                //so if last position is 0, it means that all the char are used up.             
                if (charcounter_list.get(charDictMaxIndex).counter == 0){
                    break;
                }    
                if (i <= charDictMaxIndex && charcounter_list.get(charDictMaxIndex-i).counter > 0){
                    result.append(charcounter_list.get(charDictMaxIndex-i).index);
                    charcounter_list.get(charDictMaxIndex-i).counter--;
                    //used to counter the valid char count in this sub group
                    validCharInSubLoop++;
                }
                //update the map index to switch to a new char.
                i++;
                //for sub loop not include last loop, if sub loop finished with no enough valid char can be use.
                if (charcounter_list.get(charDictMaxIndex).counter > 0 && i == k && validCharInSubLoop != k){
                    //System.out.println("validCharInSubLoop :" + validCharInSubLoop+", i: "+i+",res: "+ result.toString());
                    return "";
                }                
            }
            //always keep the max number char in the last position map[25]
            Collections.sort(charcounter_list,comparator);
        }
        return result.toString();
    }
}
public class Rearrange_String_k_Distance_Apart_3{
    public static void main(String args[]){
        int k = 3;
        String s = "aabbccdddfffff";    //expect is "fdafbcfdafbcdf"
        String s1 = "aabbccdddffffff";    //expect is ""
        Solution obj = new Solution();
        String res = obj.rearrangeString(s,k);
        System.out.println("In java code,return value is :" + res);
        res = obj.rearrangeString(s1,k);
        System.out.println("In java code,return value is :" + res);
    }
}