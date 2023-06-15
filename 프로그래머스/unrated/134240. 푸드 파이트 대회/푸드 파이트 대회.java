class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] food1 = {1, 3, 4, 6};
        System.out.println(solution.solution(food1));
        int[] food2 = {1, 7, 1, 2};
        System.out.println(solution.solution(food2));
    }

    public String solution(int[] food) {
        StringBuilder answer = new StringBuilder();

        for (int i = 1; i < food.length; i++) {
            for (int j = 0; j < food[i] / 2; j++) {
                answer.append(i);
            }
        }
        
        answer.append(food[0]/2);

        for (int i = food.length - 1; i > 0; i--) {
            for (int j = 0; j < food[i] / 2; j++) {
                answer.append(i);
            }
        }
        return answer.toString();
    }

}