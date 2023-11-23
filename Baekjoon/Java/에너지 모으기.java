import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<Integer> w = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            w.add(Integer.parseInt(st.nextToken()));
        }
        ans = 0;
        dfs(0, w);
        System.out.println(ans);
    }
    public static void dfs(int tmp, List w) {
        if (w.size() == 2) {
            if (ans < tmp) {
                ans = tmp;
            }
            return;
        } else {
            for (int i = 1; i < w.size() - 1; i++) {
                int k = (int) w.get(i);
                w.remove(i);
                dfs(tmp + ((int) w.get(i - 1) * (int) w.get(i)), w);
                w.add(i,k);
            }
        }

    }
}