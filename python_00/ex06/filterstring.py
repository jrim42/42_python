import sys

def filter_words_by_length(S, N):
    assert isinstance(S, str) and isinstance(N, int), "the arguments are bad"
    words = S.split()
    return [word for word in words if len(word) > N]

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
    else:
        try:
            S = sys.argv[1]
            N = int(sys.argv[2])
            filtered_words = filter_words_by_length(S, N)
            print(filtered_words)
        except ValueError:
            print("AssertionError: the arguments are bad")
