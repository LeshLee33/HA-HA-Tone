!!! **Когда будете работать с гитом, делайте это из корневой папки, то есть не из client или server, a из папки, где у вас весь проект.**

!!! Работаем с веткой dev

### Если до этого не пушили и не пуллили:
```
git remote add origin https://github.com/LeshLee33/HA-HA-Tone.git
```

Если вы работаете в PyCharm, то просто в самой IDE добавляйте аккаунт и выбирайте репозиторий HA-HA-Tone

### Если хотите запулить изменения, то есть загрузить их себе на компьютер (**ДЕЛАТЬ ПЕРЕД КАЖДЫМ СЕАНСОМ НАПИСАНИЯ КОДА!**):
```
git branch -M dev
git pull
```

### Если хотите запушить изменения, то есть загрузить их в удалённый репозиторий (ветка dev):
```
git add .
git commit -m "название коммита"
git branch -M dev
git push -u origin dev
```

---

# FRONT-END

Тот, кто будет делать нам frontend-составляющую, должен здесь указать, что он использует

---

# MongoDB

### ДЛЯ ТЕСТЕРОВ

Для работы с MongoDB необходимо его, собственно скачать на ПК вместе с прииложением-админкой Compass

ОБЯЗАТЕЛЬНО указываем при настройке IP localhost или 127.0.0.1 и порт 27017