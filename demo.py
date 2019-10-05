# Demo file
import time

if __name__ == "__main__":
	while True:
		for i in range(40):
			time.sleep(0.02)
			print(" " * i, end="")
			print("Frank")
		for i in range(40, 0, -1):
			time.sleep(0.02)
			print(" " * i, end="")
			print("Ass we can")
