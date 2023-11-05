from django.db import models


# ТУТ БУДЕТ КОД НАШИХ МОДЕЛЕЙ

# Создание моделей (классов, таблиц)

# создание таблицы Роли
class Role(models.Model):
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

# создание таблицы Пользователь
class User(models.Model):
    first_name = models.CharField('First_name', max_length=50)
    last_name = models.CharField('Last_name', max_length=50)
    nickname = models.CharField('Nickname', max_length=50)
    description = models.TextField('Discription')
    enabled = models.BooleanField('Enabled')
    birthday = models.DateField('Birthday')
    registration_date = models.DateField('Registration_date')
    id_role = models.ForeignKey(Role, on_delete=models.SET_NULL)

    def __str__(self):
        return self.first_name

# создание таблицы Посты
class Post(models.Model):
    title = models.CharField('Title', max_length=100)
    content = models.TextField('Content')
    date = models.DateField('Date')
    time = models.TimeField('Time')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


# создание таблицы Сообщения
class Messages(models.Model):
    content = models.TextField('Content')
    date = models.DateField('Date')
    time = models.TimeField('Time')
    user_id_from = models.ForeignKey(User, on_delete=models.SET_NULL)
    user_id_to = models.ForeignKey(User, on_delete=models.SET_NULL)

    def __str__(self):
        return self.content

# создание таблицы Подписки
class Following(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    user_id_followed = models.ForeignKey(User, on_delete=models.SET_NULL)

#Создание объектов
User.objects.create(first_name="Полина", last_name="Кобцева", nickname="POLYNOM", description="босс топ", enabled=1, birthday="25.10.2006", registration_date="24.02.2023", id_role=1)
User.objects.create(first_name="Татьяна", last_name="Таекина", nickname="TANGENS", description="а?", enabled=1, birthday="03.06.2006", registration_date="24.02.2023", id_role=1)
Role.objects.create(name="CEO")
Role.objects.create(name="Admin")
Post.objects.create(title="срочно!", content="Лалалалла", date="21.07.2023", time="4:20", user_id=1)
Messages.objects.create(content="шалом", date="01.09.2023", time="13:13", user_id_from=1, user_id_to=2)
Following.objects.create(user_id=1, user_id_followed=2)

#Обновление
user = User.objects.get(last_name="Кобцева")
user.last_name = "Захарова"
user.save()

#Удаление
post = Post.objects.get(title="срочно!")
post.delete()


