import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] L = new int[n+1];
        int[] J = new int[n+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            L[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            J[i] = Integer.parseInt(st.nextToken());
        }
        int[][] dp = new int[n + 1][100];

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j < 100; j++) {
                if (L[i] <= j) {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i - 1][j - L[i]] + J[i]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        System.out.println(dp[n][99]);

    }
}