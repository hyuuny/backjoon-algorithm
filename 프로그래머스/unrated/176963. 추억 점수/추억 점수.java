import java.util.Arrays;
import java.util.HashMap;

class Solution {

    public static void main(String[] args) {
        Solution solution = new Solution();
        String[] names = {"may", "kein", "kain", "radi"};
        int[] yearnings = {5, 10, 1, 3};
        String[][] photos = {{"may", "kein", "kain", "radi"}, {"may", "kein", "brin", "deny"}, {"kon", "kain", "may", "coni"}};
        System.out.println(Arrays.toString(solution.solution(names, yearnings, photos)));
    }

    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        HashMap<String, Integer> map = new HashMap<>();
        int idx = 0;
        for (String n : name) {
            map.put(n, yearning[idx++]);
        }

        int scoreIdx = 0;
        for (String[] onePhoto : photo) {
            for (String photoName : onePhoto) {
                if (map.containsKey(photoName)) {
                    Integer score = map.get(photoName);
                    answer[scoreIdx] += score;
                }
            }
            scoreIdx++;
        }

        return answer;
    }

}