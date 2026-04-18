# GeneForge AI Labs — Бърз Старт

> **Стартирайте тестово клониране за 5 минути.**  
> За пълното ръководство вижте [MANUALE_BG.md](MANUALE_BG.md).

---

## ⚡ Предпоставки
- DGX Spark (или който и да е Linux) с работещ Ollama и `nemotron-30b:latest`
- Активирана виртуална среда: `source ~/quigley_training/venv/bin/activate`

---

## Единична Команда (тест/демо)

```bash
cd /home/aintel/GeneForge-Mother-Clone-v1.0
python3 -m internal.cli test-run --client <КЛИЕНТ> --template <ШАБЛОН>
```

**Пример:**
```bash
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

Изпълнява пълния pipeline: Intake → Architecture Council → Personalization → Pre-Delivery Council → Packaging → Report.

---

## Ръчни Стъпки (ако имате нужда от контрол)

```bash
# 1. Инициализирайте клиент
python3 -m internal.cli init-client --id acme-corp --template AI_ML_PLATFORM

# 2. Добавете документи в internal/clients/acme-corp/docs/
# 3. Регистрирайте ги в паметта
python3 -m internal.cli add-doc --client acme-corp \
  --filename company_overview.md --summary "Мисия и ценности"

# 4. Изпълнете пълния pipeline
python3 -m internal.cli test-run --client acme-corp --template AI_ML_PLATFORM
```

---

## Резултат

```
internal/clients/acme-corp/output/
├── GeneForge-Custom-AcmeCorp-v1.0.geneclone   # Финален пакет
└── FINAL_REPORT.md                              # Одитен доклад
```

---

## Бърза Конфигурация

Редактирайте `internal/config/internal_config.yaml`, за да настроите:
- `temperature` / `ceo_temperature` — качество vs креативност
- `timeout_per_agent` — ако Nemotron е бавен
- `cooldown_seconds` — пауза между агенти
- `batch_size` — паралелни агенти

---

## Отстраняване на неизправности

| Проблем | Решение |
|---------|---------|
| `CEO Meta format drift detected` | Нормално — enforcer коригира автоматично |
| Timeout | Увеличете `timeout_per_agent` в конфигурацията |
| Temp > 80°C | Двигателят се паузира автоматично |
| `ImportError` | `source ~/quigley_training/venv/bin/activate` |
| Firefox upload не работи | Използвайте Chrome или вижте [firefox-snap-upload-fix](https://github.com/geneforge-ai/firefox-snap-upload-fix) |

---

За пълното ръководство вижте [MANUALE_BG.md](MANUALE_BG.md).
