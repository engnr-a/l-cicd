def main():
    """
    Prints a prominent, visible welcome message with a dynamic border.
    """
    message = "   🚀 Hello from GitHub Actions! 👋   "
    border = "=" * len(message)
    
    print(border)
    print(message)
    print(border)


if __name__ == "__main__":
    main()