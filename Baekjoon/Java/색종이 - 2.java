import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br;
    private static StringTokenizer st;
    private static int ans;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] boards = new int[102][102];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            for (int j = x; j < x + 10; j++) {
                for (int k = y; k < y + 10; k++) {
                    boards[j][k] = 1;
                }
            }
        }

        ans = 0;
        int[] dx = new int[]{0, 0, 1, -1};
        int[] dy = new int[]{1, -1, 0, 0};
        for (int i = 1; i < 101; i++) {
            for (int j = 1; j < 101; j++) {
                if (boards[i][j] == 1) {
                    for (int k = 0; k < 4; k++) {
                        int rx = i + dx[k];
                        int ry = j + dy[k];
                        if (boards[rx][ry] == 0) {
                            ans++;
                        }
                    }
                }
            }
        }
        System.out.println(ans);
    }
}