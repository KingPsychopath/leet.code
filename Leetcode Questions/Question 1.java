import java.util.*;
import java.lang.Math;

public class Result {
    // Graph represented as an adjacency list
    static ArrayList<Integer>[] graph;
    // Array to keep track of visited nodes
    static boolean[] visited;

    public static void main(String[] args) {
        int n = 13;
        String[] edges = {"1 3", "3 4", "3 5", "4 6", "2 4", "7 8", "8 9", "10 11"};
        // Print the sum of the floor of the natural logarithm of the size of each connected component
        System.out.println(sumOfSets(n, edges));
    }

    static int sumOfSets(int n, String[] edges) {
        // Initialize the graph
        graph = new ArrayList[n+1];
        for (int i = 0; i <= n; i++) {
            graph[i] = new ArrayList<>();
        }

        // Populate the graph with edges
        for (String edge : edges) {
            String[] nodes = edge.split(" ");
            int u = Integer.parseInt(nodes[0]);
            int v = Integer.parseInt(nodes[1]);
            graph[u].add(v);
            graph[v].add(u);
        }

        // Initialize the visited array
        visited = new boolean[n+1];
        int sum = 0;
        // For each node, if it's not visited, perform DFS to find the size of the connected component it belongs to
        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                int size = dfs(i);
                // Add the floor of the natural logarithm of the size to the sum
                sum += Math.floor(Math.log(size));
            }
        }
        // Return the sum
        return sum;
    }

    // DFS function to find the size of a connected component
    static int dfs(int node) {
        // Mark the node as visited
        visited[node] = true;
        int size = 1;
        // For each neighbor of the node, if it's not visited, perform DFS and add the size to the current size
        for (int neighbor : graph[node]) {
            if (!visited[neighbor]) {
                size += dfs(neighbor);
            }
        }
        // Return the size
        return size;
    }
}


public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        int edgesCount = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> edges = IntStream.range(0, edgesCount).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        int result = Result.sumOfSets(n, edges);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}