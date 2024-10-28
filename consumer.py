import time
from consumer.main import process_message, close_consumer

def main():
    try:
        while True:
            process_message()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nExiting gracefully...")
    finally:
        close_consumer()

if __name__ == "__main__":
    main()
