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
        String position = br.readLine();
        ans = 0;

        for (int i = 0; i < n; i++) {
            if (position.charAt(i) == 'P') {
                int start = Math.max(i - k, 0);
                int end = Math.min(i + k + 1, n);
                for (int j = start; j < end; j++) {
                    if (position.charAt(j) == 'H') {
                        position = position.substring(0, j) + 'a' + position.substring(j + 1);
                        ans++;
                        break;
                    }
                }
            }
        }
        System.out.println(ans);
    }
}