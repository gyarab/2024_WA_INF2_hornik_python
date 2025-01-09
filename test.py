def split_into_threes(text):
    if not isinstance(text, str):
        raise ValueError("Input musí být string! ")

    length = len(text)
    part_size = length // 3
    remainder = length % 3

    parts = [text[i:i+part_size] for i in range(0, length-remainder, part_size)]
    if remainder:
        parts.append(text[-remainder:])

    return parts


if __name__ == "__main__":
    chain = split_into_threes("123456789")
    print(chain)


