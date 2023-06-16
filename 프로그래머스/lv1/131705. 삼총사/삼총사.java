class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] n1 = {-2, 3, 0, 2, -5};
        System.out.println(solution.solution(n1));

        int[] n2 = {-3, -2, -1, 0, 1, 2, 3};
        System.out.println(solution.solution(n2));

        int[] n3 = {-1, 1, -1, 1};
        System.out.println(solution.solution(n3));
    }

    public int solution(int[] number) {
        int answer = 0;

        for (int i = 0; i < number.length; i++) {
            for (int j = i + 1; j < number.length; j++) {
                for (int k = j + 1; k < number.length; k++) {
                    int sumVal = number[i] + number[j] + number[k];
                    if (sumVal == 0) {
                        answer += 1;
                    }
                }
            }
        }
        return answer;
    }

}