import java.io.*;
import java.util.*;

public class Main {
    static int n, d, k, c;
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        int[] sushi = new int[n];

        for (int i = 0; i < n; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        int left = 0;
        int right = k - 1;
        Map<Integer, Integer> a = new HashMap<>();
        a.put(c, 1);

        for (int i = 0; i < right + 1; i++) {
            if (a.containsKey(sushi[i])) {
                a.put(sushi[i], a.get(sushi[i]) + 1);
            } else {
                a.put(sushi[i], 1);
            }
        }

        int ans = 0;

        while (left < n) {
            ans = Math.max(ans, a.size());
            a.put(sushi[left], a.get(sushi[left]) - 1);

            if (a.get(sushi[left]) == 0) {
                a.remove(sushi[left]);
            }

            left++;
            right++;

            if (a.containsKey(sushi[right % n])) {
                a.put(sushi[right % n], a.get(sushi[right % n]) + 1);
            } else {
                a.put(sushi[right % n], 1);
            }

        }

        System.out.println(ans);

    }
}
