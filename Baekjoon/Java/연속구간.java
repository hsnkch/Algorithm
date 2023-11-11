import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 3; i++) {
            String s = br.readLine();
            ans = 1;
            int cnt = 1;
            for (int j = 0; j < s.length()-1; j++) {
                if (s.charAt(j) == s.charAt(j + 1)) {
                    cnt++;
                } else {
                    ans = Math.max(ans, cnt);
                    cnt = 1;
                }
            }
            ans = Math.max(ans, cnt);
            System.out.println(ans);
        }
    }
}