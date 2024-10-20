# TODO Найдите количество книг, которое можно разместить на дискете

I_in_Megabytes=1.44
pages_num=100
lines_num=50
simvs_num=25
simv_hranenie=4

I=I_in_Megabytes*1024*1024
one_book=pages_num*lines_num*simvs_num*simv_hranenie
count=int(I/one_book)


print("Количество книг, помещающихся на дискету:", count)
