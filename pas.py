# Ultimate_Password_Generator_Pro_Plus_by_N00B_B0SS.py
import time
import os
import sys

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}🔐 ULTIMATE PASSWORD GENERATOR PRO PLUS{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.PURPLE}Developer: {Colors.CYAN}N00B B0SS{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")

def show_menu():
    print(f"{Colors.WHITE}1. {Colors.GREEN}Text + Number (Pass123){Colors.END}")
    print(f"{Colors.WHITE}2. {Colors.GREEN}Numbers Only (00000000-99999999){Colors.END}")
    print(f"{Colors.WHITE}3. {Colors.RED}Exit{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}")

def validate_input(prompt, input_type=str, default=None, min_val=None, max_val=None):
    while True:
        try:
            user_input = input(prompt)
            if not user_input and default is not None:
                return default
            
            if input_type == int:
                user_input = int(user_input)
                if min_val is not None and user_input < min_val:
                    print(f"{Colors.RED}❌ Value must be at least {min_val}{Colors.END}")
                    continue
                if max_val is not None and user_input > max_val:
                    print(f"{Colors.RED}❌ Value must be at most {max_val}{Colors.END}")
                    continue
            return user_input
        except ValueError:
            print(f"{Colors.RED}❌ Invalid input! Please enter a valid {input_type.__name__}{Colors.END}")

def generate_text_numeric():
    print(f"\n{Colors.GREEN}{'='*60}{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}📝 TEXT + NUMBER MODE{Colors.END}")
    print(f"{Colors.GREEN}{'='*60}{Colors.END}")
    
    prefix = validate_input(f"{Colors.WHITE}Enter text prefix (default: 'Pass'): {Colors.CYAN}", default="Pass")
    separator = validate_input(f"{Colors.WHITE}Enter separator (@/#/_ or leave blank): {Colors.CYAN}", default="")
    digits = validate_input(f"{Colors.WHITE}How many digits? (default: 4): {Colors.CYAN}", 
                          input_type=int, default=4, min_val=1, max_val=20)
    
    max_num = 10**digits - 1
    start = validate_input(f"{Colors.WHITE}Start number (0-{max_num}): {Colors.CYAN}", 
                         input_type=int, default=0, min_val=0, max_val=max_num)
    end = validate_input(f"{Colors.WHITE}End number (max {max_num}): {Colors.CYAN}", 
                       input_type=int, default=max_num, min_val=start, max_val=max_num)
    
    return [f"{prefix}{separator}{i:0{digits}d}" for i in range(start, end+1)], f"{prefix}_{digits}digits.txt"

def generate_numeric_only():
    print(f"\n{Colors.GREEN}{'='*60}{Colors.END}")
    print(f"{Colors.YELLOW}{Colors.BOLD}🔢 NUMERIC ONLY MODE{Colors.END}")
    print(f"{Colors.GREEN}{'='*60}{Colors.END}")
    
    digits = validate_input(f"{Colors.WHITE}How many digits? (default: 8): {Colors.CYAN}", 
                          input_type=int, default=8, min_val=1, max_val=20)
    
    max_num = 10**digits - 1
    start = validate_input(f"{Colors.WHITE}Start number (0-{max_num}): {Colors.CYAN}", 
                         input_type=int, default=0, min_val=0, max_val=max_num)
    end = validate_input(f"{Colors.WHITE}End number (max {max_num}): {Colors.CYAN}", 
                       input_type=int, default=max_num, min_val=start, max_val=max_num)
    
    return [f"{i:0{digits}d}" for i in range(start, end+1)], f"numeric_{digits}digits.txt"

def save_to_file(passwords, filename):
    try:
        start_time = time.time()
        total = len(passwords)
        
        print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
        print(f"{Colors.YELLOW}⚡ Generating {Colors.CYAN}{total:,}{Colors.YELLOW} passwords...{Colors.END}")
        print(f"{Colors.BLUE}{'='*60}{Colors.END}")
        
        # Check available disk space
        free_space = get_free_space()
        estimated_size = total * (len(passwords[0]) + 1) / (1024**2)  # MB
        if free_space < estimated_size * 1.5:
            print(f"{Colors.RED}❌ Not enough disk space! Required: {estimated_size:.2f}MB, Available: {free_space:.2f}MB{Colors.END}")
            return
        
        with open(filename, 'w') as f:
            chunk_size = 100000
            for i in range(0, total, chunk_size):
                chunk = passwords[i:i+chunk_size]
                f.write('\n'.join(chunk) + '\n')
                progress = min(i+chunk_size, total)
                print(f"{Colors.GREEN}Progress: {Colors.CYAN}{progress:,}/{total:,} {Colors.YELLOW}({(progress/total*100):.1f}%){Colors.END}", end='\r')
        
        file_size = os.path.getsize(filename)/(1024**2)
        
        print(f"\n\n{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.YELLOW}{Colors.BOLD}✅ GENERATION COMPLETE!{Colors.END}")
        print(f"{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.WHITE}📂 File: {Colors.CYAN}{filename}{Colors.END}")
        print(f"{Colors.WHITE}📦 Size: {Colors.CYAN}{file_size:.2f} MB{Colors.END}")
        print(f"{Colors.WHITE}⏱️ Time: {Colors.CYAN}{time.time()-start_time:.2f} seconds{Colors.END}")
        print(f"{Colors.GREEN}{'='*60}{Colors.END}")
        print(f"{Colors.PURPLE}Developer: {Colors.CYAN}N00B B0SS{Colors.END}")
        print(f"{Colors.GREEN}{'='*60}{Colors.END}")
    
    except PermissionError:
        print(f"\n{Colors.RED}❌ Permission denied! Cannot write to file.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}❌ Unexpected error: {str(e)}{Colors.END}")

def get_free_space():
    if os.name == 'nt':
        import ctypes
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p('.'), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / (1024**2)
    else:
        stat = os.statvfs('.')
        return stat.f_bavail * stat.f_frsize / (1024**2)

def main():
    while True:
        try:
            show_banner()
            show_menu()
            choice = validate_input(f"{Colors.WHITE}Select mode (1/2/3): {Colors.CYAN}", 
                                  input_type=int, default=1, min_val=1, max_val=3)
            
            if choice == 1:
                passwords, filename = generate_text_numeric()
                save_to_file(passwords, filename)
            elif choice == 2:
                passwords, filename = generate_numeric_only()
                save_to_file(passwords, filename)
            elif choice == 3:
                print(f"\n{Colors.YELLOW}Thanks for using Password Generator by {Colors.CYAN}N00B B0SS!{Colors.END}")
                break
            
            input(f"\n{Colors.WHITE}Press Enter to continue...{Colors.END}")
        except KeyboardInterrupt:
            print(f"\n{Colors.RED}🚫 Operation cancelled by user.{Colors.END}")
            break
        except Exception as e:
            print(f"\n{Colors.RED}❌ Critical error: {str(e)}{Colors.END}")
            input(f"{Colors.WHITE}Press Enter to restart...{Colors.END}")

if __name__ == "__main__":
    main()
