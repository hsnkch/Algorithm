import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(br.readLine());
        int[] course = new int[n+1];
        for (int i = 0; i < n+1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            course[i] = d(a, b, w, h);
        }

        ans = 0;
        for (int i = 0; i < n; i++) {
            int tmp = Math.abs(course[n] - course[i]);
            ans += Math.min(tmp, 2 * (w + h) - tmp);
        }
        System.out.println(ans);
    }

    public static int d(int a, int b, int w, int h) {
        int result = 0;
        switch (a) {
            case 1:
                result = b;
                break;
            case 2:
                result = w + w + h - b;
                break;
            case 3:
                result = w + w + h + h - b;
                break;
            case 4:
                result = w + b;
                break;
        }
        return result;
    }
}
