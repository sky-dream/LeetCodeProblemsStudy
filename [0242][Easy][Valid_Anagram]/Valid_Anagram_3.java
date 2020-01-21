class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] counter = new int[26];
        for (int i = 0; i < s.length(); i++) {
            counter[s.charAt(i) - 'a']++;
            counter[t.charAt(i) - 'a']--;
        }
        for (int count : counter) {
            if (count != 0) {
                return false;
            }
        }
        return true;
    }
}

public class Valid_Anagram_3{
    public static void main(String args[]){
		String str1 = "anagram";
		String str2 = "nagaram";
		Solution Solution_obj = new Solution();
		boolean result = Solution_obj.isAnagram(str1, str2);
        System.out.println("In java code,last return value is :" + result);
    }
}