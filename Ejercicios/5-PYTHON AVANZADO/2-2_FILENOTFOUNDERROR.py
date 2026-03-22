def read_file(filename):
    try:
        with open(filename) as f:
            contents = f.read()
            # print(f"Contenido de {filename}:")
            print(contents)
    except FileNotFoundError as e:
        pass
        # print(f"Error: {e}")


filenames = ["catss.txt", "dogs.txt"]
for f in filenames:
    read_file(f)
