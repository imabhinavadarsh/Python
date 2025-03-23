from collections import Counter

def anagrams_check():
    try:
        s1 = input("Enter the first string: ").strip()
        s2 = input("Enter the second string: ").strip()

        if not s1 or not s2:
            raise ValueError("Both strings must be non-empty.")

        s1_clean = s1.replace(" ", "").lower()
        s2_clean = s2.replace(" ", "").lower()

        if Counter(s1_clean) == Counter(s2_clean):
            print("Strings are anagrams.")
        else:
            print("Strings are NOT anagrams.")

    except ValueError as e:
        print(f"Input error: {e}")
