# تعریف دیکشنری برای ذخیره نتایج
genres = {
    "Horror": 0,
    "Romance": 0,
    "Comedy": 0,
    "History": 0,
    "Adventure": 0,
    "Action": 0,
}

# خواندن تعداد افراد
n = int(input())

# خواندن اسامی و ژانرهای مورد علاقه هر فرد
people = []
for i in range(n):
    name, *genres_list = input().split()
    people.append((name , genres_list))

# شمارش ژانرهای مورد علاقه هر فرد
for name, genres_list in people:
    for genre in genres_list:
        if genre in genres:
            genres[genre] += 1

# مرتب‌سازی ژانرها بر اساس تعداد علاقه‌مندی
sorted_genres = sorted(genres.items(), key=lambda x: (-x[1], x[0]))

# چاپ نتایج به ترتیب تعداد علاقه‌مندی
for genre, count in sorted_genres:
    print(f"{genre} : {count}")