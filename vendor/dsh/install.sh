#!/usr/bin/env bash
# usage: vendor/dsh/install.sh [PREFIX]   (default PREFIX: ~/.refinx-node/global)
# Restores the DSH 0.2.0-rc.2 installation used on the GPU server (Linux x86-64): PREFIX/bin/dsh and
# PREFIX/lib/node_modules/@deepseek-ai/dsh with its full dependency tree. Needs Node.js 25.9.0 on PATH.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
PREFIX=${1:-$HOME/.refinx-node/global}
ARCHIVE=dsh-0.2.0-rc.2-linux-x64.tar.gz
FULL_SHA256=9a1934d7fd998127257590edc6d36e0606341bccd5a5a59735ca8d73c00ead9e

(cd "$HERE" && sha256sum -c SHA256SUMS)
joined=$(cat "$HERE/$ARCHIVE".part-* | sha256sum | cut -d' ' -f1)
if [ "$joined" != "$FULL_SHA256" ]; then
  echo "joined archive checksum mismatch: $joined" >&2
  exit 1
fi
mkdir -p "$PREFIX"
cat "$HERE/$ARCHIVE".part-* | tar -xz -C "$PREFIX"
echo "installed $PREFIX/bin/dsh ($("$PREFIX/bin/dsh" --version 2>/dev/null || echo 'run it with Node.js 25.9.0 on PATH'))"
echo "add to PATH: export PATH=$PREFIX/bin:\$PATH"
