class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("He11oWor1d", "lloWorl", 2));
        System.out.println(solution.solution("Program29b8UYP", "merS123", 7));
    }

    public String solution(String my_string, String overwrite_string, int s) {
        int overwrite_string_length = overwrite_string.length();
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < my_string.length(); i++) {
            if (i >= s && overwrite_string_length > 0) {
                 answer.append(overwrite_string.charAt(i - s));
                overwrite_string_length--;
            } else {
                answer.append(my_string.charAt(i));
            }
        }

        return answer.toString();
    }
}