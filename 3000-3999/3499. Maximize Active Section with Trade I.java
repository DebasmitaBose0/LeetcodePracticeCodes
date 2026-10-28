class Solution {
    public int maxActiveSectionsAfterTrade(String s) {
        int totalOnes = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '1') {
                totalOnes++;
            }
        }

        String t = "1" + s + "1";
        
        // Extract lengths of alternating blocks
        java.util.List<Integer> lengths = new java.util.ArrayList<>();
        java.util.List<Character> types = new java.util.ArrayList<>();
        
        int n = t.length();
        int i = 0;
        while (i < n) {
            char ch = t.charAt(i);
            int start = i;
            while (i < n && t.charAt(i) == ch) {
                i++;
            }
            types.add(ch);
            lengths.add(i - start);
        }

        int maxDelta = 0;
        // Search for '1' blocks surrounded by '0' blocks on both sides
        for (int j = 1; j < types.size() - 1; j++) {
            if (types.get(j) == '1' && types.get(j - 1) == '0' && types.get(j + 1) == '0') {
                int delta = lengths.get(j - 1) + lengths.get(j + 1);
                maxDelta = Math.max(maxDelta, delta);
            }
        }

        return totalOnes + maxDelta;
    }
}