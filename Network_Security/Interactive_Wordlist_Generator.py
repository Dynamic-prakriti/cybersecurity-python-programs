"""
PyCrunch - Interactive Wordlist Generator
Inspired by Crunch

Author: @atlasilim
Educational use only.
"""

import argparse
import itertools
import sys
import os
import time
import math
import signal

VERSION = "1.0.0"
BUFFER_SIZE = 10 * 1024 * 1024
DEFAULT_CHARSET = "abcdefghijklmnopqrstuvwxyz"

CRUNCH_PATTERNS = {
    '@': "abcdefghijklmnopqrstuvwxyz",
    ',': "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    '%': "0123456789",
    '^': "!@#$%^&*()-_+=~`[]{}|\\:;\"'<>,.?/"
}

def signal_handler(sig, frame):
    print("\n\n[!] Process cancelled by user.")
    sys.exit(0)

def calculate_size(min_len, max_len, charset_len, joiner="", limit=None):
    total_bytes = 0
    newline_len = len(os.linesep) if not joiner else len(joiner)
    words_counted = 0
    
    for length in range(min_len, max_len + 1):
        num_combinations = charset_len ** length
        
        if limit:
            remaining_limit = limit - words_counted
            current_count = min(num_combinations, remaining_limit)
        else:
            current_count = num_combinations
            
        line_size = length + newline_len
        total_bytes += current_count * line_size
        words_counted += current_count
        
        if limit and words_counted >= limit:
            break
            
    return total_bytes

def format_size(size_bytes):
    if size_bytes == 0: return "0 B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"

def generate_wordlist(min_len, max_len, charset, output_file, limit=None):
    start_time = time.time()
    charset_list = list(charset)
    charset_len = len(charset_list)
    
    if charset_len == 0:
        print("[!] Error: Charset cannot be empty.")
        sys.exit(1)

    print(f"[*] Analyzing...")
    total_size = calculate_size(min_len, max_len, charset_len, limit=limit)
    formatted_size = format_size(total_size)
    
    print(f"--- PyCrunch v{VERSION} ---")
    print(f"[*] Charset      : {charset} (Length: {charset_len})")
    print(f"[*] Length       : {min_len} - {max_len}")
    if limit:
        print(f"[*] Word Limit   : {limit}")
    print(f"[*] Est. Size    : {formatted_size}")
    if output_file:
        print(f"[*] Output File  : {output_file}")
    else:
        print(f"[*] Output       : STDOUT")
    
    if output_file:
        try:
            f = open(output_file, 'w', encoding='utf-8', buffering=BUFFER_SIZE)
        except OSError as e:
            print(f"[!] File opening error: {e}")
            sys.exit(1)
    else:
        f = sys.stdout

    total_combinations = sum(charset_len ** l for l in range(min_len, max_len + 1))
    if limit:
        total_to_generate = min(total_combinations, limit)
    else:
        total_to_generate = total_combinations

    counter = 0
    last_update = time.time()
    
    try:
        for length in range(min_len, max_len + 1):
            if limit and counter >= limit:
                break
                
            for p in itertools.product(charset_list, repeat=length):
                word = "".join(p) + "\n"
                f.write(word)
                counter += 1
                
                if limit and counter >= limit:
                    break
                
                if output_file and time.time() - last_update > 0.5:
                    percent = (counter / total_to_generate) * 100
                    elapsed = time.time() - start_time
                    speed = counter / elapsed if elapsed > 0 else 0
                    remaining = (total_to_generate - counter) / speed if speed > 0 else 0
                    
                    sys.stdout.write(f"\r[%] Progress: {percent:.2f}% | Speed: {int(speed)} w/s | ETA: {int(remaining)}s ")
                    sys.stdout.flush()
                    last_update = time.time()
                    
    except KeyboardInterrupt:
        print("\n[!] Operation interrupted.")
    finally:
        if output_file and f:
            f.close()
            print(f"\n[*] Finished! File: {output_file}")
            print(f"[*] Total Words: {counter}")

def get_char_list_from_pattern_char(char):
    if char in CRUNCH_PATTERNS:
        return list(CRUNCH_PATTERNS[char])
    return [char]

def generate_with_pattern(pattern, output_file, limit=None):
    start_time = time.time()
    generators = []
    
    for char in pattern:
        generators.append(get_char_list_from_pattern_char(char))
    
    total_combinations = 1
    for gen in generators:
        total_combinations *= len(gen)
    
    if limit:
        total_to_generate = min(total_combinations, limit)
    else:
        total_to_generate = total_combinations
        
    line_len = len(pattern) + len(os.linesep)
    total_size = total_to_generate * line_len
    formatted_size = format_size(total_size)
    
    print(f"[*] Pattern      : {pattern}")
    if limit:
        print(f"[*] Word Limit   : {limit}")
    print(f"[*] Est. Size    : {formatted_size}")
    
    if output_file:
        try:
            f = open(output_file, 'w', encoding='utf-8', buffering=BUFFER_SIZE)
        except OSError as e:
            print(f"[!] File opening error: {e}")
            sys.exit(1)
    else:
        f = sys.stdout

    counter = 0
    last_update = time.time()

    try:
        for p in itertools.product(*generators):
            word = "".join(p) + "\n"
            f.write(word)
            counter += 1

            if limit and counter >= limit:
                break

            if output_file and time.time() - last_update > 0.5:
                percent = (counter / total_to_generate) * 100
                elapsed = time.time() - start_time
                speed = counter / elapsed if elapsed > 0 else 0
                remaining = (total_to_generate - counter) / speed if speed > 0 else 0
                
                sys.stdout.write(f"\r[%] Progress: {percent:.2f}% | Speed: {int(speed)}/s | ETA: {int(remaining)}s ")
                sys.stdout.flush()
                last_update = time.time()

    except KeyboardInterrupt:
        print("\n[!] Operation interrupted.")
    finally:
        if output_file and f:
            f.close()
            print(f"\n[*] Finished! File: {output_file}")
            print(f"[*] Total: {counter}")

def main():
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(
        description=f"PyCrunch v{VERSION} - Professional Wordlist Generator",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Examples:\n"
               "  python pycrunch.py 4 4 abcdef -o list.txt\n"
               "  python pycrunch.py 6 8 -o numbers.txt -l 5000\n"
               "  python pycrunch.py -t p@ss%% -o pattern.txt\n"
               "    @ = a-z\n"
               "    , = A-Z\n"
               "    % = 0-9\n"
               "    ^ = symbols"
    )
    
    parser.add_argument("min", type=int, nargs='?', help="Min length (required if no pattern)")
    parser.add_argument("max", type=int, nargs='?', help="Max length (required if no pattern)")
    parser.add_argument("chars", type=str, nargs='?', default=DEFAULT_CHARSET, help="Characters to use")
    parser.add_argument("-o", "--output", help="Output file")
    parser.add_argument("-t", "--pattern", help="Pattern use")
    parser.add_argument("-l", "--limit", type=int, help="Max words to generate")
    
    args = parser.parse_args()

    if args.pattern:
        generate_with_pattern(args.pattern, args.output, args.limit)
        sys.exit(0)
    
    if args.min is None or args.max is None:
        parser.print_help()
        print("\n[!] Error: Min and max values are required if pattern is not used.")
        sys.exit(1)

    if args.min > args.max:
        print("[!] Error: Min length cannot be greater than max.")
        sys.exit(1)

    generate_wordlist(args.min, args.max, args.chars, args.output, args.limit)

if __name__ == "__main__":
    main()
