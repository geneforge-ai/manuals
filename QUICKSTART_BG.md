# GeneForge Internal Engine — Бърз старт

> **Пуснете тестов клон за 5 минути.**  
> За пълното ръководство вижте [MANUALE.md](MANUALE.md).

---

## ⚡ Изисквания
- Активен DGX Spark, Ollama работи с `nematron-30b:latest`
- Активирана виртуална среда: `source ~/quigley_training/venv/bin/activate`

---

## Единична команда (тест/демо)

```bash
cd /home/aintel/GeneForge-Mother-Clone-v1.0
python3 -m internal.cli test-run --client <ИМЕ_НА_КЛИЕНТ> --template <TEMPLATE>
```

**Пример:**
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

Изпълнява всичко: Intake → Architecture Council → Personalization → Pre-Delivery Council → Packaging → Report.

---

## Ръчен режим (пълен контрол)

### 1. Инициализирайте клиента
```bash
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM
```

### 2. Поставете документите в папката docs
```bash
mkdir -p internal/clients/acme-corp/docs
# копирайте вашите .md / .pdf / .yaml файлове тук
```

### 3. Заредете документите в паметта
```bash
python3 -m internal.cli add-doc \
  --client acme-corp \
  --filename company_overview.md \
  --summary "Мисия и ценности на компанията"
```

### 4. Стартирайте пълния пайплайн
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

---

## Резултат

След изпълнение проверете:
```
internal/clients/acme-corp/output/
├── GeneForge-Custom-AcmeCorp-v1.0.geneclone   # Краен пакет
└── FINAL_REPORT.md                              # Обобщен доклад
```

---

## Бърза конфигурация

Редактирайте `internal/config/internal_config.yaml`, за да настроите:
- `temperature` / `ceo_temperature` — качество спрямо креативност
- `timeout_per_agent` — ако Nemotron е бавен
- `cooldown_seconds` — пауза между агенти
- `batch_size` — агенти, изпълнявани паралелно

---

## Отстраняване на неизправности

| Проблем | Решение |
|---------|---------|
| `CEO Meta format drift detected` | Нормално — enforcer коригира автоматично |
| Timeout | Увеличете `timeout_per_agent` в YAML конфигурацията |
| Темп > 80°C | Двигателят се паузира автоматично |
| `ImportError` | `source ~/quigley_training/venv/bin/activate` |
| Качването на файлове не работи в Firefox | Firefox Snap блокира достъпа до файловата система → използвайте Chrome или вижте [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

За пълното ръководство вижте `internal/MANUALE.md`.
