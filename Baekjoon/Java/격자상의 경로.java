import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        br.close();

        if (k == 0) {
            System.out.println(find(n, m));
        } else {
            int dotN1 = (k-1)/m + 1;
            int dotM1 = k - (dotN1 - 1) * m;
            int dotN2 = n - (dotN1 - 1);
            int dotM2 = n - (dotM1 - 1);

            int first = find(dotN1, dotM1);
            int second = find(dotN2, dotM2);
            System.out.println(first * second);
        }

    }

    public static int find(int n, int m) {
        int[][] dp = new int[n + 1][m + 1];
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < m + 1; j++) {
                if (i == 1 && j == 1) {
                    dp[i][j] = 1;
                    continue;
                }
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
            }
        }
        return dp[n][m];
    }
}