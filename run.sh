#!/usr/bin/env bash
set -e

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

exec "$ROOT_DIR/odoo17/venv/bin/python" \
    "$ROOT_DIR/odoo17/odoo-bin" \
    -d estate17_db \
    --addons-path="$ROOT_DIR/odoo17/addons,$ROOT_DIR" \
    -u estate \
    --dev=xml
