from cryptography import fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABb9tALPXJcJTSm4zmh_HXOVMolZXj21sZYT8o39c4-HKB6kN2VUv1_weXczWUQsgYolYgRtUD_OExqbOSvFfN4BaGFjE-xN3PMCqFPf8D6xFdfglG4Vey6EKrxu8AZqKrvk6e0NBoZ999PKveoKXXrVtYXyF-HEbp8j8-uCxpNRepZpfc='

def main():
    f = fernet.Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
