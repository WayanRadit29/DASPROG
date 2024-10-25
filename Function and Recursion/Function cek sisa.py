def ceksisa(apel, orang ):
    a = apel % orang
    print(f"Sisa apel : {a}")



apel = int(input("Input total apel : "))
orang = int(input("Akan dibagikan ke berapa orang? : "))
ceksisa(apel, orang)