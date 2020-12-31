def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    print(num_bits)
    return num_bits

def main():
     print "hello world!"
     count_bits(5)

main()
print "Guru99"
