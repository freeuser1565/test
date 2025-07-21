# password_generator.py
import time

def generate_passwords():
    try:
        start_time = time.time()
        total = 10001
        
        with open('password_list.txt', 'w') as f:
            for i in range(total):
                pwd = f"Baraka@{i:05d}" if i < 10000 else f"Baraka@{i}"
                f.write(f"{i+1}. {pwd}\n")
                
                # Progress indicator
                if i % 1000 == 0 or i == total-1:
                    print(f"\rGenerated {i+1}/{total} passwords...", end='')
        
        print(f"\n✔ Success! Time taken: {time.time()-start_time:.2f} seconds")
    
    except Exception as e:
        print(f"\n✖ Error: {str(e)}")

if __name__ == "__main__":
    print("🔐 Password Generator v1.0")
    generate_passwords()
