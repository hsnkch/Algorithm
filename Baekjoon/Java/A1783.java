import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class A1783 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int ans = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        if (1 < M && M <= 6) {
            if (N > 2) {
                ans = Math.min(M - 1, 3);
            } else if (N == 2) {
                ans = (M - 1) / 2;
            } else {
                ans = 0;
            }
        } else if (M == 1) {
            ans = 0;
        } else {
            if (N > 2) {
                ans = 4 + M - 7;
            } else if (N == 2) {
                ans = 3;
            } else {
                ans = 0;
            }
        }

        bw.write(String.valueOf(ans + 1));
        bw.newLine();
        bw.flush();

        // Close the streams
        br.close();
        bw.close();
    }
}