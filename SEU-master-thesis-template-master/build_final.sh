#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

MAIN_FILE="main"

echo "[1/5] 清理辅助文件..."
rm -f \
  "${MAIN_FILE}.aux" \
  "${MAIN_FILE}.bbl" \
  "${MAIN_FILE}.blg" \
  "${MAIN_FILE}.bcf" \
  "${MAIN_FILE}.dvi" \
  "${MAIN_FILE}.fdb_latexmk" \
  "${MAIN_FILE}.fls" \
  "${MAIN_FILE}.glg" \
  "${MAIN_FILE}.glo" \
  "${MAIN_FILE}.gls" \
  "${MAIN_FILE}.idx" \
  "${MAIN_FILE}.ilg" \
  "${MAIN_FILE}.ind" \
  "${MAIN_FILE}.ist" \
  "${MAIN_FILE}.lof" \
  "${MAIN_FILE}.log" \
  "${MAIN_FILE}.lol" \
  "${MAIN_FILE}.lot" \
  "${MAIN_FILE}.nav" \
  "${MAIN_FILE}.nlo" \
  "${MAIN_FILE}.nls" \
  "${MAIN_FILE}.out" \
  "${MAIN_FILE}.run.xml" \
  "${MAIN_FILE}.snm" \
  "${MAIN_FILE}.synctex.gz" \
  "${MAIN_FILE}.toc" \
  "${MAIN_FILE}.xdv"

echo "[2/5] 第一次 xelatex..."
xelatex -interaction=nonstopmode "${MAIN_FILE}.tex"

echo "[3/5] 运行 bibtex..."
bibtex "${MAIN_FILE}"

if [[ -f "${MAIN_FILE}.nlo" ]]; then
  echo "[3.5/5] 检测到术语表索引，运行 makeindex..."
  makeindex "${MAIN_FILE}.nlo" -s nomencl.ist -o "${MAIN_FILE}.nls" || true
fi

echo "[4/5] 第二次 xelatex..."
xelatex -interaction=nonstopmode "${MAIN_FILE}.tex"

echo "[5/5] 第三次 xelatex..."
xelatex -interaction=nonstopmode "${MAIN_FILE}.tex"

echo
echo "编译完成: ${ROOT_DIR}/${MAIN_FILE}.pdf"
echo "建议送审前人工检查：正文引用、参考文献编号、目录页码、图表编号。"
