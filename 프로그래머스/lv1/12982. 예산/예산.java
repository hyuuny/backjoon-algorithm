import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] d1 = {1, 3, 2, 5, 4};
        System.out.println(solution.solution(d1, 9));
        int[] d2 = {2, 2, 3, 3};
        System.out.println(solution.solution(d2, 10));
    }

    public int solution(int[] d, int budget) {
        int answer = 0;
        List<Integer> moneys = toMoneys(d);

        for (int money : moneys) {
            if (money <= budget) {
                answer++;
                budget -= money;
            }
        }
        return answer;
    }

    private List<Integer> toMoneys(int[] d) {
        return Arrays.stream(d)
                .boxed()
                .sorted()
                .collect(Collectors.toList());
    }

}