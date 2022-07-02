# ml_project

creating conda environment
```
conda create -p venv python==3.7 -y
```

to activate conda environment
```
conda activate venv/
```

pip install -r requirements.txt

to add all file in github
```
git add. 
```
or
```
git add <File_name>
```
>Note : to ignore file or folder from git we can write file/folder in .gitignore file

to check git status
```
git status
```

to check all version maintain by git 
```
git log
```

to create version/commit all changes by the git
```
git commit -m "some message"
```

to send version/changes to git
```
git push origin main
```


to setup CI/CD pipeline iin heroku we need 3 requirements
1. HEROKU_EMAIL: gaurav.g95garg@gmail.com
2. HEROKU_API_KEY:
3. APP_NAME:first-ml

BUILD DOCKER IMAGE
```
dokcer build -t <image_name>:<tagname> .
```
>NOTE: name of the docker image must be in lower case


to list docker image
```
docker images
```

run docker image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
```

