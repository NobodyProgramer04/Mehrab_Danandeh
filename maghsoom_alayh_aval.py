"""
برنامه‌ای بنویسید که 10 عدد از ورودی بخواند و در انتها عددی که بیشترین تعداد مقسوم‌علیه عدد اول را دارد به همراه تعداد مقسوم‌علیه‌های اول
آن، در خروجی چاپ کند. اگر چند عدد این حالت را داشتند، بزرگترین آن‌ها را چاپ کند.
"""
#chatgpt help
def prime_factors(n):
    """Return a set of the prime factors of a positive integer."""
    factors = set()
    d = 2
    while n > 1:
        while n % d == 0:
            factors.add(d)
            n //= d
        d += 1
        if d*d > n:
            if n > 1:
                factors.add(n)
            break
    return factors

numbers = []
for i in range(10):
    num = int(input(""))
    numbers.append(num)

max_count = 0
max_prime = None

for num in numbers:
    factors = prime_factors(num)
    count = len(factors)
    if count > max_count:
        max_count = count
        max_prime = num
    elif count == max_count and num > max_prime:
        max_prime = num

print(max_prime, max_count)