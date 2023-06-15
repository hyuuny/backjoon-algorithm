class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("3141592", "271"));
        System.out.println(solution.solution("500220839878", "7"));
        System.out.println(solution.solution("10203", "15"));
    }

    public int solution(String t, String p) {
        long tLength = t.length();
        long pLength = p.length();
        long longP = Long.parseLong(p);

        int answer = 0;
        for (int i = 0; i <= tLength - pLength; i++) {
            long longT = Long.parseLong(t.substring(i, (int) (i + pLength)));
            if (longT <= longP) {
                answer += 1;
            }
        }
        return answer;
    }

}