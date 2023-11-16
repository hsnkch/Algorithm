import java.io.*;
import java.util.*;

public class Main {
    static int ans;
    static BufferedReader br;
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        String friends[] = new String[n];
        for (int i = 0; i < n; i++) {
            friends[i] = br.readLine();
        }
        ans = 0;
        int[][] result = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    if (i == j) {
                        continue;
                    }

                    if (friends[i].charAt(j) == 'Y') {
                        result[i][j] = 1;
                    } else if (friends[i].charAt(k) == 'Y' && friends[j].charAt(k) == 'Y') {
                        result[i][j] = 1;
                    }
                }
            }
        }

        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                sum += result[i][j];
            }
            ans = Math.max(ans, sum);
        }
        System.out.println(ans);
    }
}
