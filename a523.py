def remove_duplicates(lst):
    """
    Remove duplicate integers from a list while preserving order.
    
    Args:
        lst: List of integers
    
    Returns:
        List with duplicates removed
    """
    seen = set()
    result = []
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
    return result


def main():
    # Example usage
    numbers = [1, 2, 3, 2, 4, 1, 5, 3, 6]
    print(f"Original list: {numbers}")
    
    unique_numbers = remove_duplicates(numbers)
    print(f"List without duplicates: {unique_numbers}")


if __name__ == "__main__":
    main()
