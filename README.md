# Ansibel pre-commit hooks

A collection of pre-commit hooks, which are handy when using Ansible or Ansible Vault encryption.

## How to

Install [pre-commit](https://pre-commit.com/).

Add this to your config:

```yaml
- repo: https://github.com/biozz/ansible-pre-commit-hooks
  rev: v0.0.1
  hooks:
    - id: ansible-vault-encrypted
      # it can accpet comma separated list of specific filenames to check
      # WARNING: quotes are required, otherwise yaml will treat it as a list
      # args: ["--extras=secret.yml,env.ini"]
```

## `ansible-vault-encrypted`

Adapted from https://gist.github.com/leucos/a9f42e111a8cfc2ebf6e.

It is going to check files containg `.vault.` by default.
If you want to check more files, add `--extras` argument, as shown in the example above.

