## Что такое Ansible?

Ansible — это программное решение для удаленного управления конфигурациями. Оно позволяет настраивать удаленные машины. Главное его отличие от других подобных систем в том, что Ansible использует существующую инфраструктуру SSH, в то время как другие (chef, puppet, и пр.) требуют установки специального окружения.

Поддерживается управление как Linux узлами, так и Windows, но все же чаще первое.

Оно написано на языке программирования python и языке разметки YAML для описания разметки.

Модульность - готовые команды «из коробки». Более 100 различных модулей.

Поддержка сторонних модулей - портал Ansible Galaxy, на котором вы наверняка найдете решение для своей задачи. Это объединение Ansible сообщества, где люди делятся наработками и решениями той или иной задачи.

## Как работает Ansible

Пользователь взаимодействует с окружением через ssh. Свои ключи добавляем в менеджер ключей для SSH (ssh-agent), он хранит ключи в памяти.

## Ключевые особенности

- Безагентное. В клиенте не установлено программное обеспечение или агент, который общается с сервером.
- Идемпотентное. Независимо от того, сколько раз вы вызываете операцию, результат будет одинаковым.
- Простое и расширяемое. Программа Ansible написанa на Python и использует YAML для написания команд. Оба языка считаются относительно простыми в изучении.

## Сравнение ансибл и паппет

- Императивный стиль (задачи playbooks) ±Декларативный стиль (описание в manifests)
- Push по команде контроллера ±Pull периодически (агенты)
- Централизованная ±Централизованная
- Центр: машина инженера (контроллер) ±Центр: выделенный сервер
- Язык: YAML ±Язык: Puppet DSL
- В основе: SSH и Python ±В основе: HTTPS и Ruby

## Установка

На главном контроллере:

