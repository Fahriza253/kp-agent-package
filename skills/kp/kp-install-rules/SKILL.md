---
name: kp-install-rules
description: "DEPRECATED: gunakan setup-kp-rules atau setup-kp-repo. Hanya memasang tiga rules .mdc ke .cursor/rules/."
disable-model-invocation: true
---

# KP Install Rules (deprecated)

Skill ini **tidak disarankan** untuk workflow baru.

## Gunakan sebagai gantinya

| Kebutuhan | Skill |
| --------- | ----- |
| Repo laporan baru | `setup-kp-repo` |
| Hanya rules | `setup-kp-rules` |

Kedua skill di atas memakai bundle rules yang sama dengan skill ini.

## Jika tetap memanggil skill ini

```bash
bash .agents/skills/setup-kp-rules/scripts/install-rules.sh .
```

Perintah di atas setara dengan skrip lama `kp-install-rules` dan menerima template progress di bundle `setup-kp-rules` bila diperlukan.
