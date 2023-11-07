import java.io.*;
import java.util.*;


public class Main {
    static int max_h;
    static int max_idx;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        double[] nums = new double[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Double.parseDouble(br.readLine());
        }
        double[] dp = new double[n];
        dp[0] = nums[0];
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(nums[i], nums[i] * dp[i - 1]);
        }
        double ans = Arrays.stream(dp).max().orElse(0);
        System.out.printf("%.3f",ans);
    }
}