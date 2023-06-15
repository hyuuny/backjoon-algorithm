import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;

class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] one = {1, 2, 3, 1, 2, 3, 1};
        int[] two = {4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2};
        System.out.println(solution.solution(3, 4, one));
        System.out.println(solution.solution(4, 3, two));
    }

    public int solution(int k, int m, int[] score) {
        int answer = 0;
        List<Integer> integers = Arrays.stream(score).boxed()
                .sorted(Comparator.reverseOrder())
                .collect(Collectors.toList());

        for (int i = 0; i + m <= integers.size(); i += m) {
            List<Integer> apples = integers.subList(i, i + m);
            Integer minVal = Collections.min(apples);
            int multiplyVal = minVal * m;
            answer += multiplyVal;
        }
        return answer;
    }

}