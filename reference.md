```dockerfile 
FROM some_image:some_tag

COPY ./from/local/path /container/dest/path
WORKDIR /container/dest/path

# install anything 
RUN apt-get install -y nginx

CMD ["what", "command", "to", "run", "by", "default"]
```



```
docker build -t tf-python -f Dockerfile .
```


```
docker run -p 8080:8080 --rm --name my-tf-python tf-python 
```

```
docker ps
```

```
docker exec -it my-tf-python /bin/bash
```

```
docker run -e ENV_MESSAGE="hello from the cli" -p 8080:8080 --rm --name my-tf-python tf-python
```