# GeneForge AI Labs — Ръководство за Вътрешен Двигател

## 🏆 Златни правила

> Спазвайте винаги тези правила. Нарушаването дори на едно може да компрометира качеството на клона или да причини freeze на системата.

1. **🔥 Thermal First** — Ако GPU надвиши 78 °C, забавете или спрете изпълнението. Throttling-ът е реален.
2. **🧠 Без CEO Meta без Council** — CEO Meta никога не взима решения самостоятелно. Винаги трябва да активира Council of Agents.
3. **📄 Документирай, преди да клонираш** — Персонализираният клон не стартира без одобрена документация и QA sign-off.
4. **🔴 Red Team е задължителен** — Всеки deliverable трябва да премине stress-test-a на Red Team (Compliance + QA GATE).
5. **🤖 Не измисляй роли** — Агентите никога не трябва да симулират или измислят фалшиви роли. Отговаряйте само с присъдената роля.
6. **💾 Corporate Memory е свещена** — Всяко решение, документ и checkpoint се запазва. Не заобикаляйте паметта.
7. **🌡️ 45 °C е ваш приятел** — Ако Council работи на ~41–45 °C, сте в оптималния диапазон. Ако надхвърли 50 °C, действайте.
8. **📦 .geneclone е преносим** — Никога не свързвайте пакета с конкретен хардуер. Трябва да работи на произволен Linux.

---

## 1. Какво е вътрешният двигател

**GeneForge Internal Personalization Engine** е системата, която трансформира публичен шаблон (`Templates/`) в персонализиран AI клон за конкретен клиент. Напълно е изолиран под папката `internal/` и не променя кода на публичното демо.

Основни компоненти:
- **Вътрешен CLI** (`internal/cli.py`) — входна точка за всички операции
- **Council of Agents** (`internal/engine/council_orchestrator.py`) — множество агенти за вземане на решения с Red Team
- **Corporate Memory** (`internal/memory/client_memory.py`) — JSON/YAML персистентност на документи и решения
- **Personalization Pipeline** (`internal/engine/personalization_pipeline.py`) — автоматизиран end-to-end поток
- **System Monitor** (`internal/engine/system_monitor.py`) — термална защита за DGX Spark

---

## 2. Изисквания

- **Хардуер**: NVIDIA DGX Spark (Grace Blackwell, aarch64)
- **ОС**: DGX OS 7.x / Ubuntu 24.04
- **Python**: 3.12
- **Виртуална среда**: `~/quigley_training/venv` (вече конфигурирана в системата)
- **LLM backend**: Локален Ollama на `http://localhost:11434`
- **Препоръчителен модел**: `nemotron-30b:latest`
- **Стандартна квантизация**: `Q4_K_M` (от май 2026) — осигурява максимална стабилност на DGX Spark. FP4 ще бъде активиран отново след официалната корекция на NVIDIA за GB10.

Активирайте средата преди да използвате CLI:
```bash
source ~/quigley_training/venv/bin/activate
```

---

## 3. Налични команди

Всички команди се изпълняват чрез `python3 -m internal.cli`.

### `init-client`
Инициализира нов клиент във вътрешния двигател.
```bash
python3 -m internal.cli init-client \
  --id <CLIENT_ID> \
  --template <TEMPLATE_ID>
```
**Пример:**
```bash
python3 -m internal.cli init-client \
  --id acme-corp \
  --template AI_ML_PLATFORM
```

### `add-doc`
Качва документ в Corporate Memory на клиента.
```bash
python3 -m internal.cli add-doc \
  --client <CLIENT_ID> \
  --filename <ИМЕ_НА_ФАЙЛ> \
  --summary "<КРАТКО_ОПИСАНИЕ>"
```
**Пример:**
```bash
python3 -m internal.cli add-doc \
  --client acme-corp \
  --filename company_overview.md \
  --summary "Мисия, визия, ценности и стратегически цели за 2026 г."
```

> **Забележка**: файлът трябва физически да се намира в `internal/clients/<CLIENT_ID>/docs/`. Командата регистрира името и summary-то в паметта.

### `run-council`
Ръчно активира Council of Agents за конкретна тема.
```bash
python3 -m internal.cli run-council \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID> \
  --topic "<ТЕМА>" \
  [--model nemotron-30b:latest]
```
**Примери:**
```bash
# Architecture Decision
python3 -m internal.cli run-council \
  --client acme-corp \
  --template AI_ML_PLATFORM \
  --topic "Architecture Decision: How should we personalize this template for the client?"

# Pre-Delivery Review
python3 -m internal.cli run-council \
  --client acme-corp \
  --template AI_ML_PLATFORM \
  --topic "Pre-Delivery Review: Is the personalized package ready for delivery?"
```

### `build`
Изпълнява само фазата на packaging (изисква персонализираният blueprint вече да съществува).
```bash
python3 -m internal.cli build \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID>
```

### `test-run`
**Препоръчителна команда за тестове.** Изпълнява целия end-to-end пайплайн наведнъж:
1. Инициализира клиента (ако липсва досие)
2. Architecture Council
3. Blueprint Personalization
4. Pre-Delivery Council
5. Packaging
6. Генериране на Final Report

```bash
python3 -m internal.cli test-run \
  --client <CLIENT_ID> \
  --template <TEMPLATE_ID>
```

---

## 4. Стъпка по стъпка (ръчен режим)

### Стъпка 1: Създайте клиента
```bash
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM
```

