# Ръководство за внедряване на GeneForge — пакет `.geneclone`

Това ръководство обхваща как да получите, извлечете, внедрите и стартирате **GeneForge Custom Clone**, опакован като артефакт `.geneclone`.

---

## 1. Какво представлява пакет `.geneclone`?

Файлът `.geneclone` е **преименуван ZIP архив**, съдържащ напълно персонализиран AI клон:

```
GeneForge-Custom-<CompanyName>-v1.0.geneclone
├── agents/                     # Персонализирани prompt-ове на AI агенти
├── config/                     # Конфигурационни файлове (YAML, JSON)
├── restore-geneclone.sh        # Автоматизиран скрипт за възстановяване
└── wizard/
    ├── app_onboarding.py       # Streamlit съветник (wizard) за onboardинг
    ├── launch_onboarding.sh    # Помощник за стартиране
    └── requirements.txt        # Python зависимости
```

> **Забележка:** Пакетът е **независим от хардуера** (hardware-agnostic). Той не е обвързан с конкретна машина. Можете да го внедрите на всяка Linux система, която отговаря на изискванията по-долу.

---

## 2. Системни изисквания

### Минимални изисквания
| Компонент | Изискване |
|-----------|-------------|
| **ОС** | Linux (препоръчително Ubuntu 22.04+) |
| **Python** | 3.10 или по-висока версия |
| **Bash** | GNU bash 4.0+ |
| **Памет** | 4 GB RAM (препоръчително 8 GB) |
| **Хранилище** | 2 GB свободно пространство |
| **Мрежа** | Достъп до интернет за първоначално инсталиране на зависимостите |

### Препоръчителни за пълно изживяване
| Компонент | Изискване |
|-----------|-------------|
| **GPU** | NVIDIA GPU с CUDA 11.8+ (незадължително — работи и в CPU режим) |
| **ОС** | DGX OS 7.x / Ubuntu 24.04 |
| **Браузър** | Chrome, Chromium или Firefox (non-Snap) |
| **Python среда** | `venv` или `conda` |

---

## 3. Стъпки за внедряване

### Стъпка 1 — Получаване на пакета

Файлът `.geneclone` се доставя от екипа на GeneForge чрез:
- Сигурен трансфер на файлове (SFTP, криптиран имейл)
- Споделено хранилище (S3, Google Drive, вътрешен NAS)
- Физически носител (USB флашка)

Поставете файла в работна директория:
```bash
mkdir -p ~/geneforge-deploy
cp /path/to/GeneForge-Custom-*-v1.0.geneclone ~/geneforge-deploy/
```

### Стъпка 2 — Извличане на пакета

`.geneclone` е стандартен ZIP файл. Извлечете го с някой от следните методи:

> **✅ Препоръчително: Опция B — Скрипт за възстановяване** (обработва автоматично структурата на директориите и правата за достъп).

**Опция A — Unzip (ръчно)**
```bash
cd ~/geneforge-deploy
unzip GeneForge-Custom-*-v1.0.geneclone -d my-clone/
```

**Опция B — Скрипт за възстановяване (препоръчително ⭐)**
```bash
cd ~/geneforge-deploy
bash restore-geneclone.sh ~/my-clone
```

Скриптът за възстановяване:
- Създава целевата структура на директориите
- Копира файловете на агентите, конфигурацията и съветника (wizard)
- Задава изпълнителни права на `.sh` файловете
- Проверява за наличие на виртуална Python среда

### Стъпка 3 — Проверка на целостта на пакета

Преди инсталиране, проверете дали пакетът не е повреден при трансфера:

```bash
cd ~/geneforge-deploy
sha256sum -c checksum.sha256
```

Очакван резултат:
```
GeneForge-Custom-*-v1.0.geneclone: OK
```

> ⚠️ Ако контролната сума (checksum) не съвпадне, **не продължавайте**. Незабавно се свържете с поддръжката на GeneForge — пакетът може да е повреден или манипулиран.

### Стъпка 4 — Инсталиране на зависимостите

