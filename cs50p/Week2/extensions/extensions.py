def main():
    name = input("File name: ").lower().strip()
    try:
        filetype = name.split(".")[2]

    except IndexError:
        try:
            filetype = name.split(".")[1]
        except IndexError:
            print("application/octet-stream")
            return

    match filetype:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")

main()
