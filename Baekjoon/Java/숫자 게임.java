import java.io.*;
import java.util.*;


public class Main {
    private static StringTokenizer st;
    private static BufferedReader br;

    public static void main(String[] args) throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][5];
        int[] max = new int[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            int sum = 0;
            int tmp = 0;
            for (int j = 0; j < 3; j++) {
                for (int k = j + 1; k < 4; k++) {
                    for (int l = k + 1; l < 5; l++) {
                        tmp = arr[i][j] + arr[i][k] + arr[i][l];
                        if (sum <= tmp % 10)
                            sum = tmp % 10;
                    }
                }
            }
            max[i] = sum;
        }

        int ans = 0;
        int result = max[0];

        for (int i = 0; i < n; i++) {
            if (max[i] >= result) {
                result = max[i];
                ans = i + 1;
            }
        }

        System.out.println(ans);
    }
}