- Документация по установке Ansible: [http://](http://docs.ansible.com/ansible/intro_installation.html)[docs.ansible.com/ansible/intro_installation.html](http://docs.ansible.com/ansible/intro_installation.html)
- Интерфейс: текстовый редактор и командная строка

На серверах:

- Устанавливать Ansible не требуется
- Должен быть python 2.7 или выше
- Настроен доступ по SSH c контроллера

Краткая инструкция: 

Необходимы следующие Python-модули: python-yaml, python-jinja2

1. git clone репозиторий ansible (с ветки devel)
2. Загружаем окружение Ansible **source** ./hacking/**env**-setup
3. установка vagrant и инициализация виртуальной машины на нем
4. добавление ssh-ключей на виртуальной машине
5. настройка файла Inventory (в нем содержатся данные ansible_ssh_host - содержит данные IP-узла, к которому создается соединение; ansible_ssh_user - подключение под указанным аккаунтом.)
6. Когда установлен, проверка работоспособности: **ansible** -m ping all -i step-01/hosts
7. Можно начинать работу
8. Создать playbook, настроить роли, группировать хосты, установить переменные и т.д.

## Playbooks 1

- Последовательности команд организуются в playbooks
- Для описания используется нотация YAML
- Playbook содержит не только задачи (tasks), но также может содержать:
  - hosts — шаблон серверов, к которым применяется playbooks
  - vars — переменные
  - handlers — обработчики
  - и др. директивы
- Задачи в playbook выполняются строго последовательно
- Можно сделать много playbooks для разных задач/ситуаций

## Playbooks 2

- Name – название плейбука
- Hosts – группа хостов, к которым будет создаваться подключение
- User – подключение под этим аккаунтом
- Tasks – задача для выполнения
- Name – имя задачи
- Yum – менеджер пакетов
- Service – контроллер сервисов на хостах

## Advanced Playbooks

если хочется автоматизировать качественно и правильно, но не против усложнить процесс.

## Roles

- Удобная возможность группировать сервера по назначению/функциям (по примеру выше несколько объденено в один)
- Один сервер может иметь несколько ролей и такой подход позволяет:
  - Не порождать случайных кросс-зависимостей
  - Легко "расщеплять" или комбинировать сервер при масштабировании
- Всем серверам может быть прописана "базовая" роль, которая реализует ваши любимые настройки
- Роли легче повторно использовать (в других проектах и т.п.)
- Ansible Galaxy предоставляет готовые описания ролей для использования (например, "сервер с nginx")

Роли — это просто еще один способ организации файлов. Роли полагается структурировать определенным образом, хотя вы можете делать это как угодно вам. Тем не менее, если придерживаться соглашений, вам будет гораздо легче создавать модульные плейбуки. Содержать код в порядке будет гораздо легче.

Моя любимая фича — это зависимости ролей: роль B может зависеть от другой роли A. Поэтому при применении роли B, автоматически будет применена роль A.

## Преимущества

- Взаимодействие с окружениями через SSH. Не нужно ставить клиента(агента) на машину. Для управления узлами, Ansible обрабатывает все коммуникации между мастер – узлами и узлами – агентами по стандартному SSH
- Простота написания сценариев. Плейбуки в Ansible невероятно просты и читаемы.
- Декларативный язык
- Большое количество готовых модулей. Готовые команды "из коробки". Более 100 различных модулей.
- Большое сообщество. Портал Ansible Galaxy, на котором вы наверняка найдете решение для своей задачи. Тонны плейбуков, фреймворков, дистрибутивов и сопутствующего ПО.
- Скорость развертывания новых окружений
- Гарантия того, что окружения настроены одинаково
- Уменьшение человеческого фактора

## Недостатки

- Нет менеджера зависимостей.
- Неполная документация. Некоторые вопросы приходится узнавать из сторонних источников или изучать самому.
- Неудобный debug.
- Определенное количество ошибок или багов из-за быстрого развития. (как плюс, так и минус)



## Модули

Категории модулей и выполняемые ими задачи:

- Cloud: поддержка [Amazon EC2/ECS/S3](https://ru.wikipedia.org/wiki/Amazon_Web_Services), [Azure](https://ru.wikipedia.org/wiki/Microsoft_Azure), [Cloudstack](https://ru.wikipedia.org/w/index.php?title=Cloudstack&action=edit&redlink=1), [Digital Ocean](https://ru.wikipedia.org/w/index.php?title=Digital_Ocean&action=edit&redlink=1), [Docker](https://ru.wikipedia.org/wiki/Docker), [LXC](https://ru.wikipedia.org/wiki/LXC), [OpenStack](https://ru.wikipedia.org/wiki/OpenStack), [Rackspace](https://ru.wikipedia.org/wiki/Rackspace), [VMware](https://ru.wikipedia.org/wiki/VMware) и др.
- Clustering: поддержка [Consul](https://ru.wikipedia.org/w/index.php?title=Consul&action=edit&redlink=1), [ZooKeeper](https://ru.wikipedia.org/w/index.php?title=ZooKeeper&action=edit&redlink=1) ([англ.](https://en.wikipedia.org/wiki/Apache_ZooKeeper)), [Kubernetes](https://ru.wikipedia.org/wiki/Kubernetes)
- Command: выполняют консольные команды и скрипты
- Database: поддержка баз данных [MySQL](https://ru.wikipedia.org/wiki/MySQL), [PostgreSQL](https://ru.wikipedia.org/wiki/PostgreSQL), [Vertica](https://ru.wikipedia.org/w/index.php?title=Vertica&action=edit&redlink=1), [MongoDB](https://ru.wikipedia.org/wiki/MongoDB), [Redis](https://ru.wikipedia.org/wiki/Redis), [Riak](https://ru.wikipedia.org/wiki/Riak)
- File: работа с файлами — копирование, синхронизация, модификация, проверка, архивирование и т. д.
- Inventory: работа с именами хостов или их [ip](https://ru.wikipedia.org/wiki/TCP/IP)-адресами.
- Messaging: поддержка [RabbitMQ](https://ru.wikipedia.org/wiki/RabbitMQ)
- Monitoring: поддержка систем мониторинга [DataDog](https://ru.wikipedia.org/w/index.php?title=DataDog&action=edit&redlink=1), [Nagios](https://ru.wikipedia.org/wiki/Nagios), [Zabbix](https://ru.wikipedia.org/wiki/Zabbix) и пр.
- Network: работа с сетевым оборудованием и ПО [F5 BIG-IP](https://ru.wikipedia.org/wiki/F5), [Cisco IOS/NXOS](https://ru.wikipedia.org/wiki/Cisco_IOS), [Juniper JunOS](https://ru.wikipedia.org/wiki/Juniper_Networks), [OpenSwitch](https://ru.wikipedia.org/w/index.php?title=OpenSwitch&action=edit&redlink=1), [Cumulus Linux](https://ru.wikipedia.org/wiki/Cumulus_Linux), [Mikrotik RouterOS](https://ru.wikipedia.org/wiki/MikroTik)[[6\]](https://ru.wikipedia.org/wiki/Ansible#cite_note-6)
- Notification: отсылаются сообщения в [Campfire](https://ru.wikipedia.org/w/index.php?title=Campfire&action=edit&redlink=1), [HipChat](https://ru.wikipedia.org/w/index.php?title=HipChat&action=edit&redlink=1), [Jabber](https://ru.wikipedia.org/wiki/Jabber), [Pushbullet](https://ru.wikipedia.org/w/index.php?title=Pushbullet&action=edit&redlink=1), [Slack](https://ru.wikipedia.org/wiki/Slack), через email/sms
- Packaging: работа с менеджерами пакетов [apt](https://ru.wikipedia.org/wiki/Apt), [FreeBSD Ports](https://ru.wikipedia.org/wiki/FreeBSD_Ports), [Gentoo](https://ru.wikipedia.org/wiki/Gentoo), [homebrew](https://ru.wikipedia.org/w/index.php?title=Homebrew_(система_управления_пакетами)&action=edit&redlink=1), [pacman](https://ru.wikipedia.org/wiki/Pacman_(система_управления_пакетами)), [opkg](https://ru.wikipedia.org/w/index.php?title=Opkg&action=edit&redlink=1), [Red Hat software channels](https://ru.wikipedia.org/wiki/Red_Hat_Enterprise_Linux), [yum](https://ru.wikipedia.org/wiki/Yum), [xbps](https://ru.wikipedia.org/w/index.php?title=Xbps&action=edit&redlink=1), [zypper](https://ru.wikipedia.org/wiki/Zypper)
- Source Control: работа с системами контроля версий [git](https://ru.wikipedia.org/wiki/Git), [mercurial](https://ru.wikipedia.org/wiki/Mercurial), [subversion](https://ru.wikipedia.org/wiki/Subversion)
- System: работа с компонентами Linux/Unix систем — [cron](https://ru.wikipedia.org/wiki/Cron), [iptables](https://ru.wikipedia.org/wiki/Iptables), [LVM](https://ru.wikipedia.org/wiki/LVM), [SELinux](https://ru.wikipedia.org/wiki/SELinux), [sshd](https://ru.wikipedia.org/wiki/Sshd), [zfs](https://ru.wikipedia.org/wiki/ZFS)
- Utilities: реализуют внутреннюю логику плейбуков
- Web Infrastructure: работа с [Apache](https://ru.wikipedia.org/wiki/Apache_HTTP_Server), [Django](https://ru.wikipedia.org/wiki/Django), [JBoss](https://ru.wikipedia.org/wiki/JBoss), [JIRA](https://ru.wikipedia.org/wiki/JIRA)
- Windows: работа с компонентами Windows, в том числе [IIS](https://ru.wikipedia.org/wiki/IIS), [Windows Firewall](https://ru.wikipedia.org/wiki/Windows_Firewall), [реестром](https://ru.wikipedia.org/wiki/Windows_registry)













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

Документация: [Ansible Documentation](https://docs.ansible.com/)

​	

## Инициализация

На контролирующей машине инженера (контроллере): можно посмотреть подробную [документацию](https://docs.ansible.com/ansible/devel/installation_guide/intro_installation.html#installing-ansible-on-windows). Для установки необходимы: командная строка и текстовый редактор.

На серверах: установка Ansible не требуется. Необходимы: python 2.7 или выше, доступ по SSH с контроллера.

Краткая инструкция: 

1. git clone репозиторий ansible (с ветки devel)
2. установка vagrant и инициализация виртуальной машины на нем
2. добавление ssh-ключей на виртуальной машине
2. настройка файла Inventory (в нем содержатся данные ansible_ssh_host - содержит данные IP-узла, к которому создается соединение; ansible_ssh_user - подключение под указанным аккаунтом.)
2. проверка работоспособности: **ansible** -m ping all -i step-01/hosts
2. Можно начинать работу

[Ссылка на пример](https://habr.com/ru/post/305400/)



## Положительные стороны

1. Взаимодействие с окружениями через SSH. Не нужно ставить клиента(агента) на машину. Для управления узлами, Ansible обрабатывает все коммуникации между мастер – узлами и узлами – агентами по стандартному SSH, или через модуль Paramiko, который является частью Python SSH второй версии.
2. Простота написания сценариев. Плейбуки в Ансибл невероятно просты и читаемы.
3. Декларативный язык
4. Большое количество готовых модулей. Готовые команды "из коробки". Более 100 различных модулей.
5. Большое сообщество. Портал Ansible Galaxy, на котором вы наверняка найдете решение для своей задачи. Это объединение Ansible сообщества, где люди делятся наработками и решениями той или иной задачи. Знаете, это как ответ на мэйл.ру - чтобы вам не пришло реализовать на Ансибл, то как правило, кто – то эту задачу уже решил. Тонны плейбуков, фреймворков, дистрибутивов и сопутствующего ПО.
6. Скорость развертывания новых окружений.
7. Гарантия того, что окружения настроены одинаково.
8. Уменьшение человеческого фактора.



## Недостатки

1. Нет менеджера зависимостей.
2. Неполная документация. Некоторые вопросы  приходится узнавать из сторонних источников или изучать самому.
3. Неудобный debug.
4. Определенное количество ошибок или багов из-за быстрого развития. (как плюс, так и минус)





## Ansible Playbooks

Последовательности команд организуются в playbooks. Позволяет описать процедуру автоматической настройки окружения. Можно использовать на всех окружениях один сценарий. Можно использовать таски в других сценариях.

Для описания используется нотация YAML. Внутри playbook может содержаться не только задачи(tasks), но и шаблон серверов(hosts), к которым применяется playbook, переменные(vars), обработчики(handlers) и др. директивы. Задачи выполняются строго последовательно.





### Ссылки:

[Docker, Ansible и прочие радости DevOps_ Дмитрий Абашин презентация, доклад (thepresentation.ru)](https://thepresentation.ru/uncategorized/docker-ansible-i-prochie-radosti-devops_-dmitriy-abashin)

[Ansible — Википедия (wikipedia.org)](https://ru.wikipedia.org/wiki/Ansible)

[Пособие по Ansible / Хабр (habr.com)](https://habr.com/ru/post/305400/)

[ansible-community/molecule: Molecule aids in the development and testing of Ansible roles (github.com)](https://github.com/ansible-community/molecule)

[Что такое Ansible и как его использовать (tproger.ru)](https://tproger.ru/translations/ansible-how-to-use/)

[Installing Ansible — Ansible Documentation](https://docs.ansible.com/ansible/devel/installation_guide/intro_installation.html#installing-ansible-on-windows)

[Ansible — давайте попробуем / хендлеры и т.д.](https://habr.com/ru/company/express42/blog/254959/)

