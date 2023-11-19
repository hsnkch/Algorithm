import java.io.*;
import java.util.*;


public class Main {
    private static int ans;
    private static BufferedReader br;
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        for (int i = 0; i < s.length(); i++) {
            String a = s.substring(i);
            String b = new StringBuilder(a).reverse().toString();
            if (a.equals(b)) {
                String tmp = s + new StringBuilder(s.substring(0, i)).reverse().toString();
                System.out.println(tmp.length());
                break;
            }
        }
    }
}