def cekkeganjilan(list_bil):
    count = 0
    for i in list_bil:
        if i % 2 == 1:
            count += 1
    print(f"banyak bilangan ganjil ada {count}")


bilangan = list(map(int,input().split(',')))

cekkeganjilan(bilangan)

