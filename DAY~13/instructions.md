# **Build a Command Line Restaurant Backend System using Python**

## The system needs to take orders from multiple customers at a time, the orders need to be saved in a file and the dashboard that needs to read the orders from the file and display them as no of orders & total revenue generated.


## **Module 1: restaurant_core.py**
1. Allow multiple customers to send the orders(item name, price) into a shared resource simulatenously. No duplicates or no order should miss. See what happens when all customer's orders are stored at a time and solve if any problem occurs write in the observation.
**Hints:** Use ``threading module``, understand its usage for the project & write the code.

2. After finishing the processing of every order, the data needs to write in a file as ``live_ledger.txt``.
**Hints:** Use ``mmap module``, understand its usage for the project & write the code.
Write what is happenning internally here.


## **Module 2: dashboard.py**
1. The dashboard needs to be read the orders from the file and display the No of Orders and Total Revenue.
2. Try to access the orders from the shared resource of ``restaurant_core.py``. If you can access it then process it & display the data. Write the Reason in the observations file.
3. If you cannot access it then read the orders from ``live_ledger.txt`` and display the data.
4. The dashboard needs to collect the for ``every 3 seconds`` and display the required data.
**Hints:** Use ``mmap module, time module`` to build this module.