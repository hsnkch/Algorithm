import java.io.*;
import java.util.*;


public class Main {
    private static int ans;
    private static BufferedReader br;
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] split = br.readLine().split("\\*");
        String start = split[0];
        String end = split[1];
        int l = start.length() + end.length();
        for (int i = 0; i < n; i++) {
            String file = br.readLine();
            if (file.length() < l) {
                System.out.println("NE");
            } else {
                if (start.equals(file.substring(0, start.length())) && end.equals(file.substring(file.length() - end.length(), file.length()))) {
                    System.out.println("DA");
                } else {
                    System.out.println("NE");
                }
            }
        }
    }
}