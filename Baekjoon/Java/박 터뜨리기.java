import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int ans;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int tmp = k * (k + 1) / 2;

        if (n < tmp) {
            ans = -1;
        } else if ((n - tmp) % k == 0) {
            ans = k - 1;
        } else {
            ans = k;
        }

        System.out.println(ans);
    }
}