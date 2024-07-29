import timeit

def boyer_moore(text, pattern):
    print("Starting Boyer-Moore...")
    m = len(pattern)
    n = len(text)
    if m > n:
        return -1
    skip = {}
    for k in range(len(pattern)):
        skip[pattern[k]] = m - k - 1
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            return i + 1
        k += skip.get(text[k], m)
    print("Boyer-Moore finished.")
    return -1

def knuth_morris_pratt(text, pattern):
    print("Starting Knuth-Morris-Pratt...")
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0
    compute_lps_array(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    print("Knuth-Morris-Pratt finished.")
    return -1

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

def rabin_karp(text, pattern, q=101):
    print("Starting Rabin-Karp...")
    d = 256
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m-1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    print("Rabin-Karp finished.")
    return -1

# Читання текстових файлів
def read_text_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

# Зменшення розміру тексту до 100 символів
text1 = read_text_file('C:\\Users\\shuri\\Algorith_GoIT\\goit-algo-hw-05\\artikel_1.txt')[:100]
text2 = read_text_file('C:\\Users\\shuri\\Algorith_GoIT\\goit-algo-hw-05\\artikel_2.txt')[:100]

pattern = "алгоритм"
non_existing_pattern = "неіснуючий шаблон"

algorithms = {
    "Boyer-Moore": boyer_moore,
    "Knuth-Morris-Pratt": knuth_morris_pratt,
    "Rabin-Karp": rabin_karp
}

# Функція для вимірювання часу виконання алгоритмів
def measure_time(algorithm, text, pattern):
    return timeit.timeit(lambda: algorithm(text, pattern), number=1)

for name, algorithm in algorithms.items():
    print(f"Testing {name} algorithm on Text 1...")
    time_existing = measure_time(algorithm, text1, pattern)
    time_non_existing = measure_time(algorithm, text1, non_existing_pattern)
    print(f"{name} (Text 1): Existing pattern - {time_existing:.6f} seconds")
    print(f"{name} (Text 1): Non-existing pattern - {time_non_existing:.6f} seconds")

    print(f"Testing {name} algorithm on Text 2...")
    time_existing = measure_time(algorithm, text2, pattern)
    time_non_existing = measure_time(algorithm, text2, non_existing_pattern)
    print(f"{name} (Text 2): Existing pattern - {time_existing:.6f} seconds")
    print(f"{name} (Text 2): Non-existing pattern - {time_non_existing:.6f} seconds")
