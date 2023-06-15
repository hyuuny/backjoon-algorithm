import java.util.ArrayList;
import java.util.stream.IntStream;

class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(5, 3, 2));
        System.out.println(solution.solution(10, 3, 2));
    }

    public int solution(int number, int limit, int power) {
        ArrayList<Integer> arr = new ArrayList<>();
        IntStream.range(1, number + 1)
                .forEach(arr::add);

        ArrayList<Integer> divisors = new ArrayList<>();
        arr
                .forEach(num -> {
                    int result = getDivisors(num);
                    divisors.add(result > limit ? power : result);
                });

        return divisors.stream().mapToInt(n -> n).sum();
    }

    private int getDivisors(int num) {
        int cnt = 0;
        for (int i = 1; i * i <= num; i++) {
            if (i * i == num) {
                cnt++;
            } else if (num % i == 0) {
                cnt += 2;
            }
        }
        return cnt;
    }

}