FROM python:3.8.6-buster

COPY . /root
WORKDIR /root


# ensure local python is preferred over distribution python
# ENV PATH /usr/local/bin:$PATH


# cleanup tarballs and downloaded package files
RUN pip install --upgrade pip \
	&& pip install numpy flask\
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/
	
EXPOSE 5000
	
CMD ["python3", "app.py"]
