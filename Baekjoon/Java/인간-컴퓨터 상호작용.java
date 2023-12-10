import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int ans;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int q = Integer.parseInt(br.readLine());

        int[][] dp = new int[s.length()][26];
        dp[0][(int) s.charAt(0) - 97] = 1;
        for (int i = 1; i < dp.length; i++) {
            dp[i][(int) s.charAt(i) - 97] = 1;
            for (int j = 0; j < 26; j++) {
                dp[i][j] += dp[i - 1][j];
            }
        }

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            char a = st.nextToken().charAt(0);
            Integer l = Integer.parseInt(st.nextToken());
            Integer r = Integer.parseInt(st.nextToken());
            if (l > 0) {
                ans = dp[r][(int) a - 97] - dp[l - 1][(int) a - 97];
            } else {
                ans = dp[r][(int) a - 97];
            }
            System.out.println(ans);
        }
    }
}