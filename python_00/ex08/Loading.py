def ft_tqdm(lst: range) -> None:
    total = len(lst)
    width = 40  # Width of the progress bar
    last_progress = -1
    
    for i, item in enumerate(lst):
        progress = int((i + 1) / total * width)
        
        if progress != last_progress:
            bar = "|" + "=" * progress + ">" + "." * (width - progress) + "|"
            percent_complete = int((i + 1) / total * 100)
            eta = f"{(total - i - 1) * 0.005:.2f}s"
            print(f"{percent_complete}%|{bar}| {i + 1}/{total} [{eta}] ", end="\r")
            last_progress = progress
        
        yield item

    print("100%|[===============================================================>]|", f"{total}/{total}")

# Example usage:
if __name__ == "__main__":
    from time import sleep
    
    # Using ft_tqdm
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    
    print()  # Newline for separation
