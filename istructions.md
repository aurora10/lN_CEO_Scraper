Start the Selenium server container:

docker run -d -p 4444:4444 -p 7900:7900 --shm-size="2g" selenium/standalone-chrome:latest

execute ln-connect.py file. it will output the outer html file "page_content-ln.html"

then

run extract_ceo.py file. to get Excell with CEO data.
