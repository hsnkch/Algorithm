import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int P = Integer.parseInt(st.nextToken());

        List<List<Integer>> strings = new ArrayList<>();
        ans = 0;
        for (int i = 0; i < 7; i++) {
            strings.add(new ArrayList<Integer>());
        }

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int fret = Integer.parseInt(st.nextToken());
            List<Integer> string = strings.get(num);
            if (string.isEmpty()) {
                string.add(fret);
                ans++;
            } else {
                if (fret == string.get(string.size() - 1)) {
                    string.remove(string.size() - 1);
                    ans++;
                } else if (fret > string.get(string.size() - 1)) {
                    string.add(fret);
                    ans++;
                } else {
                    while (!string.isEmpty() && string.get(string.size() - 1) > fret) {
                        string.remove(string.size() - 1);
                        ans++;
                    }
                    if (!string.isEmpty() && fret == string.get(string.size() - 1)) {
                        continue;
                    }
                    string.add(fret);
                    ans++;
                }
            }
        }
        System.out.println(ans);
    }
}