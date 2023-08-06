def check_file_type(file):
    file_array = file.split('.')
    file_type = file_array[-1].lower().strip()

    match file_type:
        case "gif" | "png":
            return "image/" + file_type
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


def main():
    file = input("File name: ")
    print(check_file_type(file))


if __name__ == "__main__":
    main()
