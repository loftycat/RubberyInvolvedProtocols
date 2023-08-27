import time

def display_ring_toss():
    ring_toss = [
        "   __/ \\__ ",
        "  /       \\",
        " |         |",
        "  \\       /",
        "   \\__/_/"
    ]
    
    for line in ring_toss:
        print(line)
        time.sleep(0.3)

def main():
    print("輪投げゲームを始めます！")
    
    while True:
        display_ring_toss()
        
        play_again = input("もう一度プレイしますか？（y/n）: ")
        if play_again.lower() != "y":
            print("ゲームを終了します。お疲れ様でした！")
            break

if __name__ == "__main__":
    main()
