#!/usr/bin/env bash
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
REPORT="$ROOT_DIR/Laporan_UAS_BigData.pdf"

TMPDIR=$(mktemp -d)
trap "rm -rf $TMPDIR" EXIT

cp "$SCRIPT_DIR/cover.md" "$TMPDIR/"
cp "$SCRIPT_DIR/Laporan_Akademik.md" "$TMPDIR/"
cp "$SCRIPT_DIR/template.latex" "$TMPDIR/"
[ -f "$SCRIPT_DIR/logo-boash.jpg" ] && cp "$SCRIPT_DIR/logo-boash.jpg" "$TMPDIR/"

if [ -d "$ROOT_DIR/Proyek_BigData/assets" ]; then
  mkdir -p "$TMPDIR/Proyek_BigData/assets"
  cp -r "$ROOT_DIR/Proyek_BigData/assets/"* "$TMPDIR/Proyek_BigData/assets/"
  for f in "$TMPDIR/Proyek_BigData/assets/"*.jpg; do
    [ -f "$f" ] && convert "$f" -alpha off "$f" 2>/dev/null || true
  done
fi

cd "$TMPDIR"

pandoc \
  "Laporan_Akademik.md" \
  --template="template.latex" \
  --include-before-body="cover.md" \
  --top-level-division=chapter \
  --pdf-engine=pdflatex \
  -o "$REPORT" 2>&1

echo ""
echo "=== PDF BERHASIL DIBUAT ==="
echo "Lokasi: $REPORT"