```bash
cd ~/my-clone/wizard

# Опция 1 — Системен Python
pip install -r requirements.txt

# Опция 2 — Виртуална среда (препоръчително)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Типични зависимости:
- `streamlit`
- `plotly`
- `pandas`
- `numpy`

### Стъпка 5 — Стартиране на съветника за onboardинг (Onboarding Wizard)

```bash
cd ~/my-clone/wizard
source venv/bin/activate  # при използване на venv

# Стартиране
streamlit run app_onboarding.py \
  --server.port 8501 \
  --server.address 0.0.0.0 \
  --server.headless true
```

Съветникът ще бъде достъпен на адрес:
```
http://localhost:8501
```

Ако внедрявате на отдалечен сървър, достъпете го чрез:
```
http://<server-ip>:8501
```

### Стъпка 6 — Завършване на onboardинга

Отворете съветника в браузъра си и следвайте водените стъпки:
1. **Health Check** — Проверка на съвместимостта на системата
2. **Agent Activation** — Инициализиране на персонализираните AI агенти
3. **Integration Test** — Валидиране на връзките към вашите източници на данни
4. **Go Live** — Започнете да използвате клона

---

## 4. Структура на директориите след внедряване

```
~/my-clone/
├── agents/
│   ├── ceo-meta/
│   │   └── system-prompt.md
│   ├── cloner/
│   ├── compliance-ai-act/
│   └── ... (персонализирани за клиента)
├── config/
│   ├── nim_config.yaml
│   └── ollama_config.yaml
├── wizard/
│   ├── app_onboarding.py
│   ├── launch_onboarding.sh
│   └── requirements.txt
└── logs/                     # Генерирани по време на изпълнение
```

---

## 5. Стартиране на клона (Headless / Продукция)

За продукционно внедряване без съветника:

```bash
cd ~/my-clone

# Активиране на средата
source venv/bin/activate

# Стартиране на основното приложение (ако е приложимо)
python3 -m agents.intake_analysis

# Или използване на предоставения лаунчер
bash wizard/launch_onboarding.sh --headless
```

---

## 6. Актуализиране на клона

Когато получите актуализиран пакет `.geneclone`:

```bash
# 1. Резервно копие на текущото внедряване
cp -r ~/my-clone ~/my-clone-backup-$(date +%Y%m%d)

# 2. Спиране на работещите услуги
pkill -f streamlit
pkill -f app_onboarding.py

# 3. Извличане на новия пакет
unzip GeneForge-Custom-*-v2.0.geneclone -d my-clone-new/

# 4. Миграция на персонализирани конфигурации (ако има такива)
cp ~/my-clone/config/custom.yaml ~/my-clone-new/config/

# 5. Замяна на старото с новото
mv ~/my-clone ~/my-clone-old
mv ~/my-clone-new ~/my-clone

# 6. Рестартиране
bash ~/my-clone/wizard/launch_onboarding.sh
```

---

## 7. Връщане към предишна версия (Rollback)

Ако новата версия причинява проблеми:

```bash
# Спиране на текущата услуга
pkill -f streamlit

# Възстановяване на резервното копие
rm -rf ~/my-clone
mv ~/my-clone-backup-20260416 ~/my-clone

