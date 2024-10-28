import time
from producer.main import send_data

def main():
    try:
        for _ in range(20):
            data = {
                "temperature": 22.5,
                "humidity": 60,
                "brightness": 300
            }
            send_data(data)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nExiting gracefully...")

if __name__ == '__main__':
    main()
