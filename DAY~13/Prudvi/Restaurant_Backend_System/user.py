from pathlib import Path
import mmap, threading, os

RED_BOLD = "\033[1;31m"
GREEN_BOLD = "\033[1;32m"
RESET = "\033[0m"
file_path = Path("orders_data.txt")

food_items = [
  {"food_item": "Chicken Dum Biryani", "price": 300},
  {"food_item": "Chicken Fried Piece Biryani", "price": 350},
  {"food_item": "Chicken + Roti", "price": 150},
  {"food_item": "Chicken Curry", "price": 120},
  {"food_item": "Chicken Curry Special", "price": 121}
]

if file_path.exists():
  print(f"'{file_path}' File Found, No issues...\n")
else:
  print("'", file_path, "'", "File Creating...\n")
  file_path.touch()

os.system('cls')

def make_order(inp):
  print(f"Hi Sir or Madam, {GREEN_BOLD}Welcome to the Restaurant:{RESET}\n\n{GREEN_BOLD}Order Please:{RESET}")

  for i, item in enumerate(food_items):
    print(f"{i + 1}. {item['food_item'].ljust(30)} - {GREEN_BOLD}₹{item['price']}{RESET}")

  # order_items = str(input(f"\nPlease Enter Serial Number of Items\n{RED_BOLD}Without Spaces or Anything{RESET} eg: 143: "))
  order_items = inp

  for item in order_items:
    if(item not in ['1', '2', '3', '4', '5']):
      exit()

  binary_output = " ".join(format(ord(char), '08b') for char in order_items) #how it working
  binary_output += "\n"
  mmap_ready_bytes = binary_output.encode('utf-8')

  print(f"\nOriginal String: {order_items}")
  print(f"Binary Format:   {binary_output}")
  print(f"MMAP Format:   {mmap_ready_bytes}")

  new_bytes = len(mmap_ready_bytes)

  with open("orders_data.txt", "r+b") as f: #why r+b
    current_size = os.path.getsize("orders_data.txt")

    f.truncate(current_size + new_bytes)

    with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE) as mm: #access Ok, waht is f.fileno(), length=0
      mm.seek(current_size)
      mm.write(mmap_ready_bytes)

      print("\nOrdered Successfully!")

t1 = threading.Thread(target=make_order, args=("15",))
t2 = threading.Thread(target=make_order, args=("2",))
t3 = threading.Thread(target=make_order, args=("3",))
t4 = threading.Thread(target=make_order, args=("4",))
t5 = threading.Thread(target=make_order, args=("5",))
t6 = threading.Thread(target=make_order, args=("1",))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

