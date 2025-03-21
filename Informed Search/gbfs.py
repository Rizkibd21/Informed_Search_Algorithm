# -*- coding: utf-8 -*-
"""GBFS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gzJT_b3XcYy0XLHMOCYk7r_xfm4CCZ54
"""

from queue import PriorityQueue

# Fungsi untuk algoritma Greedy Search
def greedy_search(graph, start, goal):
    frontier = PriorityQueue()  # Antrian prioritas untuk menyimpan simpul yang akan dieksplorasi
    frontier.put((0, start))  # Menambahkan simpul awal ke dalam antrian dengan nilai prioritas 0
    explored = set()  # Set untuk menyimpan simpul yang sudah dieksplorasi
    path = {}

    while not frontier.empty():
        # Get the item from the priority queue
        current_item = frontier.get()
        # The actual node is the second element of the tuple
        current = current_item[1]

        if current == goal:
            print("Simpul tujuan sudah ditemukan!")
            route = reconstruct_path(path, start, goal)
            print("Jalur terpendek:", route)
            return True  # Mengembalikan True jika simpul tujuan sudah ditemukan

        explored.add(current)  # Menandai simpul saat ini sebagai sudah dieksplorasi

        for neighbor in graph[current]:
            if neighbor not in explored:
                priority = heuristic[neighbor]  # Menggunakan nilai heuristik untuk menentukan prioritas
                frontier.put((priority, neighbor))
                path[neighbor] = current  # Menambahkan simpul tetangga ke dalam antrian dengan nilai prioritas heuristik

    print("Simpul tujuan tidak ditemukan!")
    return False  # Mengembalikan False jika simpul tujuan tidak ditemukan

# ... (rest of your code remains the same) ...

def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
        current = path[current]
        route.append(current)
    route.reverse()
    return route

# Daftar heuristik untuk setiap simpul
heuristic = {
    'A': 4,
    'B': 3,
    'C': 3,
    'D': 1,
    'S': 6,
    'G': 0
}

# Graf (dalam bentuk daftar kejadian)
graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'B': 1, 'D': 5},
    'B': {'C': 2, 'D': 3},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1},
}

# Titik awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Panggil fungsi greedy search
greedy_search(graph, start_node, goal_node)