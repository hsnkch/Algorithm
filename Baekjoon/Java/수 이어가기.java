import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        List<Integer> ans = new ArrayList<>();
        for (int i = 1; i < a + 1; i++) {
            int first = a;
            int second = i;
            List<Integer> tmp = new ArrayList<>();
            tmp.add(first);
            tmp.add(second);

            while (true) {
                int next = first - second;
                if (next >= 0) {
                    tmp.add(next);
                    first = second;
                    second = next;
                } else {
                    if (tmp.size() > ans.size()) {
                        ans = tmp;
                    }
                    break;
                }
            }
        }
        System.out.println(ans.size());
        for (int num : ans) {
            System.out.print(num + " ");
        }
    }
}