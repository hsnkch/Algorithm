import java.io.*;
import java.util.*;


public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[] dp = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < n+1; i++) {
            dp[i] = dp[i - 1] + dp[i - 2];
        }

        List<Integer> seats = new ArrayList<Integer>();
        seats.add(0);
        for (int i = 0; i < m; i++) {
            seats.add(Integer.parseInt(br.readLine()));
        }
        seats.add(n + 1);
        int ans = 1;
        int[] ways = new int[m + 3];

        for (int i = 1; i < m + 2; i++) {
            int a = seats.get(i) - seats.get(i - 1) - 1;
            ways[i] = dp[a];
        }

        for (int way: ways) {
            if (way != 0) {
                ans = ans * way;
            }
        }

        System.out.println(ans);


    }
}
