# Лабораторная работа №9 — GitHub Actions CI

Учебный пример приложения расчёта доставки и 12 UI-тестов Playwright.

> Важно: исходные `delivery.html`, `conftest.py` и `test_delivery_ui.py` из вашей ЛР №8 в чате не приложены. Поэтому здесь создан совместимый демонстрационный вариант с тем же порогом бесплатной доставки 10 000 ₸. Если преподаватель требует именно файлы ЛР №8, замените эти три файла своими, не меняя правила расчёта.

## Локальный запуск (Windows)

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe -m playwright install chromium
```

В первом окне терминала:
```powershell
.venv\Scripts\python.exe -m http.server 8000 --bind 127.0.0.1
```

Во втором окне, из папки проекта:
```powershell
.venv\Scripts\python.exe -m pytest -v --browser chromium
```

## GitHub

Загрузите содержимое папки в новый репозиторий GitHub. Не загружайте `.venv`, `__pycache__`, `.pytest_cache` и `test-results`. Workflow находится в `.github/workflows/ui-tests.yml` и запускается на `push`, `pull_request` и вручную.

## Проверка quality gate

Для учебной проверки временно измените в `delivery.html` условие `amount >= 10000` на `amount > 10000`, отправьте commit и убедитесь, что граничные тесты города и области падают. Затем обязательно верните `>=`, отправьте новый commit и проверьте успешный прогон.

Скриншоты и фактический статус GitHub Actions можно получить только после загрузки проекта в ваш GitHub-аккаунт и запуска workflow.