### Стъпка 2: Подгответе документите
```bash
mkdir -p internal/clients/acme-corp/docs
# копирайте вашите markdown/pdf/yaml файлове
```

### Стъпка 3: Заредете документите в Corporate Memory
```bash
python3 -m internal.cli add-doc --client acme-corp \
  --filename company_overview.md \
  --summary "Описание на компанията, мисия и ценности"

python3 -m internal.cli add-doc --client acme-corp \
  --filename process_map.md \
  --summary "Карта на основните процеси"
```

### Стъпка 4: Стартирайте първия Council (Architecture Decision)
```bash
python3 -m internal.cli run-council \
  --client acme-corp \
  --template AI_ML_PLATFORM \
  --topic "Architecture Decision: How should we personalize this template for the client?"
```

### Стъпка 5: Проверете резултата
Прегледайте логовете в:
- `internal/clients/acme-corp/council_logs/`
- `internal/clients/acme-corp/pipeline_checkpoints/`

### Стъпка 6: Стартирайте пълния пайплайн (или използвайте `test-run`)
Ако искате да продължите ръчно, изпълнете `build` след персонализацията на blueprint. Алтернативно, използвайте директно `test-run`.

---

## 5. Бърз поток с `test-run`

За повечето тестове и демонстрации използвайте директно:

```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

Тази команда:
- Автоматично инициализира клиента, ако няма досие
- Изпълнява Council за Architecture Decision
- Персонализира blueprint
- Изпълнява Council за Pre-Delivery Review
- Генерира пакет `.geneclone`
- Записва `FINAL_REPORT.md`

---

## 6. Структура на изходните данни за клиент

След успешен `test-run` ще намерите:

```
internal/clients/<CLIENT_ID>/
├── client_memory.json          # Досие + документи + решения
├── client_memory.yaml          # Четим кеш
├── docs/                       # Качени документи
├── output/
│   ├── GeneForge-Custom-<Име>-v1.0.geneclone   # Краен пакет
│   └── FINAL_REPORT.md         # Обобщен доклад
├── council_logs/               # Подробни логове за всеки Council
├── pipeline_checkpoints/       # Стъпка по стъпка checkpoint-ове
└── .work/                      # Персонализиран blueprint (временно)
```

---

## 7. Пълен end-to-end пример

```bash
# 1. Активирайте средата
source ~/quigley_training/venv/bin/activate
cd /home/aintel/GeneForge-Mother-Clone-v1.0

# 2. Инициализирайте
python3 -m internal.cli init-client \
  --id geneforge-realistic-test \
  --template AI_ML_PLATFORM

# 3. Създайте документи
mkdir -p internal/clients/geneforge-realistic-test/docs
cat > internal/clients/geneforge-realistic-test/docs/company_overview.md << 'EOF'
# GeneForge AI Labs
Mission: democratize safe AI clones...
EOF

# 4. Заредете в паметта
python3 -m internal.cli add-doc \
  --client geneforge-realistic-test \
  --filename company_overview.md \
  --summary "Company mission and strategic priorities"

# 5. Изпълнете пълния пайплайн
python3 -m internal.cli test-run \
  --client geneforge-realistic-test \
  --template AI_ML_PLATFORM

# 6. Прочетете доклада
cat internal/clients/geneforge-realistic-test/output/FINAL_REPORT.md
```

---

## 8. Конфигурация по време на изпълнение

Файлът `internal/config/internal_config.yaml` съдържа параметрите на двигателя:

```yaml
council:
  default_model: "nemotron-30b:latest"
  temperature: 0.3
  ceo_temperature: 0.25
  max_tokens_per_agent: 500
  ceo_max_tokens: 800
  timeout_per_agent: 60
  red_team_timeout: 90
  cooldown_seconds: 3.0
  batch_size: 2
  warning_temp_c: 72.0
  critical_temp_c: 80.0
```

Редактирайте тези стойности, за да настроите скорост, качество и термален стрес.

---

## 9. Отстраняване на неизправности

| Симптом | Вероятна причина | Решение |
|---------|------------------|---------|
| `CEO Meta format drift detected` | Nemotron е симулирал маркера вътре в `<think>` | **Нормално** — format enforcer-ът се намесва автоматично и коригира |
| Timeout след 60s | Nemotron-30B е бавен при дълги prompt-ове | Увеличете `timeout_per_agent` в YAML конфигурацията |
| Темп > 80°C | DGX Spark е прегрят | Двигателят се паузира автоматично; подобрете вентилацията |
| `ImportError` | Виртуалната среда не е активирана | `source ~/quigley_training/venv/bin/activate` |
| `add-doc` изисква `--summary` | Липсва задължителен аргумент | Добавете `--summary "..."` |
| Качването на файлове не работи в Firefox | Firefox Snap блокира достъпа до файловата система | Използвайте Chrome/Chromium или вижте [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

## 10. Оперативни бележки

- **Никога не променяйте** файловете в `wizard/` или `Templates/` по време на вътрешна работа: двигателят е проектиран да работи само за четене по тези пътища.
- Всеки Council добавя 2 решения в `client_memory.json`. За дългосрочни клиенти планирайте логика за pruning/заличаване.
- Пакетът `.geneclone` е преименуван `.zip` файл: преносим, несвързан с конкретен хардуер.

---

*Последна актуализация: Фаза 2 завършена — CEO Meta strict prompt + параметризиран fallback верифицирани.*
