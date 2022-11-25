user_input = input("Enter your sentence: ")


def reverseWordsInSentence():
    # Using Two Pointers : for example : [h,l,l,e,o] . [->h,l,l,e,o<-] and ...
    def flip_in_place(left_p: int, right_p: int):
        while left_p < right_p:
            s_arr[left_p], s_arr[right_p] = s_arr[right_p], s_arr[left_p]
            left_p += 1
            right_p -= 1

    left = 0
    s_arr = list(user_input)
    # For Flipping words in their place
    for i in range(len(user_input)):
        if s_arr[i] == " ":
            flip_in_place(left, i - 1)
            left = i + 1
    flip_in_place(left, len(s_arr) - 1)

    # Converting from list to string for output
    str1 = " "
    reversed_final = str1.join(s_arr)
    return print("Each words in backwards : ", reversed_final)


reverseWordsInSentence()
