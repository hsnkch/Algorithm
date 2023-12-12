import java.io.*;
import java.util.*;


public class Main {
    private static StringTokenizer st;
    private static BufferedReader br;

    public static void main(String[] args) throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[1000001];
        dp[1] = 1;
        for (int i = 2; i < 1000001; i++) {
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1000000000;
        }

        if (n < 0 && n % 2 == 0) {
            System.out.println(-1);
        } else if (n == 0) {
            System.out.println(0);
        } else {
            System.out.println(1);
        }
        System.out.println(dp[Math.abs(n)]);

    }
}