from producer.main import send_data

def main():
    try:
        send_data()
    except KeyboardInterrupt:
        print("\nExiting gracefully...")

if __name__ == '__main__':
    main()
