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
        int score = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        ans = 1;
        if (n > 0) {
            int[] ranking = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                ranking[i] = Integer.parseInt(st.nextToken());
            }
            if (n == p && ranking[n-1] >= score) {
                ans = -1;
            } else {
                while (n > 0) {
                    if (ranking[n - 1] <= score) {
                        n--;
                    } else {
                        break;
                    }
                }
                ans = n + 1;
            }
        }
        System.out.println(ans);
    }
}