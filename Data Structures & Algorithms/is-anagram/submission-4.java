class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }

        // frequency table for alphabet
        int[] letter_count = new int[26];

        for (int i = 0; i < s.length(); i++){
            letter_count[s.charAt(i) - 'a']++;
            letter_count[t.charAt(i) - 'a']--;
        }

        for(int val : letter_count){
            if (val != 0)
                return false;
        }
        return true;
    }
}
