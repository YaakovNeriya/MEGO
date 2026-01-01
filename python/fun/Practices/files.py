with open("data.txt", "a+") as file:
    coic=""
    while coic!="y":
        data=input("enter data to write to file: ")[:225]
        file.write(data+"\n")
        print("data written to file.")
        file.seek(0)
        print(f"\nfile contents {len(file.read())} characters.")
        file.seek(0)
        print("file contents:")
        print(file.read())

        file.seek(0)
        chars={}
        data=file.read(1)
        while data !="":
            if data in chars:
                chars[data]+=1
            elif data=="\n":
                pass
            else:
                chars[data]=1
            data = file.read(1)
        print("character counts:")
        for k,v in chars.items():
            print(f"'{k}': {v}")

        coic=input("do you want to exit? ( y/n ): ").lower()

