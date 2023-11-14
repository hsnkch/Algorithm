import java.io.*;
import java.util.*;


public class Main {
    private static int ans;
    private static BufferedReader br;
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int total = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        int[] students = new int[total];
        for (int i = 0; i < total; i++) {
            students[i] = Integer.parseInt(st.nextToken());
        }

        List<Integer> pic = new ArrayList<>();
        List<Integer> score = new ArrayList<>();
        for (int i = 0; i < total; i++) {
            if (pic.contains(students[i])) {
                for (int j = 0; j < pic.size(); j++) {
                    if (students[i] == pic.get(j)) {
                        score.set(j, pic.get(j) + 1);
                    }
                }
            } else {
                if (pic.size() >= n) {
                    for (int k = 0; k < n; k++) {
                        if (score.get(k) == Collections.min(score)) {
                            pic.remove(k);
                            score.remove(k);
                            break;
                        }
                    }
                }
                pic.add(students[i]);
                score.add(1);
            }
        }
        Collections.sort(pic);
        for (int i : pic) {
            System.out.print(i+" ");
        }
    }
}