class Node:
    def __init__(self, diary_id, tanggal, isi):
        self.diary_id = diary_id
        self.tanggal = tanggal
        self.isi = isi
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_entry(self, diary_id, tanggal, isi):
        new_node = Node(diary_id, tanggal, isi)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_entry(self, diary_id):
        current = self.head
        previous = None
        while current and current.diary_id != diary_id:
            previous = current
            current = current.next
        if current is None:
            print(f"Entri dengan ID {diary_id} tidak ditemukan.")
            return
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        print(f"Entri dengan ID {diary_id} telah dihapus.")

    def find_entry(self, diary_id):
        current = self.head
        while current and current.diary_id != diary_id:
            current = current.next
        if current is None:
            return f"Entri dengan ID {diary_id} tidak ditemukan."
        return f"ID: {current.diary_id}, Tanggal: {current.tanggal}, Isi: {current.isi}"

    def display_entries(self):
        current = self.head
        while current:
            print(f"ID: {current.diary_id}, Tanggal: {current.tanggal}, Isi: {current.isi}")
            current = current.next

diary = SinglyLinkedList()

diary.add_entry(1, "2024-06-01", "Mengunjungi taman dan menikmati hari yang cerah.")
diary.add_entry(2, "2024-06-02", "Menghadiri pertemuan produktif di tempat kerja.")
diary.add_entry(3, "2024-06-03", "Makan malam di restoran baru bersama teman-teman.")

print("Semua entri diary:")
diary.display_entries()

print("\nmencari entri diary dengan ID 2:")
print(diary.find_entry(2))

print("\nMenghapus entri diary dengan ID 2:")
diary.delete_entry(2)

print("\nSemua entri diary setelah dihapus:")
diary.display_entries()
