## Что такое Ansible?

Ansible — это программное решение для удаленного управления конфигурациями. Оно позволяет настраивать удаленные машины. Главное его отличие от других подобных систем в том, что Ansible использует существующую инфраструктуру SSH, в то время как другие (chef, puppet, и пр.) требуют установки специального PKI-окружения.

Оно написано на языке программирования python и языке разметки YAML для описания разметки.

Поддерживается управление как Linux узлами, так и Windows, но все же чаще первое.

В 2015 году вошла в Red Hat Inc. Входит в большинство дистрибутивов для Linux.

***Интересный факт***: Словом «**Ansible**» названа вымышленная система мгновенной гиперпространственной связи. Эта система была в мире ***Игра Эндера*** Орсона С. Карда, само слово придумано **Урсулой Ле Гуин** в романе **Мир Роканнона** (1966).



## Ключевые особенности

- **Безагентное**. В клиенте не установлено программное обеспечение или агент, который общается с сервером.
- **Идемпотентное**. Независимо от того, сколько раз вы вызываете операцию, результат будет одинаковым.
- **Простое и расширяемое**. Программа Ansible написанa на Python и использует YAML для написания команд. Оба языка считаются относительно простыми в изучении.

Изображение: [Применяем Ansible (slideshare.net)](https://www.slideshare.net/alexsvetkin/ansible-79835964)

## Инициализация

На контролирующей машине инженера (контроллере): можно посмотреть подробную [документацию](https://docs.ansible.com/ansible/devel/installation_guide/intro_installation.html#installing-ansible-on-windows). Для установки необходимы: командная строка и текстовый редактор.

На серверах: установка Ansible не требуется. Необходимы: python 2.7 или выше, доступ по SSH с контроллера.

Краткая инструкция: 

1. git clone репозиторий ansible (с ветки devel)
2. 



### Ссылки:

[Docker, Ansible и прочие радости DevOps_ Дмитрий Абашин презентация, доклад (thepresentation.ru)](https://thepresentation.ru/uncategorized/docker-ansible-i-prochie-radosti-devops_-dmitriy-abashin)

[Применяем Ansible (slideshare.net)](https://habr.com/ru/post/267295/)

[Ansible — Википедия (wikipedia.org)](https://ru.wikipedia.org/wiki/Ansible)[Пособие по Ansible / Хабр (habr.com)](https://habr.com/ru/post/305400/)

[Пособие по Ansible / Хабр (habr.com)](https://habr.com/ru/post/305400/)

[ansible-community/molecule: Molecule aids in the development and testing of Ansible roles (github.com)](https://github.com/ansible-community/molecule)

[Что такое Ansible и как его использовать (tproger.ru)](https://tproger.ru/translations/ansible-how-to-use/)

[Installing Ansible — Ansible Documentation](https://docs.ansible.com/ansible/devel/installation_guide/intro_installation.html#installing-ansible-on-windows)
