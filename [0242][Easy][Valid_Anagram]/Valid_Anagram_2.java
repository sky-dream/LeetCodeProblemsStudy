import java.util.Arrays;
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        char[] str1 = s.toCharArray();
        char[] str2 = t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        return Arrays.equals(str1, str2);
    }
}

public class Valid_Anagram_2{
    public static void main(String args[]){
		String str1 = "anagram";
		String str2 = "nagaram";
		Solution Solution_obj = new Solution();
		boolean result = Solution_obj.isAnagram(str1, str2);
        System.out.println("In java code,last return value is :" + result);
    }
}