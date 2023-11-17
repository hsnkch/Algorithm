import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] s = new int[n];
        for (int i = 0; i < s.length; i++) {
            s[i] = Integer.parseInt(st.nextToken());
        }
        System.out.println(solve(s));
    }

    public static int solve(int[] s) {
        Arrays.sort(s);
        ans = 1;
        for (int i : s) {
            if (ans < i) {
                break;
            }
            ans += i;
        }
        return ans;
    }
}