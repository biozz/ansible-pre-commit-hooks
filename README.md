# Ansibel pre-commit hooks

A collection of pre-commit hooks, which are handy when using Ansible or Ansible Vault encryption.

## How to

Install pre-commit.

Add this to your config:

```yaml
- repo: https://github.com/biozz/ansible-pre-commit-hooks
  rev: v0.0.1
  hooks:
    - id: ansible-vault-encrypted
      # args: ["any_file.md"]
```
