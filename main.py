def main():
    with open("books/frankenstein.txt") as f:
            file_contents = f.read()
    
    # Split the text into words
    words = file_contents.split()
    
    # Create a int to hold word count  
    word_count = 0
    words_lower = ""
    # letter counters
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    e_count = 0
    f_count = 0
    g_count = 0
    h_count = 0
    i_count = 0
    j_count = 0
    k_count = 0
    l_count = 0
    m_count = 0
    n_count = 0
    o_count = 0
    p_count = 0
    q_count = 0
    r_count = 0
    s_count = 0
    t_count = 0
    u_count = 0
    v_count = 0
    w_count = 0
    x_count = 0
    y_count = 0
    z_count = 0
    space_count = 0

    # Loop through the text and count spaces
    for letter in file_contents:
        if letter == " ":
            space_count += 1
    # Loop through the words and count them
    for word in words:
          word_count += 1
          words_lower = word.lower()
          for letter in words_lower:
            if letter == "a":
                a_count += 1
            elif letter == "b":
                b_count += 1
            elif letter == "c":
                c_count += 1
            elif letter == "d":
                d_count += 1
            elif letter == "e":
                e_count += 1
            elif letter == "f":
                f_count += 1
            elif letter == "g":
                g_count += 1
            elif letter == "h":
                h_count += 1
            elif letter == "i":
                i_count += 1
            elif letter == "j":
                j_count += 1
            elif letter == "k":
                k_count += 1
            elif letter == "l":
                l_count += 1
            elif letter == "m":
                m_count += 1
            elif letter == "n":
                n_count += 1
            elif letter == "o":
                o_count += 1
            elif letter == "p":
                p_count += 1
            elif letter == "q":
                q_count += 1
            elif letter == "r":
                r_count += 1
            elif letter == "s":
                s_count += 1
            elif letter == "t":
                t_count += 1
            elif letter == "u":
                u_count += 1
            elif letter == "v":
                v_count += 1
            elif letter == "w":
                w_count += 1
            elif letter == "x":
                x_count += 1
            elif letter == "y":
                y_count += 1
            elif letter == "z":
                z_count += 1
            else:
                pass
    # Print the results
    print("--- Begin report of books/frankenstein.txt ---")
    # Print the word count
    print(f"Word count: {word_count}")
    #createing space
    print(" ")
    print(" ")
    # Print the letter counts
    print(f"'a': {a_count}")
    print(f"'b': {b_count}")
    print(f"'c': {c_count}") 
    print(f"'d': {d_count}")
    print(f"'e': {e_count}")
    print(f"'f': {f_count}")
    print(f"'g': {g_count}")
    print(f"'h': {h_count}")
    print(f"'i': {i_count}")
    print(f"'j': {j_count}")
    print(f"'k': {k_count}")
    print(f"'l': {l_count}")
    print(f"'m': {m_count}")
    print(f"'n': {n_count}")
    print(f"'o': {o_count}")
    print(f"'p': {p_count}")
    print(f"'q': {q_count}")
    print(f"'r': {r_count}")
    print(f"'s': {s_count}")
    print(f"'t': {t_count}")
    print(f"'u': {u_count}")
    print(f"'v': {v_count}")
    print(f"'w': {w_count}")
    print(f"'x': {x_count}")
    print(f"'y': {y_count}")
    print(f"'z': {z_count}")
    print("--- End report of books/frankenstein.txt ---")
main()