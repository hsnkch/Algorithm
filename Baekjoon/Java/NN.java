import java.io.*;
import java.util.*;


public class Main {
    private static StringTokenizer st;
    private static BufferedReader br;

    public static void main(String[] args) throws IOException{
        br = new BufferedReader(new InputStreamReader(System.in));
        st = new StringTokenizer(br.readLine());
        String n = st.nextToken();
        int m = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Integer.parseInt(n); i++) {
            sb.append(n);
        }
        if (sb.length() > m) {
            System.out.println(sb.substring(0, m));
        } else {
            System.out.println(sb);
        }
    }
}