import java.io.*;
import java.util.*;

public class Main {
    static int x;
    static int y;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int w = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(br.readLine());

        int a = (p + t) / w;
        int b = (q + t) / h;

        if (a % 2 == 0) {
            x = (p + t) % w;
        } else {
            x = w - (p + t) % w;
        }
        if (b % 2 == 0) {
            y = (q + t) % h;
        } else {
            y = h - (q + t) % h;
        }
        bw.write(Integer.toString(x));
        bw.write(" ");
        bw.write(Integer.toString(y));
        bw.close();
        br.close();
    }
}