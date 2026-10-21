# DSH 0.2.0-rc.2 (vendored)

This directory holds the DeepSeek Harness installation used in the experiments: `@deepseek-ai/dsh` 0.2.0-rc.2 ([deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness)) with its full dependency tree of 531 packages, as installed by npm under Node.js 25.9.0. It contains prebuilt Linux x86-64 native modules, so it runs on Linux x86-64 only. On other platforms, install `@deepseek-ai/dsh@0.2.0-rc.2` from npm.

| File | Contents |
| --- | --- |
| `dsh-0.2.0-rc.2-linux-x64.tar.gz.part-00`, `.part-01` | One gzip tar archive of `bin/dsh` and `lib/node_modules/@deepseek-ai/dsh`, split to stay under GitHub's file-size limit. Joined, it is 121,899,477 bytes with SHA-256 `9a1934d7fd998127257590edc6d36e0606341bccd5a5a59735ca8d73c00ead9e`. |
| `SHA256SUMS` | Checksums of the two parts. |
| `install.sh` | Verifies the checksums and unpacks the archive under a prefix. |
| `LICENSE` | The DSH license (MIT). |
| `packages.tsv` | Name, version and declared license of every package in the archive. |

## Install

```bash
vendor/dsh/install.sh ~/.refinx-node/global
export PATH=~/.refinx-node/global/bin:$PATH   # Node.js 25.9.0 must also be on PATH
dsh --version                                  # 0.2.0-rc.2
```

## Licenses

DSH is MIT-licensed (`LICENSE`). The packages in the archive declare these licenses:

- **Permissive:** MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC, 0BSD, Unlicense, Python-2.0, and MIT OR CC0-1.0.
- **MPL-2.0:** `@deepseek-ai/libreoffice-kit` and `@deepseek-ai/libreoffice-kit-wasm` 0.1.5. Their files are included unmodified.
- **LGPL-3.0-or-later:** `@img/sharp-libvips-linux-x64` 1.3.4, a prebuilt libvips library. Its source is available from the libvips and sharp-libvips projects.

Each package's license file is inside the archive.
