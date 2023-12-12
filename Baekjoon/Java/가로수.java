import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int ans;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] org = new int[n];
        ans = 0;
        for (int i = 0; i < n; i++) {
            org[i] = Integer.parseInt(br.readLine());
        }

        int[] gap = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            gap[i] = org[i + 1] - org[i];
        }

        int num = gap[0];
        for (int i = 1; i < n - 1; i++) {
            num = gcd(num, gap[i]);
        }

        for (int i = 0; i < gap.length; i++) {
            ans += gap[i] / num - 1;
        }

        System.out.println(ans);
    }

    public static int gcd(int a, int b) {
        while (b != 0) {
            int tmp = b;
            b = a % b;
            a = tmp;
        }

        return a;
    }

}