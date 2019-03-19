import io

filename = "file.text"
mode = "r"

try:
    with open(filename, mode) as fp:
        content = fp.read()
        print(content)

except FileNotFoundError:
    print(filename, "not found. Please check if the file's name is correct.")
except io.UnsupportedOperation:
    print("Are you sure", filename, "is readable?")
except Exception as e:
    print(e)
