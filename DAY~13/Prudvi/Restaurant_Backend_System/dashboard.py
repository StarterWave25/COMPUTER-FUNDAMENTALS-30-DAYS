import os, time, mmap

food_items = [
  {"food_item": "Chicken Dum Biryani", "price": 300},
  {"food_item": "Chicken Fried Piece Biryani", "price": 350},
  {"food_item": "Chicken + Roti", "price": 150},
  {"food_item": "Chicken Curry", "price": 120},
  {"food_item": "Chicken Curry Special", "price": 121}
]

RED_BOLD = "\033[1;31m"
GREEN_BOLD = "\033[1;32m"

def get_dashboard():
  RESET = "\033[0m"
  os.system('cls')

  try:
    with open("orders_data.txt", "r+b") as f:
      with mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_READ) as mm:
        print(f"{GREEN_BOLD}S.NO   Items               Price{RESET}")
        for i, binary_line in enumerate(iter(mm.readline, b""), start=1):
          items = []
          sum = 0
          clean_str = binary_line.decode('utf-8').strip()

          if clean_str:
            decoded_order = "".join(chr(int(b,2)) for b in clean_str.split())

          for j in decoded_order:
            j = int(j)
            items.append(food_items[j-1]["food_item"])
            # print(items, '\n\n')
            sum += food_items[j-1]["price"]

          print(i, items, RED_BOLD, "P -", sum, RESET)
  except:
    print('Nohting Here...')

try:      
  while True:
    get_dashboard()
    time.sleep(3)

except KeyboardInterrupt:
  print("\nInterval stopped by user.")  