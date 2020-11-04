http://106.75.101.119:2020/api/v1/ocr

{"urls":"图片下载链接"}

post请求

https://library-simple-1256602214.cos.ap-beijing.myqcloud.com/1116009732.pdf

https://library-simple-1256602214.cos.ap-beijing.myqcloud.com/20%E4%B8%96%E7%BA%AA%E7%8E%AF%E5%A2%83%E6%B3%95%E5%AD%A6%E7%A0%94%E7%A9%B6%E8%AF%84%E8%BF%B0.pdf0.png


(paddle_env) beantechs@zmy paddle_ocr_server % docker ps
docker stop paddle_ocr_server
docker rm paddle_ocr_server
docker build -t paddle_ocr_server:1.0.2  .
docker run --name paddle_ocr_server  -p 2020:2020 paddle_ocr_server:1.0.1
