import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] dp_1 = new int[d];
        dp_1[0] = 1;
        dp_1[1] = 0;
        int[] dp_2 = new int[d];
        dp_2[0] = 0;
        dp_2[1] = 1;
        for (int i = 2; i < d; i++) {
            dp_1[i] = dp_1[i-2] + dp_1[i-1];
            dp_2[i] = dp_2[i-2] + dp_2[i-1];
        }
        int cnt_1 = dp_1[d-1];
        int cnt_2 = dp_2[d-1];

        for (int i = 1; i < k / cnt_1; i++) {
            int total_2 = k - cnt_1 * i;
            if (total_2 % cnt_2 == 0) {
                System.out.println(i);
                System.out.println(total_2 / cnt_2);
                break;
            }
        }
    }
}