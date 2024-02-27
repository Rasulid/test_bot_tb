
## Running Docker container
1. **Clone** this repository
2. **Build** Docker image <br>
   `docker build -t rlt-test .`

3. **Run** it! <br>
   `docker run -d --name=rlt-test-container -p 5000:5000 -e TG_BOT_TOKEN="YOUR_TG_BOT_TOKEN_HERE" rlt-test`


