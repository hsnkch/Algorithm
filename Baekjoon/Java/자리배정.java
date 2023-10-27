import java.io.*;
import java.util.*;
import java.util.stream.IntStream;

import static java.lang.System.exit;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(br.readLine());

        if (k > c * r) {
            System.out.println(0);;
            return;
        }

        int[] dx = {1, 0, -1, 0};
        int[] dy = {0, 1, 0, -1};
        int[][] seats = new int[c][r];
        for (int i = 0; i < c; i++) {
            for (int j = 0; j < r; j++) {
                seats[i][j] = 0;
            }
        }
        seats[0][0] = 1;
        int cur_dir = 0;
        int x = 0;
        int y = 0;

        for (int i = 2; i < k + 1; i++) {
            while (true) {
                int rx = x + dx[cur_dir];
                int ry = y + dy[cur_dir];
                if (0 <= rx && rx < r && ry >= 0 && ry < c && seats[rx][ry] == 0) {
                    seats[rx][ry] = i;
                    x = rx;
                    y = ry;
                    break;
                } else {
                    cur_dir = (cur_dir + 1) % 4;
                }
            }
        }
        System.out.println((y+1)+" "+(x+1));
    }
}