import java.io.*;
import java.util.*;


public class Main {
    private static int ans;
    private static BufferedReader br;
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            int[] dp = new int[10];
            for (int j = 0; j < 10; j++) {
                dp[j] = 1;
            }
            for (int j = 0; j < n - 1; j++) {
                for (int k = 0; k < 10; k++) {
                    dp[k] = Arrays.stream(dp, k, 10).sum();
                }
            }
            System.out.println(Arrays.stream(dp).sum());
        }

    }
}