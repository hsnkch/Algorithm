import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            int n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            int[] price = new int[n];
            for (int j = 0; j < price.length; j++) {
                price[j] = Integer.parseInt(st.nextToken());
            }
            ans = 0;
            int max = 0;

            for (int j = n - 1; j >= 0; j--) {
                if (price[j] > max) {
                    max = price[j];
                } else {
                    ans += max - price[j];
                }
            }
            System.out.println(ans);
        }

    }
}