import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int[] costs = new int[n];
        for (int i = 0; i < n; i++) {
            costs[i] = Integer.parseInt(br.readLine());
        }
        int start = Arrays.stream(costs).max().orElse(0);
        int end = Arrays.stream(costs).sum();

        while (start <= end) {
            int mid = (start + end) / 2;
            int tmp = mid;
            int cnt = 0;
            for (int i = 0; i < n; i++) {
                if (tmp < costs[i]) {
                    tmp = mid;
                    cnt++;
                }
                tmp -= costs[i];
            }

            if (cnt > m) {
                start = mid + 1;
            } else {
                end = mid - 1;
                ans = mid;
            }
        }
        System.out.println(ans);
    }
}