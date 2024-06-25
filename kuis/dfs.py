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
    
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex)

        neighbors = self.vertices[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)

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

print("DFS traversal:")
graph.dfs("A")






























# Algoritma penelusuran kedalaman pertama (DFS) adalah algoritma penelusuran yang pertama kami bahas dalam bagian ini. DFS berguna untuk 
# menguji beberapa properti graf, termasuk apakah ada jalur dari satu simpul ke simpul lain dan apakah graf tersebut terhubung.
# Penelusuran kedalaman pertama dalam graf G dapat dibandingkan dengan berkeliling di dalam labirin dengan seutas benang dan kaleng cat 
# tanpa tersesat. Kami memulai di sebuah simpul awal tertentu s dalam G, yang kami inisialisasi dengan mengikat satu ujung benang ke s dan 
# melabeli s sebagai "dikunjungi". Simpul s sekarang menjadi simpul "saat ini" kita—sebut simpul saat ini sebagai u. Kemudian kami menjelajahi G 
# dengan mempertimbangkan suatu sisi (u,v) (sembarang) yang bersinggungan dengan simpul saat ini u. Jika sisi (u,v) mengarahkan kita ke suatu 
# simpul v yang sudah dikunjungi (yaitu, sudah dilabeli), kami mengabaikan sisi tersebut. Namun, jika (u,v) mengarah ke simpul v yang belum 
# dikunjungi, maka kita mengulurkan benang kita dan pergi ke v. Kemudian kami melabeli v sebagai "dikunjungi" dan menjadikannya simpul saat 
# ini, mengulangi perhitungan di atas. Pada akhirnya, kita akan mencapai "jalan buntu", yaitu, sebuah simpul saat ini v sedemikian rupa sehingga 
# semua sisi yang bersinggungan dengan v mengarah ke simpul-simpul yang sudah dikunjungi. 
# Untuk keluar dari situasi buntu ini, kita menggulung benang kita kembali, melakukan backtracking sepanjang sisi yang membawa kita ke v, 
# kembali ke simpul yang sudah dikunjungi sebelumnya u. Kemudian kita menjadikan u sebagai simpul saat ini dan mengulangi perhitungan di atas 
# untuk sisi-sisi yang bersinggungan dengan u yang belum pernah kita pertimbangkan. Jika semua sisi yang bersinggungan dengan u mengarah ke 
# simpul-simpul yang sudah dikunjungi, maka kita lagi-lagi menggulung benang kita dan melakukan backtracking ke simpul tempat kita berasal 
# untuk mencapai u, dan mengulangi prosedur pada simpul tersebut. Dengan demikian, kita terus melakukan backtracking sepanjang jalur yang 
# telah kita jelajahi sejauh ini sampai kita menemukan sebuah simpul yang memiliki sisi-sisi yang belum dieksplorasi, kita mengambil salah satu sisi 
# tersebut, dan melanjutkan penelusuran. Proses ini berakhir ketika backtracking membawa kita kembali ke simpul awal s, dan tidak ada sisi yang 
# belum dieksplorasi yang bersinggungan dengan s.

# Penelusuran kedalaman pertama dan pengembalian mundur, seperti yang dijelaskan pada bagian sebelumnya, mendefinisikan penelusuran 
# yang dapat dilacak secara fisik oleh seorang individu yang menjelajahi sebuah graf. Pada bagian ini, kami membahas algoritma lain untuk 
# melakukan penelusuran pada komponen terhubung dalam sebuah graf, yang dikenal sebagai penelusuran lebar (breadth-first search atau BFS). 
# Algoritma BFS lebih mirip dengan mengirimkan, ke segala arah, banyak penjelajah yang secara bersama-sama menjelajahi graf dengan 
# koordinasi yang teratur.
# BFS dilakukan dalam putaran dan membagi simpul-simpul graf menjadi level-level. BFS dimulai dari simpul s, yang berada pada level 0. Pada 
# putaran pertama, kami melabeli sebagai "dikunjungi" semua simpul yang bersebelahan dengan simpul awal s—simpul-simpul ini berjarak satu 
# langkah dari titik awal dan ditempatkan pada level 1. Pada putaran kedua, kita memperbolehkan semua penjelajah untuk melakukan perjalanan 
# dua langkah (yaitu, sisi-sisi) dari simpul awal. Simpul-simpul baru ini, yang bersebelahan dengan simpul-simpul level 1 dan belum ditetapkan 
# pada suatu level sebelumnya, ditempatkan pada level 2 dan ditandai sebagai "dikunjungi." Proses ini berlanjut dengan cara yang serupa, 
# berakhir ketika tidak ada simpul baru yang ditemukan pada suatu level.
# Dengan demikian, dalam BFS, penjelajah menjelajahi graf dengan cara yang terkoordinasi dan setiap putaran menambahkan simpul-simpul baru 
# ke level-level yang lebih dalam. Algoritma BFS berguna untuk mencari jalur terpendek antara dua simpul, serta untuk memeriksa keterhubungan 
# dan sifat-sifat lain dari graf