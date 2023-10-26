import java.io.*;
import java.util.*;


public class Main {
    static int max_h;
    static int max_idx;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] stick = new int[1001];
        for (int i : stick) {
            stick[i] = 0;
        }
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            stick[l] = h;
            if (max_h < h) {
                max_h = h;
                max_idx = l;
            }
        }

        int cur_L = 0;
        int cur_R = 0;
        int ans = 0;
        for (int i = 0; i <= max_idx; i++) {
            cur_L = Math.max(cur_L, stick[i]);
            ans += cur_L;
        }
        for (int i = 1000; i > max_idx; i--) {
            cur_R = Math.max(cur_R, stick[i]);
            ans += cur_R;
        }

        System.out.println(ans);


    }
}