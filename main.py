import random

def main():
    print("数当てゲームを始めます！")
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("1から100までの整数を入力してください: "))
        attempts += 1

        if guess < target_number:
            print("もっと大きい数です。")
        elif guess > target_number:
            print("もっと小さい数です。")
        else:
            print(f"おめでとう！{target_number}を当てました！")
            print(f"試行回数: {attempts}")
            break

if __name__ == "__main__":
    main()