# Рестартиране
bash ~/my-clone/wizard/launch_onboarding.sh
```

---

## 8. Отстраняване на неизправности (Troubleshooting)

| Проблем | Причина | Решение |
|---------|-------|----------|
| `unzip: cannot find` | Скрито файлово разширение | Преименувайте: `mv file.geneclone file.zip` и разархивирайте |
| `ModuleNotFoundError: streamlit` | Зависимостите не са инсталирани | Изпълнете `pip install -r requirements.txt` |
| `Address already in use` | Порт 8501 е зает | Сменете порта: `--server.port 8502` |
| Съветникът се зарежда, но показва грешки | Блокиране от Firefox Snap | Използвайте Chrome/Chromium |
| `Permission denied` на `.sh` | Скриптовете не са изпълними | `chmod +x restore-geneclone.sh` |
| Бавна производителност | Без GPU / само CPU | Очаквано за системи без GPU; намалете конкурентността на агентите |
| Prompt-овете на агентите не се зареждат | Липсваща `agents/` директория | Извлечете отново пакета; проверете структурата на директориите |

### Разширено отстраняване на неизправности

#### "Скриптът за възстановяване се проваля с 'directory not found'"
- **Причина:** Изпълнили сте `restore-geneclone.sh` отвътре в архива ZIP без предварително извличане.
- **Решение:** Първо извлечете `.geneclone`, след което стартирайте скрипта от извлечената папка:
  ```bash
  unzip GeneForge-Custom-*-v1.0.geneclone -d temp/
  bash temp/restore-geneclone.sh ~/my-clone
  ```

#### "Streamlit стартира, но страницата е празна"
- **Причина:** Защитна стена (firewall), която блокира порт 8501, или проблем с кеша на браузъра.
- **Решение:**
  ```bash
  # Опитайте с друг порт
  streamlit run app_onboarding.py --server.port 8502
  # Или достъп чрез IP вместо localhost
  streamlit run app_onboarding.py --server.address $(hostname -I | awk '{print $1}')
  ```

#### "Виждам '404: Not Found' за статични ресурси"
- **Причина:** Папката `agents/` или `config/` липсва при извличането.
- **Решение:** Извлечете отново, използвайки скрипта за възстановяване (Опция B), вместо ръчно unzip.

#### "Клонът отговаря бавно или изтича времето за изчакване (times out)"
- **Причина:** Работа на машина само с CPU с настройки по подразбиране.
- **Решение:** Намалете броя на едновременно работещите агенти в `config/nim_config.yaml`:
  ```yaml
  max_concurrent_agents: 2  # вместо 4
  ```

#### "Изгубих оригиналния си .geneclone файл"
- **Причина:** Случайно изтриване.
- **Решение:** Свържете се с поддръжката на GeneForge, като посочите **client ID** и **дата на доставка**. Поддържаме криптирани резервни копия за 90 дни.

| Проблем | Причина | Решение |
|---------|-------|----------|
| `unzip: cannot find` | Скрито файлово разширение | Преименувайте: `mv file.geneclone file.zip` и разархивирайте |
| `ModuleNotFoundError: streamlit` | Зависимостите не са инсталирани | Изпълнете `pip install -r requirements.txt` |
| `Address already in use` | Порт 8501 е зает | Сменете порта: `--server.port 8502` |
| Съветникът се зарежда, но показва грешки | Блокиране от Firefox Snap | Използвайте Chrome/Chromium |
| `Permission denied` на `.sh` | Скриптовете не са изпълними | `chmod +x restore-geneclone.sh` |
| Бавна производителност | Без GPU / само CPU | Очаквано за системи без GPU; намалете конкурентността на агентите |
| Prompt-овете на агентите не се зареждат | Липсваща `agents/` директория | Извлечете отново пакета; проверете структурата на директориите |

---

## 9. Бележки по сигурността

- **Няма хардуерно заключване**: Пакетът `.geneclone` е преносим. Защитавайте го както всяка друга чувствителна корпоративна информация.
- **Няма зависимост от облака**: Всички AI агенти работят локално чрез Ollama. Никакви данни не напускат вашата машина, освен ако не е конфигурирано друго.
- **Файлови права**: Уверете се, че `agents/` и `config/` са четими само от потребителя на услугата.

---

## 10. Бърза справка

```bash
# --- Внедряване за 30 секунди ---
mkdir -p ~/geneforge-clone && cd ~/geneforge-clone
unzip ~/Downloads/GeneForge-Custom-*-v1.0.geneclone
bash wizard/launch_onboarding.sh

# --- Достъп ---
open http://localhost:8501

# --- Спиране ---
pkill -f streamlit

# --- Актуализация ---
# Резервно копие → Извличане на нов → Миграция на конфигурации → Рестартиране
```

---

*За пълното вътрешно ръководство на двигателя, вижте [MANUALE.md](MANUALE.md).*  
*За бележки по разработка, специфични за CUDA, вижте [CUDA_DEVELOPMENT_GUIDE.md](CUDA_DEVELOPMENT_GUIDE.md).*  
*За бизнес пътуването, вижте [CUSTOMER_JOURNEY_GUIDE.md](CUSTOMER_JOURNEY_GUIDE.md).*  
*Платформа: GeneForge AI Clone Deployment*  
*Последно актуализирано: 2026-04-16*
