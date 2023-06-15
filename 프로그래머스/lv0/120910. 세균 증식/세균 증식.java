class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(2, 10));
        System.out.println(solution.solution(7, 15));
    }

    public int solution(int n, int t) {
        int answer = n;
        for (int i = 1; i <= t; i++){
            answer = Math.multiplyExact(answer, 2);
        }
        return answer;
    }

}