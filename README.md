# Testing Pipeline Demo

A practical comparison of Testing Management Tools using a simple Python project with `pytest`.

This repository is a companion to the article:
**"From Chaos to Control: A Practical Comparison of Testing Management Tools"**
published on [Dev.to](https://dev.to/kiarazmurillo)

## Project Structure

```
testing-pipeline-demo/
├── app/
│   └── calculator.py
├── tests/
│   └── test_calculator.py
├── requirements.txt
├── .github/workflows/tests.yml       ← GitHub Actions
├── .gitlab-ci.yml                    ← GitLab CI/CD
├── Jenkinsfile                       ← Jenkins
├── .circleci/config.yml              ← CircleCI
├── bitbucket-pipelines.yml           ← Bitbucket Pipelines
└── README.md
```

## How to run locally

```bash
pip install -r requirements.txt
pytest tests/ --tb=short
```

## Tools compared

| Tool | Config file |
|------|-------------|
| GitHub Actions | `.github/workflows/tests.yml` |
| GitLab CI/CD | `.gitlab-ci.yml` |
| Jenkins | `Jenkinsfile` |
| CircleCI | `.circleci/config.yml` |
| Bitbucket Pipelines | `bitbucket-pipelines.yml` |
