import time
import os

# ====== PENGATURAN ======
DELAY = 0.8   # Ubah ke 1.0 kalau mau lebih lambat
# =========================

maze = [
    [1,1,0,1,1,0,1,1],
    [0,1,0,1,0,1,0,1],
    [1,1,1,1,0,1,1,1],
    [1,0,0,1,1,1,0,0],
    [1,1,1,0,0,1,1,1],
    [0,0,1,1,1,0,0,1],
    [1,1,1,0,1,1,1,1],
    [0,0,1,1,1,0,0,1]
]

N = len(maze)
solution = [[0]*N for _ in range(N)]

steps = 0
backtracks = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_maze(x=None, y=None, message=""):
    clear()
    print(message)
    print(f"Langkah: {steps} | Backtrack: {backtracks}\n")
    
    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                print("S", end=" ")
            elif i == N-1 and j == N-1:
                print("G", end=" ")
            elif i == x and j == y:
                print("🐭", end=" ")
            elif solution[i][j] == 1:
                print("*", end=" ")
            elif maze[i][j] == 0:
                print("█", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
    time.sleep(DELAY)

def is_safe(x, y):
    return 0 <= x < N and 0 <= y < N and maze[x][y] == 1 and solution[x][y] == 0

def solve(x, y):
    global steps, backtracks

    if x == N-1 and y == N-1:
        solution[x][y] = 1
        print_maze(x, y, "🎉 Sampai tujuan!")
        return True

    if is_safe(x, y):
        solution[x][y] = 1
        steps += 1
        print_maze(x, y, f"➡ Gerak ke ({x},{y})")

        # Urutan gerakan: bawah, kanan, atas, kiri
        if solve(x+1, y): return True
        if solve(x, y+1): return True
        if solve(x-1, y): return True
        if solve(x, y-1): return True

        # BACKTRACK
        solution[x][y] = 0
        backtracks += 1
        print_maze(x, y, f"↩ Backtrack dari ({x},{y})")

    return False


if solve(0,0):
    print("✅ Jalur ditemukan!")
else:
    print("❌ Tidak ada jalur.")