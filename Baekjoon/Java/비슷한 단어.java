import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int ans;

    public static void main(String[] args) throws IOException {
        ans = 0;
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String word = br.readLine();
        List<Character> wList = new ArrayList<>();
        for (char w : word.toCharArray()) {
            wList.add(w);
        }

        for (int i = 0; i < n - 1; i++) {
            List<Character> list = new ArrayList<>(wList);
            String target = br.readLine();
            List<Character> tList = new ArrayList<>();
            for (char t : target.toCharArray()) {
                tList.add(t);
            }
            int cnt = 0;

            for (char t : tList) {
                if (list.contains(t)) {
                    list.remove(list.indexOf(t));
                } else {
                    cnt++;
                }
            }

            if (cnt < 2 && list.size() < 2) {
                ans++;
            }
        }

        System.out.println(ans);
    }
}