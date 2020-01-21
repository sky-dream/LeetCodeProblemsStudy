class Solution {
    public boolean isAnagram(String s, String t) {
        int[] alpha = new int[26];
        for (char a:s.toCharArray()) {
        	alpha[a-'a']++;
        }
        for (char a:t.toCharArray()) {
        	if (alpha[a-'a'] == 0)
        		return false;
        	else
        		alpha[a-'a'] --;
        }
        for (int i: alpha)
        	if (i != 0)
        		return false;
        return true;
    }
}

public class Valid_Anagram{
    public static void main(String args[]){
		String str1 = "anagram";
		String str2 = "nagaram";
		Solution Solution_obj = new Solution();
		boolean result = Solution_obj.isAnagram(str1, str2);
        System.out.println("In java code,last return value is :" + result);
    }
}