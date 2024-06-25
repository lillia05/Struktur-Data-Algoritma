from collections import deque

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)
        else:
            print("One or both vertices not found.")
    
    def bfs(self, start_vertex):
        visited = set()
        queue = deque()

        visited.add(start_vertex)
        queue.append(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex)

            neighbors = self.vertices[vertex]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

graph = Graph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("C", "E")

print("BFS traversal:")
graph.bfs("A")
























# Graf merupakan cara untuk merepresentasikan hubungan yang ada antara pasangan objek. Graf adalah kumpulan objek yang disebut simpul 
# (vertices), bersama dengan kumpulan hubungan antara mereka yang disebut sisi (edges). Graf memiliki berbagai aplikasi dalam pemodelan 
# berbagai domain, termasuk pemetaan, transportasi, jaringan komputer, dan rekayasa listrik. Perlu diingat bahwa istilah "graf" dalam konteks ini 
# tidak berkaitan dengan grafik batang atau plot fungsi.
# Secara abstrak, graf G adalah sekumpulan simpul V dan kumpulan pasangan simpul dari V yang disebut sisi. Dengan demikian, graf adalah cara 
# untuk merepresentasikan hubungan antara pasangan objek dari suatu himpunan V. Beberapa buku menggunakan terminologi yang berbeda 
# untuk graf, dengan menyebut simpul sebagai node dan sisi sebagai busur (arc). Kami menggunakan istilah "simpul" dan "sisi".
# Sisi dalam graf dapat berarah atau tidak berarah. Sisi (u,v) dikatakan berarah dari u ke v jika pasangan (u,v) diurutkan, dengan u mendahului v. 
# Sisi (u,v) dikatakan tidak berarah jika pasangan (u,v) tidak diurutkan. Sisi tidak berarah kadang-kadang ditulis dengan notasi himpunan, misalnya 
# {u,v}, tetapi untuk kesederhanaan, kami menggunakan notasi pasangan (u,v), dengan catatan bahwa dalam kasus tidak berarah, (u,v) sama 
# dengan (v,u). Graf biasanya divisualisasikan dengan menggambar simpul sebagai oval atau persegi panjang dan sisi sebagai segmen atau kurva 
# yang menghubungkan pasangan oval dan persegi panjang. Berikut adalah beberapa contoh graf berarah dan tidak berarah