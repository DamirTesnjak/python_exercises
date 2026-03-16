def filter_messages(messages):
    filtered_messages = []
    dang_counts = []

    for message in messages:
        messages_split = message.split()

        good_words = []
        dangs_list = []

        for word in messages_split:
            if word == "dang":
                dangs_list.append(word)
            else:
                good_words.append(word)
        good_sentence = " ".join(good_words)
        filtered_messages.append(good_sentence)

        count_of_dangs = len(dangs_list)
        dang_counts.append(count_of_dangs)
    return filtered_messages, dang_counts
