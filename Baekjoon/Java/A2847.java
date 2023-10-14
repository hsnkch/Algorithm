import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ans = 0;
        int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = Integer.parseInt(br.readLine());
        }

        for (int i = n-2; i >= 0; i--) {
            if (scores[i] >= scores[i+1]) {
                ans += scores[i] - scores[i+1] + 1;
                scores[i] = scores[i+1] -1;
            }
        }

        System.out.println(ans);
        br.close();
    }
}