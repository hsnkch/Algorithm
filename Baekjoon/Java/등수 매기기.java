import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] rate = new int[n];
        for (int i = 0; i < n; i++) {
            rate[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(rate);
        long ans = 0;
        for (int i = 1; i <= n; i++) {
            ans += Math.abs(rate[i - 1] - i);
        }
        System.out.println(ans);
    }
}