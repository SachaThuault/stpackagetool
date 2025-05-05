#!/usr/bin/env python3

import argparse

def main():
    parser = argparse.ArgumentParser(description="My awesome CLI tool")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--greet", type=str, help="Name to greet")
    
    args = parser.parse_args()
    
    if args.version:
        print("stpackagetool v0.1.0")
    elif args.greet:
        print(f"Hello, {args.greet}!")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()