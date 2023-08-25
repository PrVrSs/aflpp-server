# AFLplusplus server


```shell
docker build . -f Dockerfile -t aflppserver
```

```shell
docker run -p 127.0.0.1:50051:50051/tcp --env-file .env aflppserver
```