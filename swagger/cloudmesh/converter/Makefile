SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAMLFILE=converter.yaml
DESTDIR=./flaskConnection
CREATED=./flaskConnection

all: service start 
	@echo "DONE"

dest:
	mkdir -p $(DESTDIR)

service: dest
	wget http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate \
	-i $(YAMLFILE) \
	-l python-flask \
	-o $(DESTDIR) \
	-D supportPython2=true

	cp -r *.py $(DESTDIR)/swagger_server/controllers

	cd $(DESTDIR) && pip install -r requirements.txt && \
	python setup.py install 

start: 
	cd $(DESTDIR) && python -m swagger_server

stop:
	ps | grep swagger | grep -v "grep"| awk '{print $$1}' | xargs kill -9

clean:
	rm -rf $(CREATED)
	rm *.jar

container:
	docker build -t converter .
	docker run -p 8080:8080 converter 
