import java.io.*;
import java.util.*;


public class Main {
    private static int ans;
    private static BufferedReader br;
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        ans = 0;
        while (Integer.bitCount(n) > k) {
            n++;
            ans++;
        }
        System.out.println(ans);
    }
}