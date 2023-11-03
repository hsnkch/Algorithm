import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Map<String, Integer> m = new HashMap<>(0);
        String tree;
        int cnt = 0;
        while ((tree = br.readLine())!=null) {
            if (m.containsKey(tree)) {
                m.put(tree, Integer.valueOf(m.get(tree) + 1));
            } else {
                m.put(tree, Integer.valueOf(1));
            }
            cnt++;
        }

        Object[] trees = m.keySet().toArray();
        Arrays.sort(trees);
        for (Object t : trees) {
            bw.append(t + " " + String.format("%.4f", (double) m.get(t) / cnt * 100) + "\n");
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}