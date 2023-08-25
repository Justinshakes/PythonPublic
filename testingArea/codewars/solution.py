def process_string(input_str):
    sep_list = input_str.split(",")
    if len(sep_list) < 3:
        return None
    processed_str = " ".join(sep_list[1:-1])
    return processed_str

def main():
    input_str = '1,2,3'
    processed_str = process_string(input_str)
    print(processed_str)

if __name__ == "__main__":
    main()
