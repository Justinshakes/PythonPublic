def check_file_type(file):
    file_type_mapping = {
        "gif": "image/gif",
        "png": "image/png",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }

    file_array = file.split(".")
    file_type = file_array[-1].lower().strip()

    return file_type_mapping.get(file_type, "application/octet-stream")


def main():
    file = input("File name: ")
    print(check_file_type(file))


if __name__ == "__main__":
    main()
