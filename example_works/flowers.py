"""
condition: price for a single flower (narcissus, tulip, rose) and amount of money

the function calculates the number of options for bouquets that can be made, without exceeding the amount of money

and not counting an even number of colors
"""

def bouquets(narcissus_price, tulip_price, rose_price, summ):
    answer=0
    counter=1
    s=[narcissus_price, tulip_price, rose_price]
    s=sorted(s)
    narcissus_price=s[0] 
    tulip_price=s[1]
    rose_price=s[2]

    def two_flowers(def_count):
        def_count=def_count-1
        inside_answer=0
        z=1

        def tree_flowers(constant_summ, second_count):
            mix_answer=0
            r=1
            for i in range (second_count):
                if constant_summ+((second_count-1)*tulip_price)+rose_price*r<=summ:
                    mix_answer=mix_answer+1
                    r=r+1
                    second_count=second_count-1
            return mix_answer

        while (def_count*narcissus_price)+(tulip_price*z)<=summ and def_count>=0:
            inside_answer=inside_answer+1
            inside_answer=inside_answer+tree_flowers((def_count*narcissus_price),z)
            def_count=def_count-1
            z=z+1

        return inside_answer

    while counter*narcissus_price<=summ:
        answer=answer+1
        answer=answer+(two_flowers(counter))
        counter=counter+2

    return answer

print (bouquets(1,2,3,10))
