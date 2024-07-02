This is my devops ui structure

devops_bot/
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   └── tests/
│       └── test_app.py
├── ui/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── templates/
│   │   ├── login.html
│   │   └── welcome.html
│   └── static/
│       └── style.css
├── docker-compose.yml
├── Jenkinsfile
└── k8s/
    ├── backend-deployment.yaml
    ├── backend-service.yaml
    ├── ui-deployment.yaml
    └── ui-service.yaml

this is a project i am working on, to help the devops world
