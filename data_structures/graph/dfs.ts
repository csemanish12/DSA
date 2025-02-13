class Solution{
    dfsOfGraph(adj: number[][]): number[]{
        const visited: boolean[] = [];
        for (let i=0; i<adj.length; i++) {
            visited[i] = false;
        }
        const dfsList: number[] = [];
        const start_node: number = 0;

        this.dfs(start_node, adj, dfsList, visited);

        return dfsList;
    }

    private dfs(node: number, adj: number[][], dfsList: number[], visited: boolean[]){
        visited[node] = true;
        dfsList.push(node);

        for (const neighbor of adj[node]){
            if (!visited[neighbor]) {
                this.dfs(neighbor, adj, dfsList, visited);
            }
        }


    }
}

// Example usage:
const graph: number[][] = [
    [1, 2],    // Node 0 is connected to 1 and 2
    [0, 3, 4], // Node 1 is connected to 0, 3, and 4
    [0, 5, 6], // Node 2 is connected to 0, 5, and 6
    [1],       // Node 3 is connected to 1
    [1],       // Node 4 is connected to 1
    [2],       // Node 5 is connected to 2
    [2]        // Node 6 is connected to 2
];
const solution = new Solution();
console.log("ans is:",solution.dfsOfGraph(graph).toString());