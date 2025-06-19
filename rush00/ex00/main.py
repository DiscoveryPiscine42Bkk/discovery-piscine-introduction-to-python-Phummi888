from typing import List

class Customer:
    def __init__(self, name, num_people):
        self.name = name
        self.num_people = num_people

class QueueManager:
    def __init__(self):  # ✅ แก้จาก init → __init__
        self.queue: List[Customer] = []

    def add_customer(self, name: str, num_people: int):
        new_customer = Customer(name, num_people)
        self.queue.append(new_customer)
        print(f"เพิ่มคิวให้ {name} จำนวน {num_people} คนแล้ว")

    def show_queue(self):
        if not self.queue:
            print("ยังไม่มีลูกค้าในคิว")
        else:
            print("\nคิวลูกค้าปัจจุบัน:")
            for i, customer in enumerate(self.queue, 1):
                print(f"{i}. {customer.name} ({customer.num_people} คน)")

    def serve_next_customer(self):
        if not self.queue:
            print("ไม่มีลูกค้าในคิว")
        else:
            customer = self.queue.pop(0)
            print(f"เสิร์ฟคิวของ {customer.name} จำนวน {customer.num_people} คนแล้ว")

def display_menu():
    print("\n=== ระบบจัดคิวหมูกระทะ ===")
    print("1. เพิ่มคิวลูกค้า")
    print("2. แสดงคิวทั้งหมด")
    print("3. เสิร์ฟลูกค้าคิวแรก")
    print("4. ออกจากโปรแกรม")

def main():
    manager = QueueManager()

    while True:
        display_menu()
        choice = input("เลือกเมนู (1-4): ").strip()

        if choice == "1":
            name = input("ชื่อลูกค้า: ")
            try:
                num = int(input("จำนวนคน: "))
                manager.add_customer(name, num)
            except ValueError:
                print("ต้องกรอกตัวเลขเท่านั้นสำหรับจำนวนคน")
        elif choice == "2":
            manager.show_queue()
        elif choice == "3":
            manager.serve_next_customer()
        elif choice == "4":
            print("ขอบคุณที่ใช้ระบบคิวหมูกระทะ")
            break
        else:
            print("กรุณาเลือกแค่ 1-4 เท่านั้น")

if __name__ == "__main__":
    main()